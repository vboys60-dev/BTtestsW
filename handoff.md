# BT2152-GUI Handoff

## 這是什麼

Keysight BT2152A/B 電池阻抗/漏電流測試儀控制程式（PyQt5 + pyvisa）。流程：OCV 偵測 → In Situ 校準 → 開始長時間記錄測試，即時繪圖 + 寫 CSV。

無 git。三支獨立檔案（非 import 關係），複製疊代出來的三個階段：

| 檔案 | 繪圖引擎 | 狀態 |
|---|---|---|
| `BT2152.py` | matplotlib | 最初版本 |
| `BT2152_v2.py` | matplotlib | v1 + 可收合通道列表 + 英文化 |
| `BT2152_v3_pyqtgraph.py` | pyqtgraph | **主力開發版，只改這支**，除非明確要求同步 v1/v2 |

參考：`BT2152B-GUIDE.pdf`（原廠 SCPI 指令手冊）、`SCPI參考字典.md`（手冊的指令摘要，標了哪些是 v3 實際有用到的）。

其他檔案：`probe_bt2152.py`（唯讀連線探測，見「驗證方式」第 4 層）、`優化任務清單.md`（code review 發現清單與修正記錄）。

## 執行

雙擊 `啟動BT2152.command`（cd 到專案目錄 → `conda activate base` → 跑 v3）。base env 已有 PyQt5/pyqtgraph/pyvisa/numpy，沒另建 env。

或手動：`python3 BT2152_v3_pyqtgraph.py`，勾「模擬模式」用 `MockInstrument` 假資料跑，不需接真儀器。

## v3 架構

- **Thread**：`OcvThread`（OCV偵測）、`InSituThread`（導線電阻校準）、`FetchThread`（測試中定時撈電壓/電流/溫度、寫CSV、通知重繪，輪詢間隔見 `_poll_sleep_seconds`，非直接用使用者設的 interval）、`ResourceSearchThread`（搜尋VISA資源）、`MockInstrument`（模擬儀器，介面同 pyvisa resource，thread 不用改）。
- **主視窗** `BT2152App`：`setup_ui()` 建 UI，`update_plot()` 是繪圖核心（結構性重建 vs 增量 setData 兩條路徑）。
- `self.data_lock` 保護 `time_data/v_data/i_data/temp_data`（`deque(maxlen=1000)`）跨執行緒存取。
- 圖A(電壓/電流) 與圖B(溫度) X軸用 `sigRangeChangedManually` 手動同步，不用 `setXLink()`（兩圖繪圖區寬度不同，幾何換算會跑掉）。

## 功能清單（v3限定）

1. 總紀錄時間 + 自動停止：`self.duration_input`（`HH:MM:SS`），`start_test()` 解析存 `self.test_duration`，格式錯誤跳警告。`QTimer` 1秒tick更新進度條，時間到自動 `stop_test()`。以真實經過秒數為準，跟 `MOCK_TIME_SPEEDUP` 無關。
2. 通道「顯示於圖表」勾選欄（表格第6欄）+ 全選/全不選按鈕。`self.channel_display: dict[int, bool]`。只影響繪圖，不影響 CSV（CSV仍依 `active_channels` 全寫）。
3. 電壓/電流線條樣式（實線/虛線、寬度1-6px）下拉+spinbox，`_pen_from(combo, spin, color)` 產生 pen。
4. 標記線資訊改用 `pg.TextItem`（`self.marker_info_item`）錨在圖A右上角，跟隨縮放/平移（`_reposition_marker_info()`）。只列已啟用且勾選顯示的通道。
5. 標記線上限 3→2（`MARKER_COLORS` 2色）。

> `plot_item_a.clear()`（結構性重建）會清掉 marker_info_item / 游標線 / 標記線，重建分支要重新建立，邏輯已抽成 `self._create_overlay_items()`（setup_ui 初始建立與重建分支共用）。加新疊加物件優先放進這個方法。

## Dark Mode

寫死深色主題，無亮/暗切換（YAGNI，目前用不到）。`DARK_QSS` 套在 `__init__`；四個動作按鈕用 inline QSS 模板保留語意色；pyqtgraph 背景/格線/游標線/marker顏色都跟著改；`channel_colors` 用 `pg.intColor(hues=32, minValue=180, sat=220)` 拉高亮度避免深色背景下看不清；表格斑馬紋。

若要做可切換亮/暗：需另維護一套淺色 QSS + pyqtgraph 設定，且切換時要重繪，目前沒預留機制。

## Bug fix：左側通道列表收合後找不到、無法復原

**根因**：`toggle_table_panel()` 收合時把 splitter 左側寬度設 0，但收合按鈕本身就在被壓縮到 0 的那個面板裡，跟著消失。

**修法**：收合時改設非0保留寬度，隱藏「通道列表」標籤與全選/全不選按鈕，只留收合/展開按鈕可見；`bottom_layout.setChildrenCollapsible(False)` 同時擋掉手動拖曳分隔線拖到0的同類問題。

v1/v2 沒有這個收合功能，不受影響、未同步修。

## 已知限制

- `FetchThread` 輪詢最快4秒（UI interval最小值5秒換算）。總紀錄時間設得比輪詢週期短，可能還沒拿到資料點就自動停止——預期行為非bug。
- 標記資訊 overlay 沒有滾動/裁切，同時顯示通道太多（如30+）文字方塊會很長蓋住圖表。因應：引導使用者取消勾選不需要的通道。
- v1/v2 沒有今天(v3)新增的任何功能、精簡、Dark Mode、收合bugfix，三檔案功能集不同步。
- 以下 SCPI 功能有意不做（YAGNI，等有實際需求再接）：`CONF:TEST:WIRE:RESistance` 沒送過，導線電阻永遠停在預設 5Ω range，>5Ω 的場合無法切到 10/20Ω；`STATus:ALARm:*` 與 `OUTPut:PROTection:CLEar` 未使用，OVP/UVP/OCP 保護事件只能在前面板手動清除；`INIT:TEST:MATC` 的保護參數只抽成常數，沒有 GUI 入口。

