# BT2152A/B SCPI 程控指令參考字典

來源：` BT2152B-prg.md`（原廠 Programming Reference，Edition 6, 2025-03）。供之後對 `BT2152_v3_pyqtgraph.py` 做 code review 時比對指令語法/參數/回傳值用。

標記說明：**[USED]** = 目前 v3 程式碼中有實際送出的指令（grep 自 `BT2152_v3_pyqtgraph.py`）。

---

## Channel Parameter（`<chanlist>`）

- 語法：`(@1,2,3)` 或 `(@1:32)`，channel 必須遞增排列，可混合範圍與單一值，如 `(@1:8,10,12:32)`。
- Query 加 chanlist 時，`?` 與 `(@...)` 之間**必須有空格**，否則 error -103 Invalid separator。
- Query 結果依 chanlist 指定順序回傳。

## 共通語法規則

- `:` 分隔關鍵字層級；大寫字母 = 縮寫可送形式（如 `INITiate` 可送 `INIT`）。
- `?` 後接 query 參數需空一格。
- `<>` 必填參數、`|` 多選一、`[]` 可省略。
- Boolean：接受 `OFF/0`、`ON/1`；query 一律回傳 `0`/`1`。
- 每次 query 只能送一次、讀完結果才能送下一指令，否則 Query Interrupted 且資料遺失。

---

## Calibration Commands (`CALibration:` / `CAL:`)

| 指令 | 參數 | 說明 |
|---|---|---|
| `CAL:DATE "<date>"` / `CAL:DATE?` | 字串 ≤16字 | 儲存/查詢校正日期 |
| `CAL:END` | 無 | 結束校正流程（在 `CAL:STORe` 前用） |
| `CAL:LOAD` | 無 | 載回舊校正值（須在 `CAL:STORe` 前執行才有效） |
| `CAL:RESult? <value>` | 量測結果值 | 輸入校正量測結果，回傳 0=成功 |
| `CAL:SECure:CODE <code>` | 1~10E32 整數 | 設定校正安全碼 |
| `CAL:SECure:STATe 0\|OFF\|1\|ON, <code>` / `?` | bool + code | 啟用/查詢安全鎖 |
| `CAL:STARt` | 無 | 啟動校正程序（會 `*RST`、關保護、DAC設3.5V） |
| `CAL:STEP <step>` / `?` | 1-3 | 逐步執行參考校正（1=電壓, 2=電壓offset, 3=10mA電流） |
| `CAL:STORe` | 無 | 寫入校正常數到 EEPROM（覆蓋舊值） |
| `CAL:STRing "<string>"` / `?` | ≤128字 | 校正備註訊息 |
| `CAL:VALue? <step>` | 1-3 | 查詢指定步驟的參考校正常數 |
| `CAL:VERification:END` | 無 | 結束驗證流程 |
| `CAL:VERification:MEASure:INITiate <time>,<tint>` | 秒,秒(1-250) | 啟動驗證量測 |
| `CAL:VERification:STARt <channel>` | 1-32 | 啟動指定通道驗證 |
| `CAL:VERification:VOLTage <voltage>` / `?` | V | 設定驗證電壓上限 |
| `CAL:WIRE:RESistance:AUTO` / `:BYSHort` | 無（同義） | 全通道 by-short 導線電阻校正（~20分鐘），需先短接電纜 |
| `CAL:WIRE:RESistance:CLEar` | 無 | 全部通道導線電阻歸零（易失性值，開機也會重置） |
| **[USED]** `CAL:WIRE:RES:INSitu (@<chanlist>)` | chanlist 1-32（手冊寫1-4疑似誤植） | In situ 導線電阻校正（電池接著校正，~2分鐘），電流大小由 `CONF:INSitu:CURRent` 決定 |
| `CAL:WIRE:RESistance:LOAD <value>` | 檔案編號 1-5 | 載入已存的導線電阻檔 |
| **[USED]** `CAL:WIRE:RES:VALues <resistance>, (@<chanlist>)` / `... VALues? (@<chanlist>)` | 0~5Ω，解析度0.001Ω | 設定/查詢導線電阻（與 `SENSe:WIRE:RESistance:CONFigure` 同義） |
| `CAL:WIRE:RESistance:SAVE <value>` | 檔案編號 1-5 | 存導線電阻值到非揮發記憶體 |

