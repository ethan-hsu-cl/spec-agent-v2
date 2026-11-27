#!/usr/bin/env python3
"""Build the Christmas & New Year Sales Android eBug draft batch for round R5 (REQ-010: light-mode rechecks of the New
Year IAP annual card, the landscape IAP page in light mode, and the Mine / Pro Credits bar proportion; 16.9.0 2611251).

Writes library/pdr/christmas-new-year-sale/android/ebugs/2026-11-26-r5/20261126_eBug_drafts_NewYear-Sale-R5_16.9.0.md and
the sibling _images/ folder (one NN_ISS-ID folder per entry: red-boxed JPEGs named 16.9.0_<slug>.jpg). Entries continue
the filed numbering (ISS-XMA-44 on). Every Fail row and observation of the run is mapped; the script stops when one is
missing. Visual findings only, so no log excerpt (overlay rule 3). Nothing is filed.

Usage: python3 library/pdr/christmas-new-year-sale/android/ebugs/2026-11-26-r5/generators/ebugs.py
"""
import csv, os, re, shutil, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(OUT, *[".."] * 6))
ROOT = f"{REPO}/library/pdr/christmas-new-year-sale"
RUN = f"{ROOT}/android/runs/2026-11-26-r5-light-mine"
FIG = f"{ROOT}/specs/2026-11-20/extracted/figma"
NAME = "20261126_eBug_drafts_NewYear-Sale-R5_16.9.0"
V, B = "16.9.0", "2611251"
TAG = "AIAgent"
DEVICE = "Device: Samsung Galaxy A51 SM-A516B / Android 13"

DS = "https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id="
NY_IAP_LIGHT = DS + "2855-39936"
NY_LAND = DS + "2844-22907"
XMAS_LAND = DS + "2750-27885"
MINE_FREE = DS + "2682-13540"
MINE_VIP = DS + "2718-4363"

# full-resolution boxes
P_ANNUAL = (48, 1300, 1032, 1516)          # portrait annual card incl. tag (1080 x 2400)
L_ANNUAL = (1244, 88, 2232, 316)           # landscape annual card incl. tag (2400 x 1080)
L_MONTHLY = (1246, 344, 2228, 495)         # landscape monthly card border
L_SEP = [(1568, 962, 1618, 1028), (1854, 962, 1904, 1028)]  # landscape 「|」 separators (white)
P_MONTHLY = (46, 1546, 1034, 1692)         # portrait monthly card
P_SEP = [(338, 2186, 384, 2240), (698, 2186, 744, 2240)]  # portrait separators (grey)
FREE_BAR = (42, 859, 1038, 1066)
PRO_BAR = (42, 568, 1038, 775)
# Figma board images are 1 image px per Figma px (frames 375 wide); frame origins found on the board image
NY_DARK_FRAME, NY_LIGHT_FRAME = (163, 226), (595, 226)
MINE_FREE_FRAME, MINE_VIP_FRAME = (1115, 282), (1664, 282)

