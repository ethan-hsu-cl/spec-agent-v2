#!/usr/bin/env python3
"""Build the Christmas & New Year Sales Android eBug draft batch for round R2 (the New Year rows, phone date in the
New Year window, 16.9.0 2611231 installed with adb, draft 20261120-165128).

Writes library/pdr/christmas-new-year-sale/android/ebugs/2026-11-25-r2/20261125_eBug_drafts_NewYear-Sale-R2_16.9.0.md,
the sibling _images/ folder (one NN_ISS-ID folder per entry: red-boxed JPEGs and log excerpts named 16.9.0_<slug>.*),
dedupe.txt and review.json. Entries continue the filed R1 / R1r numbering (ISS-XMA-24 on). The Christmas tickets
DRA262611P0254–P0275 name the Christmas sale and its screens only, so a bug that repeats on the New Year screens is a
new entry naming the related ticket (brief, 2026-11-25). Every Fail row, every defect Blocked row and every
observation of the run is mapped; the script stops when one is missing. Nothing is filed.

Usage: python3 library/pdr/christmas-new-year-sale/android/ebugs/2026-11-25-r2/generators/ebugs.py
"""
import csv, glob, json, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(OUT, *[".."] * 6))
ROOT = f"{REPO}/library/pdr/christmas-new-year-sale/android"
RUN = f"{ROOT}/runs/2026-11-25-r2-newyear"
LOG = {s: glob.glob(f"{RUN}/logs/{s}-*/logcat-live.txt")[0] for s in ("R2-a", "R2-b", "R2-c", "R2-d")}
NAME = "20261125_eBug_drafts_NewYear-Sale-R2_16.9.0"
V, B = "16.9.0", "2611231"
TAG = "AIAgent"
DEVICE = "Device: Samsung Galaxy A51 SM-A516B / Android 13"
ECL = "https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/"

DS = "https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id="
PM = "https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id="
SHEET = "https://docs.google.com/spreadsheets/d/1_rJf-7ljc0c_HO0P4isuyn-AOt6mIlbXsmyRW9xcGSk/edit?gid=1226976055"


def ds(board, node, what):
    return (f"Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), {board} board {what} -", DS + node)


def pm(board, what, node="3271-4161"):
    return (f"Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), {board} board {what} -", PM + node)


def sheet(what):
    return (f"Spec Link: 多國文案 sheet (linked from the PM rules board), block 「New Year Special」 {what} -", SHEET)


NY_INT, NY_IAP, NY_LAUNCH, XM_IAP = "2844-5895", "2844-5521", "2844-23135", "2750-19947"


def state(acct, store="Taiwan"):
    return f"Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build {B} installed with adb; {acct}; Play store {store}"


FREE, PRO = "Free account, signed in", "Pro account (New Year annual plan), signed in, no Credit Auto Pass"

# full-resolution boxes (1080 x 2400 portrait)
INT_TITLE = (250, 250, 830, 520)
INT_SAVE = (200, 690, 875, 1140)
INT_VS = (260, 1205, 820, 1305)
INT_YEAR = (700, 1340, 900, 1460)
INT_CTA = (40, 1665, 1040, 1800)
INT_MORE = (340, 2040, 740, 2105)
INT_TERMS = (40, 1845, 1040, 2035)
INT_LINKS = (10, 2170, 1070, 2250)
IAP_FEAT = (5, 980, 1075, 1260)
IAP_TAG = (750, 1285, 1035, 1365)
IAP_PCT = (860, 1360, 1020, 1480)
IAP_YEAR = (45, 1310, 1035, 1515)
IAP_MONTH = (45, 1545, 1035, 1695)
IAP_CTA = (110, 1840, 970, 2000)
L_TITLE = (25, 775, 1055, 865)
MINE_PILL = (35, 115, 505, 200)
CR_BANNER = (4, 4, 1076, 398)
CR_TOP = (60, 550, 1020, 765)
CR_CLOCK = (400, 1630, 680, 1700)
CR_LINE = (290, 1705, 790, 1760)
CR_CTA = (60, 1775, 1020, 1910)
CR_EACH = (170, 1930, 910, 1985)
VIP = (40, 245, 1040, 775)

L1 = "Launch the APP"


def date(d):
    return [f"Set the phone date to {d} in Settings (automatic date and time off)"]


def lang(name, d="2026-12-29"):
    return date(d) + [f"Set the app language of PowerDirector to {name}", L1]


def rel(code, what):
    return f"Related: {code} ({what}, filed for the Christmas sale)"


