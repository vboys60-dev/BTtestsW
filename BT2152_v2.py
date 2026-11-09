#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:42:48 2026

@author: lianshi
"""

import sys
import pyvisa
import time
import csv
import threading
import re
import math
import random
import numpy as np
from collections import deque
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QGroupBox, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton,
                             QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox,
                             QColorDialog, QHeaderView, QGridLayout, QPlainTextEdit, QSplitter)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QColor, QFont

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import RectangleSelector

# 標記線色盤（最多同時釘選 3 條，依序指派不同顏色）
MARKER_COLORS = ['#e63946', '#2a9d8f', '#f4a261']


class SimpleToolbar(NavigationToolbar):
    """精簡版工具列：只保留「儲存圖片」。
    Pan/Zoom 工具會跟自訂的框選縮放搶同一組滑鼠事件，故移除，
    改由框選縮放＋滾輪縮放＋重置縮放按鈕取代其功能。"""
    toolitems = [t for t in NavigationToolbar.toolitems if t[0] == 'Save']

# ==========================================
# 背景執行緒 1：獨立用於執行 OCV 偵測
# ==========================================
class OcvThread(QThread):
    finished_signal = pyqtSignal(bool, str, list, list)

    def __init__(self, inst, min_ocv):
        super().__init__()
        self.inst = inst
        self.min_ocv = min_ocv

    def run(self):
        try:
            self.inst.write("INIT:TEST:OCV 4.5, 0.5, 0.01, 1, (@1:32)")
            while int(self.inst.query("SENS:OCV:AVAI?")) != 1:
                time.sleep(1)
            
            ocv_data = self.inst.query("FETC:VOLT:OCV? (@1:32)").strip().split(',')
            
            active_channels = []
            valid_ocvs = []
            
            for i, v_str in enumerate(ocv_data, 1):
                v = float(v_str)
                if self.min_ocv <= v <= 4.5:
                    active_channels.append(i)
                valid_ocvs.append(v)
            
            msg = "OCV偵測完成。" if active_channels else "無可用通道大於最低電壓設定。"
            self.finished_signal.emit(True, msg, active_channels, valid_ocvs)
            
        except Exception as e:
            self.finished_signal.emit(False, f"OCV執行錯誤: {str(e)}", [], [])

# ==========================================
# 背景執行緒 2：獨立用於執行 In Situ 校準 (僅針對選用通道)
# ==========================================
class InSituThread(QThread):
    finished_signal = pyqtSignal(bool, str, list)

    def __init__(self, inst, active_channels, cal_level):
        super().__init__()
        self.inst = inst
        self.active_channels = active_channels
        self.cal_level = cal_level

    def run(self):
        try:
            if not self.active_channels:
                self.finished_signal.emit(False, "沒有需要校準的通道。", [])
                return
                
            active_str = ",".join(map(str, self.active_channels))
            
            self.inst.write(f"CONF:INS:CURR {self.cal_level}")
            self.inst.write(f"CAL:WIRE:RES:INS (@{active_str})")
            while int(self.inst.query("SENS:WIRE:RES:AVAI?")) != 1:
                time.sleep(1)
            
            res_data = self.inst.query(f"CAL:WIRE:RES:VAL? (@{active_str})").strip().split(',')
            self.inst.write("CAL:WIRE:RES:SAVE 1")
            
            self.finished_signal.emit(True, "In Situ 校準完成，並已存入記憶體 1。", res_data)
            
        except Exception as e:
            self.finished_signal.emit(False, f"校準執行錯誤: {str(e)}", [])

# ==========================================
# 背景執行緒 3：用於定時從內部記憶體撈取測試資料
# ==========================================
class FetchThread(QThread):
    update_signal = pyqtSignal()
    error_signal = pyqtSignal(str)
    temp_signal = pyqtSignal(float)

    def __init__(self, inst, active_channels, interval, fetch_v, fetch_i, fetch_temp,
                 csv_writer, csv_file, data_lock, time_data, v_data, i_data, temp_data):
        super().__init__()
        self.inst = inst
        self.active_channels = active_channels
        self.interval = interval
        self.fetch_v = fetch_v
        self.fetch_i = fetch_i
        self.fetch_temp = fetch_temp
        self.csv_writer = csv_writer
        self.csv_file = csv_file
        self.data_lock = data_lock
        self.is_running = True
        self.current_offset = 0
        self.temp_offset = 0

        self.time_data = time_data
        self.v_data = v_data
        self.i_data = i_data
        self.temp_data = temp_data

    def _poll_sleep_seconds(self):
        # 依手冊 Time Interval Parameter 的 Data update rate 表格換算，
        # 避免在慢速測試（interval 較大）時仍每 2 秒無意義地輪詢儀器
        if self.interval <= 4: update_rate = 4
        elif self.interval <= 8: update_rate = 8
        elif self.interval <= 16: update_rate = 16
        elif self.interval <= 32: update_rate = 32
        elif self.interval <= 64: update_rate = 64
        elif self.interval <= 128: update_rate = 128
        else: update_rate = 256
        return min(10, max(1, update_rate / 2))

    def _fetch_new_temperatures(self, max_points):
        try:
            pts_str = self.inst.query("FETC:TEMP:LOG:POIN?").strip()
            available = int(pts_str) if pts_str else 0
        except Exception:
            return []

        remaining = available - self.temp_offset
        if remaining <= 0:
            return []

        temp_to_read = min(max_points, remaining)
        temp_str = self.inst.query(f"FETC:TEMP:LOG? {temp_to_read}, {self.temp_offset}").strip().split(',')
        values = []
        for v in temp_str:
            val = float(v)
            values.append(None if val > 1e30 else val)  # 9.91E37 代表外部感測器未接
        self.temp_offset += temp_to_read
        return values

    def run(self):
        active_str = ",".join(map(str, self.active_channels))
        sleep_time = self._poll_sleep_seconds()

        while self.is_running:
            try:
                pts_str = self.inst.query(f"FETC:VOLT:LOG:POIN?").strip()
                if not pts_str:
                    time.sleep(1)
                    continue

                available_points = int(pts_str)

                if available_points > self.current_offset:
                    points_to_read = available_points - self.current_offset
                    v_vals, i_vals = [], []

                    if self.fetch_v:
                        v_str = self.inst.query(f"FETC:VOLT:LOG? {points_to_read}, {self.current_offset}, (@{active_str})").strip().split(',')
                        v_vals = [float(v) for v in v_str]
                    if self.fetch_i:
                        i_str = self.inst.query(f"FETC:CURR:LOG? {points_to_read}, {self.current_offset}, (@{active_str})").strip().split(',')
                        i_vals = [float(i)*1e6 for i in i_str]

                    temp_vals = self._fetch_new_temperatures(points_to_read) if self.fetch_temp else []

                    rows = []
                    with self.data_lock:
                        for pt_idx in range(points_to_read):
                            # 依照擷取頻率計算時間(秒)
                            t_s = (self.current_offset + pt_idx + 1) * self.interval
                            self.time_data.append(t_s)
                            row_data = [f"{t_s:.1f}"]

                            for ch_idx, ch in enumerate(self.active_channels):
                                flat_idx = ch_idx * points_to_read + pt_idx
                                if self.fetch_v:
                                    v = v_vals[flat_idx]
                                    self.v_data[ch].append(v)
                                    row_data.append(f"{v:.3f}")
                                if self.fetch_i:
                                    i_val = i_vals[flat_idx]
                                    self.i_data[ch].append(i_val)
                                    row_data.append(f"{i_val:.3f}")

                            if self.fetch_temp:
                                if pt_idx < len(temp_vals):
                                    t_val = temp_vals[pt_idx]
                                    self.temp_data.append(t_val if t_val is not None else float('nan'))
                                    row_data.append("" if t_val is None else f"{t_val:.2f}")
                                else:
                                    row_data.append("")

                            rows.append(row_data)

                    for row_data in rows:
                        self.csv_writer.writerow(row_data)
                    self.csv_file.flush()

                    if self.fetch_temp and temp_vals:
                        last_valid = temp_vals[-1]
                        self.temp_signal.emit(last_valid if last_valid is not None else float('nan'))

                    self.current_offset += points_to_read
                    self.update_signal.emit()

            except Exception as e:
                self.error_signal.emit(f"擷取資料錯誤: {str(e)}")

            time.sleep(sleep_time)

    def stop(self):
        self.is_running = False

# ==========================================
# 模擬儀器：不需要真實 BT2152A/B 與 VISA 連線，供介面驗證/展示使用
# ==========================================
MOCK_TIME_SPEEDUP = 20  # 模擬時間加速倍率，展示時不用真的等滿使用者設定的間隔秒數


class MockInstrument:
    """
    模擬 BT2152A/B 儀器，實作與 pyvisa resource 相同的 write()/query()/close() 介面，
    讓 OcvThread/InSituThread/FetchThread 完全不用修改就能把 self.inst 直接換成這個物件。
    只涵蓋這支程式實際會送出的固定 SCPI 指令格式，不是通用 SCPI 模擬器。
    """

    def __init__(self):
        self.timeout = 10000
        self._rng = random.Random()

        self._ocv_ready_at = None
        self._ocv_values = {}   # ch -> 模擬 OCV 電壓(V)

        self._wire_ready_at = None
        self._wire_values = {}  # ch -> 模擬導線電阻(Ω)

        self._test_start = None      # 測試開始的真實時間戳 (time.time())
        self._test_interval = 30.0   # 使用者設定的擷取間隔(秒)
        self._test_channels = []     # INIT:TEST:MATC 指定的通道清單

    # ---------- 對外介面 (與 pyvisa resource 相同) ----------
    def write(self, cmd):
        cmd = cmd.strip()
        if cmd.startswith("INIT:TEST:OCV"):
            self._start_ocv()
        elif cmd.startswith("CAL:WIRE:RES:INS"):
            self._start_wire_cal(cmd)
        elif cmd.startswith("INIT:TEST:MATC"):
            self._start_test(cmd)
        elif cmd.startswith("ABORt"):
            self._test_start = None
        # CONF:INS:CURR、CAL:WIRE:RES:SAVE 等指令對模擬行為沒有影響，忽略即可

    def query(self, cmd):
        cmd = cmd.strip()

        if cmd == "SENS:OCV:AVAI?":
            ready = self._ocv_ready_at is not None and time.time() >= self._ocv_ready_at
            return "1" if ready else "0"

        if cmd.startswith("FETC:VOLT:OCV?"):
            return ",".join(f"{self._ocv_values.get(ch, 0.0):.4f}" for ch in range(1, 33))

        if cmd == "SENS:WIRE:RES:AVAI?":
            ready = self._wire_ready_at is not None and time.time() >= self._wire_ready_at
            return "1" if ready else "0"

        if cmd.startswith("CAL:WIRE:RES:VAL?"):
            chans = self._parse_chanlist(cmd)
            return ",".join(f"{self._wire_values.get(ch, 0.1):.4f}" for ch in chans)

        if cmd in ("FETC:VOLT:LOG:POIN?", "FETC:TEMP:LOG:POIN?"):
            return str(self._available_points())

        if cmd.startswith("FETC:VOLT:LOG?"):
            return self._log_values(cmd, kind='v')

        if cmd.startswith("FETC:CURR:LOG?"):
            return self._log_values(cmd, kind='i')

        if cmd.startswith("FETC:TEMP:LOG?"):
            return self._log_values(cmd, kind='t')

        return "0"

    def close(self):
        pass

    # ---------- 內部邏輯 ----------
    def _start_ocv(self):
        self._ocv_ready_at = time.time() + 1.5
        self._ocv_values = {}
        for ch in range(1, 33):
            if self._rng.random() < 0.85:
                self._ocv_values[ch] = round(self._rng.uniform(3.5, 3.95), 4)
            else:
                self._ocv_values[ch] = round(self._rng.uniform(0.0, 1.0), 4)

    def _start_wire_cal(self, cmd):
        chans = self._parse_chanlist(cmd)
        self._wire_ready_at = time.time() + 1.5
        self._wire_values = {ch: round(self._rng.uniform(0.05, 0.25), 4) for ch in chans}

    def _start_test(self, cmd):
        m = re.search(
            r"INIT:TEST:MATC\s+[\d.]+,\s*[\d.]+,\s*[\d.]+,\s*[\d.]+,\s*([\d.]+),\s*"
            r"[\d.eE+-]+,\s*[\d.eE+-]+,\s*\(@([\d,]+)\)",
            cmd
        )
        if not m:
            return
        self._test_interval = float(m.group(1))
        self._test_channels = [int(x) for x in m.group(2).split(',')]
        self._test_start = time.time()

    def _parse_chanlist(self, cmd):
        m = re.search(r"\(@([\d,]+)\)", cmd)
        return [int(x) for x in m.group(1).split(',')] if m else []

    def _available_points(self):
        if self._test_start is None:
            return 0
        elapsed_real = time.time() - self._test_start
        elapsed_sim = elapsed_real * MOCK_TIME_SPEEDUP
        pts = int(elapsed_sim // self._test_interval)
        return max(0, min(pts, 259200))  # 手冊：每通道最多 259200 筆

    def _log_values(self, cmd, kind):
        m = re.search(r"\?\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*\(@([\d,]+)\))?", cmd)
        if not m:
            return ""
        n = int(m.group(1))
        offset = int(m.group(2))

        if kind == 't':
            return ",".join(f"{self._simulate_temp(offset + i):.3f}" for i in range(n))

        chans = [int(x) for x in m.group(3).split(',')] if m.group(3) else self._test_channels
        out = []
        for ch in chans:
            for i in range(n):
                idx = offset + i
                if kind == 'v':
                    out.append(self._simulate_voltage(ch, idx))
                else:
                    out.append(self._simulate_current(ch, idx))
        return ",".join(f"{v:.6f}" for v in out)

    def _simulate_voltage(self, ch, idx):
        base = self._ocv_values.get(ch, 3.7)
        return base + self._rng.gauss(0, 0.0002)

    def _simulate_current(self, ch, idx):
        t = idx * self._test_interval
        decay = 5e-6 * math.exp(-t / 3600.0)          # 隨時間緩慢衰減的自放電電流
        baseline = 1e-6 * (1 + 0.1 * (ch % 5))         # 各通道略有差異的穩態基準
        noise = self._rng.gauss(0, 2e-7)
        return decay + baseline + noise

    def _simulate_temp(self, idx):
        t = idx * self._test_interval
        return 24.0 + 0.5 * math.sin(t / 1800.0) + self._rng.gauss(0, 0.05)


# ==========================================
# 背景執行緒 4：搜尋可用的儀器資源 (VISA)
# ==========================================
class ResourceSearchThread(QThread):
    finished_signal = pyqtSignal(bool, str, list)

    def __init__(self, rm):
        super().__init__()
        self.rm = rm

    def run(self):
        try:
            resources = list(self.rm.list_resources())
            if resources:
                msg = f"找到 {len(resources)} 個儀器資源。"
            else:
                msg = "未找到任何儀器資源，請確認連線狀態，或手動輸入位址。"
            self.finished_signal.emit(True, msg, resources)
        except Exception as e:
            self.finished_signal.emit(False, f"搜尋儀器時發生錯誤: {str(e)}", [])

# ==========================================
# 主視窗 GUI 介面
# ==========================================
class BT2152App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keysight BT2152A/B 測試控制程式")
        self.resize(1300, 850)
        
        self.rm = pyvisa.ResourceManager()
        self.inst = None
        self.active_channels = []

        # 通道預設顏色改用 qualitative colormap 自動分色，避免 32 通道全部同色難以辨識
        tab20 = plt.get_cmap('tab20').colors
        tab20b = plt.get_cmap('tab20b').colors
        palette = list(tab20) + list(tab20b)
        self.channel_colors = {
            i: QColor.fromRgbF(*palette[(i - 1) % len(palette)][:3])
            for i in range(1, 33)
        }

        self.is_user_zoomed = False # 紀錄使用者是否自行縮放圖表

        self.max_points = 1000
        self.time_data = deque(maxlen=self.max_points)
        self.v_data = {i: deque(maxlen=self.max_points) for i in range(1, 33)}
        self.i_data = {i: deque(maxlen=self.max_points) for i in range(1, 33)}
        self.temp_data = deque(maxlen=self.max_points)

        self.data_lock = threading.Lock() # 保護 FetchThread 寫入與主執行緒繪圖讀取之間的資料一致性
        self.lines_v = {}  # 通道 -> 電壓 Line2D，供增量更新繪圖
        self.lines_i = {}  # 通道 -> 電流 Line2D，供增量更新繪圖
        self.line_temp = None  # 外部溫度 Line2D，供增量更新繪圖

        self.hover_line_a = None  # 圖A 游標對照線 (setup_ui 中建立)
        self.hover_line_b = None  # 圖B 游標對照線 (setup_ui 中建立)
        self.pinned_markers = []  # 已釘選的標記線: [{'time','color','line_a','line_b'}, ...]，最多 3 筆
        self._press_xy = None     # 判斷「點擊」還是「拖曳框選」用
        self.current_interval = 30  # 目前測試的擷取間隔（供標記面板判斷資料是否已捲出緩衝區）

        self.csv_file = None
        self.csv_writer = None

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # --- 頂部設定區 ---
        settings_group = QGroupBox("測試與儲存設定")
        grid = QGridLayout()
        
        grid.addWidget(QLabel("I/O 位址:"), 0, 0)
        self.io_addr_input = QComboBox()
        self.io_addr_input.setEditable(True)
        self.io_addr_input.addItem("TCPIP0::169.254.4.61::inst0::INSTR")
        grid.addWidget(self.io_addr_input, 0, 1)
        
        grid.addWidget(QLabel("間隔時間(>=5秒):"), 0, 2)
        self.interval_input = QLineEdit("30")
        self.interval_input.setToolTip("原廠手冊建議擷取間隔為 30 秒，兼顧雜訊平滑與資料量，可依需求調整。")
        grid.addWidget(self.interval_input, 0, 3)

        self.chk_v = QCheckBox("擷取 電壓(V)")
        self.chk_v.setChecked(True)
        grid.addWidget(self.chk_v, 0, 4)
        self.chk_i = QCheckBox("擷取 電流(uA)")
        self.chk_i.setChecked(True)
        grid.addWidget(self.chk_i, 0, 5)

        self.chk_temp = QCheckBox("擷取 外部溫度(°C)")
        self.chk_temp.setChecked(False)
        self.chk_temp.setToolTip("需在儀器後方 TEMP 端子接上 10kΩ 熱敏電阻才有效。")
        grid.addWidget(self.chk_temp, 0, 6)

        grid.addWidget(QLabel("OCV最低電壓(V):"), 1, 0)
        self.min_ocv_input = QLineEdit("2.8")
        grid.addWidget(self.min_ocv_input, 1, 1)
        
        grid.addWidget(QLabel("In Situ校準檔位:"), 1, 2)
        self.cal_level_combo = QComboBox()
        self.cal_level_combo.addItems(["HIGH", "MED", "LOW"])
        self.cal_level_combo.setCurrentText("MED")
        grid.addWidget(self.cal_level_combo, 1, 3)
        
        self.btn_file = QPushButton("選擇儲存 CSV 路徑")
        self.btn_file.clicked.connect(self.choose_file)
        grid.addWidget(self.btn_file, 1, 4)
        
        self.filepath_input = QLineEdit()
        self.filepath_input.setReadOnly(True)
        grid.addWidget(self.filepath_input, 1, 5, 1, 2)

        self.chk_sim_mode = QCheckBox("模擬模式 (無需儀器，展示/測試用)")
        self.chk_sim_mode.setChecked(False)
        self.chk_sim_mode.setToolTip("使用內建的假儀器產生模擬資料，不需連接真實 BT2152A/B，方便介面展示或驗證。")
        grid.addWidget(self.chk_sim_mode, 2, 0, 1, 2)

        self.btn_search = QPushButton("搜尋儀器")
        self.btn_search.clicked.connect(self.search_instruments)
        grid.addWidget(self.btn_search, 2, 2)

        settings_group.setLayout(grid)
        main_layout.addWidget(settings_group)
        
        # --- 獨立操作按鈕區 ---
        btn_layout = QHBoxLayout()
        self.btn_detect = QPushButton("1. OCV 偵測")
        self.btn_detect.setStyleSheet("background-color: lightblue; padding: 10px;")
        self.btn_detect.clicked.connect(self.start_ocv)
        
        self.btn_cal = QPushButton("2. In Situ 校準 (依OCV結果)")
        self.btn_cal.setStyleSheet("background-color: #ffd166; padding: 10px;")
        self.btn_cal.setEnabled(False)
        self.btn_cal.clicked.connect(self.start_in_situ)
        
        self.btn_start = QPushButton("3. 開始測試")
        self.btn_start.setStyleSheet("background-color: lightgreen; padding: 10px;")
        self.btn_start.setEnabled(False)
        self.btn_start.clicked.connect(self.start_test)
        
        self.btn_stop = QPushButton("中斷測試")
        self.btn_stop.setStyleSheet("background-color: salmon; padding: 10px;")
        self.btn_stop.setEnabled(False)
        self.btn_stop.clicked.connect(self.stop_test)
        
        btn_layout.addWidget(self.btn_detect)
        btn_layout.addWidget(self.btn_cal)
        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)

        self.lbl_conn_status = QLabel("● 未連線")
        self.lbl_conn_status.setStyleSheet("color: gray; font-weight: bold; padding-left: 10px;")
        btn_layout.addWidget(self.lbl_conn_status)
        btn_layout.addStretch()

        main_layout.addLayout(btn_layout)
        
        # --- 底部視圖區 (Table + Plot)，改用 QSplitter 讓表格可收合/可拖曳調整寬度 ---
        bottom_layout = QSplitter(Qt.Horizontal)
        self.bottom_splitter = bottom_layout

        table_container = QWidget()
        table_container_layout = QVBoxLayout(table_container)
        table_container_layout.setContentsMargins(0, 0, 0, 0)

        table_header_layout = QHBoxLayout()
        table_header_layout.addWidget(QLabel("通道列表"))
        self.btn_toggle_table = QPushButton("◀ 收合")
        self.btn_toggle_table.setToolTip("設定完通道後可收合此列表，讓圖表區域有更多顯示空間。")
        self.btn_toggle_table.clicked.connect(self.toggle_table_panel)
        table_header_layout.addWidget(self.btn_toggle_table)
        table_header_layout.addStretch()
        table_container_layout.addLayout(table_header_layout)

        self.table = QTableWidget(32, 5)
        self.table.setHorizontalHeaderLabels(["CH", "狀態", "OCV(V)", "電阻(Ω)", "顏色"])
        self.table.verticalHeader().setVisible(False)
        self.table.cellDoubleClicked.connect(self.change_color)

        self.table.setColumnWidth(0, 40)
        self.table.setColumnWidth(1, 40)
        self.table.setColumnWidth(2, 60)
        self.table.setColumnWidth(3, 70)
        self.table.setColumnWidth(4, 70)

        for row in range(32):
            self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.table.setItem(row, 1, QTableWidgetItem("X"))
            self.table.setItem(row, 2, QTableWidgetItem("NA"))
            self.table.setItem(row, 3, QTableWidgetItem("NA"))
            color_item = QTableWidgetItem("雙擊修改")
            color_item.setBackground(self.channel_colors[row+1])
            self.table.setItem(row, 4, color_item)

        table_container_layout.addWidget(self.table)
        bottom_layout.addWidget(table_container)
        self._table_container = table_container
        self._table_expanded_width = 320

        # 右側繪圖區塊
        plot_container = QWidget()
        plot_wrapper = QVBoxLayout(plot_container)
        plot_wrapper.setContentsMargins(0, 0, 0, 0)

        # 圖表顯示設定區
        plot_ctrl_layout = QHBoxLayout()
        plot_ctrl_layout.addWidget(QLabel("圖表顯示設定:"))
        self.plot_chk_v = QCheckBox("顯示電壓曲線 (左Y軸)")
        self.plot_chk_v.setChecked(True)
        self.plot_chk_v.stateChanged.connect(lambda: self.update_plot(force_redraw=True))
        plot_ctrl_layout.addWidget(self.plot_chk_v)

        self.plot_chk_i = QCheckBox("顯示電流曲線 (右Y軸)")
        self.plot_chk_i.setChecked(True)
        self.plot_chk_i.stateChanged.connect(lambda: self.update_plot(force_redraw=True))
        plot_ctrl_layout.addWidget(self.plot_chk_i)

        self.plot_chk_temp = QCheckBox("顯示溫度曲線")
        self.plot_chk_temp.setChecked(True)
        self.plot_chk_temp.stateChanged.connect(lambda: self.update_plot(force_redraw=True))
        plot_ctrl_layout.addWidget(self.plot_chk_temp)

        self.btn_reset_zoom = QPushButton("重置縮放 (自動對齊)")
        self.btn_reset_zoom.clicked.connect(self.reset_zoom)
        plot_ctrl_layout.addWidget(self.btn_reset_zoom)

        self.btn_clear_markers = QPushButton("清除標記線")
        self.btn_clear_markers.clicked.connect(self._clear_all_markers)
        plot_ctrl_layout.addWidget(self.btn_clear_markers)

        self.lbl_temp_value = QLabel("外部溫度: N/A")
        plot_ctrl_layout.addWidget(self.lbl_temp_value)

        self.lbl_hover_info = QLabel("游標: -")
        plot_ctrl_layout.addWidget(self.lbl_hover_info)

        plot_ctrl_layout.addStretch()
        plot_wrapper.addLayout(plot_ctrl_layout)

        # --- 圖表 A：電壓/電流 (雙 Y 軸) ---
        self.fig_a, self.ax1 = plt.subplots()
        self.ax2 = self.ax1.twinx()
        self.fig_a.tight_layout(pad=3.0)
        self.canvas_a = FigureCanvas(self.fig_a)
        self.toolbar_a = SimpleToolbar(self.canvas_a, self)
        plot_wrapper.addWidget(self.toolbar_a)
        plot_wrapper.addWidget(self.canvas_a, 3)  # 電壓/電流圖佔較大比例

        # --- 圖表 B：外部溫度 (單一 Y 軸) ---
        self.fig_b, self.ax_temp = plt.subplots()
        self.fig_b.tight_layout(pad=3.0)
        self.canvas_b = FigureCanvas(self.fig_b)
        self.toolbar_b = SimpleToolbar(self.canvas_b, self)
        plot_wrapper.addWidget(self.toolbar_b)
        plot_wrapper.addWidget(self.canvas_b, 1)  # 溫度圖佔較小比例

        # 游標對照線 (初始隱藏)，懸停時兩圖同步顯示同一時間點
        self.hover_line_a = self.ax1.axvline(0, color='gray', linewidth=1, linestyle='-', visible=False)
        self.hover_line_b = self.ax_temp.axvline(0, color='gray', linewidth=1, linestyle='-', visible=False)

        # 框選縮放：左鍵拖曳畫框即可縮放到選取的時間範圍，跟滾輪縮放並存
        self.selector_a = RectangleSelector(self.ax1, self._on_box_select, useblit=True,
                                             button=[1], minspanx=5, minspany=5,
                                             spancoords='pixels', interactive=False)
        self.selector_b = RectangleSelector(self.ax_temp, self._on_box_select, useblit=True,
                                             button=[1], minspanx=5, minspany=5,
                                             spancoords='pixels', interactive=False)

        # 滑鼠滾輪縮放：X 軸在兩圖之間同步，Y 軸各自依游標所在軸縮放
        self.canvas_a.mpl_connect('scroll_event',
            lambda e: self._wheel_zoom(e, self.ax1, self.ax2 if self.plot_chk_i.isChecked() else None))
        self.canvas_b.mpl_connect('scroll_event',
            lambda e: self._wheel_zoom(e, self.ax_temp, None))

        # 懸停游標對照線 + 點擊釘選/移除標記線
        self.canvas_a.mpl_connect('motion_notify_event', self._on_hover)
        self.canvas_b.mpl_connect('motion_notify_event', self._on_hover)
        self.canvas_a.mpl_connect('axes_leave_event', self._on_leave)
        self.canvas_b.mpl_connect('axes_leave_event', self._on_leave)
        self.canvas_a.mpl_connect('button_press_event', self._on_button_press)
        self.canvas_b.mpl_connect('button_press_event', self._on_button_press)
        self.canvas_a.mpl_connect('button_release_event', self._on_button_release)
        self.canvas_b.mpl_connect('button_release_event', self._on_button_release)

        bottom_layout.addWidget(plot_container)
        bottom_layout.setSizes([self._table_expanded_width, 980])
        main_layout.addWidget(bottom_layout)

        # 標記數值面板：點擊釘選標記後，列出該時間點所有已啟用通道的完整數值
        self.marker_panel = QPlainTextEdit()
        self.marker_panel.setReadOnly(True)
        self.marker_panel.setMaximumHeight(140)
        marker_font = QFont()
        marker_font.setStyleHint(QFont.Monospace)
        marker_font.setFixedPitch(True)
        marker_font.setPointSize(9)
        self.marker_panel.setFont(marker_font)
        self.marker_panel.setPlaceholderText("點擊圖表可釘選標記線 (最多 3 條)，此處會顯示該時間點所有通道的完整數值。")
        main_layout.addWidget(self.marker_panel)

    def _autoscale_axis_y(self, ax, xlim, force_zero_bottom=False):
        """
        只依據 xlim 範圍內「可見」的資料點自動計算並設定 Y 軸範圍。
        跳過游標對照線與標記線 (axvline 建立的輔助線)，只採計真正的資料線。
        範圍內沒有任何資料時直接 return，維持現有 Y 範圍不變。
        """
        skip = {self.hover_line_a, self.hover_line_b}
        skip |= {m.get('line_a') for m in self.pinned_markers}
        skip |= {m.get('line_b') for m in self.pinned_markers}

        y_min = y_max = None
        for line in ax.get_lines():
            if line in skip:
                continue
            xdata = np.asarray(line.get_xdata(), dtype=float)
            ydata = np.asarray(line.get_ydata(), dtype=float)
            if xdata.size == 0:
                continue
            mask = (xdata >= xlim[0]) & (xdata <= xlim[1]) & ~np.isnan(ydata)
            if not mask.any():
                continue
            y_visible = ydata[mask]
            cur_min, cur_max = float(y_visible.min()), float(y_visible.max())
            y_min = cur_min if y_min is None else min(y_min, cur_min)
            y_max = cur_max if y_max is None else max(y_max, cur_max)

        if y_min is None:
            return

        if force_zero_bottom:
            y_min = min(0, y_min)

        pad = (y_max - y_min) * 0.1 if y_max != y_min else (abs(y_min) * 0.1 or 1.0)
        ax.set_ylim(y_min - pad, y_max + pad)

    def _auto_scale_all(self, time_snapshot, show_v, show_i, show_temp):
        """自動對齊模式：X 軸涵蓋全部資料範圍，Y 軸依可見資料自動 fit，兩張圖 X 軸同步。"""
        if time_snapshot:
            xlim = (min(time_snapshot), max(time_snapshot))
            if xlim[0] == xlim[1]:
                xlim = (xlim[0] - 1, xlim[1] + 1)
        else:
            xlim = (0, 1)

        self.ax1.set_xlim(xlim)
        self.ax_temp.set_xlim(xlim)

        if show_v:
            self._autoscale_axis_y(self.ax1, xlim, force_zero_bottom=True)
        if show_i:
            self._autoscale_axis_y(self.ax2, xlim, force_zero_bottom=True)
        if show_temp:
            self._autoscale_axis_y(self.ax_temp, xlim, force_zero_bottom=False)

    def _on_box_select(self, eclick, erelease):
        """框選縮放：只決定 X（時間）範圍，Y 軸一律依縮放後可見窗口自動 fit。"""
        x0, x1 = eclick.xdata, erelease.xdata
        if x0 is None or x1 is None or x0 == x1:
            return

        lo, hi = sorted((x0, x1))
        self.is_user_zoomed = True
        self.ax1.set_xlim(lo, hi)
        self.ax_temp.set_xlim(lo, hi)

        if self.plot_chk_v.isChecked():
            self._autoscale_axis_y(self.ax1, (lo, hi), force_zero_bottom=True)
        if self.plot_chk_i.isChecked():
            self._autoscale_axis_y(self.ax2, (lo, hi), force_zero_bottom=True)
        if self.plot_chk_temp.isChecked():
            self._autoscale_axis_y(self.ax_temp, (lo, hi), force_zero_bottom=False)

        self.canvas_a.draw_idle()
        self.canvas_b.draw_idle()

    def _wheel_zoom(self, event, primary_ax, secondary_ax):
        """
        滑鼠滾輪縮放：對游標所在圖表的 X 軸與主要 Y 軸依游標位置縮放
        (若有次要 Y 軸如電流軸，也一併以中心對齊方式縮放)，
        再把縮放後的 X 範圍同步套用到另一張圖，其 Y 軸自動 fit 到新的可見窗口。
        """
        if event.inaxes is None or event.x is None or event.y is None:
            return

        self.is_user_zoomed = True

        base_scale = 1.2
        if event.button == 'up':
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            scale_factor = base_scale
        else:
            scale_factor = 1

        # 用 primary_ax 自身的座標轉換重新換算游標位置，避免雙 Y 軸重疊時
        # event.ydata 實際上是取自另一個重疊軸（電壓/電流單位不同）的問題
        xdata, ydata = primary_ax.transData.inverted().transform((event.x, event.y))

        cur_xlim = primary_ax.get_xlim()
        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
        new_xlim = (xdata - new_width * (1 - relx), xdata + new_width * relx)
        primary_ax.set_xlim(new_xlim)

        cur_ylim1 = primary_ax.get_ylim()
        new_height1 = (cur_ylim1[1] - cur_ylim1[0]) * scale_factor
        rely1 = (cur_ylim1[1] - ydata) / (cur_ylim1[1] - cur_ylim1[0])
        new_ymin1 = max(0, ydata - new_height1 * (1 - rely1))
        primary_ax.set_ylim([new_ymin1, ydata + new_height1 * rely1])

        if secondary_ax is not None:
            cur_ylim2 = secondary_ax.get_ylim()
            new_height2 = (cur_ylim2[1] - cur_ylim2[0]) * scale_factor
            center_y2 = (cur_ylim2[1] + cur_ylim2[0]) / 2
            new_ymin2 = max(0, center_y2 - new_height2 / 2)
            secondary_ax.set_ylim([new_ymin2, center_y2 + new_height2 / 2])

        # 同步另一張圖的 X 範圍，Y 軸自動 fit 到新的可見窗口
        if primary_ax is self.ax1:
            self.ax_temp.set_xlim(new_xlim)
            if self.plot_chk_temp.isChecked():
                self._autoscale_axis_y(self.ax_temp, new_xlim, force_zero_bottom=False)
        else:
            self.ax1.set_xlim(new_xlim)
            if self.plot_chk_v.isChecked():
                self._autoscale_axis_y(self.ax1, new_xlim, force_zero_bottom=True)
            if self.plot_chk_i.isChecked():
                self._autoscale_axis_y(self.ax2, new_xlim, force_zero_bottom=True)

        self.canvas_a.draw_idle()
        self.canvas_b.draw_idle()

    def reset_zoom(self):
        """重置縮放狀態為自動對齊"""
        self.is_user_zoomed = False
        self.update_plot(force_redraw=True)

    def choose_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "選擇儲存 CSV 路徑", "", "CSV Files (*.csv)")
        if filename:
            self.filepath_input.setText(filename)

    def connect_inst(self):
        try:
            if self.inst is None:
                if self.chk_sim_mode.isChecked():
                    self.inst = MockInstrument()
                else:
                    self.inst = self.rm.open_resource(self.io_addr_input.currentText())
                    self.inst.timeout = 10000
            status_suffix = "（模擬模式）" if isinstance(self.inst, MockInstrument) else ""
            self.lbl_conn_status.setText(f"● 已連線{status_suffix}")
            self.lbl_conn_status.setStyleSheet("color: green; font-weight: bold; padding-left: 10px;")
            return True
        except Exception as e:
            self.lbl_conn_status.setText("● 未連線")
            self.lbl_conn_status.setStyleSheet("color: red; font-weight: bold; padding-left: 10px;")
            QMessageBox.critical(self, "連線錯誤", str(e))
            return False

    def search_instruments(self):
        self.btn_search.setEnabled(False)
        self.btn_search.setText("搜尋中...")
        self.search_thread = ResourceSearchThread(self.rm)
        self.search_thread.finished_signal.connect(self.on_search_finished)
        self.search_thread.start()

    def on_search_finished(self, success, msg, resources):
        self.btn_search.setEnabled(True)
        self.btn_search.setText("搜尋儀器")

        if success:
            current_text = self.io_addr_input.currentText()
            self.io_addr_input.clear()
            if resources:
                self.io_addr_input.addItems(resources)
            if current_text:
                idx = self.io_addr_input.findText(current_text)
                if idx >= 0:
                    self.io_addr_input.setCurrentIndex(idx)
                else:
                    self.io_addr_input.insertItem(0, current_text)
                    self.io_addr_input.setCurrentIndex(0)
            QMessageBox.information(self, "搜尋完成", msg)
        else:
            QMessageBox.warning(self, "搜尋失敗", msg)

    def change_color(self, row, col):
        if col == 4:
            ch = row + 1
            color = QColorDialog.getColor(self.channel_colors[ch], self, "選擇通道顏色")
            if color.isValid():
                self.channel_colors[ch] = color
                self.table.item(row, 4).setBackground(color)
                self.update_plot(force_redraw=True)

    def toggle_table_panel(self):
        """收合/展開左側通道列表，讓圖表區在設定完通道後可以有更多顯示空間。"""
        splitter = self.bottom_splitter

        if self.table.isVisible():
            current_sizes = splitter.sizes()
            if current_sizes and current_sizes[0] > 0:
                self._table_expanded_width = current_sizes[0]
            self.table.setVisible(False)
            splitter.setSizes([0, sum(current_sizes) if current_sizes else 980])
            self.btn_toggle_table.setText("▶ 展開")
        else:
            self.table.setVisible(True)
            total = sum(splitter.sizes()) or (self._table_expanded_width + 980)
            splitter.setSizes([self._table_expanded_width, max(1, total - self._table_expanded_width)])
            self.btn_toggle_table.setText("◀ 收合")

    def on_temp_update(self, value):
        """更新外部熱敏電阻溫度即時顯示 (value 為 NaN 代表感測器未接)"""
        if value != value:  # NaN 判斷
            self.lbl_temp_value.setText("外部溫度: N/A")
        else:
            self.lbl_temp_value.setText(f"外部溫度: {value:.2f} °C")

    def _nearest_index(self, times, t, max_gap=None):
        """在 times 中找出最接近 t 的索引；若 max_gap 有指定且差距超過門檻，回傳 None（代表資料已不在目前緩衝區內）。"""
        if not times:
            return None
        idx = min(range(len(times)), key=lambda i: abs(times[i] - t))
        if max_gap is not None and abs(times[idx] - t) > max_gap:
            return None
        return idx

    # --- 游標對照線 (懸停即時跟隨) ---
    def _on_hover(self, event):
        if event.xdata is None or event.inaxes is None:
            return

        with self.data_lock:
            times = list(self.time_data)
        if not times:
            return

        idx = self._nearest_index(times, event.xdata)
        t = times[idx]

        self.hover_line_a.set_xdata([t, t])
        self.hover_line_a.set_visible(True)
        self.hover_line_b.set_xdata([t, t])
        self.hover_line_b.set_visible(True)
        self.canvas_a.draw_idle()
        self.canvas_b.draw_idle()

        nearest = self._find_nearest_line(event, idx)
        if nearest is None:
            self.lbl_hover_info.setText(f"游標: t={t:.1f}s")
        else:
            label, y_val = nearest
            if y_val != y_val:  # NaN
                self.lbl_hover_info.setText(f"游標: t={t:.1f}s ｜ {label}: N/A")
            else:
                self.lbl_hover_info.setText(f"游標: t={t:.1f}s ｜ {label}: {y_val:.3f}")

    def _on_leave(self, event):
        if self.hover_line_a is not None:
            self.hover_line_a.set_visible(False)
        if self.hover_line_b is not None:
            self.hover_line_b.set_visible(False)
        self.canvas_a.draw_idle()
        self.canvas_b.draw_idle()
        self.lbl_hover_info.setText("游標: -")

    def _find_nearest_line(self, event, idx):
        """找出游標在螢幕像素距離上最接近的資料線 (排除游標線/標記線本身)，回傳 (label, y_value)。"""
        axes_list = [self.ax1, self.ax2] if event.canvas is self.canvas_a else [self.ax_temp]

        skip = {self.hover_line_a, self.hover_line_b}
        skip |= {m.get('line_a') for m in self.pinned_markers}
        skip |= {m.get('line_b') for m in self.pinned_markers}

        best = None
        for ax in axes_list:
            for line in ax.get_lines():
                if line in skip:
                    continue
                xdata = line.get_xdata()
                ydata = line.get_ydata()
                if idx >= len(xdata) or idx >= len(ydata):
                    continue
                y_val = ydata[idx]
                if y_val != y_val:  # NaN
                    continue
                xt, yt = ax.transData.transform((xdata[idx], y_val))
                dist = (xt - event.x) ** 2 + (yt - event.y) ** 2
                if best is None or dist < best[0]:
                    best = (dist, line.get_label(), y_val)

        if best is None:
            return None
        return best[1], best[2]

    # --- 點擊釘選/移除標記線 ---
    def _on_button_press(self, event):
        if event.button == 1 and event.xdata is not None:
            self._press_xy = (event.x, event.y)
        else:
            self._press_xy = None

    def _on_button_release(self, event):
        press_xy = self._press_xy
        self._press_xy = None
        if press_xy is None or event.button != 1 or event.xdata is None:
            return

        dx = abs(event.x - press_xy[0])
        dy = abs(event.y - press_xy[1])
        if dx < 5 and dy < 5:  # 位移很小才視為「點擊」，避免跟框選縮放的拖曳手勢衝突
            self._toggle_pin_marker(event.xdata)

    def _toggle_pin_marker(self, x):
        with self.data_lock:
            times = list(self.time_data)
        idx = self._nearest_index(times, x)
        if idx is None:
            return
        t = times[idx]

        for m in self.pinned_markers:
            if m['time'] == t:
                self._remove_marker(m)
                self._render_marker_panel()
                self.canvas_a.draw_idle()
                self.canvas_b.draw_idle()
                return

        if len(self.pinned_markers) >= 3:
            QMessageBox.information(self, "標記已達上限", "最多同時釘選 3 條標記線，請先清除部分標記。")
            return

        color = MARKER_COLORS[len(self.pinned_markers) % len(MARKER_COLORS)]
        marker = {
            'time': t,
            'color': color,
            'line_a': self.ax1.axvline(t, color=color, linestyle='--', linewidth=1.2),
            'line_b': self.ax_temp.axvline(t, color=color, linestyle='--', linewidth=1.2),
        }
        self.pinned_markers.append(marker)
        self._render_marker_panel()
        self.canvas_a.draw_idle()
        self.canvas_b.draw_idle()

    def _remove_marker(self, marker):
        for key in ('line_a', 'line_b'):
            line = marker.get(key)
            if line is not None:
                try:
                    line.remove()
                except Exception:
                    pass
        if marker in self.pinned_markers:
            self.pinned_markers.remove(marker)

    def _clear_all_markers(self):
        for m in list(self.pinned_markers):
            self._remove_marker(m)
        self._render_marker_panel()
        self.canvas_a.draw_idle()
        self.canvas_b.draw_idle()

    def _render_marker_panel(self):
        """依目前釘選的標記線，列出該時間點所有已啟用通道的完整 V/I/溫度數值。"""
        if not self.pinned_markers:
            self.marker_panel.setPlainText("")
            return

        with self.data_lock:
            times = list(self.time_data)
            v_snapshot = {ch: list(self.v_data[ch]) for ch in self.active_channels}
            i_snapshot = {ch: list(self.i_data[ch]) for ch in self.active_channels}
            temp_snapshot = list(self.temp_data)

        max_gap = self.current_interval * 1.5
        lines = []
        for n, m in enumerate(self.pinned_markers, 1):
            idx = self._nearest_index(times, m['time'], max_gap=max_gap)
            header = f"標記 {n} ({m['color']}) @ t={m['time']:.1f}s"

            if idx is None:
                lines.append(header)
                lines.append("  (資料已捲出顯示緩衝區，數值無法讀取)")
                lines.append("")
                continue

            temp_str = "N/A"
            if idx < len(temp_snapshot):
                tv = temp_snapshot[idx]
                if tv == tv:  # not NaN
                    temp_str = f"{tv:.2f}°C"
            lines.append(f"{header} ｜ 溫度: {temp_str}")

            for ch in self.active_channels:
                v_vals = v_snapshot.get(ch, [])
                i_vals = i_snapshot.get(ch, [])
                v_str = f"{v_vals[idx]:.3f}V" if idx < len(v_vals) else "N/A"
                i_str = f"{i_vals[idx]:.3f}uA" if idx < len(i_vals) else "N/A"
                lines.append(f"  CH{ch}: V={v_str}, I={i_str}")
            lines.append("")

        self.marker_panel.setPlainText("\n".join(lines))

    # --- 1. OCV 偵測 ---
    def start_ocv(self):
        if not self.connect_inst(): return
        try:
            min_v = float(self.min_ocv_input.text())
            if not (2.8 <= min_v <= 4.3): raise ValueError
        except:
            QMessageBox.warning(self, "警告", "OCV 最低電壓必須介於 2.8V 至 4.3V 之間")
            return

        self.btn_detect.setEnabled(False)
        self.btn_cal.setEnabled(False)
        self.btn_start.setEnabled(False)
        
        for row in range(32):
            self.table.setItem(row, 1, QTableWidgetItem("X"))
            self.table.setItem(row, 2, QTableWidgetItem("測量中.."))
            self.table.setItem(row, 3, QTableWidgetItem("NA"))
            
        self.ocv_thread = OcvThread(self.inst, min_v)
        self.ocv_thread.finished_signal.connect(self.on_ocv_finished)
        self.ocv_thread.start()

    def on_ocv_finished(self, success, msg, active_chs, valid_ocvs):
        self.btn_detect.setEnabled(True)
        if success:
            self.active_channels = active_chs
            for row in range(32):
                ch = row + 1
                v = valid_ocvs[row]
                self.table.setItem(row, 2, QTableWidgetItem(f"{v:.3f}"))
                if ch in active_chs:
                    self.table.setItem(row, 1, QTableWidgetItem("V"))
                else:
                    self.table.setItem(row, 1, QTableWidgetItem("X"))
            
            if active_chs:
                self.btn_cal.setEnabled(True) 
                QMessageBox.information(self, "完成", msg + f"\n已自動勾選 {len(active_chs)} 個通道。")
            else:
                QMessageBox.warning(self, "警告", msg)
        else:
            QMessageBox.warning(self, "執行失敗", msg)

    # --- 2. In Situ 校準 ---
    def start_in_situ(self):
        self.btn_detect.setEnabled(False)
        self.btn_cal.setEnabled(False)
        
        for ch in self.active_channels:
            self.table.setItem(ch-1, 3, QTableWidgetItem("校準中.."))
            
        self.insitu_thread = InSituThread(self.inst, self.active_channels, self.cal_level_combo.currentText())
        self.insitu_thread.finished_signal.connect(self.on_insitu_finished)
        self.insitu_thread.start()

    def on_insitu_finished(self, success, msg, res_data):
        self.btn_detect.setEnabled(True)
        self.btn_cal.setEnabled(True)
        if success:
            res_idx = 0
            for ch in self.active_channels:
                self.table.setItem(ch-1, 3, QTableWidgetItem(f"{float(res_data[res_idx]):.3f}"))
                res_idx += 1
            
            QMessageBox.information(self, "完成", msg)
            self.btn_start.setEnabled(True) 
        else:
            for ch in self.active_channels:
                self.table.setItem(ch-1, 3, QTableWidgetItem("Error"))
            QMessageBox.warning(self, "執行失敗", msg)

    # --- 3. 開始測試 ---
    def start_test(self):
        filepath = self.filepath_input.text()
        if not filepath:
            QMessageBox.warning(self, "警告", "請先設定 CSV 檔案儲存路徑")
            return
            
        try:
            interval = int(self.interval_input.text())
            if interval < 5: raise ValueError
        except:
            QMessageBox.warning(self, "警告", "間隔時間必須為大於等於 5 的整數")
            return
            
        if not (self.chk_v.isChecked() or self.chk_i.isChecked()):
            QMessageBox.warning(self, "警告", "請在設定區至少勾選擷取電壓或電流")
            return

        self.btn_detect.setEnabled(False)
        self.btn_cal.setEnabled(False)
        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)

        with self.data_lock:
            self.time_data.clear()
            for i in range(1, 33):
                self.v_data[i].clear()
                self.i_data[i].clear()
            self.temp_data.clear()

        self.lines_v = {}
        self.lines_i = {}
        self.line_temp = None
        self.lbl_temp_value.setText("外部溫度: N/A")
        self.current_interval = interval

        # 新測試開始，清除上一次測試留下的標記線 (時間點在新資料中已無意義)
        self._clear_all_markers()
        if self.hover_line_a is not None:
            self.hover_line_a.set_visible(False)
        if self.hover_line_b is not None:
            self.hover_line_b.set_visible(False)
        self.lbl_hover_info.setText("游標: -")

        self.is_user_zoomed = False # 開始測試時預設自動對齊

        active_str = ",".join(map(str, self.active_channels))
        try:
            self.inst.write(f"INIT:TEST:MATC 720, 4.3, 2.5, 1.0, {interval}, 0.0001, 0.01, (@{active_str})")
        except Exception as e:
            QMessageBox.critical(self, "啟動失敗", str(e))
            self.stop_test()
            return

        fetch_temp = self.chk_temp.isChecked()

        # CSV 檔案在測試期間保持開啟，避免每筆資料都重新開關檔案（長時間測試可達數十萬筆）
        self.csv_file = open(filepath, mode='w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        header = ["Time(s)"]
        for ch in self.active_channels:
            if self.chk_v.isChecked(): header.append(f"CH{ch}_V")
            if self.chk_i.isChecked(): header.append(f"CH{ch}_uA")
        if fetch_temp:
            header.append("Temp_C")
        self.csv_writer.writerow(header)
        self.csv_file.flush()

        self.fetch_thread = FetchThread(
            self.inst, self.active_channels, interval,
            self.chk_v.isChecked(), self.chk_i.isChecked(), fetch_temp,
            self.csv_writer, self.csv_file, self.data_lock,
            self.time_data, self.v_data, self.i_data, self.temp_data
        )
        self.fetch_thread.update_signal.connect(lambda: self.update_plot(force_redraw=False))
        self.fetch_thread.error_signal.connect(lambda e: print(e))
        self.fetch_thread.temp_signal.connect(self.on_temp_update)
        self.fetch_thread.start()

    def update_plot(self, force_redraw=False):
        """
        繪圖更新分為兩種路徑（同時更新圖A「電壓/電流」與圖B「溫度」兩張圖）：
        - 結構性重建 (force_redraw=True，或啟用通道集合改變，或溫度曲線顯示與否對不上)：
          clear 後完整重繪，含 legend，並重新建立游標線/標記線 (clear() 會把它們一併清掉)。
        - 一般資料更新：只用 set_data 更新既有 Line2D，避免每次都整張圖重繪，
          長時間測試、通道數多時可大幅降低繪圖負擔。
        """
        show_v = self.plot_chk_v.isChecked()
        show_i = self.plot_chk_i.isChecked()
        show_temp = self.plot_chk_temp.isChecked()

        existing_line_channels = set(self.lines_v.keys()) | set(self.lines_i.keys())
        channels_changed = existing_line_channels != set(self.active_channels)
        temp_line_mismatch = show_temp != (self.line_temp is not None)
        need_full_rebuild = force_redraw or channels_changed or temp_line_mismatch

        with self.data_lock:
            time_snapshot = list(self.time_data)
            v_snapshot = {ch: list(self.v_data[ch]) for ch in self.active_channels}
            i_snapshot = {ch: list(self.i_data[ch]) for ch in self.active_channels}
            temp_snapshot = list(self.temp_data)

        if need_full_rebuild:
            # 記住目前的縮放視野，若仍在「使用者縮放模式」，重建後要還原
            cur_xlim = self.ax1.get_xlim()
            cur_ylim1 = self.ax1.get_ylim()
            cur_ylim2 = self.ax2.get_ylim()
            cur_ylim3 = self.ax_temp.get_ylim()

            self.ax1.clear()
            self.ax2.clear()
            self.ax_temp.clear()
            self.lines_v = {}
            self.lines_i = {}
            self.line_temp = None

            self.ax1.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            self.ax1.set_xlabel("Time (s)")
            self.ax_temp.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            self.ax_temp.set_xlabel("Time (s)")

            for ch in self.active_channels:
                color = self.channel_colors[ch].name()

                if show_v:
                    line, = self.ax1.plot(time_snapshot, v_snapshot[ch], color=color, label=f"CH{ch} (V)")
                    self.lines_v[ch] = line

                if show_i:
                    line, = self.ax2.plot(time_snapshot, i_snapshot[ch], color=color, linestyle=':', label=f"CH{ch} (uA)")
                    self.lines_i[ch] = line

            if show_temp:
                line, = self.ax_temp.plot(time_snapshot, temp_snapshot, color='black', linewidth=1.5,
                                           label="External Temp (°C)")
                self.line_temp = line

            if show_v:
                self.ax1.set_ylabel("Voltage (V)")
                self.ax1.legend(loc="upper left", fontsize='small')
                self.ax1.get_yaxis().set_visible(True)
            else:
                self.ax1.get_yaxis().set_visible(False)

            if show_i:
                self.ax2.get_yaxis().set_visible(True)
                self.ax2.set_ylabel("Current (uA)")
                self.ax2.legend(loc="upper right", fontsize='small')
            else:
                self.ax2.get_yaxis().set_visible(False)

            if show_temp:
                self.ax_temp.set_ylabel("Temperature (°C)")
                self.ax_temp.legend(loc="upper right", fontsize='small')

            # clear() 會把游標線與標記線一併清掉，這裡重新建立
            self.hover_line_a = self.ax1.axvline(0, color='gray', linewidth=1, linestyle='-', visible=False)
            self.hover_line_b = self.ax_temp.axvline(0, color='gray', linewidth=1, linestyle='-', visible=False)
            for m in self.pinned_markers:
                m['line_a'] = self.ax1.axvline(m['time'], color=m['color'], linestyle='--', linewidth=1.2)
                m['line_b'] = self.ax_temp.axvline(m['time'], color=m['color'], linestyle='--', linewidth=1.2)

            # 若使用者曾經縮放，維持使用者的視野；否則啟動自動對齊 (兩圖 X 軸同步)
            if self.is_user_zoomed and not force_redraw:
                self.ax1.set_xlim(cur_xlim)
                self.ax_temp.set_xlim(cur_xlim)
                self.ax1.set_ylim(cur_ylim1)
                self.ax2.set_ylim(cur_ylim2)
                self.ax_temp.set_ylim(cur_ylim3)
            else:
                self._auto_scale_all(time_snapshot, show_v, show_i, show_temp)
        else:
            # 增量更新：只更新既有線條的資料，不重建座標軸與 legend
            for ch in self.active_channels:
                if show_v and ch in self.lines_v:
                    self.lines_v[ch].set_data(time_snapshot, v_snapshot[ch])
                if show_i and ch in self.lines_i:
                    self.lines_i[ch].set_data(time_snapshot, i_snapshot[ch])
            if show_temp and self.line_temp is not None:
                self.line_temp.set_data(time_snapshot, temp_snapshot)

            if not self.is_user_zoomed:
                self._auto_scale_all(time_snapshot, show_v, show_i, show_temp)

        self.canvas_a.draw_idle()
        self.canvas_b.draw_idle()

    def _close_csv_file(self):
        if self.csv_file is not None:
            try:
                self.csv_file.close()
            except:
                pass
            self.csv_file = None
            self.csv_writer = None

    def stop_test(self):
        if hasattr(self, 'fetch_thread'):
            self.fetch_thread.stop()
            self.fetch_thread.wait()

        try:
            self.inst.write("ABORt")
        except:
            pass

        self._close_csv_file()

        self.btn_detect.setEnabled(True)
        if self.active_channels: self.btn_cal.setEnabled(True)
        if self.active_channels: self.btn_start.setEnabled(True)
        self.btn_stop.setEnabled(False)

    def closeEvent(self, event):
        if hasattr(self, 'fetch_thread') and self.fetch_thread.isRunning():
            self.fetch_thread.stop()
            self.fetch_thread.wait()
        self._close_csv_file()
        if self.inst:
            try: self.inst.write("ABORt")
            except: pass
            self.inst.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BT2152App()
    window.show()
    sys.exit(app.exec_())