E = [
 dict(iss="ISS-XMA-44", title="New Year IAP page: the annual plan card keeps its dark-mode navy background in light mode (portrait and landscape)",
      cls="UI", sev=3, owner="RD", cases=["TC-102", "TC-146"], extra="O-1", rep=(2, 2), feat="New Year Sale (IAP)",
      short="Annual plan card uses the dark-mode background in light mode",
      state="Related: New Year sale window (Stage server, phone date 2026-12-30); build 2611251; Free account, signed in; app Appearance 「Device Settings」 with the system in light mode (also with Appearance 「Light Mode」)",
      related="Related: the Christmas IAP annual card follows the mode (cream in light, burgundy in dark)",
      note="REQ-010 (user, 2026-11-26): 「但在Light mode下New Year Sales IAP年方案卡片的背景顏色不對(用到Dark mode圖樣)」. Background only: the plan-card texts (Special Offer / 57% OFF / NT$1210/Year) follow the Design and were ruled NAB by the user on DRA262611P0309, so they are not raised here and P0309 is not a duplicate (it is about text, this is the card's background); P0309 is not commented on. "
           "Measured (R5-a, 12/30, Mine 「Claim Holiday Deal」, Free, acda.test9): the annual card is navy (3,24,114) at the left edge to (19,49,152) on the right in LIGHT mode, pixel-identical to DARK mode; the page background follows the mode (249,251,255 light / 12,12,12 dark). Design New Year IAP & Credit board: light IAP_year 2855:39936 draws a pale cream card (251,246,221), dark IAP_year 2855:39855 a dark navy card (9,18,55). Control: Christmas on 12/24 follows the mode, light cream (251,246,223)-(251,247,231) = Design light, dark burgundy (64,7,10)-(76,9,12) = Design dark. "
           "Merge (ebugs.md step 1, one defect per entry): TC-146's landscape New Year annual card (17,47,149) in light is the same card and the same art in another orientation, so it is folded in here rather than into ISS-XMA-45, whose defects (separators, monthly border) are landscape-only and affect both seasons. Class UI, RD: the Design states the light card and the app shows the dark one. S3: the whole selected plan card is the wrong scheme on the purchase page in light mode, readable, nothing blocked. "
           "O-1: the app's Appearance (☰ › Preferences) overrides the system dark mode; the run used 「Device Settings」. Visual finding: no log (overlay rule 3).",
      steps=["Set the phone date to 2026-12-30 in Settings (automatic date and time off)",
             "Set the phone to light mode in Settings",
             "Launch the APP",
             "Tap 「Mine」",
             "Tap 「Claim Holiday Deal」",
             "Look at the annual plan card"],
      res="In light mode the annual card has the dark-mode navy background, the same pixels as in dark mode.",
      res_zh="淺色模式下年方案卡片仍是深色模式的深藍背景，與深色模式完全相同。",
      exp="In light mode the annual card has the light background the Design draws (pale cream), as Christmas does.",
      exp_zh="淺色模式下年方案卡片應為設計稿的淺色（米白）背景，與聖誕節一致。",
      imgs=[("shot", "r5a-ny-iap-light", "xma44_light", [P_ANNUAL]),
            ("shot", "r5a-ny-iap-dark", "xma44_dark", [P_ANNUAL]),
            ("shot", "r5b-ny-iap-land-light", "xma44_land_light", [L_ANNUAL]),
            ("figny", None, "xma44_design", None)],
      links=[("Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year IAP & Credit board (IAP_year, light: cream annual card) -", NY_IAP_LIGHT)]),
 dict(iss="ISS-XMA-45", title="Landscape IAP page: link separators and monthly card border keep fixed colours, separators invisible in light mode",
      cls="UI", sev=3, owner="RD", cases=["TC-146"], extra="", rep=(2, 2), feat="Christmas & New Year Sale (Landscape IAP)",
      short="Separators invisible in light, border not themed",
      state="Related: Christmas (phone date 2026-12-24) and New Year (2026-12-30) sale windows, Stage server; build 2611251; Free account, signed in; auto-rotate off, landscape; app Appearance 「Device Settings」; closed 15.9.1 landscape IAP colour tickets: DRA252511-0121 / 0122 (selected monthly highlight), DRA252512-0005 (text colours)",
      related=None,
      basis="Basis: In-product — IAP page in portrait: light mode draws the 「|」 separators and the monthly card border grey (176,186,204), dark mode (89,97,110) / (54,59,67)",
      note="REQ-010 (user, 2026-11-26): 「TC-146 Landscape mode下的Light mode的UI，雖然Design spec沒有畫出來，但配色應該也要follow light mode設定」. The Design draws landscape in the dark scheme only (Christmas board 2750:27885, New Year 2844:22907), so the basis is the app's own portrait IAP page in each mode plus the user's ruling (Basis: In-product); Class UI, owner RD, not [UX] (rule 5). "
           "Measured (R5-a, both seasons identical): the 「|」 separators between Terms of Service / Privacy Policy / Restore Purchase are white (255,255,255) in light and in dark, so they vanish on the light background (249,251,255); portrait draws them (176,186,204) light / (89,97,110) dark. The monthly card border is (204,213,225) in both modes; portrait (176,186,204) light / (54,59,67) dark, so in light it is fainter than portrait and in dark it becomes a bright outline. Landscape follows the mode for the right-side background, monthly fill, prices, disclaimer and link text (same values as portrait). The New Year annual card in landscape is ISS-XMA-44 (same card as portrait). "
           "Closed same-OS tickets from last year's sale (15.9.1) fixed other landscape IAP colours: DRA252511-0121 / 0122 (the selected monthly plan's highlight, light / dark) and DRA252512-0005 (prices, discount and terms text colours; RD added landscape colours for the Christmas / New Year period); the separators and the unselected monthly border were not named, so this stays a new entry naming them as related (overlay rule 7, closed tickets). The two elements are merged: one screen, one cause (the landscape layout's fixed colours), the same Repro steps. S3: the links lose their separators in light mode and the border is wrong in both, nothing blocked. Visual finding: no log.",
      steps=["Set the phone date to 2026-12-24 in Settings (automatic date and time off)",
             "Set the phone to light mode in Settings",
             "Turn auto-rotate off",
             "Launch the APP",
             "Tap the sale pill at the top of the Launcher",
             "Turn the phone to landscape",
             "Look at the links and the monthly card"],
      res="In landscape the 「|」 separators are white in both modes (invisible in light) and the monthly border is a fixed grey.",
      res_zh="橫向時連結間的「|」分隔線在兩種模式都是白色（淺色下看不見），月方案外框顏色固定不變。",
      exp="Separators and monthly border follow light/dark mode with the colours portrait uses.",
      exp_zh="分隔線與月方案外框應跟隨淺色／深色模式，使用直向畫面的顏色。",
      imgs=[("shot", "r5b-xmas-iap-land-light", "xma45_xmas_land_light", [L_MONTHLY] + L_SEP),
            ("shot", "r5b-ny-iap-land-light", "xma45_ny_land_light", [L_MONTHLY] + L_SEP),
            ("shot", "r5b-xmas-iap-land-dark", "xma45_xmas_land_dark", [L_MONTHLY] + L_SEP),
            ("shot", "r5a-xmas-iap-light", "xma45_portrait_light", [P_MONTHLY] + P_SEP)],
      links=[("Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Christmas Landscape board (IAP, dark only) -", XMAS_LAND),
             ("Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Landscape board (IAP, dark only) -", NY_LAND)]),
 dict(iss="ISS-XMA-46", title="Mine / Pro page: the Credits bar under the Free / Pro card is 27 % taller than the Design",
      cls="UI", sev=3, owner="RD", cases=[], extra="O-5, O-8", rep=(4, 4), feat="Mine / Pro Page (Credits Bar)",
      short="Credits bar 27% taller than Design, card proportions off",
      state="Related: Free (balance 22) and Pro (122) on acda.test9, light and dark the same; build 2611251; Stage server",
      related=None,
      comparison=("Comparison: Credits bar, Figma vs app (1 Figma px = 2.904 px: card 343 px = 996 px)",
                  ["- Bar height: Figma 56 (= 162.6 px) / app 207 px (+27.3 %)",
                   "- Bar height / Free card height: Figma 56/232 = 0.241 / app 207/778 = 0.266",
                   "- Bar height / Pro card height: Figma 56/180 = 0.311 / app 207/529 = 0.391",
                   "- Bar height / card width: Figma 0.163 / app 0.208",
                   "- Space above and below the icon row: Figma 16 (= 46.5 px) / app 77 px",
                   "- Credits icon: Figma 24 (= 69.7 px) / app 53 px (-24 %)"]),
      note="REQ-010 (user, 2026-11-26): 「Mine / Pro頁裡 Free/Pro卡片下方Credits橫條的高度比例看起來與Design Figma上面比例不符，這個請你額外測量比例後去列隻Mine / Pro 頁的bug」. No casebook row covers the bar's height (O-5, O-8), so the Report step names the observations. "
           "Figma (figma-design get_metadata, specs/2026-11-20/extracted/figma-mine-credit-bar.json): mine_free 2682:13540 card 343×232, credit bar 343×56 (y 176 in the card); mine_vip 2718:4363 card 343×180, bar 343×56 (y 124); bar content icon+「Credits」 y 16 h 24, value+chevron y 18 h 20. App (page source, mine-credit-bar.json): Free card 996×778, Pro card 996×529, credit_remain_area 996×207 in both, light and dark identical (Free/Pro light and dark = 4 of 4). Content is vertically centred within 1 px; the extra height is padding (icon row 77 px above and below vs 46.5; value row 68 vs 52.3) while the content itself is smaller (icon 53 vs 69.7 px). Free card 778 vs 673.7 (+15.5 %) mostly from the bar; Pro card 529 vs 522.7 (+1.2 %), so the Pro card's top part is shorter and the bar takes 39 % of the card instead of 31 %. "
           "The Design draws Mine in dark only and calls the paid card 「VIP」; the app's tab reads 「Mine」 for Free and 「Pro」 for Pro (O-7), so the feature is named 「Mine / Pro Page」 as the user did. Class UI, RD: the Design states the size. S3 like the other layout tickets of this batch (reviewer may lower to S4: proportion only, nothing hidden or blocked). Comparison block in the Note as ISS-XMA-31 (DRA262611P0304 convention). Visual finding: no log.",
      steps=["Launch the APP",
             "Tap 「Mine」 (「Pro」 for a Pro account)",
             "Look at the Credits bar under the Free / Pro card"],
      res="The Credits bar is 207 px tall against 163 px from the Design (+27 %), so it takes too much of the card.",
      res_zh="Credits 橫條高 207 px，設計稿換算為 163 px（高 27%），占卡片比例過大。",
      exp="The bar keeps the Design's height (56 of the card's 343 width, 163 px here): 0.241 of the Free card, 0.311 of Pro.",
      exp_zh="Credits 橫條應為設計稿高度（此機 163 px），約占 Free 卡 0.241、Pro 卡 0.311。",
      imgs=[("mine", "free", "xma46_free_vs_figma", None),
            ("mine", "pro", "xma46_pro_vs_figma", None),
            ("shot", "r5c-mine-free-light", "xma46_free_light", [FREE_BAR]),
            ("shot", "r5c-mine-pro-light", "xma46_pro_light", [PRO_BAR])],
      links=[("Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Launcher & dialog board (mine_free: card 343×232, Credits bar 56) -", MINE_FREE),
             ("Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Launcher & dialog board (mine_vip: card 343×180, Credits bar 56) -", MINE_VIP)]),
]