## 驗證方式

無正式測試套件，不引入 pytest。四層，由快到慢：

**1. 語法**

```bash
python3 -m py_compile BT2152_v3_pyqtgraph.py
```

**2. 內建自我檢查（留在專案內，唯一常駐的測試）**

```bash
QT_QPA_PLATFORM=offscreen python3 BT2152_v3_pyqtgraph.py --selftest
```

跑 `_selftest_fetch_alignment()`（檔案底部），用假儀器驗 `FetchThread` 的不變式：

```
len(time_data) == len(v_data[ch]) == len(i_data[ch]) == len(temp_data)
```

這條一旦破壞，`update_plot()` 會永久丟 `X and Y arrays must be the same shape` 且無法恢復，所以改動 `FetchThread` 的取樣管線後**一定要重跑**。涵蓋：回應被截斷時整批丟棄（deque 與 `current_offset` 都不動）、溫度落後時補 NaN、32 通道單批請求量不超過 8192 值、`MockInstrument` 正常路徑。

**3. 模擬模式 headless smoke test**

`QT_QPA_PLATFORM=offscreen` + 勾模擬模式，monkeypatch `QMessageBox`（三個都要，否則彈窗卡住），跑 OCV → In Situ → 開始測試 → CSV 產出 → 繪圖 全流程並斷言關鍵狀態。腳本寫在系統暫存目錄，不留在專案內，需要時照此模式重寫。

`MockInstrument` 讓 `FETC:VOLT:LOG:POIN?` 與 `FETC:TEMP:LOG:POIN?` 回同一個值、每次 `_start_ocv()` 都重設 `_ocv_ready_at`，所以**溫度落後**與**overlapped command 殘留狀態**這兩類問題模擬模式永遠測不到——要驗那兩項只能靠第 2 層的假儀器或第 4 層的真機。

**4. 真機驗證**

先跑唯讀探測，確認連得到、順便讀出幾個關鍵前提：

```bash
python3 probe_bt2152.py --list                  # 只列 VISA 資源
python3 probe_bt2152.py                         # 用內建預設位址
python3 probe_bt2152.py --addr TCPIP0::169.254.4.61::inst0::INSTR
```

只送查詢，沒有 `INIT` / `CAL` / `ABORt` / 設定指令，接著正在跑的測試不會被打斷。唯一改動狀態的是 `SYST:ERR?`（FIFO，讀取即清除），輸出有標示。會清暫存器的 `STAT:*:EVENt?` / `*ESR?` 刻意排除，`*TST?` 也不自動跑（要數十秒且會中斷量測）。

輸出最後會直接給判讀：授權通道數（決定 `(@1:32)` 的回傳會不會比 32 短）、`8192 ÷ 通道數` 的單批上限、電壓與溫度 log 的點數差、`INIT:TEST:MATC? (@1)` 回讀的 `<time>`。

接著用 GUI 跑，重點是模擬模式測不到的四項：

| 檢查 | 怎麼做 | 預期 |
|---|---|---|
| 溫度落後 | 勾「外部溫度」跑 10 分鐘以上 | 圖 B 不噴 shape mismatch；CSV 的 `Temp_C` 可能有空格但列數不變 |
| 回應截斷 | 32 通道 + interval 5s，測試中途拔網路線約 3 分鐘再接回 | 狀態列出現「擷取資料錯誤(n/5)」，接回後自動追平，CSV 不錯位；連續 5 次失敗會跳「擷取中斷」並停止測試 |
| 殘留狀態 | 連按兩次「OCV 偵測」 | 第二次的電壓值與第一次不同（不是上一輪的快取） |
| 測試時長 | 設 `24:00:00` 開始後查 `INIT:TEST:MATC? (@1)` | `<time>` 回 1440，不是 720 |

拔網路線那項會真的中斷量測，正式樣品上請跳過或另接測試用電芯。

## Code review 修正記錄

2026-09-19 對 v3 做過一次完整 review，13 項發現全部修掉，分三波套用。發現清單、每項的觸發情境與任務邊界在 `優化任務清單.md`。

改動集中在四處，之後動到這些地方要特別小心：

- `FetchThread`：`run()` 拆成 `_fetch_once()` + `_fetch_log()`，**長度驗證一律在寫入 deque 之前**，不符就整批丟棄且不推進 `current_offset`。溫度以 `current_offset` 為單一時間軸基準（`temp_offset` 已移除），缺值補 NaN。單批上限 `8192 // 通道數`。
- `_PollingThread`：`OcvThread` / `InSituThread` 的共同基底，`_wait_available()` 帶取消旗標與逾時，進等待迴圈前先等 `AVAI?` 歸零（沒用 `*OPC?`，理由寫在 docstring）。
- `start_test()`：CSV 先開才送 `INIT:TEST:MATC`；`<time>` 由總紀錄時間推導；送出後必讀 `SYST:ERR?`。
- `connect_inst()`：勾選狀態與 `self.inst` 型別不一致就重建連線，但測試進行中不動。

保護參數 `TEST_OVP_V` / `TEST_UVP_V` / `TEST_RES_OHM` / `TEST_CURR_A` / `TEST_OCP_A` 抽成模組常數（原本硬編在指令字串裡），尚未做成 GUI 選項。
