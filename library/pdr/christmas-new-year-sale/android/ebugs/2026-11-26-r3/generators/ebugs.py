#!/usr/bin/env python3
"""Build the Christmas & New Year Sales Android eBug draft batch for round R3 (the low-balance Not Enough Credit rows,
16.9.0 2611251, draft 20261120-165128, REQ-007 / REQ-008).

Writes library/pdr/christmas-new-year-sale/android/ebugs/2026-11-26-r3/20261126_eBug_drafts_NewYear-Sale-R3_16.9.0.md and
the sibling _images/ folder (one NN_ISS-ID folder per entry: red-boxed JPEGs and log excerpts named 16.9.0_<slug>.*).
Entries continue the filed numbering (ISS-XMA-41 on). Every Fail row of the run is mapped; the script stops when one is
missing. Nothing is filed.

Usage: python3 library/pdr/christmas-new-year-sale/android/ebugs/2026-11-26-r3/generators/ebugs.py
"""
import csv, glob, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(OUT, *[".."] * 6))
ROOT = f"{REPO}/library/pdr/christmas-new-year-sale/android"
RUN = f"{ROOT}/runs/2026-11-26-r3-lowbalance"
LOG = {"R3-a2": glob.glob(f"{RUN}/logs/R3-a2-*/logcat-live.txt")[0]}
NAME = "20261126_eBug_drafts_NewYear-Sale-R3_16.9.0"
V, B = "16.9.0", "2611251"
TAG = "AIAgent"
DEVICE = "Device: Samsung Galaxy A51 SM-A516B / Android 13"

PM_X = "https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365"
PM_N = "https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161"

# full-resolution boxes (1080 x 2400 portrait)
DIALOG = (105, 715, 975, 1650)
LAUNCHER = (6, 90, 1074, 870)
INPUTS = (40, 765, 1040, 1660)

E = [
 dict(iss="ISS-XMA-41", title="Not Enough Credit dialog (Free, 「Upgrade to Pro」): one system Back closes the dialog and Image to Video together; photo, prompt and model are lost",
      cls="Functional", sev=2, owner="RD", cases=["TC-142"], extra="O-7", rep=(3, 3), feat="Christmas & New Year Sale (Not Enough Credit)",
      short="Free dialog: one Back also closes Image to Video",
      state=f"Related: Christmas sale window (Stage server, phone date 2026-12-24) and New Year sale window (phone date 2026-12-30); build {B}; Free account, signed in, balance 7 credits (below the price); Image to Video Custom (Kling 4.0, 5 s) costs 70",
      related="Related: same on the New Year dialog (phone date 2026-12-30); the same dialog's ⓧ closes only the dialog (TC-142 third setup, TC-141 on the paid dialog); Back on the paid 「More Credits Needed!」 dialog was not tried",
      note="R-062 (team rule, Android system Back: Back on the Not Enough Credit dialog closes it like ⓧ) with R-057 (PM pm-xmas-credit: ⓧ closes it, back on the feature page). Seen on 12/24 two times in results.csv (three per O-7; Appium pressKey and adb keyevent 4) and on the New Year dialog on 12/30 once (O-7). Logcat 2026-12-24 15:24:33.430: the Back key goes to ViewRootImpl[ImageToVideoActivity] (ViewPostIme key 0/1), 15:24:33.473 Project2Activity (Launcher) becomes visible, then ImageToVideoActivity stops: the dialog does not consume the key. Phone-date note: with the date after 2026-12-04 a Stage certificate error leaves Image to Video with no model when the page loads (O-1, environment), so the run loaded the page on the real date and moved the date before Generate (O-4); the campaign follows the phone date (KF-003). Pro dialog Back: no row, not tried.",
      steps=["Launch the APP",
             "Tap 「Image to Video」 on the Launcher",
             "Tap 「Custom」",
             "Tap the photo area",
             "Select a photo",
             "Enter a prompt",
             "Set the phone date to 2026-12-24 in Settings (automatic date and time off)",
             "Return to the APP",
             "Tap 「Generate」 (70 credits)",
             "Wait until the 「Upgrade to Pro」 dialog shows",
             "Press system Back once"],
      res="One Back closes the dialog and Image to Video: the Launcher shows, photo and prompt lost. ⓧ closes only the dialog.",
      res_zh="按一次返回鍵，對話框與 Image to Video 一起關閉回到首頁，輸入遺失；ⓧ 只關對話框。",
      exp="One Back closes only the dialog, back on Image to Video with the inputs kept, as ⓧ does.",
      exp_zh="按一次返回鍵應如 ⓧ 只關閉對話框，留在 Image to Video，輸入保留。",
      imgs=[("TC-134-nec-free-1224", "xma41_dialog", [DIALOG]),
            ("TC-142-after-back", "xma41_after_back", [LAUNCHER]),
            ("TC-142-after-x", "xma41_after_x", [INPUTS])],
      log=("xma41_log", "R3-a2", ["2026-12-24 15:24:33", "2026-12-30 15:30:07"],
           r"ViewPostIme key|\[Project2Activity\]: handleAppVisibility mAppVisible = false|\[ImageToVideoActivity\]: (MSG_WINDOW_FOCUS_CHANGED|WindowStopped)"),
      links=[("Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-credit board (free user without enough credits: 「Upgrade to Pro」 dialog; ⓧ closes it, back on the feature page; Android system Back acts as ⓧ, QA rule R-062) -", PM_X),
             ("Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-credit board (New Year Not Enough Credit dialog, same logic) -", PM_N)]),
]