## Common Commands（IEEE488.2，`*xxx`）

| 指令 | 說明 |
|---|---|
| **[USED]** `ABORt` | 中止進行中量測，回到 idle 狀態；建議用此指令而非 Device Clear |
| `*CAL?` | 觸發全通道自動校正（最久1小時），須先過 self-test 且已 warm up（Ready 燈綠燈），否則中止；回傳0=成功 |
| `*CLS` | 清除事件暫存器、Status Byte、Error Queue |
| `*ESE <mask>` / `*ESE?` | Standard Event Status Enable，設定/查詢遮罩 |
| `*ESR?` | 讀取並清除 Standard Event Status Register |
| `*IDN?` | 回傳 `製造商,型號,序號,韌體版本`，如 `Keysight Technologies,BT2152B,MY06009010,A.01.51-60-04-10` |
| `*OPC?` | 所有待完成操作完成後回傳1，用來同步（含 `INIT:TEST`/校正指令） |
| `*RST` | 重設到預設值；強制 `ABORt`；**需等待至少4秒**完成，IO timeout 設 >4秒；不影響 `DIGital:PINx:POLarity`/`FUNCtion` |
| `*SRE <mask>` | Service Request Enable |
| `*STB?` | 讀 Status Byte Register（唯讀，讀取不清除） |
| `*TST?` | 執行 self-test，0=通過 |
| `*WAI` | 暫停後續指令處理直到所有待完成操作結束；只能被 Device Clear 中斷 |

## CONFigure Command

| 指令 | 參數 | 說明 |
|---|---|---|
| `CONF:INSitu:CURRent HIGH\|MED\|LOW` / `?` | HIGH=±9mA, MED=±5mA, LOW=±1mA；`*RST`→LOW | 設定 in situ 導線電阻校正用電流 |
| `CONF:TEST:WIRE:RESistance 5\|10\|20\|<value>` / `?` | 0~20，依區間自動取5/10/20Ω range；`*RST`→5Ω | 設定全通道導線電阻量測 range；影響 in situ 校正與測試啟動所需時間（5Ω:90s校正/110s測試啟動；10Ω:170s/230s；20Ω:250s/350s） |

## Digital Commands（`[SOURce:]DIGital:`，`SOURce` 可省略）

| 指令 | 參數 | 說明 |
|---|---|---|
| `DIG:INPut:DATA?` | 無 | 讀數位控制埠狀態（bit0-6 對應 pin1-7） |
| `DIG:OUTPut:DATA <value>` / `?` | 0-127；`*RST`→0 | 設定數位控制埠輸出（只影響設為 DIO 的 pin） |
| `DIG:PIN<1-7>:FUNCtion <fn>` / `?` | `DIO\|DINPut\|FAULt\|INHibit`；`*RST`→DINPut；**不受 `*RST` 影響** | 設定 pin 功能。FAULt=pin1隔離故障輸出(pin2為共用)；INHibit=pin3抑制輸入 |
| `DIG:PIN<1-7>:POLarity POSitive\|NEGative` / `?` | `*RST`→POSitive | 設定 pin 極性（`*RST` 不再影響此值，避免校正時 DIO 抖動） |

## Fetch Commands