E = [
 dict(iss="ISS-XMA-24", title="New Year interstitial (US store): 「SAVE 52%」 and 「vs. paying $7.99/mo × 12」 come from the regular monthly plan, not the campaign $6.99",
      cls="Functional", sev=2, owner="RD", cases=["TC-020"], extra="O-2", rep=(1, 1), feat="New Year Sale (Interstitial)",
      short="US store: SAVE 52% from the regular $7.99 monthly, not $6.99 (45%)",
      state=state(FREE, "United States (Play Billing Lab)"), related=rel("DRA262611P0254", "same calculation on the Christmas interstitial"),
      note="R-006 / R-018 / R-036, ruling Q-3 (REQ-002): the % and 「vs. paying …/mo」 come from the campaign SKUs' store prices (annualsubscription_newyear_2611 $45.99, monthlysubscription_newyear_2611 $6.99 → 45%). Logcat 2027-01-01 12:00:28: the interstitial asked Play for monthly_sub_usd6.99_202209 ($7.99, regular) and the New Year annual. The IAP page reads $6.99 and 45% (O-2). Same as P0254 on the Christmas interstitial; P0254's steps and title name the Christmas sale only.",
      steps=date("2027-01-01") + ["Set the Play country to United States in Play Billing Lab", "Force-stop the APP", L1, "Look at the 「SAVE」 line and the 「vs. paying」 line"],
      res="The interstitial reads 「SAVE 52%」 「vs. paying $7.99/mo × 12」; the IAP page shows $6.99 and 45%.",
      res_zh="新年插頁以一般月訂 $7.99 算出 52%，IAP 頁為 $6.99、45%。",
      exp="The interstitial uses the New Year monthly $6.99: 「SAVE 45%」 「vs. paying $6.99/mo × 12」.",
      exp_zh="插頁應以新年活動月訂 $6.99 計算：SAVE 45%。",
      imgs=[("TC-020-01", "xma24_interstitial_us", [INT_SAVE, INT_VS])],
      log=("xma24_log", "R2-a", [r"2027-01-01 12:00:28"], r"getProductDetails: (monthly\S*|annualsubscription_newyear_2611) price:"),
      links=[pm("pm-ny-rules", "(➊ monthly plan SKU monthlysubscription_newyear_2611, SKU 表 US $6.99; ➍ 年價格 vs 月價格*12個月的價差%)"), ds("New Year Interstitial", NY_INT, "(「SAVE」 「<xx>」 「%」, 「vs. paying <monthly price>/mo × 12」)")]),

 dict(iss="ISS-XMA-25", title="New Year interstitial: trial terms read 「until cancelled」, the spec 「until canceled」",
      cls="UI", sev=4, owner="RD", cases=["TC-021"], rep=(1, 1), feat="New Year Sale (Interstitial)",
      short="Trial terms read 「until cancelled」, not 「until canceled」",
      state=state(FREE, "United States (Play Billing Lab)"), related=rel("DRA262611P0255", "same string on the Christmas interstitial"),
      note="R-020: 「…Subscription renews automatically until canceled. Cancel in Google Play…」. The annual price in the terms matches the big price ($45.99). The spec states the string and the app shows another: RD (text rule 2026-11-11). The interstitial is likely shared with Christmas (P0255); the ticket names the Christmas sale only.",
      steps=date("2027-01-01") + [L1, "Look at the trial terms under the yellow button"],
      res="The New Year trial terms use the British spelling with a double 「l」, not the spec's US spelling.",
      res_zh="新年插頁試用條款拼字為英式（雙 l）。",
      exp="The terms read 「…Subscription renews automatically until canceled. …」 as the spec states.",
      exp_zh="條款應為規格文字「until canceled」。",
      imgs=[("TC-020-01", "xma25_terms", [INT_TERMS])],
      links=[ds("New Year Interstitial", NY_INT, "(trial terms 「…renews automatically until canceled…」)")]),

 dict(iss="ISS-XMA-26", title="New Year interstitial: the first system Back does nothing; a second Back closes it",
      cls="Functional", sev=3, owner="RD", cases=["TC-023"], rep=(2, 3), feat="New Year Sale (Interstitial)",
      short="First system Back is ignored; a second Back closes it",
      state=state(FREE),
      related="Related: R1 on build 2611201 closed the Christmas interstitial with one Back (TC-016)",
      note="R-025, ruling Q-5 (REQ-002): system Back on the interstitial does what X does, one press, back to the Launcher. Seen 12/31 11:58 (Appium Back) and 1/2 12:01 (adb keyevent 4, ~10 s after the interstitial showed: dumpsys still topResumed PromotionInterstitialActivity; the second keyevent reached the Launcher). Once (1/1 12:00) a single Back left the app entirely. X closes it in one tap (TC-022 Pass). No log line for the ignored Back.",
      steps=date("2026-12-31") + [L1, "Wait until the New Year Special interstitial shows", "Press system Back once", "Look at the screen", "Press system Back again"],
      res="After the first Back the interstitial is still on screen; the second Back closes it to the Launcher.",
      res_zh="第一次按系統返回鍵插頁不關閉，第二次才回到首頁。",
      exp="One system Back closes the interstitial and shows the Launcher, as X does.",
      exp_zh="按一次系統返回鍵即應如 X 關閉插頁回到首頁。",
      imgs=[("TC-023-02", "xma26_after_first_back", []), ("TC-023-07", "xma26_after_second_back", [])],
      links=[pm("pm-ny-launch", "(New Year interstitial, X closes to the Launcher; Android system Back acts as X per ruling Q-5)")]),

 dict(iss="ISS-XMA-27", title="Launcher (New Year): the top banner title is 「Turn one photo to cinematic reel」, not 「Bring New Year moments to life」",
      cls="UI", sev=2, owner="RD", cases=["TC-003", "TC-085", "TC-086"], rep=(3, 3), feat="New Year Sale (Launcher)",
      short="Top banner title is not 「Bring New Year moments to life」",
      state=state(FREE), related=rel("DRA262611P0270", "Christmas banner title 「Make Christmas magic with AI」 missing"),
      note="R-027 (Design New Year Launcher & dialog, dark and light): the New Year banner title is 「Bring New Year moments to life」 ›. The New Year banner image shows (fireworks, woman with a sparkler) and reads well in dark and light, but the title (tv_banner_tagline) is the regular 「Turn one photo to cinematic reel」 ›. Seen at the 12/28 00:00 switch (TC-003), 12/29 light (TC-086) and dark (TC-085).",
      steps=date("2026-12-29") + [L1, "Tap X on the New Year Special interstitial", "Look at the top banner title"],
      res="The New Year banner shows the title 「Turn one photo to cinematic reel」 ›, in light and dark mode.",
      res_zh="新年橫幅標題顯示為一般文案「Turn one photo to cinematic reel」。",
      exp="The banner title reads 「Bring New Year moments to life」 ›.",
      exp_zh="橫幅標題應為「Bring New Year moments to life」。",
      imgs=[("TC-086-01", "xma27_light", [L_TITLE]), ("TC-085-01", "xma27_dark", [L_TITLE])],
      links=[ds("New Year Launcher & dialog", NY_LAUNCH, "(Launcher dark / light: 「Bring New Year moments to life」)")]),

 dict(iss="ISS-XMA-28", title="New Year interstitial: 「SAVE」 and 「vs. paying …/mo × 12」 stay English in all 26 other languages",
      cls="UI", sev=2, owner="RD", cases=[f"TC-0{i}" for i in range(57, 83)], extra="O-6", rep=(26, 26), feat="New Year Sale (Interstitial)",
      short="[MUI] 「SAVE」 and 「vs. paying …/mo × 12」 are not localized",
      state=state(FREE), related=rel("DRA262611P0264", "same lines on the Christmas interstitial"),
      note="R-022 (PM rules 底圖 & 價格 + 多國文案 sheet; ruling Q-16): the lines under the title art are localized by RD per the sheet. All 26 non-English languages (TC-057–TC-082), per-app locale, interstitial brought back by moving the phone date 12/29 ↔ 12/30. In Arabic and Persian the English line takes local digits (「× ١٢」, 「× ۱۲」).",
      steps=lang("中文（台灣）") + ["Look at the lines under the title art"],
      res="In all 26 non-English languages 「SAVE」 and 「vs. paying NT$240/mo × 12」 stay in English.",
      res_zh="新年插頁在 26 種非英文語系仍顯示英文「SAVE」與「vs. paying NT$240/mo × 12」。",
      exp="Both lines use the 多國文案 sheet's Save and vs. text for the app language (繁中「現省 xx%」).",
      exp_zh="兩行應依多國文案表翻譯成該語系。",
      imgs=[("TC-057-01", "xma28_cht", [INT_SAVE, INT_VS]), ("TC-069-01", "xma28_rus", [INT_SAVE, INT_VS]), ("TC-075-01", "xma28_ara", [INT_SAVE, INT_VS])],
      links=[pm("pm-ny-rules", "(底圖 & 價格: lines under the art localized by RD per the linked 多國文案 sheet)"), sheet("(Save and vs. rows)")]),

 dict(iss="ISS-XMA-29", title="New Year interstitial: 「/year」 and 「More subscription plan」 stay English in all 26 other languages; the sheet has no translation",
      cls="UI", sev=2, owner="PM", cases=[f"TC-0{i}" for i in range(57, 83)], extra="O-6", rep=(26, 26), feat="New Year Sale (Interstitial)",
      short="[MUI] 「/year」 and 「More subscription plan」 are not localized",
      state=state(FREE), related=rel("DRA262611P0265", "same strings on the Christmas interstitial"),
      note="The Design draws 「/year」 and 「More subscription plan」; the 多國文案 sheet has no row for either, so no translation exists in the spec: PM supplies it (text rule 2026-11-11), as P0265 for Christmas.",
      steps=lang("Русский") + ["Look at the annual price and the link under the trial terms"],
      res="「/year」 and 「More subscription plan」 are English in all 26 non-English languages.",
      res_zh="「/year」與「More subscription plan」在 26 種語系皆為英文，多國文案表無此兩列。",
      exp="PM supplies both strings for each app language; the interstitial shows them translated.",
      exp_zh="請 PM 提供兩字串各語系翻譯。",
      imgs=[("TC-069-01", "xma29_rus", [INT_YEAR, INT_MORE]), ("TC-064-01", "xma29_jpn", [INT_YEAR, INT_MORE])],
      links=[ds("New Year Interstitial", NY_INT, "(「/year」, 「More subscription plan」)"), sheet("(no row for 「/year」 or 「More subscription plan」)")]),

 dict(iss="ISS-XMA-30", title="New Year interstitial: title art English in French and Italian, Russian in Ukrainian; es-ES shows the Mexican Spanish title and CTA",
      cls="UI", sev=2, owner="RD", cases=["TC-059", "TC-063", "TC-082", "TC-066"], extra="O-6", rep=(4, 4), feat="New Year Sale (Interstitial)",
      short="[FRA/ITA/UKR/ESP] Title art not in the app language",
      state=state(FREE),
      related="Related: new on the New Year art; the Christmas art was French, Italian and Ukrainian in R1 (TC-032, TC-036, TC-055)",
      note="R-022 / multilang sheet (block 「New Year Special」): FRA 「Vente du Nouvel An」, ITA 「Capodanno Speciale」, UKR 「Новорічна пропозиція」, ESP title 「Especial Año Nuevo」 and CTA 「Prueba 7 días gratis」. The app shows the English art in fr-FR (TC-059) and it-IT (TC-063), the Russian art 「Новогодняя акция」 in uk-UA (TC-082), and in es-ES the ESP (MX) title 「Especial de Año Nuevo」 and CTA 「Prueba gratis por 7 días」 (TC-066; es-MX's own CTA 「Inicia tu prueba gratuita de 7 días」 is in ISS-XMA-31). Titles in the other 22 languages match the sheet.",
      steps=lang("Français") + ["Look at the title art"],
      res="FRA and ITA show the English title art, UKR the Russian art, es-ES the Mexican Spanish title and CTA.",
      res_zh="法文、義大利文顯示英文標題圖；烏克蘭文顯示俄文標題圖；西班牙文（西班牙）顯示墨西哥西文標題與按鈕。",
      exp="The title art is the sheet's title for the app language (FRA 「Vente du Nouvel An」, UKR 「Новорічна пропозиція」).",
      exp_zh="標題圖應為該語系多國文案（法、義、烏、西）。",
      imgs=[("TC-059-01", "xma30_fra", [INT_TITLE]), ("TC-063-01", "xma30_ita", [INT_TITLE]), ("TC-082-01", "xma30_ukr", [INT_TITLE]), ("TC-066-01", "xma30_esp", [INT_TITLE, INT_CTA])],
      links=[sheet("(title rows FRA, ITA, UKR, ESP; CTA row ESP)"), ds("New Year Interstitial", NY_INT, "(title art 「New Year Special」, 多國 title per language)")]),

 dict(iss="ISS-XMA-31", title="New Year interstitial: CTA wording differs from the 多國文案 sheet in 12 languages",
      cls="UI", sev=3, owner="RD", cases=["TC-057", "TC-058", "TC-059", "TC-063", "TC-064", "TC-065", "TC-066", "TC-069", "TC-071", "TC-072", "TC-075", "TC-078"], extra="O-6", rep=(12, 12), feat="New Year Sale (Interstitial)",
      short="[MUI] CTA text differs from the 多國文案 sheet in 12 languages",
      state=state(FREE), related=rel("DRA262611P0266", "same CTA strings on the Christmas interstitial"),
      note="Sheet CTA vs app: CHT 「７天免費試用」/「7 天免費試用」, CHS 「7天免费试用」/「7 天免费试用」, FRA 「Essai gratuit de 7 jours」/「Recevoir 7 jours d'essai gratuits」, ITA 「Prova Gratis per 7 Giorni」/「Prova Gratuita di 7gg.」, JPN 「7 日間無料で試す」/「７日間無料お試し」, KOR 「7일 무료 체험 시작하기」/「7일 무료 체험」, ESP (see ISS-XMA-30), ESP (MX) 「Prueba gratis por 7 días」/「Inicia tu prueba gratuita de 7 días」, RUS 「Попробовать 7 дней бесплатно」/「7-дн. беспл. пробное」, Viet 「Dùng thử miễn phí 7 ngày」/「Dùng Thử Miễn Phí 7 Ngày」, Arabic 「بدء تجربة مجانية لمدة 7 أيام」/「ابدأ تجربة مجانية لمدة 7 أيام」, Hebrew (TC-078). The same 12 as P0266.",
      steps=lang("Русский") + ["Look at the yellow button"],
      res="In 12 languages the CTA reads differently from the sheet (e.g. RUS 「7-дн. беспл. пробное」).",
      res_zh="12 種語系按鈕文字與多國文案表不同。",
      exp="The CTA shows the sheet's string for each language (RUS 「Попробовать 7 дней бесплатно」).",
      exp_zh="按鈕應為多國文案表文字。",
      imgs=[("TC-069-01", "xma31_rus", [INT_CTA]), ("TC-059-01", "xma31_fra", [INT_CTA]), ("TC-064-01", "xma31_jpn", [INT_CTA])],
      links=[sheet("(CTA row)")]),

 dict(iss="ISS-XMA-32", title="New Year interstitial: bottom links run into each other or the separators in RUS, FRA, UKR and Polish",
      cls="UI", sev=3, owner="RD", cases=["TC-069", "TC-059", "TC-082", "TC-076"], extra="O-6", rep=(4, 4), feat="New Year Sale (Interstitial)",
      short="[RUS/FRA/UKR/POL] Bottom links overlap each other or separators",
      state=state(FREE), related=rel("DRA262611P0267", "same bar on the Christmas interstitial"),
      note="Design bottom bar 「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」 with clear separators. RUS: the three links overlap (x 78–366, 344–738, 720–996) and cover both separators; FRA 「Politique de confidentialité」 (388–694) touches both separators (381, 698); UKR 「Політика конфіденційності」 (376–706) runs into both; Polish 「Warunki korzystania z usługi」 (63–385) runs into the left one.",
      steps=lang("Русский") + ["Look at the three links at the bottom"],
      res="In Russian the bottom links overlap; in French, Ukrainian and Polish a link runs into the separators.",
      res_zh="俄文底部連結互相重疊；法、烏、波蘭文連結壓到分隔線。",
      exp="The three links fit with space around each separator, as the Design draws.",
      exp_zh="三個連結應與分隔線保持間距。",
      imgs=[("TC-069-01", "xma32_rus", [INT_LINKS]), ("TC-059-01", "xma32_fra", [INT_LINKS]), ("TC-082-01", "xma32_ukr", [INT_LINKS]), ("TC-076-01", "xma32_pol", [INT_LINKS])],
      links=[ds("New Year Interstitial", NY_INT, "(「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」)")]),

 dict(iss="ISS-XMA-33", title="New Year interstitial (Polish): the CTA wraps to two lines that fill the button edge to edge",
      cls="UI", sev=3, owner="RD", cases=["TC-076"], rep=(1, 1), feat="New Year Sale (Interstitial)",
      short="[POL] CTA wraps to two lines with no side padding in the button",
      state=state(FREE), related=rel("DRA262611P0268", "same button on the Christmas interstitial"),
      note="Sheet CTA 「Rozpocznij 7-dniowy bezpłatny okres próbny」 matches; the text box spans the whole button (63–1017) in two lines. The Design draws a one-line CTA with side padding.",
      steps=lang("Polski") + ["Look at the yellow button"],
      res="The Polish CTA wraps to two lines and touches both sides of the button.",
      res_zh="波蘭文按鈕文字換成兩行且貼齊按鈕左右。",
      exp="The CTA fits with side padding (smaller text or one line), as the Design draws.",
      exp_zh="按鈕文字應保有左右留白。",
      imgs=[("TC-076-01", "xma33_pol_cta", [INT_CTA])],
      links=[ds("New Year Interstitial", NY_INT, "(CTA 「Get 7-Day Free Trial」, one line)")]),

 dict(iss="ISS-XMA-34", title="New Year interstitial and IAP show 57% where NT$1,210 vs NT$240 × 12 gives 57.99% (58%)",
      cls="Functional", sev=3, owner="RD", cases=["TC-102"], extra="O-6", rep=(27, 27), feat="New Year Sale (IAP)",
      short="Discount shows 57% though NT$1,210 vs NT$240 × 12 gives 57.99%",
      state=state(FREE), related=rel("DRA262611P0269", "same truncation on the Christmas pages"),
      note="R-036 (PM ➍ 年價格 vs 月價格*12個月的價差%, ruling Q-3): (NT$240 × 12 − NT$1,210) ÷ (NT$240 × 12) = 57.99% → 58 rounded; the app truncates to 57 on the New Year interstitial in all 27 languages (TC-056–TC-082) and on the IAP card 「57% OFF」 (TC-102). Store prices in logcat 2026-12-29 11:50:29.",
      steps=date("2026-12-29") + [L1, "Look at the big percentage", "Tap X", "Tap the Mine tab", "Tap 「Claim Holiday Deal」", "Look at the annual plan card"],
      res="Both pages show 57% for NT$1,210 / NT$240 (57.99%).",
      res_zh="兩頁皆顯示 57%（實際 57.99%）。",
      exp="The % is rounded from the store prices: 58%.",
      exp_zh="百分比應四捨五入為 58%。",
      imgs=[("TC-057-01", "xma34_interstitial_57", [INT_SAVE, INT_VS, INT_YEAR]), ("TC-097-01", "xma34_iap_57", [IAP_PCT])],
      log=("xma34_log", "R2-a", [r"2026-12-29 11:50:29"], r"getProductDetails: (monthly\S*|annualsubscription_newyear_2611) price:"),
      links=[pm("pm-ny-rules", "(➍ 年價格 vs 月價格*12個月的價差%)"), ds("New Year Interstitial", NY_INT, "(「SAVE」 「<xx>」 「%」)")]),

 dict(iss="ISS-XMA-35", title="Mine (Free, New Year): the top pill shows no countdown; the Launcher pill does",
      cls="UI", sev=3, owner="RD", cases=["TC-089"], extra="O-9", rep=(2, 2), feat="New Year Sale (Mine)",
      short="Mine top pill has no clock or countdown",
      state=state(FREE), related="Related: none on the Christmas sale (it has no countdown)",
      note="R-029, ruling Q-9 (REQ-003): in the New Year campaign the Launcher and Mine top pill show a clock icon and a countdown 「<d>D hh:mm:ss」 (Design 「2D 23:56:18」, PM 「6D 23:56:18」). At 2027-01-03 12:00 the Launcher pill counts 「2D 11:59:40」 to 1/6 00:00 (Q-18 assumption); Mine's pill reads only 「Try Pro 7 days for free」 with the gift icon (watched 12:00:43–12:00:50; also 12/29 12:34). The IAP CTA and the credit page count to the same target.",
      steps=date("2027-01-03") + [L1, "Tap X on the New Year Special interstitial", "Look at the pill at the top of the Launcher", "Tap the Mine tab", "Look at the pill at the top of Mine"],
      res="The Launcher pill shows 「2D 11:59:40」 counting down; Mine's pill shows only 「Try Pro 7 days for free」.",
      res_zh="首頁膠囊有倒數，Mine 頁膠囊無時鐘與倒數。",
      exp="Mine's top pill shows the clock icon and the same countdown as the Launcher.",
      exp_zh="Mine 頁膠囊應與首頁同樣顯示時鐘與倒數。",
      imgs=[("TC-089-01", "xma35_launcher_pill", [(150, 120, 560, 210)]), ("TC-089-03", "xma35_mine_pill", [MINE_PILL])],
      links=[ds("New Year Launcher & dialog", NY_LAUNCH, "(Launcher and Mine top pill with clock and 「2D 23:56:18」)"), pm("pm-ny-launch", "(Mine pill countdown 「6D 23:56:18」)")]),

 dict(iss="ISS-XMA-36", title="IAP (New Year): tag 「Special Offer」 and 「57% OFF」, not 「New Year Treat」 and 「Save 57%」; monthly not struck; CTA 「Continue」; other feature cards",
      cls="UI", sev=2, owner="RD", cases=["TC-102"], rep=(1, 1), feat="New Year Sale (IAP)",
      short="Tag 「Special Offer」 and 「57% OFF」 instead of 「New Year Treat」, 「Save xx%」",
      state=state(FREE), related=rel("DRA262611P0275", "same card on the Christmas IAP page"),
      note="R-035 / R-037 / R-040 (PM New Year 1104 Update; Design New Year IAP & Credit): annual card tag 「New Year Treat」 with a small decoration, 「Save <xx>%」 on its right half, no 「Offer」 on the page; monthly card with the original price struck; CTA 「Get 7-Day Free Trial」; feature cards 「Auto Edit」, 「4K Output」, 「Remove Watermark」. App: 「Special Offer」 (balloon/star), 「57% OFF」, 「NT$240/Month」 only, CTA 「Continue」 with the countdown under it, cards 「No Watermark」, 「100 Monthly Credits」, 「Video Enhance」, 「15K+ Music Tracks」, 「4K Output」. The New Year header art and countdown are right.",
      steps=date("2026-12-29") + [L1, "Tap X on the New Year Special interstitial", "Tap the Mine tab", "Tap 「Claim Holiday Deal」", "Look at the plan cards and the yellow button"],
      res="Tag 「Special Offer」, 「57% OFF」, monthly price not struck, CTA 「Continue」, other feature cards.",
      res_zh="年訂卡標籤為「Special Offer」「57% OFF」，月訂無劃線原價，按鈕為「Continue」，功能卡不同。",
      exp="Tag 「New Year Treat」, 「Save 57%」, struck monthly price, CTA 「Get 7-Day Free Trial」, the Design's cards.",
      exp_zh="應為 New Year Treat、Save xx%、月訂劃線原價與 Get 7-Day Free Trial 按鈕。",
      imgs=[("TC-097-01", "xma36_iap_card", [IAP_TAG, IAP_PCT, IAP_MONTH, IAP_CTA, IAP_FEAT])],
      links=[pm("pm-ny-launch", "(1104 Update, IAP: 「New Year Treat」, struck monthly price, no 「Offer」)"), ds("New Year IAP & Credit", NY_IAP, "(IAP_year plan cards, CTA, feature cards)")]),

 dict(iss="ISS-XMA-37", title="Mine (Pro, New Year): the VIP card has no New Year decoration",
      cls="UI", sev=2, owner="RD", cases=["TC-116"], extra="O-13", rep=(1, 1), feat="New Year Sale (Mine)",
      short="Pro VIP card lacks New Year decoration",
      state=state(PRO), related=rel("DRA262611P0258", "Pro VIP card lacks Christmas decoration"),
      note="R-043 (PM rules ➍ Paid: VIP Welcome Banner decorated; New Year decoration in the New Year campaign). On 2611231 the Pro Mine opens on the plain card (crown 「Pro」, 「You're on the highest plan…」, Credits) with no decoration; tapping it opens nothing (no separate VIP Benefits page). The only New Year touch is the tab icon. 「Your VIP Features」 and 「More VIP Benefits」 stayed empty (O-13).",
      steps=date("2026-12-30") + [L1, "Tap the 「Pro」 tab", "Look at the VIP card at the top", "Tap the VIP card"],
      res="The Pro VIP card is the plain card with no New Year decoration; tapping it opens nothing.",
      res_zh="Pro 的 VIP 卡片無新年裝飾，點擊無反應。",
      exp="The VIP welcome banner carries New Year decoration.",
      exp_zh="VIP 歡迎橫幅應有新年裝飾。",
      imgs=[("TC-116-02", "xma37_vip", [VIP])],
      links=[pm("pm-ny-rules", "(➍ Paid: VIP Welcome Banner with New Year decoration)")]),

 dict(iss="ISS-XMA-38", title="Credit page (Pro, New Year): the 2000-credit Special Offer pack is never offered; the Auto Pass card takes its place",
      cls="Functional", sev=2, owner="RD", cases=["TC-121", "TC-123"], rep=(1, 1), feat="New Year Sale (Credit)",
      short="Pro: New Year 2000-credit pack never offered; no 「Get 2000 credits for …」",
      state=state(PRO), related=rel("DRA262611P0261", "Christmas 2000-credit pack never offered"),
      note="R-046 / R-008: for a paid user the Special Offer pack 「1000+1000」 (white 1000, green +1000) with the CTA 「Get 2000 credits for <price>」 buys pdrm_2000_credit_paiduser_christmas (the New Year campaign uses the same SKU, PM New Year rules). On 12/30 (no Auto Pass) the special card is the Auto Pass card 「Annual Auto Pass Discount」 「1000 +1000」 「NT$2490」 (ISS-XMA-39); selecting the regular 2000 card gives 「Get 2000 Credits for NT$3350」, whose Play sheet is pdrm_2000_credits_paiduser (TC-123, cancelled). Logcat 2026-12-30 13:04:56 fetches pdrm_2000_credit_paiduser_christmas (NT$2,740.00) and never shows it.",
      steps=date("2026-12-30") + [L1, "Tap the 「Pro」 tab", "Tap 「Credit Special Offer」", "Look at the top card", "Tap the 2000 pack", "Tap 「Get 2000 Credits for NT$3350」"],
      res="No 2000-credit Special Offer pack; the 2000 card opens the regular SKU pdrm_2000_credits_paiduser.",
      res_zh="無新年 2000 點特惠包；2000 點卡開啟一般會員 SKU。",
      exp="The 「1000+1000」 pack with 「Get 2000 credits for <price>」 opens pdrm_2000_credit_paiduser_christmas.",
      exp_zh="應顯示 1000+1000 特惠包並開啟活動 SKU。",
      imgs=[("TC-121-01", "xma38_page", [CR_TOP]), ("TC-123-01", "xma38_regular_2000", [(720, 1090, 1020, 1340), CR_CTA]), ("TC-123-02", "xma38_play_regular", [])],
      log=("xma38_log", "R2-d", [r"2026-12-30 13:04:56"], r"getProductDetails: pdrm_2000_credit\S* price:"),
      links=[pm("pm-ny-rules", "(➎ Credit IAP: paid Special Offer pack 1000+1000, SKU pdrm_2000_credit_paiduser_christmas)"), ds("New Year IAP & Credit", NY_IAP, "(credit purchase page: Special Offer 1000+1000, 「Get 2000 credits for $166.99」)")]),

 dict(iss="ISS-XMA-39", title="Credit page (Pro, no Auto Pass, New Year): no 「Subscribe for 3000 free credits!」; 「Continue with the best deal」 and 「Cancel anytime.」 instead",
      cls="UI", sev=3, owner="RD", cases=["TC-121"], rep=(1, 1), feat="New Year Sale (Credit)",
      short="No Auto Pass: CTA not 「Subscribe for 3000 free credits!」",
      state=state(PRO), related=rel("DRA262611P0260", "same CTA on the Christmas credit page"),
      note="R-048 / R-052, ruling Q-14: without Credit Auto Pass the page leads with the Auto Pass sale under 「Subscribe for 3000 free credits!」 and 「Each credit for about <price>」. App: 「Annual top-up automatically!」, CTA 「Continue with the best deal」, 「Each credit for about NT$1.24. Cancel anytime.」. The footer 「Terms of Service | Privacy Policy」 and 「unused credits」 vs the Design's 「Privacy Policy | Terms of Use」 and 「consumed credits」 were held by the reviewer as ISS-XMA-20 (not filed) and are not raised again. The 「New Year Special」 banner and the countdown are right.",
      steps=date("2026-12-30") + [L1, "Tap the 「Pro」 tab", "Tap 「Credit Special Offer」", "Look at the lines above and under the CTA"],
      res="CTA 「Continue with the best deal」 and 「Each credit for about NT$1.24. Cancel anytime.」",
      res_zh="自動續購按鈕文字與規格不同。",
      exp="「Subscribe for 3000 free credits!」 and 「Each credit for about <price>」, as the Design draws.",
      exp_zh="應為 Subscribe for 3000 free credits! 與 Each credit for about。",
      imgs=[("TC-121-01", "xma39_autopass_cta", [CR_LINE, CR_CTA, CR_EACH])],
      links=[ds("New Year IAP & Credit", NY_IAP, "(credit purchase page: 「Subscribe for 3000 free credits!」, 「Each credit for about $0.1」)"), pm("pm-ny-credit", "(no-subscription Credit Auto Pass version of the credit purchase page)")]),

 dict(iss="ISS-XMA-40", title="Credit page (Christmas window): a countdown shows above the CTAs; only the New Year page should have one",
      cls="UI", sev=3, owner="RD", cases=["TC-129"], rep=(1, 1), feat="Christmas Sale (Credit)",
      short="Countdown 「2D 23:56:30」 shows above the CTAs on 12/25",
      state="Related: Christmas sale window (Stage server, phone date 2026-12-25 00:03); build 2611231 installed with adb; " + PRO + "; Play store Taiwan",
      related="Related: R1r (build 2611201, RD test date) saw no countdown on the Christmas credit page; no ticket",
      note="R-049, ruling Q-11 (REQ-003): only the New Year credit page shows the countdown; the Christmas credit page has none (the Design draws 「2D 23:56:18」 there, overruled). At 2026-12-25 00:03:29 the page (「Christmas Special」 banner) shows the clock and 「2D 23:56:30」, counting to 12/28 00:00. The New Year countdown itself is right (TC-121).",
      steps=date("2026-12-25 00:03") + [L1, "Tap the 「Pro」 tab", "Tap 「Credit Special Offer」", "Look above the CTA"],
      res="The Christmas credit page shows a clock icon and 「2D 23:56:30」 above the CTAs.",
      res_zh="聖誕節點數購買頁 CTA 上方出現倒數。",
      exp="No clock icon and no countdown on the Christmas credit page (ruling Q-11).",
      exp_zh="聖誕節點數頁不應有時鐘與倒數。",
      imgs=[("TC-129-02", "xma40_xmas_countdown", [CR_CLOCK])],
      links=[ds("IAP & Credit", XM_IAP, "(Christmas credit purchase page; its 「2D 23:56:18」 countdown removed by ruling Q-11)"), pm("pm-ny-rules", "(➎ New Year credit page countdown, New Year only)")]),
]

