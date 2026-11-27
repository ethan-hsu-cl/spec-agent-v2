#!/usr/bin/env python3
"""Build the Christmas & New Year Sales Android eBug draft batch for round R4-b (the paid 「More Credits Needed!」
dialog in 26 languages, re-run after the balance was lowered; R-070 / R-053 / Q-19, REQ-009, 16.9.0 2611251, draft
20261126-154459 in review). TC-159 / TC-168 (R4-a) were filed from batch 2026-11-26-r4 as DRA262611P0328.

Writes library/pdr/christmas-new-year-sale/android/ebugs/2026-11-26-r4b/20261126_eBug_drafts_NewYear-Sale-R4_16.9.0.md and
the sibling _images/ folder (one NN_ISS-ID folder per entry: red-boxed JPEGs named 16.9.0_<slug>.jpg). Entries continue
the filed numbering (ISS-XMA-43 on). Every Fail row of the run is mapped; the script stops when one is missing. Text
finding only, so no log excerpt (overlay rule 3). Nothing is filed.

Usage: python3 library/pdr/christmas-new-year-sale/android/ebugs/2026-11-26-r4b/generators/ebugs.py
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
NAME = "20261126_eBug_drafts_NewYear-Sale-R4b_16.9.0"
V, B = "16.9.0", "2611251"
TAG = "AIAgent"
DEVICE = "Device: Samsung Galaxy A51 SM-A516B / Android 13"

PM_X = "https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365"

# full-resolution boxes (1080 x 2400 portrait): the dialog body text
BODY = (160, 1250, 925, 1378)  # paid dialog body (below the title, above the CTA)

E = [
 dict(iss="ISS-XMA-43", title="More Credits Needed dialog (paid, Christmas): the Vietnamese body is English except 「tín dụng」",
      cls="UI", sev=3, owner="RD", cases=["TC-194"], extra="O-9", rep=(1, 1), feat="Christmas Sale (Not Enough Credit)",
      short="Paid dialog body mostly English", lang="VIE",
      state=f"Related: Christmas sale window (Stage server, phone date 2026-12-24); build {B}; Pro account (subscribed), signed in, balance 22 credits (below the price); Image to Video Custom (Kling 4.0, 5 s) costs 70; app language set per app",
      related="Related: DRA262611P0328 covers the Free dialog 「Nâng Cấp Lên Pro」 (its body says Pro+ and is mostly English); this is the paid dialog 「Cần Thêm Tín Dụng!」, another string. The other 25 languages translate the paid body (TC-179 – TC-204)",
      note="A new ticket, not a comment on DRA262611P0328 (no comments on existing eBugs, AGENTS.md): P0328 names the Free 「Upgrade to Pro」 dialog and its body string (TC-159, TC-168); this is the paid 「More Credits Needed!」 dialog (R-053), a different string, shown to a subscribed user. The pattern is the same (the Vietnamese body keeps English around 「tín dụng」), so the Note lists P0328 as related. Owner RD (text rule, 2026-11-11): the PM spec states the English body (R-053, pm-xmas-credit: 「You don’t have enough credits to use this feature. Get credits now!」) and R-070 says title, body and CTA are in the app language and not left in English; the spec gives no translation (Q-19, open), but Q-19's own assumption makes a text left in English a defect, so it is filed, not held (ebugs.md step 1). The Expect quotes no translation of our own. Class UI, as ISS-XMA-42 / P0328. Note for the reviewer: the team moved earlier 「not localized」 tickets (P0264 / P0301) to PC-Doc; the casebook rule says RD or PM, never Doc, so RD is proposed and the reviewer may choose. S3 like P0328: a purchase prompt half in English for Vietnamese users; the meaning still reads and the CTA and title are Vietnamese, nothing is blocked. "
           "Reached by the KP-144 route (O-1, O-8): Image to Video loaded on the real date (Stage certificate fails after 2026-12-04), photo and prompt (inspiration chip) entered, Kling 4.0, phone moved to 2026-12-24, per-app language switched with the page open (cmd locale set-app-locales), Generate. Read 2026-11-26 16:25 host. Vietnamese: title 「Cần Thêm Tín Dụng!」, body 「You don't have enough tín dụng to use this feature. Get tín dụng now!」, CTA 「Nhận Ưu Đãi Ngay!」. English (TC-132, R3, 12/24): 「More Credits Needed!」 / 「You don’t have enough credits to use this feature. Get credits now!」 / 「Grab Discount Now!」. Italian paid body has no plan name and passes (TC-185). Text finding: no log (overlay rule 3). New Year window not seen in Vietnamese.",
      steps=["Launch the APP with the phone on the real date",
             "Tap 「Image to Video」 on the Launcher",
             "Tap 「Custom」",
             "Tap the photo area",
             "Select a photo",
             "Tap an inspiration chip to fill the prompt",
             "Set the phone date to 2026-12-24 in Settings (automatic date and time off)",
             "Set the app language of PowerDirector to Tiếng Việt in Settings (per-app language)",
             "Return to the APP (Image to Video still open)",
             "Tap 「Tạo」 (70 credits)",
             "Wait until the 「Cần Thêm Tín Dụng!」 dialog shows",
             "Read the dialog body"],
      res="The VIE body reads 「You don't have enough tín dụng to use this feature. Get tín dụng now!」 (English).",
      res_zh="越南文付費對話框內文除了「tín dụng」外仍是英文（標題與按鈕已翻譯）。",
      exp="The body is fully in Vietnamese, saying 「…enough credits… Get credits now!」 like the title and CTA.",
      exp_zh="內文應完整翻譯成越南文，意思與英文內文相同。",
      imgs=[("TC-194-VIE", "xma43_vie", [BODY], RUN),
            ("TC-132-nec-1224", "xma43_eng", [BODY], R3)],
      log=None,
      links=[("Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-credit board (paid user without enough credits: 「More Credits Needed!」 dialog, English body 「You don’t have enough credits to use this feature. Get credits now!」) -", PM_X)]),
]

NOT_RAISED = [
 ("O-8", "R4-b setup: acda.test9 Pro, balance 22 after the user's two spends; KP-144 route held; dialog ⓧ moves with height", "Account state and tooling note."),
 ("O-9 (rest)", "JPN body asks to buy credits; ESP CTA drops 「now」; ESP (MX) title ends with a period; FRA CTA on two lines; NLD 「tegoed」", "Wording per Q-19 (same meaning, fits); rows passed."),
]
FOLDED = {"O-9": "1. ISS-XMA-43"}
PRIOR = {"TC-159": "filed in 2026-11-26-r4 as DRA262611P0328", "TC-168": "filed in 2026-11-26-r4 as DRA262611P0328",
         **{f"O-{i}": "covered by batch 2026-11-26-r4" for i in range(1, 8)}}


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
            MAP.setdefault(k.split()[0], []).append("not raised (rest)" if " " in k else "not raised")
    for k, v in PRIOR.items():
        MAP.setdefault(k, []).append(v)
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
    w(f"# Christmas & New Year Sales (Android) — eBug drafts, round R4-b (paid More Credits Needed dialog in 26 languages), PDR-A {V} build {B}")
    w("")
    w(f"**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-26-r4-dialog-mui/` — R4-b re-run (2026-11-26 16:19–16:28) of round R4, draft `drafts/20261126-154459` (in review, not yet saved; R-070, R-053, Q-19, TC-179 – TC-204, REQ-009), on {DEVICE[8:]} through Appium / UiAutomator2, build 16.9.0.{B}, Stage server, phone date 2026-12-24 (Christmas window, KF-003; Image to Video loaded on the real date first, KP-144), per-app language switched with the page open, acda.test9 Pro, balance 22, Image to Video Custom (Kling 4.0, 5 s) 70 credits. R4-b tally: 25 Pass, 1 Fail (TC-194). R4 total: 49 Pass, 3 Fail, 0 Blocked; TC-159 / TC-168 already filed as DRA262611P0328 (batch 2026-11-26-r4).")
    w("")
    w("**Status:** nothing filed, uploaded or commented. Sixth batch of this feature (R1, R1r, R2, R3, R4 filed: P0254–P0275, P0299–P0313, P0327, P0328). Dedupe: per OS, read-only (`dedupe.txt`).")
    w("")
    w("Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` owner RD for defects, no `[UX]`; no comment on DRA262611P0328 (related only). Severity is proposed.")
    w("")
    w(f"**What is drafted:** {len(E)} entry (ISS-XMA-43, TC-194): 1 RD UI.")
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
    w(f"{len(fails)} Fail in R4 (TC-159, TC-168 filed as DRA262611P0328 from batch 2026-11-26-r4; TC-194 here), 0 Blocked, {len(obs)} observations ({obs[0]} … {obs[-1]}; O-1 – O-7 belong to the R4 batch).")
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
