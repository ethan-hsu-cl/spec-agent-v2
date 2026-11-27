#!/usr/bin/env python3
"""Build the Christmas & New Year Sales Android eBug draft batch for round R4 (the Not Enough Credit dialog in 26
languages, R-070 / Q-19, REQ-009, 16.9.0 2611251, draft 20261126-154459 in review).

Writes library/pdr/christmas-new-year-sale/android/ebugs/2026-11-26-r4/20261126_eBug_drafts_NewYear-Sale-R4_16.9.0.md and
the sibling _images/ folder (one NN_ISS-ID folder per entry: red-boxed JPEGs named 16.9.0_<slug>.jpg). Entries continue
the filed numbering (ISS-XMA-42 on). Every Fail row of the run is mapped; the script stops when one is missing. Text
finding only, so no log excerpt (overlay rule 3). Nothing is filed.

Usage: python3 library/pdr/christmas-new-year-sale/android/ebugs/2026-11-26-r4/generators/ebugs.py
"""
import csv, glob, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(OUT, *[".."] * 6))
ROOT = f"{REPO}/library/pdr/christmas-new-year-sale/android"
RUN = f"{ROOT}/runs/2026-11-26-r4-dialog-mui"
R3 = f"{ROOT}/runs/2026-11-26-r3-lowbalance"
LOG = {}
NAME = "20261126_eBug_drafts_NewYear-Sale-R4_16.9.0"
V, B = "16.9.0", "2611251"
TAG = "AIAgent"
DEVICE = "Device: Samsung Galaxy A51 SM-A516B / Android 13"

PM_X = "https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365"

# full-resolution boxes (1080 x 2400 portrait): the dialog body text
BODY = (160, 1225, 925, 1385)

E = [
 dict(iss="ISS-XMA-42", title="Not Enough Credit dialog (Free, 「Upgrade to Pro」): the body names Pro+ in Italian and Vietnamese; the Vietnamese body is mostly English",
      cls="UI", sev=3, owner="RD", cases=["TC-159", "TC-168"], extra="O-4", rep=(2, 2), feat="Christmas Sale (Not Enough Credit)",
      short="Free dialog body says Pro+; VIE mostly English", lang="ITA/VIE",
      state=f"Related: Christmas sale window (Stage server, phone date 2026-12-24); build {B}; Free account, signed in, balance 7 credits (below the price); Image to Video Custom (Kling 4.0, 5 s) costs 70; app language set per app",
      related="Related: the other 24 languages and English say Pro in the body (TC-134, TC-153 – TC-178); title and CTA are translated in ITA and VIE",
      note="One ticket, not two: both fails are the same string (the free dialog body) in two locales, and both put Pro+ where the English and the title say Pro, so the localized body looks taken from a Pro+ variant of the string (O-4); the Vietnamese one is also left largely untranslated. The fix is the same resource in two locale files, like ISS-XMA-30 grouping four languages. Owner RD (text rule, 2026-11-11): the PM spec states the English text (R-055, pm-xmas-credit: 「Upgrade to Pro」 / 「… Upgrade to Pro to get free bonus credits every month.」), the plan name Pro is not open, and R-070 says the dialog is in the app language and not left in English; the spec gives no translation (Q-19, open), but Q-19's own assumption makes a text left in English a defect, and naming another plan is wrong whatever the wording decision, so it is filed, not held (ebugs.md step 1). Note for the reviewer: on filing, the team moved the R1/R2 「not localized」 tickets P0264 / P0301 to PC-Doc (and P0316, P0319, P0320 on Cinematic Reel are PC-Doc); the casebook rule says RD or PM, never Doc, so RD is proposed and the reviewer may choose. Expect quotes no translation of our own beyond the plan name. Pro+ is the top tier (VIP, KP-037), a different, dearer plan than the CTA's Pro offer: misleading in a purchase prompt, hence S3 (S2 if the reviewer counts a wrong plan in a paywall as important). "
           "Reached by the KP-144 workaround: Image to Video loaded on the real date (Stage certificate fails after 2026-12-04), phone moved to 2026-12-24, per-app language switched with the page open (cmd locale set-app-locales; the activity recreates and keeps photo, prompt, model, price), Generate (O-1, O-4). "
           "Bodies read: ITA 「Non disponi di sufficienti crediti per usare questa funzione. Passa Pro+ per ricevere crediti bonus gratuiti ogni mese.」 (Pro+, and 「a」 missing: title 「Passa a Pro」); VIE 「You don't have enough tín dụng to use this feature. Nâng cấp lên Pro+ to get free bonus tín dụng every month.」 (title 「Nâng Cấp Lên Pro」, CTA 「Nhận Ưu Đãi Ngay!」); ENG 「You don’t have enough credits to use this feature. Upgrade to Pro to get free bonus credits every month.」 (TC-134, R3). Text finding: no log (overlay rule 3). New Year window and the paid dialog (TC-179 – TC-204, Blocked test-data) not seen in these languages.",
      steps=["Launch the APP with the phone on the real date",
             "Tap 「Image to Video」 on the Launcher",
             "Tap 「Custom」",
             "Tap the photo area",
             "Select a photo",
             "Enter a prompt",
             "Set the phone date to 2026-12-24 in Settings (automatic date and time off)",
             "Set the app language of PowerDirector to Italiano in Settings (per-app language)",
             "Return to the APP (Image to Video still open)",
             "Tap 「Genera」 (70 credits)",
             "Wait until the 「Passa a Pro」 dialog shows",
             "Read the dialog body",
             "Tap ⓧ",
             "Set the app language of PowerDirector to Tiếng Việt in Settings",
             "Return to the APP",
             "Tap 「Tạo」 (70 credits)",
             "Wait until the 「Nâng Cấp Lên Pro」 dialog shows",
             "Read the dialog body"],
      res="ITA body says 「Passa Pro+」, VIE 「Nâng cấp lên Pro+」 (titles say Pro); the VIE body is mostly English.",
      res_zh="義大利文與越南文內文寫成 Pro+（標題為 Pro）；越南文內文大多仍是英文。",
      exp="The body names Pro like the title and the English 「Upgrade to Pro」, fully in the app language.",
      exp_zh="內文應與標題及英文一致寫 Pro，且完整翻譯成該語言。",
      imgs=[("TC-159-ITA", "xma42_ita", [BODY], RUN),
            ("TC-168-VIE", "xma42_vie", [BODY], RUN),
            ("TC-134-nec-free-1224", "xma42_eng", [BODY], R3)],
      log=None,
      links=[("Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-credit board (free user without enough credits: 「Upgrade to Pro」 dialog, English body 「… Upgrade to Pro to get free bonus credits every month.」) -", PM_X)]),
]

