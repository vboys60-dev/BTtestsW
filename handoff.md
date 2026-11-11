# BT2152-GUI Handoff

## 這是什麼

Keysight BT2152A/B 電池阻抗/漏電流測試儀控制程式（PyQt5 + pyvisa）。流程：OCV 偵測 → In Situ 校準 → 開始長時間記錄測試，即時繪圖 + 寫 CSV。

已有 git（分支 `my-project`）。三支獨立檔案（非 import 關係），複製疊代出來的三個階段：

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

- `FetchThread`：`run()` 拆成 `_fetch_once()` + `_fetch_log()`，**長度驗證一律在寫入 deque 之前**，不符就整批丟棄且不推進 `current_offset`；**CSV 先整批寫入並 flush 成功，才 append 進 deque**（2026-11-09 起）。溫度以 `current_offset` 為單一時間軸基準（`temp_offset` 已移除），缺值補 NaN。單批上限 `8192 // 通道數`。
- `_PollingThread`：`OcvThread` / `InSituThread` 的共同基底，`_wait_available()` 帶取消旗標與逾時，進等待迴圈前先等 `AVAI?` 歸零（沒用 `*OPC?`，理由寫在 docstring）。
- `start_test()`：CSV 先開才送 `INIT:TEST:MATC`；`<time>` 由總紀錄時間推導；送出後必讀 `SYST:ERR?`。
- `connect_inst()`：勾選狀態與 `self.inst` 型別不一致就重建連線，但測試進行中不動。

保護參數 `TEST_OVP_V` / `TEST_UVP_V` / `TEST_RES_OHM` / `TEST_CURR_A` / `TEST_OCP_A` 抽成模組常數（原本硬編在指令字串裡），尚未做成 GUI 選項。

## Codex + Opus 審查修正（2026-11-09）

流程：Codex 整檔靜態審查（17 項）→ Opus 對照原始碼複核（13 屬實／4 部分屬實，#2 降 WARNING、#4 降 SUGGESTION，另補 A–D 四項）→ Codex 分批修 → Opus 審查 diff → commit。

| 批次 | commit | 內容 |
|---|---|---|
| 1 | `1974e11` | #1 校準中停用/拒絕開始測試；#3 覆寫非空 CSV 先確認；#5 先停再通知；#7 ABORt 失敗警告＋紅燈；A `FetchThread` 改 `threading.Event` 可中斷等待；B/#2 關窗確認、`wait()` 逾時取消關窗；#15 無 VISA backend 仍可用模擬模式；#16 標記容差 0.5×interval；#17 以 `_plotted_channels` 避免重複重建；C 連續擷取失敗只停擷取、**不送 ABORt**，使用者手動停止才送 |
| 2 | `0f8f132` | #8 CSV 錯誤即 fatal 不重試、先寫 CSV 再進 deque、表頭/關檔失敗處理；#6 停止時 ABORt 前補抓（上限 1024 批）；#11 時長超限直接拒絕；#4 繪圖只畫本輪有擷取的量；#14 溫度點數查詢失敗獨立計數＋警告；#12 位址變更重連；停止中忽略遲到的 fatal；selftest 新增 CSV 部分寫入/flush 失敗案例 |
| 3 | 見 git log | `/codex-review:code` 整檔複審 4 輪：closeEvent 逾時不再取消 OCV/校準、擷取逾時明示狀態；`stop_test()` 回傳成功/失敗，ABORt 失敗進入 `_inst_unconfirmed`（鎖定 OCV/校準/開始、中斷鈕可重試、不顯示完成），OCV/校準完成回呼不得解除鎖定；通訊 fatal 後使用者手動停止可做一次有界補抓（CSV fatal 仍禁止）；未確認狀態下關窗可選「強制關閉」，重試中斷失敗時重建 session 再 ABORt |

兩批皆通過 `py_compile` 與 offscreen `--selftest`；Opus 另用 MockInstrument 整合腳本驗過關鍵路徑。**尚未真機驗證。**

### 待辦

- **第 3 批（需真機確認語意）**：
  - #9 settle 階段可能把上一輪殘留的 `AVAI?`=1 當成功 → 先加 `SYST:ERR?` 檢查，再確認 AVAI 實際行為。
    - **工作區已改、未 commit、待真機**：settle 未見 0 → 查 `SYST:ERR?` 並 raise；INIT 前加 `*CLS`；假儀器自檢已接入 `--selftest`。風險：若真機 INIT 後 `AVAI?` 不一定先讀到 0（量測極快或 INIT 不清 AVAI），OCV/In Situ 會誤判失敗。真機請錄 `AVAI?` 讀值序列確認；不成立則改 `*OPC` + `*ESR?` 輪詢。
  - #10 校準結果未驗證（筆數、9.91E37 sentinel、合理範圍）就 `SAVE 1` 並放行測試；電阻上限需依手冊或實測定。
  - #6 確認 `ABORt` 前後 log 是否仍可讀（目前補抓放在 ABORt 之前）。
  - C 的策略（fatal 不送 ABORt）建議和真機使用者確認。
  - #11 偵測「儀器已自停」（不限時長時儀器於 tint×24h 自停，GUI 計時照跑）。