| 指令 | 參數 | 說明 |
|---|---|---|
| `FETC:CURRent:LATest? (@<chanlist>)` / `FETC:VOLTage:LATest?` | 1-32 | 最新一筆量測值（ASCII）。查詢不清空 buffer，可重複查；`INIT` 執行時會清空所有 reading memory；非active channel 回傳 `+9.91e37` (NaN) |
| **[USED]** `FETC:CURRent:LOG? <values/chan>[,<offset/chan>], (@<chanlist>)` / `FETC:VOLTage:LOG?` | values/chan, offset(選), chanlist 1-32 | 取歷史量測 log（ASCII），依 channel 分組依序回傳；單次最多回傳 8192 個 ASCII 值 |
| `FETC:CURRent:LOG:BINary? <values/chan> (@<chanlist>)` / `FETC:VOLTage:LOG:BINary?` | — | 二進位版本，無 8192 上限；每點 64-bit float；受 `FORMat:BORDer` 影響 byte order |
| **[USED]** `FETC:CURR:LOG:POINts?` / `FETC:VOLT:LOG:POINts?` | 無 | 查詢每通道可用 reading 數 |
| `FETC:CURRent:MEDian:FIT:LOG?` / `...MEDian:SUBtraction:LOG? <values/chan>[,<offset/chan>], (@<chanlist>)` | 需至少2通道；processing 上限 3600 點(=1hr@1s間隔) | 雜訊去除（中位數扣除 / 中位數擬合）後的處理結果 |
| `FETC:CURRent:MEDian:FIT:LOG:BINary?` / `...SUBtraction:LOG:BINary?` | 同上，二進位 | — |
| `FETC:CURR:MEDian:SUBtraction:LOG:POINts?` / `...FIT:LOG:POINts?` | 無 | 查詢處理後可用點數 |
| `FETC:PROBecheck? (@<chanlist>)` | 1-32 | 探針/電池存在檢測結果（0=無電池,1=有） |
| `FETC:TEMPerature:LATest?` | 無 | 外部熱敏電阻最新溫度（同 `SYST:TEMP?EXT`） |
| **[USED]** `FETC:TEMPerature:LOG? <values>[,<offset>]` | — | 外部溫度歷史 log（ASCII） |
| `FETC:TEMPerature:LOG:BINary? <values>` | — | 同上，二進位 |
| **[USED]** `FETC:TEMP:LOG:POINts?` | 無 | 查詢溫度 log 可用點數 |
| **[USED]** `FETC:VOLTage:OCV? (@<chanlist>)` | 1-32 | 取得 OCV 測試結果，需搭配 `INIT:TEST:OCV` 先執行 |

> 共通規則：`FETCh?` 查詢不會清除 reading memory，可重複查詢；`INIT` 執行時會清空所有量測 buffer；若查詢的 chanlist 與 `INIT:TEST:MATChed` 設定的 channel group 不同，非 active channel 一律回傳 `+9.91000000e37`（NaN）。

## Format Command

| 指令 | 參數 | 說明 |
|---|---|---|
| `FORMat:BORDer NORMal\|SWAPped` / `?` | `*RST`→SWAPped（廠方最常用設定） | 二進位傳輸的 byte order（僅影響 `...:BINary?` 系列） |

## Initiate Commands

一次只能執行一個 `INIT:TEST:*`（不可同時多種測試同時跑）。

| 指令 | 參數（依序） | 說明 |
|---|---|---|
| **[USED]** `INIT:TEST:MATChed <time>,<ovp>,<uvp>,<res>[,<tint>[,<curr>[,<ocp>]]], (@<chanlist>)` / `...MATChed? (@<chanlist>)` | time:分鐘；ovp/uvp: 0.5~4.5V(0.1mV精度)；res: BT2152A 0.1~10Ω / BT2152B 0.05~10Ω(0.001Ω精度)；tint: 1~256秒(預設1)；curr: ±10mA(0.1µA精度)；ocp: ±10mA(0.1µA精度)；chanlist 1-32 | 設定並啟動電壓匹配放電量測（主要測試指令）。建議測試前先做 in situ 導線電阻校正 |
| **[USED]** `INIT:TEST:OCV <ovp>,<uvp>,<ocp>,<tint>, (@<chanlist>)` / `...OCV? (@<chanlist>)` | ovp/uvp: 0.5~4.5V；ocp: ±10mA；tint: 1~256秒；chanlist 1-32 | 啟動開路電壓測試，結果用 `FETC:VOLT:OCV?` 取得 |
| `INIT:TEST:PROBecheck (@<chanlist>)` | chanlist | 啟動探針/電池存在檢測，結果用 `FETC:PROBecheck?`，完成狀態用 `SENS:PROBecheck:AVAIlable?` 查 |

