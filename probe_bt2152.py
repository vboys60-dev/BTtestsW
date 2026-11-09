#!/usr/bin/env python3
"""BT2152A/B 唯讀連線探測。

只送查詢指令，不送任何 INIT / CAL / ABORt / 設定指令，接著正在跑的測試也不會被打斷。
唯一會改變儀器狀態的是 SYST:ERR?（FIFO，讀取即清除），輸出會明確標示。

用法：
    python3 probe_bt2152.py
    python3 probe_bt2152.py --addr TCPIP0::169.254.4.61::inst0::INSTR
    python3 probe_bt2152.py --list          # 只列出看得到的資源
"""
import argparse
import sys

import pyvisa

DEFAULT_ADDR = "TCPIP0::169.254.4.61::inst0::INSTR"

# (標題, 指令)。全部唯讀；會清除狀態的暫存器查詢（STAT:*:EVENt?、*ESR?）刻意不放進來。
PROBES = [
    ("識別",           "*IDN?"),
    ("授權通道數",     "SYST:LIC:CAT?"),
    ("自我測試",       None),  # *TST? 會花數十秒且中斷量測，不自動跑
    ("外部溫度",       "SYST:TEMP? EXTernal"),
    ("熱敏電阻設定",   "SENS:THER:CONF?"),
    ("導線電阻 range", "CONF:TEST:WIRE:RES?"),
    ("in situ 電流",   "CONF:INS:CURR?"),
    ("Operation 狀態", "STAT:OPER:COND?"),
    ("Alarm 條件",     "STAT:ALARm:CONDiton?"),
    ("OVP 通道位元",   "STAT:ALARm:CONDiton:VOLTage?"),
    ("UVP 通道位元",   "STAT:ALARm:CONDiton:VOLTage:UNDer?"),
    ("OCP 通道位元",   "STAT:ALARm:CONDiton:CURRent?"),
    ("OCV 完成旗標",   "SENS:OCV:AVAI?"),
    ("導線校準旗標",   "SENS:WIRE:RES:AVAI?"),
    ("測試剩餘時間",   "SENS:TTIM:REM?"),
    ("電壓 log 點數",  "FETC:VOLT:LOG:POIN?"),
    ("溫度 log 點數",  "FETC:TEMP:LOG:POIN?"),
    ("測試設定回讀",   "INIT:TEST:MATC? (@1)"),
]

OPER_BITS = {0: "Calibrating", 1: "WarmUp", 2: "EmergencyStop", 4: "Measuring",
             8: "ConfigChanged", 9: "Inhibit", 12: "溫度不穩", 13: "GlobalError"}

MAX_ASCII_VALUES = 8192   # 手冊：ASCII 版 FETC:*:LOG? 單次上限


def ask(inst, cmd):
    try:
        return inst.query(cmd).strip()
    except Exception as e:
        return f"!! {type(e).__name__}: {e}"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--addr", default=DEFAULT_ADDR, help=f"VISA 位址（預設 {DEFAULT_ADDR}）")
    ap.add_argument("--timeout", type=int, default=10000, help="VISA timeout(ms)，預設 10000")
    ap.add_argument("--list", action="store_true", help="只列出看得到的資源後結束")
    args = ap.parse_args()

    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    print(f"VISA backend : {rm.visalib}")
    print(f"可見資源     : {resources or '(無)'}")
    if args.list:
        return 0

    print(f"連線         : {args.addr}")
    try:
        inst = rm.open_resource(args.addr)
        inst.timeout = args.timeout
    except Exception as e:
        print(f"\n連線失敗: {type(e).__name__}: {e}")
        print("請確認網路線已接、儀器已開機，且本機有該網段的位址（link-local 需等 169.254.x 介面起來）。")
        return 1

    results = {}
    print("\n--- 唯讀查詢 ---")
    for label, cmd in PROBES:
        if cmd is None:
            continue
        val = ask(inst, cmd)
        results[cmd] = val
        print(f"{label:<16} {cmd:<32} {val}")

    print("\n--- 錯誤佇列（讀取會清除，FIFO）---")
    for _ in range(20):
        err = ask(inst, "SYST:ERR?")
        print(f"  {err}")
        if err.startswith("!!") or err.lstrip('+').startswith("0,"):
            break

    print("\n--- 對照 code review 的判讀 ---")

    lic = results.get("SYST:LIC:CAT?", "")
    try:
        n_lic = int(float(lic))
        note = "全 32 通道" if n_lic >= 32 else f"少於 32！(@1:32) 的回傳會比 32 短"
        print(f"授權通道數 {n_lic}：{note}  → A6/A7 索引防護{'（此機不會觸發）' if n_lic >= 32 else '在這台機器上會被用到'}")
        print(f"單次可安全取用點數上限：{MAX_ASCII_VALUES // max(1, n_lic)} 點/批（{MAX_ASCII_VALUES} 值 ÷ {n_lic} 通道）→ A3 分批上限")
    except ValueError:
        print(f"授權通道數讀取失敗：{lic}")

    v_pts, t_pts = results.get("FETC:VOLT:LOG:POIN?", ""), results.get("FETC:TEMP:LOG:POIN?", "")
    try:
        lag = int(float(v_pts)) - int(float(t_pts))
        verdict = "兩邊同步" if lag == 0 else f"溫度落後 {lag} 點" if lag > 0 else f"溫度超前 {-lag} 點"
        print(f"電壓 log {v_pts} 點 / 溫度 log {t_pts} 點：{verdict}  → A4 就是靠這個差值觸發")
    except ValueError:
        print(f"log 點數讀取失敗：volt={v_pts} temp={t_pts}")

    oper = results.get("STAT:OPER:COND?", "")
    try:
        bits = int(float(oper))
        flags = [name for bit, name in OPER_BITS.items() if bits & (1 << bit)]
        print(f"Operation 條件 {bits}：{', '.join(flags) or '無旗標'}")
        if bits & (1 << 4):
            print("  ⚠ 儀器正在量測中，本腳本沒有中斷它，但要跑其他驗證前請先確認可以停。")
    except ValueError:
        print(f"Operation 狀態讀取失敗：{oper}")

    matc = results.get("INIT:TEST:MATC? (@1)", "")
    print(f"測試設定回讀：{matc}")
    print("  第一個參數是 <time>(分鐘)。A1 修好後，總紀錄時間設 24:00:00 應回讀 1440，而非 720。")

    inst.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
