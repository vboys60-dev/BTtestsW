#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:42:48 2026

@author: lianshi
"""

import sys
import os

# pyqtgraph 若偵測到系統同時裝有多套 Qt binding (PyQt5/PyQt6/PySide6...)，
# 預設可能選到跟本程式（PyQt5）不同的一套，導致 QApplication 不匹配而崩潰。
# 必須在 `import pyqtgraph` 之前強制指定，確保跟其餘程式碼使用同一套 Qt binding。
os.environ.setdefault("PYQTGRAPH_QT_LIB", "PyQt5")

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
                             QColorDialog, QGridLayout, QSplitter,
                             QProgressBar, QSpinBox)
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QPointF, QTimer
from PyQt5.QtGui import QColor

import pyqtgraph as pg

# 標記線色盤（最多同時釘選 2 條，依序指派不同顏色）
MARKER_COLORS = ['#e63946', '#2a9d8f']

# 深色主題 QSS（取代 Qt 預設淺色系統風格；按鈕等需要語意色的元件仍保留各自的 inline setStyleSheet，
# 其優先權高於這裡的全域規則，不會互相衝突）
DARK_QSS = """
QMainWindow, QWidget {
    background-color: #1e1f26;
    color: #e8e8ea;
    font-size: 13px;
}
QGroupBox {
    background-color: #2a2b33;
    border: 1px solid #3a3b45;
    border-radius: 8px;
    margin-top: 10px;
    padding-top: 6px;
    font-weight: bold;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 4px;
    color: #c9c9cf;
}
QLabel {
    color: #c9c9cf;
    background: transparent;
}
QLineEdit, QComboBox, QSpinBox {
    background-color: #33343d;
    border: 1px solid #4a4b56;
    border-radius: 4px;
    padding: 3px 6px;
    color: #e8e8ea;
    selection-background-color: #5b8def;
}
QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
    border: 1px solid #5b8def;
}
QLineEdit:read-only {
    color: #9a9ba5;
}
QComboBox QAbstractItemView {
    background-color: #2a2b33;
    color: #e8e8ea;
    selection-background-color: #3d5a80;
}
QCheckBox {
    color: #e8e8ea;
    background: transparent;
}
QPushButton {
    background-color: #33343d;
    border: 1px solid #4a4b56;
    border-radius: 6px;
    padding: 5px 10px;
    color: #e8e8ea;
}
QPushButton:hover {
    background-color: #3d3e4a;
}
QPushButton:pressed {
    background-color: #2a2b33;
}
QPushButton:disabled {
    background-color: #2a2b33;
    color: #6a6b75;
    border: 1px solid #3a3b45;
}
QTableWidget {
    background-color: #26272e;
    alternate-background-color: #2c2d35;
    gridline-color: #3a3b45;
    color: #e8e8ea;
    border: 1px solid #3a3b45;
    selection-background-color: #3d5a80;
}
QHeaderView::section {
    background-color: #2a2b33;
    color: #c9c9cf;
    padding: 4px;
    border: 1px solid #3a3b45;
}
QProgressBar {
    background-color: #33343d;
    border: 1px solid #4a4b56;
    border-radius: 4px;
    text-align: center;
    color: #e8e8ea;
}
QProgressBar::chunk {
    background-color: #3d5a80;
    border-radius: 4px;
}
QSplitter::handle {
    background-color: #3a3b45;
}
QToolTip {
    background-color: #2a2b33;
    color: #e8e8ea;
    border: 1px solid #4a4b56;
}
"""

# ==========================================
# 背景執行緒 1：獨立用於執行 OCV 偵測
# ==========================================
OCV_WAIT_TIMEOUT_S = 300      # OCV 量測正常約數秒；逾時代表指令被拒或保護跳脫
INSITU_WAIT_TIMEOUT_S = 600   # in situ 導線電阻校準最長約 2 分鐘，留 5 倍餘裕


class _PollingThread(QThread):
    """共用的 `SENS:*:AVAIlable?` 輪詢：原本的 while 迴圈沒有逾時也沒有取消旗標，
    指令被拒或保護事件發生時會永久空轉，對應的按鈕就永遠 disabled，關窗也停不下來。"""

    def __init__(self, inst):
        super().__init__()
        self.inst = inst
        self._cancelled = False

    def stop(self):
        self._cancelled = True

    def _wait_available(self, query, timeout_s, settle_s=10):
        """回傳 True=儀器回報完成；False=被 stop() 取消（呼叫端應直接結束，不發 signal）。
        逾時則丟 TimeoutError，由 run() 既有的 except 轉成 finished_signal(False, ...)。

        進入等待迴圈前先等 AVAI? 翻回 0，確認儀器已受理這次的指令。
        `INIT:TEST:OCV` / `CAL:WIRE:RES:INS` 都是 overlapped command，write() 送出後儀器未必
        已開始執行，直接輪詢會讀到上一輪殘留的 1，於是 FETC 取回的是上一輪的舊資料。
        手冊建議用 *OPC? 同步，但 *OPC? 會一路阻塞到操作完成（in situ 校準約 2 分鐘，遠超過
        inst.timeout=10 秒），而且阻塞期間無法取消，closeEvent 就收不掉這個執行緒。
        等 AVAI? 歸零則不阻塞、可取消，最壞情況（settle_s 內沒讀到 0）也只是退回原本的行為。"""
        settle_deadline = time.time() + settle_s
        while not self._cancelled and time.time() < settle_deadline:
            if int(self.inst.query(query)) == 0:
                break
            time.sleep(0.2)

        deadline = time.time() + timeout_s
        while not self._cancelled:
            if int(self.inst.query(query)) == 1:
                return True
            if time.time() > deadline:
                raise TimeoutError(f"等待 {query} 逾時（{timeout_s} 秒），請檢查儀器狀態或保護事件")
            time.sleep(1)
        return False


class OcvThread(_PollingThread):
    finished_signal = pyqtSignal(bool, str, list, list)

    def __init__(self, inst, min_ocv):
        super().__init__(inst)
        self.min_ocv = min_ocv

    def run(self):
        try:
            self.inst.write("INIT:TEST:OCV 4.5, 0.5, 0.01, 1, (@1:32)")
            if not self._wait_available("SENS:OCV:AVAI?", OCV_WAIT_TIMEOUT_S):
                return

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
class InSituThread(_PollingThread):
    finished_signal = pyqtSignal(bool, str, list)

    def __init__(self, inst, active_channels, cal_level):
        super().__init__(inst)
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
            if not self._wait_available("SENS:WIRE:RES:AVAI?", INSITU_WAIT_TIMEOUT_S):
                return

            res_data = self.inst.query(f"CAL:WIRE:RES:VAL? (@{active_str})").strip().split(',')
            self.inst.write("CAL:WIRE:RES:SAVE 1")
            
            self.finished_signal.emit(True, "In Situ 校準完成，並已存入記憶體 1。", res_data)
            
        except Exception as e:
            self.finished_signal.emit(False, f"校準執行錯誤: {str(e)}", [])

# ==========================================
# 背景執行緒 3：用於定時從內部記憶體撈取測試資料
# ==========================================
# 儀器以 +9.91E37 表示「此筆無效」：外部感測器未接、通道觸發 OVP/UVP 保護、電池被拔除等。
# 直接收進繪圖資料會把 Y 軸 autorange 拉到 1e37，其他曲線全被壓平。
SENTINEL_THRESHOLD = 1e30

# INIT:TEST:MATChed 的保護參數，目前未做成 GUI 選項（手冊範圍註記於後，日後接 UI 從這裡改）
TEST_OVP_V = 4.3        # 過電壓保護，手冊 0.5~4.5 V
TEST_UVP_V = 2.5        # 低電壓保護，手冊 0.5~4.5 V
TEST_RES_OHM = 1.0      # 放電電阻，BT2152A 0.1~10Ω / BT2152B 0.05~10Ω
TEST_CURR_A = 0.0001    # 匹配電流，手冊 ±10 mA
TEST_OCP_A = 0.01       # 過電流保護，手冊 ±10 mA


# 手冊：ASCII 格式的 FETC:*:LOG? 單次最多回傳 8192 個值，而實際回傳量 = 點數 × 通道數。
# 32 通道時只要一次要超過 256 點就會被截斷（例：VISA 卡住數分鐘後欠的點全部累積）。
MAX_ASCII_VALUES = 8192

# 連續這麼多輪都失敗就停止擷取並通知 UI。否則儀器斷線時 GUI 會一直顯示「測試進行中」，
# 進度條照跑，實際上 CSV 早就停止增長。
MAX_ERROR_STREAK = 5


def _nan_if_sentinel(val):
    return float('nan') if val > SENTINEL_THRESHOLD else val


class FetchThread(QThread):
    update_signal = pyqtSignal()
    error_signal = pyqtSignal(str)
    fatal_signal = pyqtSignal(str)
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
        self._stop_event = threading.Event()
        self.current_offset = 0
        self._error_streak = 0
        self._temp_error_streak = 0
        self._fatal_error = False
        self._csv_error = False

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

    def _max_points_per_batch(self):
        return max(1, MAX_ASCII_VALUES // max(1, len(self.active_channels)))

    def _fetch_log(self, cmd, points_to_read, expected):
        """撈一批 log 並驗證長度。長度不符就整批丟棄（丟例外），不寫入任何 deque、
        不推進 offset，下一輪重取。一旦讓半批寫進去，time_data 與 v_data[ch] 會永久
        錯開，之後每次 update_plot() 都丟 X and Y arrays must be the same shape。"""
        active_str = ",".join(map(str, self.active_channels))
        raw = self.inst.query(f"{cmd} {points_to_read}, {self.current_offset}, (@{active_str})").strip().split(',')
        if len(raw) != expected:
            raise ValueError(f"{cmd} 回傳 {len(raw)} 筆，預期 {expected} 筆（回應可能被截斷）")
        return [_nan_if_sentinel(float(x)) for x in raw]

    def _fetch_new_temperatures(self, points_to_read):
        """溫度 log 與電壓 log 由儀器以同一個 tint 記錄，索引一一對應，所以直接用
        current_offset 當基準，不再維護獨立的 temp_offset —— 獨立 offset 在兩邊點數不同步時
        會讓 temp_data 比 time_data 短，line_temp.setData() 直接丟 shape mismatch。
        取不到就回較短的 list，由呼叫端補 NaN，時間軸一律以電壓 log 為準。"""
        try:
            pts_str = self.inst.query("FETC:TEMP:LOG:POIN?").strip()
            available = int(pts_str) if pts_str else 0
            temp_to_read = min(points_to_read, available - self.current_offset)
            values = []
            if temp_to_read > 0:
                temp_str = self.inst.query(f"FETC:TEMP:LOG? {temp_to_read}, {self.current_offset}").strip().split(',')
                # 9.91E37 代表外部感測器未接
                values = [None if float(v) > SENTINEL_THRESHOLD else float(v) for v in temp_str[:temp_to_read]]
            self._temp_error_streak = 0
            return values
        except Exception as e:
            self._temp_error_streak += 1
            self.error_signal.emit(f"溫度擷取錯誤（連續 {self._temp_error_streak} 次；本批補 NaN）: {e}")
            return []

    def _fetch_once(self):
        """撈一批資料並寫出。回傳 True 表示這輪有進度（可能還有欠的點，可立刻再撈下一批）。"""
        if self._fatal_error or self._csv_error:
            return False
        pts_str = self.inst.query("FETC:VOLT:LOG:POIN?").strip()
        if not pts_str:
            return False

        remaining = int(pts_str) - self.current_offset
        if remaining <= 0:
            return False

        points_to_read = min(remaining, self._max_points_per_batch())
        expected = points_to_read * len(self.active_channels)

        # 電壓／電流 query 在寫入之前完成；溫度失敗則獨立警告並補 NaN。
        v_vals = self._fetch_log("FETC:VOLT:LOG?", points_to_read, expected) if self.fetch_v else []
        i_vals = [v * 1e6 for v in self._fetch_log("FETC:CURR:LOG?", points_to_read, expected)] if self.fetch_i else []
        temp_vals = self._fetch_new_temperatures(points_to_read) if self.fetch_temp else []

        rows = []
        for pt_idx in range(points_to_read):
            # 依照擷取頻率計算時間(秒)
            t_s = (self.current_offset + pt_idx + 1) * self.interval
            row_data = [f"{t_s:.1f}"]

            for ch_idx, ch in enumerate(self.active_channels):
                flat_idx = ch_idx * points_to_read + pt_idx
                if self.fetch_v:
                    v = v_vals[flat_idx]
                    row_data.append("" if math.isnan(v) else f"{v:.3f}")
                if self.fetch_i:
                    i_val = i_vals[flat_idx]
                    row_data.append("" if math.isnan(i_val) else f"{i_val:.3f}")

            if self.fetch_temp:
                t_val = temp_vals[pt_idx] if pt_idx < len(temp_vals) else None
                row_data.append("" if t_val is None else f"{t_val:.2f}")

            rows.append(row_data)

        try:
            for row_data in rows:
                self.csv_writer.writerow(row_data)
            self.csv_file.flush()
        except (OSError, ValueError) as e:
            # CSV 可能已寫入部分資料，不能重試同一批，否則 deque 與 CSV 都會重複。
            self._csv_error = True
            self._fatal_error = True
            self.stop()
            self.fatal_signal.emit(f"CSV 寫入失敗，已停止擷取，不再重試：{e}")
            return False

        # 整批寫入並 flush 成功後，才讓圖表看見這批資料。
        with self.data_lock:
            for pt_idx in range(points_to_read):
                self.time_data.append((self.current_offset + pt_idx + 1) * self.interval)
                for ch_idx, ch in enumerate(self.active_channels):
                    flat_idx = ch_idx * points_to_read + pt_idx
                    if self.fetch_v:
                        self.v_data[ch].append(v_vals[flat_idx])
                    if self.fetch_i:
                        self.i_data[ch].append(i_vals[flat_idx])
                if self.fetch_temp:
                    # 溫度不足補 NaN，維持各 deque 長度一致。
                    t_val = temp_vals[pt_idx] if pt_idx < len(temp_vals) else None
                    self.temp_data.append(float('nan') if t_val is None else t_val)

        if self.fetch_temp and temp_vals:
            last_valid = temp_vals[-1]
            self.temp_signal.emit(last_valid if last_valid is not None else float('nan'))

        self.current_offset += points_to_read
        self.update_signal.emit()
        return True

    def run(self):
        sleep_time = self._poll_sleep_seconds()

        while self.is_running:
            try:
                # 有進度就不睡，直接撈下一批，讓分批上限不會拖慢追平積欠點數的速度
                progressed = self._fetch_once()
                if self._fatal_error:
                    return
                self._error_streak = 0
            except Exception as e:
                progressed = False
                self._error_streak += 1
                self.error_signal.emit(f"擷取資料錯誤({self._error_streak}/{MAX_ERROR_STREAK}): {str(e)}")
                if self._error_streak >= MAX_ERROR_STREAK:
                    self._fatal_error = True
                    self.is_running = False
                    self.fatal_signal.emit(f"連續 {MAX_ERROR_STREAK} 次擷取失敗，已停止擷取：{str(e)}")
                    return

            if not progressed:
                self._stop_event.wait(sleep_time)

    def stop(self):
        self.is_running = False
        self._stop_event.set()

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

        if cmd in ("SYST:ERR?", "SYST:ERRor?"):
            return '+0,"No error"'

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
        self.setStyleSheet(DARK_QSS)

        try:
            self.rm = pyvisa.ResourceManager()
        except Exception:
            self.rm = None
        self.inst = None
        self.active_channels = []

        # 通道預設顏色自動分色，避免 32 通道全部同色難以辨識
        # minValue/sat 拉高避免在深色背景下部分色相（深藍/深綠）對比不足
        self.channel_colors = {
            i: pg.intColor(i - 1, hues=32, minValue=180, sat=220)
            for i in range(1, 33)
        }


        self.max_points = 1000
        self.time_data = deque(maxlen=self.max_points)
        self.v_data = {i: deque(maxlen=self.max_points) for i in range(1, 33)}
        self.i_data = {i: deque(maxlen=self.max_points) for i in range(1, 33)}
        self.temp_data = deque(maxlen=self.max_points)

        self.data_lock = threading.Lock() # 保護 FetchThread 寫入與主執行緒繪圖讀取之間的資料一致性
        self.lines_v = {}  # 通道 -> 電壓 Line2D，供增量更新繪圖
        self.lines_i = {}  # 通道 -> 電流 Line2D，供增量更新繪圖
        self._plotted_channels = set()
        self.line_temp = None  # 外部溫度 Line2D，供增量更新繪圖

        self.hover_line_a = None  # 圖A 游標對照線 (setup_ui 中建立)
        self.hover_line_b = None  # 圖B 游標對照線 (setup_ui 中建立)
        self.pinned_markers = []  # 已釘選的標記線: [{'time','color','line_a','line_b'}, ...]，最多 2 筆
        self.marker_info_item = None  # 圖A 右上角標記資訊文字方塊 (setup_ui 中建立)
        self.current_interval = 30  # 目前測試的擷取間隔（供標記面板判斷資料是否已捲出緩衝區）

        # 通道是否顯示於圖表 (僅影響繪圖，不影響資料記錄/CSV)，預設全部顯示
        self.channel_display = {i: True for i in range(1, 33)}

        # 記錄總時間 / 進度條
        self.test_start_time = None
        self.test_duration = None
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self._update_test_progress)

        self.csv_file = None
        self.csv_writer = None
        self._stopping = True  # 停止後維持，直到下一次開始測試。
        self._connected_addr = None
        self.fetched_v = self.fetched_i = self.fetched_temp = False

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
        self.btn_search.setEnabled(self.rm is not None)
        self.btn_search.clicked.connect(self.search_instruments)
        grid.addWidget(self.btn_search, 2, 2)

        grid.addWidget(QLabel("總紀錄時間(HH:MM:SS，留空=不限制):"), 2, 3)
        self.duration_input = QLineEdit("")
        self.duration_input.setPlaceholderText("HH:MM:SS")
        self.duration_input.setToolTip("設定測試自動停止的總時間，格式為 HH:MM:SS(例如 01:30:00 代表 1 小時 30 分)，時間到會自動停止測試；留空代表不限制。")
        grid.addWidget(self.duration_input, 2, 4)

        settings_group.setLayout(grid)
        main_layout.addWidget(settings_group)
        
        # --- 獨立操作按鈕區 ---
        btn_layout = QHBoxLayout()
        action_btn_style = """
            QPushButton {{
                background-color: {bg}; color: white; font-weight: bold;
                padding: 10px; border: none; border-radius: 6px;
            }}
            QPushButton:hover {{ background-color: {hover}; }}
            QPushButton:pressed {{ background-color: {pressed}; }}
            QPushButton:disabled {{ background-color: #33343d; color: #6a6b75; }}
        """

        self.btn_detect = QPushButton("1. OCV 偵測")
        self.btn_detect.setStyleSheet(action_btn_style.format(bg="#3b6ea5", hover="#4a7fba", pressed="#325d8c"))
        self.btn_detect.clicked.connect(self.start_ocv)

        self.btn_cal = QPushButton("2. In Situ 校準 (依OCV結果)")
        self.btn_cal.setStyleSheet(action_btn_style.format(bg="#b8863d", hover="#c99a51", pressed="#9c7133"))
        self.btn_cal.setEnabled(False)
        self.btn_cal.clicked.connect(self.start_in_situ)

        self.btn_start = QPushButton("3. 開始測試")
        self.btn_start.setStyleSheet(action_btn_style.format(bg="#3f9d5c", hover="#4db06e", pressed="#35854e"))
        self.btn_start.setEnabled(False)
        self.btn_start.clicked.connect(self.start_test)

        self.btn_stop = QPushButton("中斷測試")
        self.btn_stop.setStyleSheet(action_btn_style.format(bg="#b23b3b", hover="#c74a4a", pressed="#973131"))
        self.btn_stop.setEnabled(False)
        self.btn_stop.clicked.connect(self.stop_test)
        
        btn_layout.addWidget(self.btn_detect)
        btn_layout.addWidget(self.btn_cal)
        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)

        self.lbl_conn_status = QLabel("● 未連線")
        self.lbl_conn_status.setStyleSheet("color: #9a9ba5; font-weight: bold; padding-left: 10px;")
        btn_layout.addWidget(self.lbl_conn_status)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("測試進度: %p%")
        self.progress_bar.setFixedWidth(180)
        btn_layout.addWidget(self.progress_bar)

        btn_layout.addStretch()

        main_layout.addLayout(btn_layout)
        
        # --- 底部視圖區 (Table + Plot)，改用 QSplitter 讓表格可收合/可拖曳調整寬度 ---
        bottom_layout = QSplitter(Qt.Horizontal)
        bottom_layout.setChildrenCollapsible(False)  # 避免手動拖曳分隔線把面板拖到 0 寬度而連按鈕都消失
        self.bottom_splitter = bottom_layout

        table_container = QWidget()
        table_container_layout = QVBoxLayout(table_container)
        table_container_layout.setContentsMargins(0, 0, 0, 0)

        table_header_layout = QHBoxLayout()
        self.lbl_table_header = QLabel("通道列表")
        table_header_layout.addWidget(self.lbl_table_header)
        self.btn_toggle_table = QPushButton("◀ 收合")
        self.btn_toggle_table.setToolTip("設定完通道後可收合此列表，讓圖表區域有更多顯示空間。")
        self.btn_toggle_table.clicked.connect(self.toggle_table_panel)
        table_header_layout.addWidget(self.btn_toggle_table)
        table_header_layout.addStretch()
        table_container_layout.addLayout(table_header_layout)

        display_toggle_layout = QHBoxLayout()
        display_toggle_layout.addWidget(QLabel("圖表顯示:"))
        self.btn_display_select_all = QPushButton("全選")
        self.btn_display_select_all.setToolTip("勾選全部通道，皆顯示於圖表上 (不影響資料記錄)。")
        self.btn_display_select_all.clicked.connect(lambda: self._set_all_channel_display(True))
        display_toggle_layout.addWidget(self.btn_display_select_all)
        self.btn_display_select_none = QPushButton("全不選")
        self.btn_display_select_none.setToolTip("取消全部通道顯示，再自行勾選要觀察的通道。")
        self.btn_display_select_none.clicked.connect(lambda: self._set_all_channel_display(False))
        display_toggle_layout.addWidget(self.btn_display_select_none)
        display_toggle_layout.addStretch()
        table_container_layout.addLayout(display_toggle_layout)

        self.table = QTableWidget(32, 6)
        self.table.setHorizontalHeaderLabels(["CH", "狀態", "OCV(V)", "電阻(Ω)", "顏色", "顯示"])
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.cellDoubleClicked.connect(self.change_color)

        self.table.setColumnWidth(0, 40)
        self.table.setColumnWidth(1, 40)
        self.table.setColumnWidth(2, 60)
        self.table.setColumnWidth(3, 70)
        self.table.setColumnWidth(4, 70)
        self.table.setColumnWidth(5, 45)

        for row in range(32):
            self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.table.setItem(row, 1, QTableWidgetItem("X"))
            self.table.setItem(row, 2, QTableWidgetItem("NA"))
            self.table.setItem(row, 3, QTableWidgetItem("NA"))
            color_item = QTableWidgetItem("雙擊修改")
            color_item.setBackground(self.channel_colors[row+1])
            self.table.setItem(row, 4, color_item)

            disp_item = QTableWidgetItem()
            disp_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            disp_item.setCheckState(Qt.Checked)
            disp_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 5, disp_item)

        # 初始化完成後才接線，避免上面初始化過程中觸發不必要的 update_plot
        self.table.itemChanged.connect(self._on_table_item_changed)

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

        # 曲線樣式設定區 (電壓/電流各自可選實線/虛線與粗度)
        line_style_layout = QHBoxLayout()
        line_style_layout.addWidget(QLabel("電壓線樣式:"))
        self.combo_v_style = QComboBox()
        self.combo_v_style.addItems(["實線", "虛線"])
        self.combo_v_style.currentIndexChanged.connect(lambda: self.update_plot(force_redraw=True))
        line_style_layout.addWidget(self.combo_v_style)

        line_style_layout.addWidget(QLabel("粗度:"))
        self.spin_v_width = QSpinBox()
        self.spin_v_width.setRange(1, 6)
        self.spin_v_width.setValue(2)
        self.spin_v_width.valueChanged.connect(lambda: self.update_plot(force_redraw=True))
        line_style_layout.addWidget(self.spin_v_width)

        line_style_layout.addWidget(QLabel("電流線樣式:"))
        self.combo_i_style = QComboBox()
        self.combo_i_style.addItems(["虛線", "實線"])
        self.combo_i_style.currentIndexChanged.connect(lambda: self.update_plot(force_redraw=True))
        line_style_layout.addWidget(self.combo_i_style)

        line_style_layout.addWidget(QLabel("粗度:"))
        self.spin_i_width = QSpinBox()
        self.spin_i_width.setRange(1, 6)
        self.spin_i_width.setValue(1)
        self.spin_i_width.valueChanged.connect(lambda: self.update_plot(force_redraw=True))
        line_style_layout.addWidget(self.spin_i_width)

        line_style_layout.addStretch()
        plot_wrapper.addLayout(line_style_layout)

        # --- 圖表 A：電壓/電流 (雙 Y 軸，電流用疊加的第二個 ViewBox 實現) ---
        pg.setConfigOptions(antialias=True, background='#1e1f26', foreground='#c9c9cf')

        self.plot_a = pg.PlotWidget()
        self.plot_item_a = self.plot_a.getPlotItem()
        self.plot_item_a.setLabel('bottom', 'Time (s)')
        self.plot_item_a.setLabel('left', 'Voltage (V)')
        self.plot_item_a.showGrid(x=True, y=True, alpha=0.15)
        self.legend_a = self.plot_item_a.addLegend(offset=(10, 10))

        self.plot_item_a.showAxis('right')
        self.plot_item_a.getAxis('right').setLabel('Current (uA)')
        self.vb_current = pg.ViewBox()
        self.plot_item_a.scene().addItem(self.vb_current)
        self.plot_item_a.getAxis('right').linkToView(self.vb_current)
        self.vb_current.setXLink(self.plot_item_a)
        self.vb_current.setMouseEnabled(x=False, y=False)  # 只有主視圖(電壓)接收拖曳/框選，電流軸的 Y 持續自動 fit
        self.vb_current.enableAutoRange(axis=pg.ViewBox.YAxis, enable=True)

        def _sync_current_viewbox():
            self.vb_current.setGeometry(self.plot_item_a.vb.sceneBoundingRect())
            self.vb_current.linkedViewChanged(self.plot_item_a.vb, self.vb_current.XAxis)
        self.plot_item_a.vb.sigResized.connect(_sync_current_viewbox)
        _sync_current_viewbox()

        self.plot_item_a.vb.sigRangeChanged.connect(lambda *a: self._reposition_marker_info())

        plot_wrapper.addWidget(self.plot_a, 3)  # 電壓/電流圖佔較大比例

        # --- 圖表 B：外部溫度 (單一 Y 軸) ---
        self.plot_b = pg.PlotWidget()
        self.plot_item_b = self.plot_b.getPlotItem()
        self.plot_item_b.setLabel('bottom', 'Time (s)')
        self.plot_item_b.setLabel('left', 'Temperature (°C)')
        self.plot_item_b.showGrid(x=True, y=True, alpha=0.15)
        self.legend_b = self.plot_item_b.addLegend(offset=(10, 10))

        # X 軸同步：兩圖平移/縮放連動。改用 sigRangeChangedManually 手動雙向同步而非
        # setXLink()：(1) 圖A 顯示了右側電流軸、圖B 沒有，兩圖繪圖區寬度不同，
        # setXLink() 內部依幾何比例換算連動範圍時會跑掉 (經測試證實)；(2) sigXRangeChanged
        # 在 autorange 自動重算時也會觸發，若拿來同步會把「autorange 算出來的變化」
        # 誤判成使用者手動縮放，進而把另一張圖的 autorange 關掉。
        # sigRangeChangedManually 只在真正的滑鼠拖曳/滾輪縮放時才會觸發，不會被
        # setRange() 或 autorange 重算觸發，因此不需要額外的防遞迴 guard。
        def _sync_a_to_b(mask):
            r = self.plot_item_a.vb.viewRange()[0]
            self.plot_item_b.vb.setXRange(*r, padding=0)

        def _sync_b_to_a(mask):
            r = self.plot_item_b.vb.viewRange()[0]
            self.plot_item_a.vb.setXRange(*r, padding=0)

        self.plot_item_a.vb.sigRangeChangedManually.connect(_sync_a_to_b)
        self.plot_item_b.vb.sigRangeChangedManually.connect(_sync_b_to_a)

        plot_wrapper.addWidget(self.plot_b, 1)  # 溫度圖佔較小比例

        # 框選縮放：左鍵拖曳畫框即可縮放 (pyqtgraph 原生支援，跟滾輪縮放並存，不用額外接線)
        self.plot_item_a.vb.setMouseMode(pg.ViewBox.RectMode)
        self.plot_item_b.vb.setMouseMode(pg.ViewBox.RectMode)

        # 游標對照線 (初始隱藏)，懸停時兩圖同步顯示同一時間點；標記資訊文字方塊
        self._create_overlay_items()

        # 懸停游標對照線
        self._hover_proxy_a = pg.SignalProxy(self.plot_item_a.scene().sigMouseMoved, rateLimit=30,
                                              slot=lambda evt: self._on_hover(evt[0], self.plot_item_a))
        self._hover_proxy_b = pg.SignalProxy(self.plot_item_b.scene().sigMouseMoved, rateLimit=30,
                                              slot=lambda evt: self._on_hover(evt[0], self.plot_item_b))
        self.plot_a.leaveEvent = lambda ev: self._on_leave()
        self.plot_b.leaveEvent = lambda ev: self._on_leave()

        # 點擊釘選/移除標記線 (sigMouseClicked 原生區分點擊與拖曳，不需要自己算像素位移)
        self.plot_item_a.scene().sigMouseClicked.connect(lambda evt: self._on_plot_clicked(evt, self.plot_item_a))
        self.plot_item_b.scene().sigMouseClicked.connect(lambda evt: self._on_plot_clicked(evt, self.plot_item_b))

        bottom_layout.addWidget(plot_container)
        bottom_layout.setSizes([self._table_expanded_width, 980])
        main_layout.addWidget(bottom_layout)

    def _create_overlay_items(self):
        """建立游標對照線 (hover_line_a/b) 與標記資訊文字方塊 (marker_info_item)，
        並加入圖A/圖B。setup_ui() 初始建立與 update_plot() 的 clear()-重建路徑共用。"""
        self.hover_line_a = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen('#8a8b95', width=1))
        self.hover_line_b = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen('#8a8b95', width=1))
        self.hover_line_a.setVisible(False)
        self.hover_line_b.setVisible(False)
        self.plot_item_a.addItem(self.hover_line_a, ignoreBounds=True)
        self.plot_item_b.addItem(self.hover_line_b, ignoreBounds=True)

        # 標記資訊文字方塊：釘選標記後，於圖表右上角顯示通道名/電壓/電流
        self.marker_info_item = pg.TextItem(anchor=(1, 0), color='#e8e8ea',
                                             fill=pg.mkBrush(42, 43, 51, 230),
                                             border=pg.mkPen('#4a4b56'))
        self.plot_item_a.addItem(self.marker_info_item, ignoreBounds=True)

    def reset_zoom(self):
        """
        重置縮放狀態為自動對齊。
        框選縮放 (RectMode 拖曳) 與滾輪縮放都是 pyqtgraph ViewBox 的原生行為，
        使用者一互動就會自動關閉該 ViewBox 的 autorange；這裡重新打開即可恢復自動對齊，
        不需要像 matplotlib 版那樣手動計算/還原 xlim、ylim。
        """
        self.plot_item_a.enableAutoRange()
        self.plot_item_b.enableAutoRange()
        self.vb_current.enableAutoRange()

    def choose_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "選擇儲存 CSV 路徑", "", "CSV Files (*.csv)")
        if filename:
            self.filepath_input.setText(filename)

    def connect_inst(self):
        try:
            want_sim = self.chk_sim_mode.isChecked()
            address = self.io_addr_input.currentText()
            if not want_sim and self.rm is None:
                raise RuntimeError("VISA 資源管理員無法初始化，請確認 VISA 後端；仍可使用模擬模式。")
            # 連線型別或真機位址改變時重建連線。
            # 測試進行中（btn_stop 可按）不動連線，避免把 FetchThread 正在用的 session 抽掉。
            if (self.inst is not None
                    and (want_sim != isinstance(self.inst, MockInstrument)
                         or (not want_sim and address != self._connected_addr))
                    and not self.btn_stop.isEnabled()):
                try:
                    self.inst.close()
                except Exception:
                    pass
                self.inst = None
                self._connected_addr = None

            if self.inst is None:
                if want_sim:
                    self.inst = MockInstrument()
                else:
                    self.inst = self.rm.open_resource(address)
                    self.inst.timeout = 10000
                    self._connected_addr = address
            status_suffix = "（模擬模式）" if isinstance(self.inst, MockInstrument) else ""
            self.lbl_conn_status.setText(f"● 已連線{status_suffix}")
            self.lbl_conn_status.setStyleSheet("color: #4db06e; font-weight: bold; padding-left: 10px;")
            return True
        except Exception as e:
            self.lbl_conn_status.setText("● 未連線")
            self.lbl_conn_status.setStyleSheet("color: #d16a6a; font-weight: bold; padding-left: 10px;")
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
        """收合/展開左側通道列表，讓圖表區在設定完通道後可以有更多顯示空間。

        收合時保留一條窄 header（只放收合/展開按鈕），不能把 splitter 寬度設為 0，
        否則連按鈕本身都會被壓縮消失，導致無法點擊復原。
        """
        splitter = self.bottom_splitter
        collapsed_width = 90

        if self.table.isVisible():
            current_sizes = splitter.sizes()
            if current_sizes and current_sizes[0] > collapsed_width:
                self._table_expanded_width = current_sizes[0]
            self.table.setVisible(False)
            self.lbl_table_header.setVisible(False)
            self.btn_display_select_all.setVisible(False)
            self.btn_display_select_none.setVisible(False)
            total = sum(current_sizes) if current_sizes else 980
            splitter.setSizes([collapsed_width, max(1, total - collapsed_width)])
            self.btn_toggle_table.setText("▶")
        else:
            self.table.setVisible(True)
            self.lbl_table_header.setVisible(True)
            self.btn_display_select_all.setVisible(True)
            self.btn_display_select_none.setVisible(True)
            total = sum(splitter.sizes()) or (self._table_expanded_width + 980)
            splitter.setSizes([self._table_expanded_width, max(1, total - self._table_expanded_width)])
            self.btn_toggle_table.setText("◀ 收合")

    # --- 通道圖表顯示 (col 5)：只影響繪圖，不影響資料記錄/CSV ---
    def _on_table_item_changed(self, item):
        if item.column() != 5:
            return
        ch = item.row() + 1
        self.channel_display[ch] = (item.checkState() == Qt.Checked)
        self.update_plot(force_redraw=True)

    def _set_all_channel_display(self, checked):
        state = Qt.Checked if checked else Qt.Unchecked
        self.table.blockSignals(True)
        for row in range(32):
            item = self.table.item(row, 5)
            if item is not None:
                item.setCheckState(state)
            self.channel_display[row + 1] = checked
        self.table.blockSignals(False)
        self.update_plot(force_redraw=True)

    # --- 曲線樣式 (實線/虛線 + 粗度) ---
    def _pen_from(self, combo, spin, color):
        style = Qt.SolidLine if combo.currentText() == "實線" else Qt.DashLine
        return pg.mkPen(color, width=spin.value(), style=style)

    # --- 記錄總時間 / 進度條 ---
    def _update_test_progress(self):
        if self.test_start_time is None or not self.test_duration:
            return
        elapsed = time.time() - self.test_start_time
        percent = min(100, int(elapsed / self.test_duration * 100))
        self.progress_bar.setValue(percent)
        if elapsed >= self.test_duration:
            self.progress_timer.stop()
            self.stop_test()
            QMessageBox.information(self, "測試完成", "已達設定的總紀錄時間，測試自動停止。")

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
    def _on_hover(self, scene_pos, plot_item):
        vb = plot_item.vb
        if not vb.sceneBoundingRect().contains(scene_pos):
            self._on_leave()
            return

        with self.data_lock:
            times = list(self.time_data)
        if not times:
            return

        data_pos = vb.mapSceneToView(scene_pos)
        idx = self._nearest_index(times, data_pos.x())
        t = times[idx]

        self.hover_line_a.setPos(t)
        self.hover_line_a.setVisible(True)
        self.hover_line_b.setPos(t)
        self.hover_line_b.setVisible(True)

        nearest = self._find_nearest_line(scene_pos, plot_item, idx)
        if nearest is None:
            self.lbl_hover_info.setText(f"游標: t={t:.1f}s")
        else:
            label, y_val = nearest
            if y_val != y_val:  # NaN
                self.lbl_hover_info.setText(f"游標: t={t:.1f}s ｜ {label}: N/A")
            else:
                self.lbl_hover_info.setText(f"游標: t={t:.1f}s ｜ {label}: {y_val:.3f}")

    def _on_leave(self, event=None):
        if self.hover_line_a is not None:
            self.hover_line_a.setVisible(False)
        if self.hover_line_b is not None:
            self.hover_line_b.setVisible(False)
        self.lbl_hover_info.setText("游標: -")

    def _find_nearest_line(self, scene_pos, plot_item, idx):
        """找出游標在螢幕像素距離上最接近的資料線 (排除游標線/標記線本身)，回傳 (label, y_value)。"""
        candidates = []  # (viewbox, line, label)
        if plot_item is self.plot_item_a:
            for ch, line in self.lines_v.items():
                candidates.append((self.plot_item_a.vb, line, f"CH{ch} (V)"))
            for ch, line in self.lines_i.items():
                candidates.append((self.vb_current, line, f"CH{ch} (uA)"))
        elif self.line_temp is not None:
            candidates.append((self.plot_item_b.vb, self.line_temp, "External Temp (°C)"))

        best = None
        for vb, line, label in candidates:
            xdata = line.xData
            ydata = line.yData
            if xdata is None or idx >= len(xdata) or idx >= len(ydata):
                continue
            y_val = ydata[idx]
            if y_val != y_val:  # NaN
                continue
            scene_pt = vb.mapViewToScene(QPointF(float(xdata[idx]), float(y_val)))
            dist = (scene_pt.x() - scene_pos.x()) ** 2 + (scene_pt.y() - scene_pos.y()) ** 2
            if best is None or dist < best[0]:
                best = (dist, label, y_val)

        if best is None:
            return None
        return best[1], best[2]

    # --- 點擊釘選/移除標記線 ---
    # sigMouseClicked 由 pyqtgraph 原生區分點擊與拖曳，不用像 matplotlib 版那樣自己算像素位移
    def _on_plot_clicked(self, click_event, plot_item):
        if click_event.button() != Qt.LeftButton:
            return
        scene_pos = click_event.scenePos()
        vb = plot_item.vb
        if not vb.sceneBoundingRect().contains(scene_pos):
            return
        data_pos = vb.mapSceneToView(scene_pos)
        self._toggle_pin_marker(data_pos.x())

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
                return

        if len(self.pinned_markers) >= 2:
            QMessageBox.information(self, "標記已達上限", "最多同時釘選 2 條標記線，請先清除部分標記。")
            return

        color = MARKER_COLORS[len(self.pinned_markers) % len(MARKER_COLORS)]
        pen = pg.mkPen(color, width=1.2, style=Qt.DashLine)
        marker = {
            'time': t,
            'color': color,
            'line_a': pg.InfiniteLine(angle=90, movable=False, pen=pen, pos=t),
            'line_b': pg.InfiniteLine(angle=90, movable=False, pen=pen, pos=t),
        }
        self.plot_item_a.addItem(marker['line_a'], ignoreBounds=True)
        self.plot_item_b.addItem(marker['line_b'], ignoreBounds=True)
        self.pinned_markers.append(marker)
        self._render_marker_panel()

    def _remove_marker(self, marker):
        for plot_item, key in ((self.plot_item_a, 'line_a'), (self.plot_item_b, 'line_b')):
            line = marker.get(key)
            if line is not None:
                try:
                    plot_item.removeItem(line)
                except Exception:
                    pass
        if marker in self.pinned_markers:
            self.pinned_markers.remove(marker)

    def _clear_all_markers(self):
        for m in list(self.pinned_markers):
            self._remove_marker(m)
        self._render_marker_panel()

    def _reposition_marker_info(self):
        """讓標記資訊文字方塊固定顯示在圖A目前可視範圍的右上角 (隨縮放/平移跟著移動)。"""
        if self.marker_info_item is None:
            return
        (x0, x1), (y0, y1) = self.plot_item_a.vb.viewRange()
        self.marker_info_item.setPos(x1, y1)

    def _render_marker_panel(self):
        """依目前釘選的標記線 (最多2條)，於圖A右上角顯示該時間點「目前有顯示於圖表」通道的通道名/電壓/電流。"""
        if self.marker_info_item is None:
            return

        if not self.pinned_markers:
            self.marker_info_item.setHtml("")
            return

        with self.data_lock:
            times = list(self.time_data)
            v_snapshot = {ch: list(self.v_data[ch]) for ch in self.active_channels}
            i_snapshot = {ch: list(self.i_data[ch]) for ch in self.active_channels}

        target_channels = [ch for ch in self.active_channels if self.channel_display.get(ch, True)]
        max_gap = self.current_interval * 0.5
        blocks = []
        for m in self.pinned_markers:
            idx = self._nearest_index(times, m['time'], max_gap=max_gap)
            color = m['color']
            header = f"<b>t={m['time']:.1f}s</b>"

            if idx is None:
                blocks.append(f"<div style='color:{color}'>{header}<br>(資料已捲出緩衝區)</div>")
                continue

            rows = [header]
            for ch in target_channels:
                v_vals = v_snapshot.get(ch, [])
                i_vals = i_snapshot.get(ch, [])
                v_str = f"{v_vals[idx]:.3f}V" if idx < len(v_vals) else "N/A"
                i_str = f"{i_vals[idx]:.3f}uA" if idx < len(i_vals) else "N/A"
                rows.append(f"CH{ch}: V={v_str}, I={i_str}")
            blocks.append(f"<div style='color:{color}'>" + "<br>".join(rows) + "</div>")

        self.marker_info_item.setHtml("<div style='background-color:transparent'>" + "<br>".join(blocks) + "</div>")
        self._reposition_marker_info()

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
                # 授權通道數可能少於 32 (SYST:LIC:CATalog? 回 004~032)，回傳筆數會比 32 短
                if row < len(valid_ocvs):
                    try:
                        text = f"{float(valid_ocvs[row]):.3f}"
                    except (TypeError, ValueError):
                        text = "Error"
                else:
                    text = "NA"
                self.table.setItem(row, 2, QTableWidgetItem(text))
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
        self.btn_start.setEnabled(False)
        
        for ch in self.active_channels:
            self.table.setItem(ch-1, 3, QTableWidgetItem("校準中.."))
            
        self.insitu_thread = InSituThread(self.inst, self.active_channels, self.cal_level_combo.currentText())
        self.insitu_thread.finished_signal.connect(self.on_insitu_finished)
        self.insitu_thread.start()

    def on_insitu_finished(self, success, msg, res_data):
        self.btn_detect.setEnabled(True)
        self.btn_cal.setEnabled(True)
        if success:
            for res_idx, ch in enumerate(self.active_channels):
                # 儀器回傳筆數可能少於 active_channels（授權通道數不足或回應被截斷）
                if res_idx < len(res_data):
                    try:
                        text = f"{float(res_data[res_idx]):.3f}"
                    except (TypeError, ValueError):
                        text = "Error"
                else:
                    text = "NA"
                self.table.setItem(ch-1, 3, QTableWidgetItem(text))


            QMessageBox.information(self, "完成", msg)
            self.btn_start.setEnabled(True) 
        else:
            for ch in self.active_channels:
                self.table.setItem(ch-1, 3, QTableWidgetItem("Error"))
            QMessageBox.warning(self, "執行失敗", msg)

    # --- 3. 開始測試 ---
    def start_test(self):
        if hasattr(self, 'insitu_thread') and self.insitu_thread.isRunning():
            QMessageBox.warning(self, "警告", "校準仍在執行中，請等校準結束後再開始測試。")
            return
        filepath = self.filepath_input.text()
        if not filepath:
            QMessageBox.warning(self, "警告", "請先設定 CSV 檔案儲存路徑")
            return
        if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
            if QMessageBox.question(
                    self, "確認覆寫", f"CSV 檔案已有資料，是否覆寫？\n{filepath}",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No) != QMessageBox.Yes:
                return
            
        try:
            interval = int(self.interval_input.text())
            # 手冊 INIT:TEST:MATC 的 <tint> 範圍為 1~256 秒；超過會被儀器丟進 error queue，
            # write() 不會拋例外，結果是 GUI 顯示測試進行中卻永遠讀不到資料。
            if not (5 <= interval <= 256): raise ValueError
        except:
            QMessageBox.warning(self, "警告", "間隔時間必須為 5~256 的整數（手冊 <tint> 上限 256 秒）")
            return
            
        if not (self.chk_v.isChecked() or self.chk_i.isChecked()):
            QMessageBox.warning(self, "警告", "請在設定區至少勾選擷取電壓或電流")
            return

        duration_text = self.duration_input.text().strip()
        if duration_text:
            try:
                parts = duration_text.split(":")
                if len(parts) != 3: raise ValueError
                h, m, s = (int(p) for p in parts)
                if h < 0 or not (0 <= m < 60) or not (0 <= s < 60): raise ValueError
                self.test_duration = h * 3600 + m * 60 + s
                if self.test_duration <= 0: raise ValueError
            except ValueError:
                QMessageBox.warning(self, "警告", "總紀錄時間格式須為 HH:MM:SS(例如 01:30:00)，或留空代表不限制")
                return
        else:
            self.test_duration = None

        # 手冊：<time> 單位為分鐘，最大測試時長 = tint × 24 小時。
        # 留空時使用儀器上限，並明確提示；超過上限的指定時長直接拒絕。
        max_test_minutes = interval * 24 * 60
        limit_text = f"{interval * 24}:00:00（{interval * 24} 小時）"
        if self.test_duration:
            if self.test_duration > max_test_minutes * 60:
                QMessageBox.warning(self, "超過儀器時長上限", f"目前間隔 {interval} 秒，測試時長上限為 {limit_text}。")
                return
            test_minutes = math.ceil(self.test_duration / 60)
        else:
            test_minutes = max_test_minutes
            QMessageBox.information(self, "儀器時長上限", f"未指定總時間；目前間隔 {interval} 秒，儀器最多記錄 {limit_text}，屆時會自行停止記錄。GUI 不偵測儀器自停，請手動中斷測試。")

        self._stopping = False
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
        self._plotted_channels = None  # 下一次更新必須重建曲線
        self.line_temp = None
        self.lbl_temp_value.setText("外部溫度: N/A")
        self.current_interval = interval

        # 新測試開始，清除上一次測試留下的標記線 (時間點在新資料中已無意義)
        self._clear_all_markers()
        if self.hover_line_a is not None:
            self.hover_line_a.setVisible(False)
        if self.hover_line_b is not None:
            self.hover_line_b.setVisible(False)
        self.lbl_hover_info.setText("游標: -")

        self.reset_zoom()  # 開始測試時預設自動對齊

        self.fetched_v = self.chk_v.isChecked()
        self.fetched_i = self.chk_i.isChecked()
        self.fetched_temp = self.chk_temp.isChecked()
        fetch_temp = self.fetched_temp

        # CSV 先開：路徑不可寫時儀器還沒開始量測，直接退回即可，不會留下「儀器在跑但沒有
        # fetch_thread」的死狀態。檔案在測試期間保持開啟，避免每筆資料都重新開關（長測可達數十萬筆）。
        try:
            self.csv_file = open(filepath, mode='w', newline='')
        except OSError as e:
            self.csv_file = None
            QMessageBox.critical(self, "無法建立 CSV", f"{filepath}\n{e}")
            self.stop_test()
            return

        try:
            self.csv_writer = csv.writer(self.csv_file)
            header = ["Time(s)"]
            for ch in self.active_channels:
                if self.fetched_v: header.append(f"CH{ch}_V")
                if self.fetched_i: header.append(f"CH{ch}_uA")
            if fetch_temp:
                header.append("Temp_C")
            self.csv_writer.writerow(header)
            self.csv_file.flush()
        except (OSError, ValueError) as e:
            self._close_csv_file(warn=False)  # 關檔錯誤併入表頭失敗提示。
            self.stop_test()
            QMessageBox.critical(self, "CSV 表頭寫入失敗", f"{filepath}\n{e}")
            return

        active_str = ",".join(map(str, self.active_channels))
        try:
            self.inst.write(
                f"INIT:TEST:MATC {test_minutes}, {TEST_OVP_V}, {TEST_UVP_V}, {TEST_RES_OHM}, "
                f"{interval}, {TEST_CURR_A}, {TEST_OCP_A}, (@{active_str})"
            )
            # write() 對被拒絕的指令不會拋例外，只會進 error queue，所以必須主動讀回來
            err = self.inst.query("SYST:ERR?").strip()
            if not err.lstrip('+').startswith("0"):
                raise RuntimeError(f"儀器拒絕測試指令：{err}")
        except Exception as e:
            QMessageBox.critical(self, "啟動失敗", str(e))
            self.stop_test()
            return

        self.fetch_thread = FetchThread(
            self.inst, self.active_channels, interval,
            self.fetched_v, self.fetched_i, fetch_temp,
            self.csv_writer, self.csv_file, self.data_lock,
            self.time_data, self.v_data, self.i_data, self.temp_data
        )
        self.fetch_thread.update_signal.connect(lambda: self.update_plot(force_redraw=False))
        self.fetch_thread.error_signal.connect(self.on_fetch_error)
        self.fetch_thread.fatal_signal.connect(self.on_fetch_fatal)
        self.fetch_thread.temp_signal.connect(self.on_temp_update)
        self.fetch_thread.start()

        self.test_start_time = time.time()
        self.progress_bar.setValue(0)
        if self.test_duration:
            self.progress_timer.start(1000)
        else:
            self.progress_timer.stop()

    def update_plot(self, force_redraw=False):
        """
        繪圖更新分為兩種路徑（同時更新圖A「電壓/電流」與圖B「溫度」兩張圖）：
        - 結構性重建 (force_redraw=True，或啟用通道集合改變，或溫度曲線顯示與否對不上)：
          clear 後完整重繪，含 legend，並重新建立游標線/標記線 (clear() 會把它們一併清掉)。
        - 一般資料更新：只用 setData 更新既有 PlotDataItem，不用重建整張圖。

        跟 matplotlib 版不同的是：pyqtgraph 的 ViewBox 會依自己的 autorange 狀態
        自動決定要不要跟著新資料重新縮放（使用者一手動縮放，autorange 就會被
        pyqtgraph 自動關閉），所以這裡完全不需要手動判斷/還原縮放視野。
        """
        show_v = self.plot_chk_v.isChecked() and self.fetched_v
        show_i = self.plot_chk_i.isChecked() and self.fetched_i
        show_temp = self.plot_chk_temp.isChecked() and self.fetched_temp

        # 只繪製「已啟用 且 使用者勾選要顯示於圖表」的通道；不影響資料記錄/CSV (仍以 active_channels 為準)
        target_channels = [ch for ch in self.active_channels if self.channel_display.get(ch, True)]

        channels_changed = self._plotted_channels != set(target_channels)
        temp_line_mismatch = show_temp != (self.line_temp is not None)
        need_full_rebuild = force_redraw or channels_changed or temp_line_mismatch

        with self.data_lock:
            time_snapshot = list(self.time_data)
            v_snapshot = {ch: list(self.v_data[ch]) for ch in target_channels}
            i_snapshot = {ch: list(self.i_data[ch]) for ch in target_channels}
            temp_snapshot = list(self.temp_data)

        if need_full_rebuild:
            self.plot_item_a.clear()
            self.vb_current.clear()
            self.plot_item_b.clear()
            self.legend_a.clear()
            self.legend_b.clear()
            self.lines_v = {}
            self.lines_i = {}
            self.line_temp = None

            for ch in target_channels:
                color = self.channel_colors[ch]

                if show_v:
                    line = self.plot_item_a.plot(time_snapshot, v_snapshot[ch],
                                                  pen=self._pen_from(self.combo_v_style, self.spin_v_width, color),
                                                  name=f"CH{ch} (V)")
                    self.lines_v[ch] = line

                if show_i:
                    pen = self._pen_from(self.combo_i_style, self.spin_i_width, color)
                    line = pg.PlotDataItem(time_snapshot, i_snapshot[ch], pen=pen)
                    self.vb_current.addItem(line)
                    self.legend_a.addItem(line, f"CH{ch} (uA)")
                    self.lines_i[ch] = line

            if show_temp:
                line = self.plot_item_b.plot(time_snapshot, temp_snapshot,
                                              pen=pg.mkPen('#e8e8ea', width=1.5), name="External Temp (°C)")
                self.line_temp = line

            # clear() 會把游標線/標記線/標記資訊文字方塊一併清掉，這裡重新建立
            self._create_overlay_items()

            for m in self.pinned_markers:
                pen = pg.mkPen(m['color'], width=1.2, style=Qt.DashLine)
                m['line_a'] = pg.InfiniteLine(angle=90, movable=False, pen=pen, pos=m['time'])
                m['line_b'] = pg.InfiniteLine(angle=90, movable=False, pen=pen, pos=m['time'])
                self.plot_item_a.addItem(m['line_a'], ignoreBounds=True)
                self.plot_item_b.addItem(m['line_b'], ignoreBounds=True)

            self._render_marker_panel()
            self._plotted_channels = set(target_channels)
        else:
            # 增量更新：只更新既有線條的資料
            for ch in target_channels:
                if show_v and ch in self.lines_v:
                    self.lines_v[ch].setData(time_snapshot, v_snapshot[ch])
                if show_i and ch in self.lines_i:
                    self.lines_i[ch].setData(time_snapshot, i_snapshot[ch])
            if show_temp and self.line_temp is not None:
                self.line_temp.setData(time_snapshot, temp_snapshot)
            if self.pinned_markers:
                self._render_marker_panel()

    def _close_csv_file(self, warn=True):
        csv_file = self.csv_file
        self.csv_file = None
        self.csv_writer = None
        if csv_file is not None:
            try:
                csv_file.close()
            except (OSError, ValueError) as e:
                if warn:
                    QMessageBox.warning(self, "CSV 關閉失敗", f"資料可能未完整儲存：\n{e}")

    def on_fetch_error(self, msg):
        # 原本只 print 到 stdout，用 .command 啟動時根本沒人看得到
        print(msg)
        self.lbl_conn_status.setText(f"● {msg}")
        self.lbl_conn_status.setStyleSheet("color: #d1a04a; font-weight: bold; padding-left: 10px;")

    def on_fetch_fatal(self, msg):
        if self._stopping or not self.btn_stop.isEnabled():
            return
        print(msg)
        self.fetch_thread.stop()
        self.fetch_thread.wait()
        # 儀器仍在內部記錄，停用自動停止，保留手動中斷按鈕。
        self.progress_timer.stop()
        self.test_start_time = None
        self.lbl_conn_status.setText("● 擷取中斷")
        self.lbl_conn_status.setStyleSheet("color: #d16a6a; font-weight: bold; padding-left: 10px;")
        QMessageBox.warning(self, "擷取中斷", msg + "\n儀器仍在內部記錄；如需停止，請按「中斷測試」或手動處理儀器。")

    def stop_test(self):
        self._stopping = True
        self.progress_timer.stop()

        if hasattr(self, 'fetch_thread'):
            self.fetch_thread.stop()
            self.fetch_thread.wait()
            # wait 後才可從 UI 執行緒使用同一個 VISA session；必須在 ABORt 前補抓。
            # 檔案身分避免啟動失敗時誤用上一輪的 fetch_thread。
            if (self.csv_file is not None
                    and self.fetch_thread.csv_file is self.csv_file
                    and not self.fetch_thread._fatal_error
                    and not self.fetch_thread._csv_error):
                try:
                    for _ in range(1024):
                        if not self.fetch_thread._fetch_once():
                            if self.fetch_thread._csv_error:
                                raise OSError("CSV 寫入失敗，補抓資料可能未完整儲存。")
                            break
                    else:
                        QMessageBox.warning(self, "停止補抓未完成", "已達 1024 批補抓上限，可能仍有未擷取資料。")
                except Exception as e:
                    QMessageBox.warning(self, "停止補抓失敗", f"最後資料可能未完整擷取：\n{e}")

        if self.inst is not None:
            try:
                self.inst.write("ABORt")
            except Exception as e:
                self.lbl_conn_status.setText("● 中斷指令失敗")
                self.lbl_conn_status.setStyleSheet("color: #d16a6a; font-weight: bold; padding-left: 10px;")
                QMessageBox.warning(self, "中斷失敗", f"ABORt 傳送失敗，請確認儀器狀態：\n{e}")

        self._close_csv_file()

        self.btn_detect.setEnabled(True)
        if self.active_channels: self.btn_cal.setEnabled(True)
        if self.active_channels: self.btn_start.setEnabled(True)
        self.btn_stop.setEnabled(False)

    def closeEvent(self, event):
        if self.btn_stop.isEnabled():
            if QMessageBox.question(
                    self, "確認關閉", "測試仍在進行中，是否中斷測試並關閉？",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No) != QMessageBox.Yes:
                event.ignore()
                return
        self.progress_timer.stop()
        # 四個背景執行緒都要收乾淨，否則關窗時會出現 QThread: Destroyed while thread is still running
        for name in ('fetch_thread', 'ocv_thread', 'insitu_thread', 'search_thread'):
            thread = getattr(self, name, None)
            if thread is None or not thread.isRunning():
                continue
            if hasattr(thread, 'stop'):
                thread.stop()
            if not thread.wait(5000):
                QMessageBox.warning(self, "無法關閉", f"{name} 尚未結束，已保留 CSV 與儀器連線；請稍後重試關閉或手動停止測試。")
                event.ignore()
                return
        self.stop_test()
        if self.inst is not None:
            try:
                self.inst.close()
            except Exception as e:
                QMessageBox.warning(self, "關閉連線失敗", str(e))
        event.accept()

def _selftest_fetch_alignment():
    """FetchThread 取樣管線的不變式檢查，執行方式：

        python3 BT2152_v3_pyqtgraph.py --selftest

    不變式：len(time_data) == len(v_data[ch]) == len(i_data[ch]) == len(temp_data)。
    一旦破壞，update_plot() 會永久丟 "X and Y arrays must be the same shape"，且無法恢復。
    """

    class _NullSink:
        def writerow(self, row): pass
        def flush(self): pass

    def make_thread(inst, channels, fetch_temp=True):
        sink = _NullSink()
        time_data, temp_data = deque(), deque()
        v_data = {i: deque() for i in range(1, 33)}
        i_data = {i: deque() for i in range(1, 33)}
        t = FetchThread(inst, channels, 5, True, True, fetch_temp,
                        sink, sink, threading.Lock(),
                        time_data, v_data, i_data, temp_data)
        return t

    def check_invariant(t, expected_len):
        assert len(t.time_data) == expected_len, (len(t.time_data), expected_len)
        for ch in t.active_channels:
            assert len(t.v_data[ch]) == expected_len, (ch, len(t.v_data[ch]))
            assert len(t.i_data[ch]) == expected_len, (ch, len(t.i_data[ch]))
        if t.fetch_temp:
            assert len(t.temp_data) == expected_len, (len(t.temp_data), expected_len)

    class _TruncatingInst:
        """電壓 log 故意少回幾筆，模擬回應超過 8192 值上限而被截斷。"""
        def query(self, cmd):
            cmd = cmd.strip()
            if cmd == "FETC:VOLT:LOG:POIN?":
                return "3"
            if cmd.startswith("FETC:VOLT:LOG?"):
                return "3.7,3.7,3.7,3.7"          # 2 通道 × 3 點應為 6 筆，只回 4 筆
            if cmd.startswith("FETC:CURR:LOG?"):
                return ",".join(["1e-6"] * 6)
            if cmd == "FETC:TEMP:LOG:POIN?":
                return "3"
            if cmd.startswith("FETC:TEMP:LOG?"):
                return "25.0,25.0,25.0"
            return "0"

    # (1) 回應被截斷：整批丟棄，deque 與 offset 都不得被動到
    t = make_thread(_TruncatingInst(), [1, 2])
    try:
        t._fetch_once()
    except ValueError as e:
        assert "截斷" in str(e), e
    else:
        raise AssertionError("回應被截斷卻沒有拋例外")
    check_invariant(t, 0)
    assert t.current_offset == 0, t.current_offset

    class _LaggingTempInst(_TruncatingInst):
        """溫度 log 落後電壓 log，是真機才會出現、模擬模式測不到的情境。"""
        def query(self, cmd):
            cmd = cmd.strip()
            if cmd.startswith("FETC:VOLT:LOG?"):
                return ",".join(["3.7"] * 6)      # 這次長度正確
            if cmd == "FETC:TEMP:LOG:POIN?":
                return "1"                        # 電壓有 3 點，溫度只有 1 點
            if cmd.startswith("FETC:TEMP:LOG?"):
                return "25.0"
            return super().query(cmd)

    # (2) 溫度落後：不足的點補 NaN，長度仍須一致
    t = make_thread(_LaggingTempInst(), [1, 2])
    assert t._fetch_once() is True
    check_invariant(t, 3)
    assert t.temp_data[0] == 25.0
    assert math.isnan(t.temp_data[1]) and math.isnan(t.temp_data[2])
    assert t.current_offset == 3

    # (3) 分批上限：一次請求的值不得超過 8192
    requested = []

    class _BigBacklogInst(_TruncatingInst):
        def query(self, cmd):
            cmd = cmd.strip()
            if cmd == "FETC:VOLT:LOG:POIN?":
                return "100000"                   # 大量積欠點數
            if cmd.startswith("FETC:VOLT:LOG?") or cmd.startswith("FETC:CURR:LOG?"):
                n = int(cmd.split()[1].rstrip(","))
                requested.append(n)
                return ",".join(["3.7"] * (n * 32))
            if cmd == "FETC:TEMP:LOG:POIN?":
                return "0"
            return super().query(cmd)

    t = make_thread(_BigBacklogInst(), list(range(1, 33)))
    assert t._fetch_once() is True
    assert requested and all(n * 32 <= MAX_ASCII_VALUES for n in requested), requested
    assert requested[0] == MAX_ASCII_VALUES // 32, requested[0]
    check_invariant(t, requested[0])

    # (4) 模擬儀器正常路徑
    mock = MockInstrument()
    mock.write("INIT:TEST:MATC 60, 4.3, 2.5, 1.0, 5, 0.0001, 0.01, (@1,2)")
    time.sleep(5.0 / MOCK_TIME_SPEEDUP + 0.3)
    t = make_thread(mock, [1, 2])
    assert t._fetch_once() is True
    check_invariant(t, t.current_offset)
    assert t.current_offset > 0

    # (5) CSV 在部分寫入或 flush 時失敗：立即 fatal，不得再次查詢／寫入同批。
    class _FailingSink:
        def __init__(self, exc_type, fail_flush):
            self.calls = 0
            self.exc_type = exc_type
            self.fail_flush = fail_flush

        def writerow(self, row):
            self.calls += 1
            if not self.fail_flush and self.calls == 2:
                raise self.exc_type("selftest CSV 寫入失敗")

        def flush(self):
            if self.fail_flush:
                raise self.exc_type("selftest CSV flush 失敗")

    for exc_type in (OSError, ValueError):
        for fail_flush in (False, True):
            t = make_thread(_LaggingTempInst(), [1, 2])
            sink = _FailingSink(exc_type, fail_flush)
            t.csv_writer = t.csv_file = sink
            fatals, errors = [], []
            t.fatal_signal.connect(fatals.append)
            t.error_signal.connect(errors.append)
            t.run()
            assert len(fatals) == 1 and "CSV" in fatals[0], fatals
            assert not errors, errors
            assert t._fatal_error and t._csv_error and not t.is_running
            check_invariant(t, 0)
            assert t.current_offset == 0
            calls = sink.calls
            class _NoQueryInst:
                def query(self, cmd):
                    raise AssertionError("CSV fatal 後不得重抓")
            t.inst = _NoQueryInst()
            assert t._fetch_once() is False
            assert sink.calls == calls
            check_invariant(t, 0)

    # (6) 溫度點數／資料查詢失敗只警告，電壓／電流繼續且不觸發 fatal。
    class _FailingTempInst(_LaggingTempInst):
        def __init__(self, fail_points):
            self.fail_points = fail_points

        def query(self, cmd):
            failing_cmd = "FETC:TEMP:LOG:POIN?" if self.fail_points else "FETC:TEMP:LOG?"
            if cmd.startswith(failing_cmd):
                raise OSError("selftest 溫度查詢失敗")
            return super().query(cmd)

    for fail_points in (True, False):
        t = make_thread(_FailingTempInst(fail_points), [1, 2])
        errors, fatals = [], []
        t.error_signal.connect(errors.append)
        t.fatal_signal.connect(fatals.append)
        assert t._fetch_once() is True
        check_invariant(t, 3)
        assert all(math.isnan(v) for v in t.temp_data)
        assert len(errors) == 1 and not fatals
        assert t._temp_error_streak == 1 and t._error_streak == 0
        assert t.current_offset == 3 and not t._fatal_error

    print("_selftest_fetch_alignment 全部通過")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _app = QApplication(sys.argv)     # QThread 物件需要 QApplication
        _selftest_fetch_alignment()
        sys.exit(0)

    app = QApplication(sys.argv)
    window = BT2152App()
    window.show()
    sys.exit(app.exec_())