**`<tint>` 參數細節**：預設1秒，建議值30秒（兼顧取樣頻率與資料量）。最大測試時長 = tint × 24 小時（1秒→1天，60秒→60天…）；實際資料回傳頻率會依 tint 分段（1-4秒→每4秒回1筆，5-8秒→8秒，9-16→16秒，17-32→32秒，33-64→64秒，65-128→128秒，129-250→256秒）。**v3 的 `_poll_sleep_seconds` 輪詢設計即對應此段落。**

## LXI Command

| 指令 | 參數 | 說明 |
|---|---|---|
| `LXI:IDENtify[:STATe] 0\|OFF\|1\|ON` / `?` | bool | 控制前面板 LAN 燈閃爍（識別儀器） |

## Output Commands

| 指令 | 參數 | 說明 |
|---|---|---|
| `OUTPut:INHibit:MODE LATChing\|LIVE\|OFF` / `?` | `*RST`→OFF | Inhibit輸入(pin3)行為：LATChing=鎖存需手動清除、LIVE=即時跟隨、OFF=忽略 |
| `OUTPut:PROTection:CLEar` | 無 | 清除保護事件/inhibit/錯誤，關閉前面板 Error 燈 |

## Sense Commands

| 指令 | 參數 | 說明 |
|---|---|---|
| **[USED]** `SENS:OCV:AVAIlable?` | 無 | OCV測試是否完成（1=完成，僅搭配 `INIT:TEST:OCV` 有效） |
| `SENS:PROBecheck:AVAIlable?` | 無 | 探針檢測是否完成 |
| `SENS:THERmistor:CONFigure <temp>,<resistance>,<beta>` / `?` | temp: -272.15~273.15°C；resistance: 1~1,000,000Ω；beta: 1~1,000,000 | 設定外部熱敏電阻參數（預設 25°C, 10000Ω, 4073） |
| `SENS:TTIMe:REMaining?` | 無 | 目前測試剩餘時間（分鐘） |
| `SENS:VERification:AVAIlable?` | 無 | 驗證程序是否完成 |
| **[USED]** `SENS:WIRE:RES:AVAIlable?` | 無 | 導線電阻校正是否完成 |
| `SENS:WIRE:RESistance:CONFigure <resistance>, (@<chanlist>)` / `...CONFigure? (@<chanlist>)` | 0~5Ω(0.001Ω精度)，chanlist 1-32 | 與 `CAL:WIRE:RES:VALues` 同義 |

## Status Commands

| 指令 | 說明 |
|---|---|
| `STAT:ALARm[:EVENt]?` | 讀取(並清除)Alarm事件暫存器 |
| `STAT:ALARm:CONDiton?` | 讀取Alarm條件暫存器（OVP/OCP/UVP綜合，不清除） |
| `STAT:ALARm:ENABle <value>` / `?` | 設定/查詢哪些bit回報到Status Byte（binary-weighted） |
| `STAT:ALARm:CONDiton:CURRent?` | 各通道OCP條件位元（32-bit，bit0=ch1…bit31=ch32） |
| `STAT:ALARm:CONDiton:VOLTage?` | 各通道OVP條件位元 |
| `STAT:ALARm:CONDiton:VOLTage:UNDer?` | 各通道UVP條件位元 |
| `STAT:OPERation[:EVENt]?` | 讀取(並清除)Standard Operation事件暫存器 |
| `STAT:OPERation:CONDition?` | 讀取Operation條件暫存器（bit0=Calibrating,1=WarmUp,2=EmergencyStop,4=Measuring,8=ConfigChanged,9=Inhibit,12=溫度不穩,13=GlobalError） |
| `STAT:OPERation:ENABle <value>` / `?` | 設定/查詢Operation enable暫存器 |