NOT_RAISED = [
 ("O-1", "Image to Video loads no model with the phone date after 2026-12-04 (Stage GW certificate)", "Environment (server certificate), not an app defect."),
 ("O-2", "acda.test9 still Pro ~25 h after the R2 New Year test subscription", "Account state; knowledge (I-031)."),
 ("O-3", "Black Friday Not Enough Credit dialog on the real date; missing from the page source", "Other campaign; tooling note."),
 ("O-4", "Workaround: load the page on the real date, then move the date", "Tooling note."),
 ("O-5", "「3 Credits Received」 on opening the Christmas credit page", "Daily credit, expected."),
 ("O-6", "AI Video Enhance task banner from another session on the shared account", "Shared account."),
 ("O-8", "acda.test9 now Free, balance 7; Samsung update screen after date moves", "Account state; tooling note."),
 ("O-9", "Black Friday countdown pill on the real date; interstitial after moving the date back", "Other campaign / artifact of moving the clock."),
 ("TC-133 countdown", "Christmas credit page countdown 3D 09:23", "Already DRA262611P0313 (ISS-XMA-40, R2)."),
]
FOLDED = {"O-7": "1. ISS-XMA-41"}


def shot(src, dst, boxes):
    im = Image.open(src).convert("RGB")
    d = ImageDraw.Draw(im)
    w = max(4, im.size[0] // 160)
    for b in boxes:
        d.rectangle(b, outline=(255, 0, 0), width=w)
    im.thumbnail((1400, 1400))
    im.save(dst, "JPEG", quality=82)


def excerpt(path, times, pat, cap=24):
    out, seen = [], set()
    for line in open(path, encoding="utf-8", errors="replace"):
        if any(line.startswith(t) for t in times) and re.search(pat, line):
            key = line[:10] + re.sub(r"^\S+ \S+ +\d+ +\d+ ", "", line.strip())
            if key in seen:
                continue
            seen.add(key)
            out.append(line.rstrip()[:240])
            if len(out) >= cap:
                break
    return out


def main():
    rows = list(csv.DictReader(open(f"{RUN}/results.csv", encoding="utf-8-sig")))
    fails = [r["ID"] for r in rows if r["Result"] == "Fail"]
    obs_file = open(f"{RUN}/observations.md", encoding="utf-8").read()
    obs = sorted(set(re.findall(r"^- (O-\d+)", obs_file, re.M)), key=lambda s: int(s[2:]))
    MAP = {}
    for n, e in enumerate(E, 1):
        for c in e["cases"]:
            MAP.setdefault(c, []).append(f"{n}. {e['iss']}")
    for k, _, _ in NOT_RAISED:
        if k.startswith("O-"):
            MAP.setdefault(k, []).append("not raised")
    for k, v in FOLDED.items():
        MAP.setdefault(k, []).append(f"folded into {v}")
    MAP = {k: "; ".join(dict.fromkeys(v)) for k, v in MAP.items()}
    need = fails + obs
    missing = [k for k in need if k not in MAP]
    extra = [k for k in MAP if k not in need]
    if missing or extra:
        sys.exit(f"unmapped: {missing}; not in run: {extra}")

    img_root = f"{OUT}/{NAME}_images"
    if os.path.isdir(img_root):
        shutil.rmtree(img_root)
    os.makedirs(img_root)
    L = []
    w = L.append
    w(f"# Christmas & New Year Sales (Android) — eBug drafts, round R3 (low-balance Not Enough Credit rows), PDR-A {V} build {B}")
    w("")
    w(f"**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-26-r3-lowbalance/` — round R3 of draft `drafts/20261120-165128` (table v2; the 10 low-balance Not Enough Credit rows, REQ-007, R3-a re-run REQ-008), 2026-11-26, on {DEVICE[8:]} through Appium / UiAutomator2, build 16.9.0.{B} updated on the phone by the user, Stage server, the campaign driven by the phone's system date (KF-003), acda.test9 signed in (Pro in R3-b; Free, balance 7, in the R3-a re-run), Image to Video Custom (Kling 4.0, 5 s) 70 credits. Tally: 9 Pass, 1 Fail, 0 Blocked.")
    w("")
    w("**Status:** nothing filed, uploaded or commented. Fourth batch of this feature (R1, R1r, R2 filed: P0254–P0275, P0299–P0313). Dedupe: per OS, read-only (`dedupe.txt`).")
    w("")
    w("Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` owner RD for defects, no `[UX]`. Severity is proposed.")
    w("")
    w(f"**What is drafted:** {len(E)} entry (ISS-XMA-41): 1 RD Functional.")
    w("")
    w("Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.")
    w("")
    for n, e in enumerate(E, 1):
        folder = f"{n:02d}_{e['iss']}"
        os.makedirs(f"{img_root}/{folder}")
        names = []
        for src, slug, boxes in e["imgs"]:
            p = f"{RUN}/screenshots/{src}.png"
            if not os.path.exists(p):
                sys.exit(f"missing {p}")
            name = f"{V}_{slug}.jpg"
            shot(p, f"{img_root}/{folder}/{name}", boxes)
            names.append(name)
        logname = None
        if e.get("log"):
            slug, seg, times, pat = e["log"]
            lines = excerpt(LOG[seg], times, pat)
            if not lines:
                sys.exit(f"{e['iss']}: empty log excerpt")
            txt = "\n".join(lines) + "\n"
            if re.search(r"(?i)bearer|authorization|token=|signature=|public_key", txt):
                sys.exit(f"{e['iss']}: secret-looking text in log excerpt")
            logname = f"{V}_{slug}.txt"
            open(f"{img_root}/{folder}/{logname}", "w", encoding="utf-8").write(txt)
        tagtype = "" if e["cls"] == "Functional" else f"[{e['cls']}]"
        short = f"PDR-A {V} - [{TAG}]{tagtype} {e['feat']}: {e['short']}"
        if len(short) > 125:
            sys.exit(f"{e['iss']} short description {len(short)} > 125")
        for s in e["steps"]:
            if ">" in s or "›" in s:
                sys.exit(f"{e['iss']} step has a chain: {s}")
        rs = ", ".join(e["cases"])
        if e.get("extra"):
            rs = (rs + ", " if rs else "") + e["extra"]
        w("---"); w("")
        w(f"## {n}. {e['iss']} — {e['title']}  ·  Class: {e['cls']}  ·  Severity: S{e['sev']}  ·  Owner: {e['owner']}")
        w("")
        w(f"**Report step:** {rs}  ·  **Reproduce:** {e['rep'][0]}/{e['rep'][1]}  ·  **Verified on:** {V}.{B}")
        w("")
        w(f"> **QA note — not pasted into eBug.** {e['note']}")
        w("")
        w("**Short Description:**"); w(""); w("```"); w(short); w("```"); w("")
        w("**Description:**"); w(""); w("```"); w("Repro Steps:")
        for i, s in enumerate(e["steps"], 1):
            w(f"{i}. {s}")
        w(f"{len(e['steps']) + 1}. Check the result")
        w(""); w("Result:"); w(e["res"]); w(f"摘要：{e['res_zh']}"); w(" ".join("{" + x + "}" for x in names + ([logname] if logname else [])))
        w(""); w("Expect Result:"); w(e["exp"]); w(f"摘要：{e['exp_zh']}")
        w(""); w("Note:"); w(DEVICE); w(e["state"])
        if e.get("related"):
            w(e["related"])
        for label, url in e["links"]:
            w(label); w(url)
        w("<Claude Reviewed>"); w("```"); w("")
        w(f"**Images:** `{NAME}_images/{folder}/`"); w("")

    w("---"); w("")
    w("## Not raised (for the record)")
    w("")
    w("| Item | What was seen | Why not raised |")
    w("|---|---|---|")
    for k, a, b in NOT_RAISED:
        w(f"| {k} | {a} | {b} |")
    w("")
    w("## Reconciliation against the run")
    w("")
    w(f"{len(fails)} Fail (all defect), 0 Blocked, {len(obs)} observations ({obs[0]} … {obs[-1]}).")
    w("")
    w("### Row-by-row map")
    w("")
    w("| Item | Result | Disposition | Became |")
    w("|---|---|---|---|")
    disp = {r["ID"]: (r["Result"], r["Disposition"]) for r in rows}
    for k in fails:
        w(f"| {k} | {disp[k][0]} | {disp[k][1] or '—'} | {MAP[k]} |")
    for k in obs:
        w(f"| {k} | observation | — | {MAP[k]} |")
    w("")
    w("### Owner split")
    w("")
    w("| Owner | Entries |")
    w("|---|---|")
    w("| RD | 1 |")
    w("")
    w("### Filing order")
    w("")
    w("**1**. Nothing is filed until the review page's decisions come back.")
    w("")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(L))
    print(f"wrote {len(E)} entries → {OUT}/{NAME}.md")


if __name__ == "__main__":
    main()