NOT_RAISED = [
 ("O-1", "Toast 「PiP video was enabled before.」 at some launches after a date change", "No spec; app debug toast after clock changes; report only."),
 ("O-3", "IAP CTA and Launcher pill countdowns run to the end of 1/5", "Pass in TC-089 / TC-152."),
 ("O-4", "Interstitial again on 12/29 after the clock went back", "Artifact of moving the clock backwards."),
 ("O-5", "Settings date tooling; Samsung update screen; log-slice windows empty", "Tooling note."),
 ("O-7", "Samsung 「Software update」 screen after each date move", "Phone, not the app."),
 ("O-8", "New Year Mine icon selected state outline vs Design filled disc", "TC-092 passed; left for the design check."),
 ("O-10", "Time picker tooling, dark mode, Play Billing Lab expiry display", "Tooling note."),
 ("O-11", "Pro test purchase worked on the adb build 2611231 (no 「Unofficial Version」)", "Account / build state; knowledge."),
 ("O-12", "Christmas credit page banner is 「Christmas Special」 on 2611231 (P0259 looked fixed)", "Not a recheck of P0259; no comment on tickets."),
 ("O-14", "Google Play's own 「Here’s a related item」 upsell after cancelling", "Google's sheet."),
 ("O-15", "Samsung update screen interrupted the time picker", "Tooling note."),
 ("TC-121 footer", "「Terms of Service | Privacy Policy」, 「unused credits」", "Same as ISS-XMA-20, held by the reviewer in R1r; not raised again."),
]
FOLDED = {"O-2": "1. ISS-XMA-24", "O-6": "5–10. ISS-XMA-28…33", "O-9": "12. ISS-XMA-35", "O-13": "14. ISS-XMA-37"}
OBS_ALL = [f"O-{i}" for i in range(1, 16)]
ROW_EXTRA = {f"TC-0{i}": "11. ISS-XMA-34 (57 vs 58)" for i in range(56, 83)}