- **第 4 批（#13 已完成，`c3edb99`＋`83d5549`，未真機驗證）**：連線／`INIT:TEST:MATC`＋`SYST:ERR?`／停止（等擷取執行緒＋補抓＋ABORt＋重建 session）全改由 `_IoTask`（QThread）執行，`_run_io(fn, on_done)` 派工、`_io_busy` 旗標防重入（忙碌中 `start_ocv/start_in_situ/start_test/stop_test` 直接 return，`closeEvent` 提示稍後再關）。`stop_test(manual, on_done)` 改非同步，結果以 `on_done(ok)` 回報；`closeEvent` 改為 ignore → 停止完成後 `_on_close_stopped` 再 `close()`。**規則**：`_run_io` 的 fn 在背景跑，不可碰 widget／彈窗（警告收集成 notes 由主執行緒顯示），且作業期間 `self.inst` 由該作業獨占。殘留：`closeEvent` 內 `thread.wait(5000)` 與最後的 `inst.close()` 仍在 GUI 執行緒。
  - **Codex 整檔複審（2026-11-09，4 輪，最終 APPROVED）**：已修三項——連線重建失敗且 `inst` 為 None 時清空 `active_channels`、停用校準/開始、表格設 X；停止期間發生的 CSV fatal 會被 `on_fetch_fatal` 忽略，改由 `stop_test` 的 job 在 `wait()` 後補報（`FetchThread._fatal_notified` 記錄 GUI 是否已提示，補抓例外已涵蓋時不重複）；`closeEvent` 確認對話框（巢狀事件迴圈）之後再檢查 `_io_busy`。
  - **複審中提出但刻意不修**：settle 階段殘留 `AVAI?`=1（即 #9）、校準結果未驗證就 `SAVE 1`（即 #10）——兩者仍待真機；`closeEvent` 的 `wait`／`inst.close()` 阻塞 GUI（已知殘留）；追平積欠資料時每批都發更新訊號、重複重繪（等實際卡頓再做 dirty flag＋固定頻率重繪）。
  - 驗證腳本（模擬模式 headless，連線→OCV→校準→測試→停止→ABORt 失敗重試→關窗）寫在暫存目錄未留專案內，需要時照 `_run_io` 的非同步流程用 `processEvents` 輪詢重寫。
- **小項**：（#2 逾時警告文字已於第 3 批處理）（已決定）校準重跑失敗會讓「開始測試」保持停用，需再校準成功才能按——接受此行為；`__pycache__` 已加入 `.gitignore` 並移出版控。
- 第 3 批（真機語意項）完成後再跑一次 `/codex-review:code` 整檔複審（#13 後的複審已 APPROVED）。
- 第 3 輪新增的 UI 流程（強制關閉、重試中斷時重建 session）與 #13 的非同步連線／啟停流程，需在真機上實際走一遍。
### 刻意不修：位址/模式變更只在 OCV 重連（Codex 複審 #4）

`connect_inst()` 只由 `start_ocv()` 呼叫。OCV 完成後改 I/O 位址或模擬模式，再按校準/開始測試仍沿用舊 session。**取捨**：OCV 是必經第一步，之後沿用同一連線是設計使然；要改位址就重跑 OCV。若日後要嚴格化：把 OCV/校準結果綁定連線身分，位址或模式變更時使結果失效並要求重新偵測。

### 已知殘留限制

- Event 能中斷輪詢等待，但無法取消進行中的 VISA query（最長 10 秒）。
- CSV 失敗時檔案可能留有部分批次資料，該批不會進圖表也不會重試。
- 溫度 query 逾時，遲到的回應可能被下一個 query 讀走，會被 `_fetch_log` 長度驗證擋下並計入 error streak，不污染資料。

## 錯誤日誌（除錯用）

- **位置**：`logs/bt2152.log`（專案目錄下，已加入 `.gitignore`）。1 MB × 5 份輪替，總量上限約 6 MB。日誌目錄不可寫時退回 stderr（Terminal 視窗）。
- **何時寫入**：只有正式啟動（`python3 BT2152_v3_pyqtgraph.py` / `啟動BT2152.command`）；`--selftest` 不寫。
- **記什麼**：啟動時的 Python/pyvisa/pyqtgraph 版本；擷取錯誤（WARNING）、擷取中斷 fatal（ERROR）、`ABORt` 失敗含堆疊、測試開始/停止（INFO）；以及所有未處理例外（CRITICAL，含 slot、QTimer、`QThread.run` 內的）。每行格式帶時間與 `[執行緒名稱]`。
- **實作**：`_setup_logging()`，模組 logger 為 `log`。PyQt5 的 slot/QTimer/QThread 例外一律走 `sys.excepthook`，**不是** `threading.excepthook`（對 QThread 無效，已實測），所以只掛前者。掛上後未處理例外不再讓程式 abort，而是繼續跑——`FetchThread` 若意外死掉，GUI 可能仍顯示「測試中」，請看日誌。
- **加新紀錄點**：直接 `log.info/warning/exception(...)`，參數用 `%s` 佔位符傳入。不要在輪詢迴圈逐筆記 SCPI 指令，會灌爆日誌。
- **注意**：日誌含完整 CSV 路徑與 VISA 錯誤字串（可能有使用者名稱、儀器位址）；外傳前先檢查。
- **未做**：`--debug`/DEBUG 等級（目前沒有 `log.debug` 呼叫）、持續錯誤節流（首次/每 N 次/恢復）、GUI「開啟日誌資料夾」按鈕。