NOT_RAISED = [
 ("O-1", "The app's Appearance 「Light Mode」 overrides the system dark switch; the run used 「Device Settings」", "Intended setting; tooling note (folded into the ISS-XMA-44 QA note)."),
 ("O-2", "Start state: acda.test9 Free with 22 credits, phone date 2027-01-01", "Account state."),
 ("O-3", "Mine's top pill counts down in the New Year window (contradicts KF-004)", "Knowledge correction for KF-004, not a spec defect; parked for the knowledge wrap-up."),
 ("O-4", "IAP page opened from the Launcher pill is outside the page source; system Back reaches the Launcher", "Tooling limit; Back behaviour already covered by earlier tickets (R1)."),
 ("O-6", "New Year interstitial shown after the date change", "Expected (KF-003)."),
 ("O-7", "Pro test subscription bought; tab label reads 「Pro」", "Setup for request C."),
 ("TC-102 texts", "Plan-card texts Special Offer / 57% OFF / NT$1210/Year", "Ruled NAB by the user (DRA262611P0309 follows the Design); not re-raised."),
]
FOLDED = {"O-1": "1. ISS-XMA-44 (QA note)", "O-5": "3. ISS-XMA-46", "O-8": "3. ISS-XMA-46"}


def font(n):
    for p in ["/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, n)
    return ImageFont.load_default()


def boxed(im, boxes):
    im = im.convert("RGB")
    d = ImageDraw.Draw(im)
    w = max(5, im.size[0] // 200)
    for b in boxes:
        d.rectangle(b, outline=(255, 0, 0), width=w)
    return im


def save(im, dst):
    im.thumbnail((1400, 1400))
    im.save(dst, "JPEG", quality=85)


def labelled(panels, gap=40):
    """Side-by-side panels [(image, caption)] on a white sheet with captions above."""
    f = font(34)
    h = max(p.size[1] for p, _ in panels) + 70
    w = sum(p.size[0] for p, _ in panels) + gap * (len(panels) + 1)
    sheet = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(sheet)
    x = gap
    for p, cap in panels:
        d.text((x, 14), cap, fill=(0, 0, 0), font=f)
        sheet.paste(p, (x, 60))
        x += p.size[0] + gap
    return sheet


def fig_ny():
    """Design New Year IAP_year dark and light frames, red box on the light annual card."""
    im = Image.open(f"{FIG}/ds-ny-iap-credit.png").convert("RGB")
    dark = im.crop((NY_DARK_FRAME[0], NY_DARK_FRAME[1], NY_DARK_FRAME[0] + 375, NY_DARK_FRAME[1] + 812))
    light = im.crop((NY_LIGHT_FRAME[0], NY_LIGHT_FRAME[1], NY_LIGHT_FRAME[0] + 375, NY_LIGHT_FRAME[1] + 812))
    s = 2
    dark, light = dark.resize((750, 1624)), light.resize((750, 1624))
    light = boxed(light, [(18 * s, 432 * s, 357 * s, 522 * s)])
    return labelled([(light, "Design light (2855:39936)"), (dark, "Design dark (2855:39855)")])


def fig_mine(tier):
    """Figma card (scaled 2.904 to the app's 996 px) beside the app card, red box on each Credits bar."""
    k = 996 / 343
    if tier == "free":
        fx, fy = MINE_FREE_FRAME
        card, bar_y, node = (16, 104, 343, 232), 176, "mine_free 2682:13540"
        app, acard, abar = "r5c-mine-free-light", (42, 288, 1038, 1066), FREE_BAR
    else:
        fx, fy = MINE_VIP_FRAME
        card, bar_y, node = (16, 96, 343, 180), 124, "mine_vip 2718:4363"
        app, acard, abar = "r5c-mine-pro-light", (42, 246, 1038, 775), PRO_BAR
    im = Image.open(f"{FIG}/ds-xmas-launcher-dialog.png").convert("RGB")
    fc = im.crop((fx + card[0], fy + card[1], fx + card[0] + card[2], fy + card[1] + card[3]))
    fc = fc.resize((996, round(card[3] * k)))
    fc = boxed(fc, [(0, round(bar_y * k), 995, fc.size[1] - 1)])
    ac = Image.open(f"{RUN}/screenshots/{app}.png").convert("RGB").crop(acard)
    ac = boxed(ac, [(0, abar[1] - acard[1], 995, ac.size[1] - 1)])
    return labelled([(fc, f"Figma {node}: bar 56 of {card[3]} (x2.904 = 163 px)"),
                     (ac, f"App {tier.capitalize()} (light): bar 207 of {acard[3] - acard[1]} px")])


def main():
    rows = list(csv.DictReader(open(f"{RUN}/results.csv", encoding="utf-8-sig")))
    fails = [r["ID"] for r in rows if r["Result"] == "Fail"]
    obs = sorted(set(re.findall(r"^- \*\*(O-\d+)", open(f"{RUN}/observations.md", encoding="utf-8").read(), re.M)), key=lambda s: int(s[2:]))
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
    w(f"# Christmas & New Year Sales (Android) — eBug drafts, round R5 (light mode and the Mine / Pro Credits bar), PDR-A {V} build {B}")
    w("")
    w(f"**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-26-r5-light-mine/` — round R5 (2026-11-26 17:20–17:45, REQ-010: A. New Year IAP annual card in light mode, TC-102; B. landscape IAP in light mode, TC-146; C. Mine / Pro Credits bar proportion, O-5 / O-8), on {DEVICE[8:]} through Appium / UiAutomator2, build 16.9.0.{B}, Stage server, acda.test9 (Free 22 credits, then Pro 122 by the test subscription), light/dark by the system switch with the app's Appearance on 「Device Settings」. R5 tally: 0 Pass, 2 Fail (TC-102, TC-146), 0 Blocked; 8 observations.")
    w("")
    w("**Status:** nothing filed, uploaded or commented. Seventh batch of this feature (R1, R1r, R2, R3, R4, R4-b filed: P0254–P0275, P0299–P0313, P0327–P0329). Dedupe: per OS, read-only (`dedupe.txt`). Plan-card texts are NAB by the user's ruling on DRA262611P0309 and are not re-raised.")
    w("")
    w("Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` owner RD for defects, no `[UX]`. Severity is proposed. Visual findings: no logs.")
    w("")
    w(f"**What is drafted:** {len(E)} entries (ISS-XMA-44 – ISS-XMA-46): 3 RD UI.")
    w("")
    w("Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.")
    w("")
    for n, e in enumerate(E, 1):
        folder = f"{n:02d}_{e['iss']}"
        os.makedirs(f"{img_root}/{folder}")
        names = []
        for kind, src, slug, boxes in e["imgs"]:
            name = f"{V}_{slug}.jpg"
            dst = f"{img_root}/{folder}/{name}"
            if kind == "shot":
                p = f"{RUN}/screenshots/{src}.png"
                if not os.path.exists(p):
                    sys.exit(f"missing {p}")
                save(boxed(Image.open(p), boxes), dst)
            elif kind == "figny":
                save(fig_ny(), dst)
            else:
                save(fig_mine(src), dst)
            names.append(name)
        tagtype = "" if e["cls"] == "Functional" else f"[{e['cls']}]"
        short = f"PDR-A {V} - [{TAG}]{tagtype} {e['feat']}: {e['short']}"
        if len(short) > 125:
            sys.exit(f"{e['iss']} short description {len(short)} > 125")
        for s in e["steps"]:
            if ">" in s or "›" in s:
                sys.exit(f"{e['iss']} step has a chain: {s}")
        rs = ", ".join(e["cases"] + ([e["extra"]] if e["extra"] else []))
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
        w(""); w("Result:"); w(e["res"]); w(f"摘要：{e['res_zh']}"); w(" ".join("{" + x + "}" for x in names))
        w(""); w("Expect Result:"); w(e["exp"]); w(f"摘要：{e['exp_zh']}")
        w(""); w("Note:"); w(DEVICE); w(e["state"])
        if e.get("related"):
            w(e["related"])
        if e.get("comparison"):
            w(e["comparison"][0]); [w(r) for r in e["comparison"][1]]
        for label, url in e["links"]:
            w(label); w(url)
        if e.get("basis"):
            w(e["basis"])
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
    w(f"{len(fails)} Fail in R5 (TC-102, TC-146), 0 Blocked, {len(obs)} observations ({obs[0]} … {obs[-1]}). TC-102 and TC-146's landscape New Year card are one defect (ISS-XMA-44); TC-146's separators and monthly border are a second (ISS-XMA-45); request C (O-5, O-8) is ISS-XMA-46. 2 Fail rows + 1 request → 3 entries.")
    w("")
    w("### Row-by-row map")
    w("")
    w("| Item | Result | Disposition | Became |")
    w("|---|---|---|---|")
    disp = {r["ID"]: (r["Result"], r["Disposition"]) for r in rows}
    MAP["TC-146"] = "1. ISS-XMA-44 (New Year annual card); 2. ISS-XMA-45 (separators, monthly border)"
    for k in fails:
        w(f"| {k} | {disp[k][0]} | {disp[k][1] or '—'} | {MAP[k]} |")
    for k in obs:
        w(f"| {k} | observation | — | {MAP[k]} |")
    w("")
    w("### Owner split")
    w("")
    w("| Owner | Entries |")
    w("|---|---|")
    w("| RD | 1, 2, 3 |")
    w("")
    w("### Filing order")
    w("")
    w("**1**, **2**, **3**. Nothing is filed until the review page's decisions come back.")
    w("")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(L))
    print(f"wrote {len(E)} entries → {OUT}/{NAME}.md")


if __name__ == "__main__":
    main()