DUPS_TXT = [
 "Read-only check against the filed Android tickets of this feature: DRA262611P0254–P0263 (R1r) and P0264–P0275 (R1), all titled 「Christmas Sale (…)」 with Christmas-window steps. None covers the New Year screens, so the New Year repeats are new entries naming the related ticket (brief 2026-11-25).",
 "Android pool search (ecl_query.py dedupe): see the lines below when run; no comment, upload or filing.",
]


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
            key = re.sub(r"^\S+ \S+ +\d+ +\d+ ", "", line.strip())
            if key in seen:
                continue
            seen.add(key)
            out.append(line.rstrip()[:240])
            if len(out) >= cap:
                break
    return out


def main():
    rows = list(csv.DictReader(open(f"{RUN}/results.csv", encoding="utf-8-sig")))
    tally = {}
    for r in rows:
        tally[r["Result"]] = tally.get(r["Result"], 0) + 1
    fails = [r["ID"] for r in rows if r["Result"] == "Fail"]
    dblk = [r["ID"] for r in rows if r["Result"] == "Blocked" and r["Disposition"] == "defect"]
    disp = {r["ID"]: (r["Result"], r["Disposition"]) for r in rows}
    obs_file = open(f"{RUN}/observations.md", encoding="utf-8").read()
    obs = [o for o in OBS_ALL if re.search(rf"^- \*\*{o} ", obs_file, re.M)]
    if len(obs) != 15:
        sys.exit(f"observations: {obs}")
    MAP = {}
    for n, e in enumerate(E, 1):
        for c in e["cases"]:
            MAP.setdefault(c, []).append(f"{n}. {e['iss']}")
    for k, v in ROW_EXTRA.items():
        if disp.get(k, ("",))[0] == "Fail":
            MAP.setdefault(k, []).append(v)
    for k, _, _ in NOT_RAISED:
        if k.startswith("O-"):
            MAP.setdefault(k, []).append("not raised")
    for k, v in FOLDED.items():
        MAP.setdefault(k, []).append(f"folded into {v}")
    MAP = {k: "; ".join(dict.fromkeys(v)) for k, v in MAP.items()}
    need = fails + dblk + obs
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
    w(f"# Christmas & New Year Sales (Android) — eBug drafts, round R2 (New Year rows, phone date in the New Year window), PDR-A {V} build {B}")
    w("")
    w(f"**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-25-r2-newyear/` — round R2 of draft `drafts/20261120-165128` (table v2; the 57 New Year rows plus TC-129 and TC-151, REQ-006), 2026-11-25 11:49 → 13:09, on {DEVICE[8:]} (adb R5CN8194YSN) through Appium / UiAutomator2, build 16.9.0.{B} installed with adb by the user, Stage server, the campaign driven by the phone's system date (user, REQ-006), acda.test9 signed in (Free; Pro from R2-d after buying the New Year annual test subscription), Play store Taiwan (US through Play Billing Lab for TC-020/021/003/103). Tally: " + ", ".join(f"{v} {k}" for k, v in tally.items()) + ".")
    w("")
    w("**Status:** nothing filed, uploaded or commented. Third batch of this feature; R1 (P0264–P0275) and R1r (P0254–P0263) are filed, all titled for the Christmas sale. The New Year repeats of those bugs are new entries whose Note names the related Christmas ticket; new bugs have none. Dedupe: per OS, read-only (`dedupe.txt`).")
    w("")
    w("Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` / `[AIAgent][UI]` owner RD for defects; text the spec must supply to PM (BugBelong PM), 2026-11-11. Severity is proposed.")
    w("")
    owners = ", ".join(f"{sum(1 for e in E if e['owner'] == o and e['cls'] == c)} {o} {c}" for o, c in (("RD", "Functional"), ("RD", "UI"), ("PM", "UI")) if any(e['owner'] == o and e['cls'] == c for e in E))
    w(f"**What is drafted:** {len(E)} entries (ISS-XMA-24…{23 + len(E)}): {owners}.")
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
    blocked = [r for r in rows if r["Result"] == "Blocked"]
    tdata = [r["ID"] for r in blocked if r["Disposition"] != "defect"]
    w(f"| Blocked test-data ({len(tdata)}) | {', '.join(tdata)} | No verdict: a balance below the Image to Video (Custom) price is needed (acda.test9 holds 3720–3755 credits); reasons in report.md and blocked-reasons.json. |")
    w("")
    w("## Reconciliation against the run")
    w("")
    w(f"{len(fails)} Fail (all defect), {len(blocked)} Blocked ({len(dblk)} defect, {len(tdata)} test-data), {len(obs)} observations (O-1 … O-15).")
    w("")
    w("### Row-by-row map")
    w("")
    w("| Item | Result | Disposition | Became |")
    w("|---|---|---|---|")
    for k in fails + dblk:
        w(f"| {k} | {disp[k][0]} | {disp[k][1] or '—'} | {MAP[k]} |")
    for k in obs:
        w(f"| {k} | observation | — | {MAP[k]} |")
    w("")
    w("### Related Christmas tickets")
    w("")
    w("| Entry | Related ticket |")
    w("|---|---|")
    for n, e in enumerate(E, 1):
        m = re.search(r"DRA\d+P\d+", e.get("related", ""))
        w(f"| {n}. {e['iss']} | " + (f"[{m.group(0)}]({ECL}{m.group(0)})" if m else "— (new)") + " |")
    w("")
    w("### Owner split")
    w("")
    w("| Owner | Entries |")
    w("|---|---|")
    for o in ("RD", "PM"):
        w(f"| {o} | " + ", ".join(str(i) for i, e in enumerate(E, 1) if e["owner"] == o) + " |")
    w("")
    w("### Filing order")
    w("")
    w("By severity: " + ", ".join(f"**{i}**" for s in (1, 2, 3, 4) for i, e in enumerate(E, 1) if e["sev"] == s) + ". Nothing is filed until the review page's decisions come back.")
    w("")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(L))
    if not os.path.exists(f"{OUT}/dedupe.txt"):
        D = ["# Dedupe — Christmas & New Year Sales Android R2 (16.9.0.2611231), read-only, PowerDirector Mobile for Android only", ""] + DUPS_TXT
        open(f"{OUT}/dedupe.txt", "w", encoding="utf-8").write("\n".join(D) + "\n")
    review = {"lede": "Third batch of this feature, from R2: the New Year rows with the phone's date inside the New Year window (REQ-006), build 2611231 installed with adb, Stage. Most entries are the filed Christmas bugs (P0254–P0275) repeating on the New Year screens: those tickets name the Christmas sale only, so each is a new entry naming its related ticket. New: ISS-XMA-26 (Back needs two presses), ISS-XMA-30 (title art language), ISS-XMA-35 (Mine pill countdown), ISS-XMA-40 (countdown on the Christmas credit page).",
              "why": {"ISS-XMA-26": "New on 2611231: R1 on 2611201 closed with one Back.",
                      "ISS-XMA-30": "New Year art only: the Christmas art was translated.",
                      "ISS-XMA-34": "57 vs 58 in all 27 languages; the rows failed on other items too.",
                      "ISS-XMA-39": "The footer and 「unused credits」 stay with held ISS-XMA-20.",
                      "ISS-XMA-40": "Ruling Q-11: countdown on New Year only."}}
    json.dump(review, open(f"{OUT}/review.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {len(E)} entries → {OUT}/{NAME}.md")


if __name__ == "__main__":
    main()