NOT_RAISED = [
 ("O-1", "Cheaper route: per-app language switched with Image to Video open keeps its inputs", "Tooling note (extends KP-144)."),
 ("O-2", "KOR / JPN / ESP drop 「free」 or 「bonus」; KOR title 프로, 「요.」 alone; FRA CTA on two lines", "Wording per Q-19 (same meaning, fits); rows passed."),
 ("O-3", "acda.test9 Free, balance 7; Black Friday pill on the real date", "Account state; other campaign."),
 ("O-5", "THA / FAS titles spell the plan out; RTL page behind the dialog not mirrored", "Wording per Q-19; the page is outside these rows."),
 ("O-6", "Pro test purchase adds 100 credits at once (7 → 107); paid dialog rows Blocked", "Test data (TC-179 – TC-204 Blocked)."),
 ("O-7", "Bottom tab reads 「Pro」 after purchase; stray taps; empty project left", "Tooling note."),
]
FOLDED = {"O-4": "1. ISS-XMA-42"}


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
    w(f"# Christmas & New Year Sales (Android) — eBug drafts, round R4 (Not Enough Credit dialog in 26 languages), PDR-A {V} build {B}")
    w("")
    w(f"**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-26-r4-dialog-mui/` — round R4 of draft `drafts/20261126-154459` (in review, not yet saved; R-070, Q-19, TC-153 – TC-204, REQ-009), 2026-11-26, on {DEVICE[8:]} through Appium / UiAutomator2, build 16.9.0.{B}, Stage server, phone date 2026-12-24 (Christmas window, KF-003; Image to Video loaded on the real date first, KP-144), per-app language switched with the page open, acda.test9 Free, balance 7, Image to Video Custom (Kling 4.0, 5 s) 70 credits. Tally: 24 Pass, 2 Fail, 26 Blocked (test-data: the paid dialog rows, O-6).")
    w("")
    w("**Status:** nothing filed, uploaded or commented. Fifth batch of this feature (R1, R1r, R2, R3 filed: P0254–P0275, P0299–P0313, P0327). Dedupe: per OS, read-only (`dedupe.txt`).")
    w("")
    w("Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` owner RD for defects, no `[UX]`. Severity is proposed.")
    w("")
    w(f"**What is drafted:** {len(E)} entry (ISS-XMA-42, TC-159 and TC-168 merged): 1 RD UI.")
    w("")
    w("Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.")
    w("")
    for n, e in enumerate(E, 1):
        folder = f"{n:02d}_{e['iss']}"
        os.makedirs(f"{img_root}/{folder}")
        names = []
        for src, slug, boxes, run in e["imgs"]:
            p = f"{run}/screenshots/{src}.png"
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
        tagtype = ("" if e["cls"] == "Functional" else f"[{e['cls']}]") + (f"[{e['lang']}]" if e.get("lang") else "")
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
        w(""); w("Result:"); w(e["res"]); w(f"摘要：{e['res_zh']}"); [w(q) for q in e.get("quotes", [])]; w(" ".join("{" + x + "}" for x in names + ([logname] if logname else [])))
        w(""); w("Expect Result:"); w(e["exp"]); w(f"摘要：{e['exp_zh']}"); [w(q) for q in e.get("exp_quotes", [])]
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
    w(f"{len(fails)} Fail (all defect, merged into one entry), 26 Blocked (test-data, O-6, not raised), {len(obs)} observations ({obs[0]} … {obs[-1]}).")
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