**保護事件清除流程（重要，供 code review 核對錯誤處理邏輯）**：
1. `STAT:ALARm:EVENt?` → 讀取即清除事件位元，回傳值：OV=1, OC=2, UV=512
2. `STAT:ALARm:CONDiton:CURRent?` / `...VOLTage?` / `...VOLTage:UNDer?` → 確認故障源是否已排除（非0=仍存在）
3. 確認排除後送 `OUTPut:PROTection:CLEar` → 清除前面板 Error 燈
4. 一般命令錯誤（非保護事件）用 `SYSTem:ERRor?` 逐筆讀取並清除，回傳0代表 queue 已空

## System Commands

| 指令 | 參數 | 說明 |
|---|---|---|
| `SYST:COMMunicate:ENABle 0\|OFF\|1\|ON, <interface>` / `?` | interface: USB\|LAN；預設全ON | 啟用/停用介面，需重開機生效 |
| `SYST:COMMunicate:LAN:*` | — | LAN 設定群（CONTrol/DHCP/DNS/DOMain/GATeway/HOSTname/IPADdress/MAC/SMASk/TELNet/UPDate/WINS），與本 GUI 功能無直接關係 |
| `SYST:ERRor?` | 無 | 讀取並清除一筆錯誤（FIFO），格式 `<code>,"<string>"`；`+0,"No error"`=queue空；queue溢位時最新一筆變成 `-350,"Error queue overflow"`；開機才清空，`*RST`不清 |
| `SYST:LICense:CATalog?` | 無 | 回傳授權通道數（004~032，4的倍數） |
| `SYST:TEMPerature? EXTernal` | 無 | 外部熱敏電阻溫度（°C）；未接線回傳 `9.91E37` |

---

## 與 v3 程式碼的落差檢查重點（供之後 code review 使用）

1. **`*RST` 完成時間**：手冊要求「至少等待4秒，IO timeout 設 >4秒」——需確認 v3 送 `*RST`（若有）或依賴預設值時，pyvisa 的 timeout 設定是否足夠。目前 grep 未見 v3 直接送 `*RST`。
2. **保護事件清除流程**：v3 目前的 grep 結果中沒看到 `STATus:ALARm:*` / `OUTPut:PROTection:CLEar` 的使用——若程式沒有處理 OVP/UVP/OCP 保護事件（只靠使用者手動於前面板清除），屬已知限制，可在 review 時對照 handoff.md 的「已知限制」章節確認是否要補。
3. **`SYSTem:ERRor?` 未使用**：v3 grep 未見送出此指令，代表指令層級錯誤（非保護事件）目前完全依賴 pyvisa exception / timeout，SCPI error queue 從未被讀取或清除——長時間測試若累積 error queue 溢位（`-350`）不會被察覺。
4. **`FETC:*:LOG?` 的 8192 值上限**：ASCII log 查詢單次最多回傳 8192 個值；v3 用 `FETC:CURR:LOG?` / `FETC:VOLT:LOG?` 搭配 `LOG:POINts?`，需確認長時間測試（deque maxlen=1000，但儀器端 log 可能遠超過1000點）時有沒有分批索取、有沒有可能單次超過8192值上限。
5. **`<tint>` 與輪詢週期**：手冊資料回傳頻率表（1-4秒間隔→每4秒更新一次…）與 handoff.md 提到的「`FETchThread` 輪詢最快4秒」一致，可用此表核對 `_poll_sleep_seconds` 的對照邏輯是否正確覆蓋所有 tint 區間（5-8/9-16/17-32/33-64/65-128/129-250）。
6. **`CONF:TEST:WIRE:RESistance` 未見使用**：v3 grep 未見送出此指令，代表可能一直使用預設5Ω range；若使用者的導線電阻超過5Ω會需要這個指令切換10/20Ω range，值得在 review 時確認 GUI 是否有對應設定入口。
7. **`CAL:WIRE:RES:INSitu` 的 chanlist 範圍**：手冊該指令段落寫「activechannelsfrom1-4」，但其餘所有 chanlist 敘述皆為 1-32（本機種32通道），研判是原廠文件排版/OCR錯誤，應以1-32為準；review 時不需照本宣科限制成4通道。
