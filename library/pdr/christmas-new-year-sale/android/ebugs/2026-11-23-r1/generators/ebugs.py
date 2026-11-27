#!/usr/bin/env python3
"""Build the Christmas & New Year Sales Android eBug draft batch for round R1 (table v2, draft 20261120-165128) on 16.9.0 (2611201).

Writes library/pdr/christmas-new-year-sale/android/ebugs/2026-11-23-r1/20261123_eBug_drafts_Christmas-Sale-R1_16.9.0.md,
the sibling _images/ folder (one NN_ISS-ID folder per entry: red-boxed JPEGs named 16.9.0_<slug>.jpg) and dedupe.txt.
First batch of this feature: ISS-XMA-01 on. Nothing is filed. Every Fail row of results.csv and every observation O-n
is mapped (entry / not raised / held); the script stops when one is missing.

Usage: python3 library/pdr/christmas-new-year-sale/android/ebugs/2026-11-23-r1/generators/ebugs.py
"""
import csv, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(OUT, *[".."] * 6))
ROOT = f"{REPO}/library/pdr/christmas-new-year-sale/android"
RUN = f"{ROOT}/runs/2026-11-23-r1-christmas"
NAME = "20261123_eBug_drafts_Christmas-Sale-R1_16.9.0"
V, B = "16.9.0", "2611201"
TAG = "AIAgent"
DEVICE = "Device: Samsung Galaxy A51 SM-A516B / Android 13"
STATE = "Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan"

DS = "https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id="
PM = "https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id="
SHEET = "https://docs.google.com/spreadsheets/d/1_rJf-7ljc0c_HO0P4isuyn-AOt6mIlbXsmyRW9xcGSk/edit?gid=1226976055"


def ds(board, node, what):
    return (f"Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), {board} board {what} -", DS + node)


def pm(board, what, node="3226-21365"):
    return (f"Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), {board} board {what} -", PM + node)


def sheet(what):
    return (f"Spec Link: 多國文案 sheet (linked from the PM rules board), block 「Christmas Special 11/E」 {what} -", SHEET)


# full-resolution boxes (1080 x 2400 portrait unless noted)
BX_SAVE = (180, 680, 410, 800)
BX_VS = (250, 1195, 830, 1305)
BX_YEAR = (690, 1335, 900, 1455)
BX_MORE = (330, 2030, 750, 2115)
BX_CTA = (45, 1725, 1035, 1890)
BX_PCT = (180, 680, 900, 1200)
BX_LINKS = (10, 2165, 1070, 2250)
STRIP = (6, 6, 1074, 104)

L1 = "Launch the APP"


def lang(name):
    return ["Clear the app data", f"Set the app language to {name}", L1, "Tap 「Get Started」", "Tap 「Allow」 on the notification prompt"]


E = [
 dict(iss="ISS-XMA-01", title="Interstitial: 「SAVE」 and 「vs. paying …/mo × 12」 stay English in all 26 other languages",
      cls="UI", sev=2, owner="RD", cases=[f"TC-0{i}" for i in range(30, 56)], extra="O-7", rep=(26, 26), feat="Christmas Sale (Interstitial)",
      short="[MUI] 「SAVE」 and 「vs. paying …/mo × 12」 are not localized",
      note="R-022 (PM rules 底圖 & 價格 + 多國文案 sheet; ruling Q-16: all 27 languages ship): the lines under the title art (Save, vs., CTA) are localized text made by RD per the sheet. Seen in all 26 non-English languages (TC-030 – TC-055), each run on pm clear + per-app locale (system language untouched). The CTA, disclaimer and bottom links are translated; only these lines and 「/year」 / 「More subscription plan」 (ISS-XMA-02) stay English. The app follows the Design layout (「SAVE」 「57」 「%」, 「vs. paying …/mo × 12」), the sheet gives one line 「Save 57%」 / 「vs. $6.79/mo」 per language, so the sheet's Save and vs. strings are the translations to use (with the store's % and monthly price, ruling Q-3). In Arabic and Persian the English line even takes local digits (「× ١٢」, 「× ۱۲」). Older campaigns had the same class of bug (DRA262607-0038 「Save up to」 not localized, closed).",
      steps=lang("中文（台灣）") + ["Look at the lines under the title art"],
      res="In every non-English language (26 of 26) 「SAVE」 and 「vs. paying NT$240/mo × 12」 stay in English.",
      res_zh="所有非英文語系（26 種）的插頁仍顯示英文「SAVE」與「vs. paying NT$240/mo × 12」。",
      exp="Both lines use the 多國文案 sheet's Save and vs. text for the app language, with the store's % and price.",
      exp_zh="兩行文字應依多國文案表翻譯成該語系（百分比與月價依商店價格），例如繁中「現省 xx%」「相較於每月NT$240」。",
      imgs=[("TC-030-01", "xma01_cht", [BX_SAVE, BX_VS]), ("TC-042-01", "xma01_rus", [BX_SAVE, BX_VS]), ("TC-048-02", "xma01_ara_digits", [(6, 6, 674, 134)])],
      links=[pm("pm-xmas-rules", "(底圖 & 價格: lines under the art localized by RD per the linked 多國文案 sheet, Save and vs. rows)")]),

 dict(iss="ISS-XMA-02", title="Interstitial: 「/year」 and 「More subscription plan」 stay English in all 26 other languages; the sheet has no translation",
      cls="UI", sev=2, owner="PM", cases=[f"TC-0{i}" for i in range(30, 56)], extra="O-7", rep=(26, 26), feat="Christmas Sale (Interstitial)",
      short="[MUI] 「/year」 and 「More subscription plan」 are not localized",
      note="Text with no spec source: the 多國文案 sheet translates only the title, Save, vs. and CTA; 「/year」 after the annual price and the link 「More subscription plan」 have no translation anywhere in the spec, so PM must supply them (AGENTS.md text rule 2026-11-11: PM when no sheet states it). Plainly wrong on screen (English in a localized page), so filed, not held. Same 26 rows as ISS-XMA-01.",
      steps=lang("Русский") + ["Look at the annual price and the link under the trial terms"],
      res="「NT$1,210/year」 and 「More subscription plan」 are English in every non-English app language (26 of 26).",
      res_zh="所有非英文語系中「/year」與「More subscription plan」仍為英文。",
      exp="PM to supply 「/year」 and 「More subscription plan」 for the 26 languages; then both show translated.",
      exp_zh="請 PM 提供 26 種語系的「/year」與「More subscription plan」翻譯。",
      imgs=[("TC-042-01", "xma02_rus", [BX_YEAR, BX_MORE]), ("TC-037-01", "xma02_jpn", [BX_YEAR, BX_MORE])],
      links=[pm("pm-xmas-rules", "(linked 多國文案 sheet: no row for 「/year」 or 「More subscription plan」)"), ds("Interstitial", "2750-19946", "(「/year」, 「More subscription plan」)")]),

 dict(iss="ISS-XMA-03", title="Interstitial: CTA wording differs from the 多國文案 sheet in 12 languages",
      cls="UI", sev=3, owner="RD", cases=["TC-030", "TC-031", "TC-032", "TC-036", "TC-037", "TC-038", "TC-039", "TC-042", "TC-044", "TC-045", "TC-048", "TC-051"], extra="O-7", rep=(12, 12), feat="Christmas Sale (Interstitial)",
      short="[MUI] CTA text differs from the 多國文案 sheet in 12 languages",
      note="R-022: the CTA is RD's localized text per the 多國文案 sheet. The app shows the generic trial string instead in 12 languages; the other 14 match. Note ESP shows the ESP (MX) sheet text and ESP (MX) a third wording. App vs sheet: CHT 「7 天免費試用」 vs 「７天免費試用」 (full-width 7, no space); CHS 「7 天免费试用」 vs 「7天免费试用」; FRA 「Recevoir 7 jours d'essai gratuits」 vs 「Essai gratuit de 7 jours」; ITA 「Prova Gratuita di 7gg.」 vs 「Prova Gratis per 7gg.」; JPN 「７日間無料お試し」 vs 「7 日間無料で試す」; KOR 「7일 무료 체험」 vs 「7일 무료 체험 시작하기」; ESP 「Prueba gratis por 7 días」 vs 「Prueba 7 días gratis」; RUS 「7-дн. беспл. пробное」 vs 「Попробовать 7 дней бесплатно」; ESP (MX) 「Inicia tu prueba gratuita de 7 días」 vs 「Prueba gratis por 7 días」; Viet 「Dùng Thử Miễn Phí 7 Ngày」 vs 「Dùng thử miễn phí 7 ngày」; Arabic 「ابدأ تجربة مجانية لمدة 7 أيام」 vs 「بدء تجربة مجانية لمدة 7 أيام」; Hebrew 「נסה בחינם למשך 7 ימים」 vs 「ניסיון חינם ל-7 ימים」.",
      steps=lang("Français") + ["Look at the yellow button"],
      res="The CTA reads 「Recevoir 7 jours d'essai gratuits」 (FRA); 12 languages differ from the sheet.",
      res_zh="12 種語系的 CTA 與多國文案表不同（例如法文、俄文、韓文、日文）。",
      exp="The CTA uses the sheet's text in each language (FRA 「Essai gratuit de 7 jours」).",
      exp_zh="CTA 應使用多國文案表的各語系文字。",
      imgs=[("TC-032-01", "xma03_fra", [BX_CTA]), ("TC-042-01", "xma03_rus", [BX_CTA]), ("TC-038-01", "xma03_kor", [BX_CTA]), ("TC-037-01", "xma03_jpn", [BX_CTA])],
      links=[pm("pm-xmas-rules", "(linked 多國文案 sheet, CTA row)")]),

 dict(iss="ISS-XMA-04", title="Interstitial: bottom links run into each other or into the separators in RUS, FRA, UKR and Polish",
      cls="UI", sev=3, owner="RD", cases=["TC-042", "TC-032", "TC-055", "TC-049"], extra="O-7", rep=(4, 4), feat="Christmas Sale (Interstitial)",
      short="[RUS/FRA/UKR/POL] Bottom links overlap each other or separators",
      note="R-022 rows check 「No text clipped, overlapped or in another language」. Measured from the page source: RUS 「Условия обслуживания」 (x 78–366), 「Политика конфиденциальности」 (344–738) and 「Восстановить покупку」 (720–996) overlap each other and the separators; FRA both separators touch 「Politique de confidentialité」; UKR 「Політика конфіденційності」 (376–706) under both separators (381, 698), the right one over its last letter; Polish the left separator (381) touches 「Warunki korzystania z usługi」 (63–385).",
      steps=lang("Русский") + ["Look at the three links at the bottom"],
      res="RUS: the three links overlap each other; FRA, UKR, Polish: separators touch or cover the link text.",
      res_zh="俄文三個連結互相重疊並壓到分隔線；法文、烏克蘭文、波蘭文分隔線碰到或壓到文字。",
      exp="The three links and their separators sit apart with nothing overlapping (wrap or shrink the links when they do not fit).",
      exp_zh="三個連結與分隔線應各自分開、不重疊。",
      imgs=[("TC-042-02", "xma04_rus_links", [STRIP]), ("TC-032-02", "xma04_fra_links", [STRIP]), ("TC-055-02", "xma04_ukr_links", [STRIP]), ("TC-049-02", "xma04_pol", [(6, 6, 1074, 564)])],
      links=[ds("Interstitial", "2750-19946", "(「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」)")]),

 dict(iss="ISS-XMA-05", title="Interstitial (Polish): the CTA wraps to two lines that fill the button edge to edge",
      cls="UI", sev=3, owner="RD", cases=["TC-049"], rep=(1, 1), feat="Christmas Sale (Interstitial)",
      short="[POL] CTA wraps to two lines with no side padding in the button",
      note="R-022 (Polish CTA 「Rozpocznij 7-dniowy bezpłatny okres próbny」, text matches the sheet). The text box spans x 63–1017, the whole button, so the words touch the rounded ends; the Design draws one line centred with padding.",
      steps=lang("Polski") + ["Look at the yellow button"],
      res="The Polish CTA wraps to two lines that run to both edges of the button.",
      res_zh="波蘭文 CTA 折成兩行，文字貼滿按鈕左右兩端，沒有內距。",
      exp="The CTA text sits inside the button with side padding (one line, smaller text or a taller button).",
      exp_zh="CTA 文字應在按鈕內保留左右內距。",
      imgs=[("TC-049-01", "xma05_pol_cta", [BX_CTA])],
      links=[ds("Interstitial", "2750-19946", "(CTA 「Get 7-Day Free Trial」, one line)")]),

 dict(iss="ISS-XMA-06", title="Interstitial and IAP show 57% where the store prices give 57.99% (58%)",
      cls="Functional", sev=3, owner="RD", cases=[f"TC-0{i}" for i in range(30, 56)], extra="O-3", rep=(3, 3), feat="Christmas Sale (IAP)",
      short="Discount shows 57% though NT$1,210 vs NT$240 × 12 gives 57.99%",
      note="R-018 / R-036, ruling Q-3 (REQ-002): the % is computed by the app from the store's campaign prices (PM 「Xmas 年價格 vs 月價格*12個月的價差%」); Q-3 itself says TW gives 58%. On the Taiwan store (NT$1,210/year, NT$240/month, both shown on the page) (2880 − 1210) ÷ 2880 = 57.99%, but the interstitial (every language, TC-029 – TC-055) and the IAP card (TC-019, TC-100) show 57: either truncated or the mockups' fixed 57. The US store ($45.99 / $6.99 → 45%) tells them apart; it waits for Play Billing Lab (TC-013, TC-101 Blocked). If truncation is intended, RD forwards it to PM to rule on rounding. Listed on the Fail rows' Report step because each language row noted it; those rows fail on the text items too.",
      steps=[L1, "Close the Christmas interstitial with X" , "Tap the top pill on the Launcher", "Look at the annual plan card", "Tap the back arrow", "Clear the app data", L1, "Tap 「Get Started」", "Tap 「Allow」 on the notification prompt", "Look at the big percentage"],
      res="Both pages show 57% while their own prices, NT$1,210/year and NT$240/month, give 57.99%.",
      res_zh="插頁與 IAP 顯示 57%，但 NT$1,210 與 NT$240×12 計算為 57.99%。",
      exp="The % is computed from the store's campaign prices and rounded: 58% on the Taiwan store, 45% on the US store (Q-3).",
      exp_zh="百分比應由商店價格計算並四捨五入：台灣 58%、美國 45%。",
      imgs=[("TC-029-01", "xma06_interstitial_57", [BX_PCT, BX_YEAR, BX_VS]), ("TC-100-01", "xma06_iap_57", [(740, 1290, 1060, 1500)])],
      links=[pm("pm-xmas-rules", "(➍ formula: 年價格 vs 月價格*12個月的價差%)"), ds("Interstitial", "2750-19946", "(「SAVE」 「<xx>」 「%」)")]),

 dict(iss="ISS-XMA-07", title="Launcher: the top banner shows 「Turn one photo to cinematic reel」, not 「Make Christmas magic with AI」",
      cls="UI", sev=2, owner="RD", cases=["TC-083", "TC-084"], rep=(2, 2), feat="Christmas Sale (Launcher)",
      short="Top banner title is not 「Make Christmas magic with AI」",
      note="R-026 (Design Launcher dark / light, PM rules ➌). The banner image is a Christmas picture, so the campaign banner may be on with the wrong title, or the Stage CMS still holds the Cinematic Reel banner text; RD to say which. Unchanged over 15 s (no rotation). Legibility in dark and light mode is fine. Banner target (Q-7) not judged.",
      steps=[L1, "Tap X on the Christmas interstitial", "Look at the top banner title"],
      res="The top banner shows a Christmas image titled 「Turn one photo to cinematic reel」, in dark and light mode.",
      res_zh="頂部橫幅標題為「Turn one photo to cinematic reel」。",
      exp="The top banner is the Christmas banner titled 「Make Christmas magic with AI」 › in dark and light mode.",
      exp_zh="頂部橫幅應為聖誕橫幅，標題「Make Christmas magic with AI」。",
      imgs=[("TC-083-01", "xma07_dark", [(25, 770, 1055, 870)]), ("TC-084-01", "xma07_light", [(25, 770, 1055, 870)])],
      links=[ds("Launcher & dialog", "2772-10246", "(Launcher dark / light: 「Make Christmas magic with AI」)")]),

 dict(iss="ISS-XMA-08", title="Launcher: the top pill reads only 「Pro」, not 「Try Pro 7 days for free」",
      cls="UI", sev=2, owner="RD", cases=["TC-087", "TC-090"], rep=(2, 2), feat="Christmas Sale (Launcher)",
      short="Top pill reads 「Pro」, not 「Try Pro 7 days for free」",
      note="R-028 (Design Launcher pill 「Try Pro+ 7 days for free」 with Santa hat; ruling Q-8: Android says Pro, never Pro+). The Santa-hat icon is right and the pill opens the Christmas IAP page; no countdown (as expected for Christmas). The Mine tab's pill in the same state does read 「Try Pro 7 days for free」 (TC-095, TC-098), so only the Launcher pill is short.",
      steps=[L1, "Tap X on the Christmas interstitial", "Look at the pill at the top of the Launcher"],
      res="The Launcher pill reads only 「Pro」 with the Santa hat; Mine's pill reads 「Try Pro 7 days for free」.",
      res_zh="Launcher 頂部膠囊只顯示「Pro」（Mine 頁的膠囊則為「Try Pro 7 days for free」）。",
      exp="The Launcher top pill reads 「Try Pro 7 days for free」 with the Santa-hat icon (Pro, never Pro+).",
      exp_zh="Launcher 頂部膠囊應顯示「Try Pro 7 days for free」並有聖誕帽圖示。",
      imgs=[("TC-090-01", "xma08_launcher_pill", [(150, 130, 420, 250)]), ("signin-03", "xma08_mine_pill", [])],
      links=[ds("Launcher & dialog", "2772-10246", "(top pill 「Try Pro+ 7 days for free」, Santa hat; Pro per ruling Q-8)")]),

 dict(iss="ISS-XMA-09", title="IAP opened from the interstitial: back arrow and system Back go to the Launcher, not back to the interstitial",
      cls="UX", sev=3, owner="PM", basis="Basis: In-product — Christmas IAP page: its back arrow returns to the page it was opened from (R-042); the interstitial case is not stated", cases=["TC-109"], extra="O-5", rep=(2, 2), feat="Christmas Sale (IAP)",
      short="Back from IAP opened via 「More subscription plan」 skips the interstitial",
      note="Question for PM, filed for a decision (AGENTS.md 2026-11-11). R-042 says the IAP back arrow ‹ returns to the page it was opened from, R-061 that system Back does what ‹ does. From the interstitial both land on the Launcher (TC-109, and ‹ in R1-a TC-019 / O-5). Whether closing the interstitial on the way back is intended (it shows once a day) is not stated; an older ticket on 15.9.1 (DRA252511-0129, closed) complained that Back from the plans 「briefly shows interstitial before launcher」.",
      steps=["Clear the app data", L1, "Tap 「Get Started」", "Tap 「Allow」 on the notification prompt", "Tap 「More subscription plan」", "Press system Back"],
      res="System Back (and the ‹ arrow) on the IAP page goes to the Launcher Home; the interstitial is gone.",
      res_zh="從插頁進入 IAP 後，按系統返回鍵（或左上返回）直接回到 Launcher，不回插頁。",
      exp="PM to decide: should Back return to the interstitial (R-042) or close both to the Launcher?",
      exp_zh="請 PM 決定：從此 IAP 返回應回到插頁，或直接回到 Launcher？",
      imgs=[("TC-143-02", "xma09_iap_from_interstitial", []), ("TC-109-01", "xma09_after_back", [(20, 770, 1060, 870)])],
      links=[ds("IAP & Credit", "2750-19947", "(IAP_year back arrow ‹)"), pm("pm-xmas-launch", "(flow arrow 「More subscription plan」 → IAP_T1)", "3226-31190")]),

 dict(iss="ISS-XMA-10", title="Short screen: the IAP banner title 「Christmas Special」 is clipped at the bottom",
      cls="UI", sev=3, owner="RD", cases=["TC-143"], rep=(1, 1), feat="Christmas Sale (IAP)",
      short="[Short screen] Banner title 「Christmas Special」 is clipped at the bottom",
      note="R-023 (Design 「短裝置」 Pixel 2 411×731 frames 2750:20070, 2750:20280). The run set wm size 1080×1920 at 420 dpi = 411×731 dp (restored after). The banner shrinks to a 245 px strip and the descender of 「p」 in 「Special」 is cut off; the ‹ arrow sits on a snowflake. The interstitial and the credit pages fit.",
      steps=["Set the screen to 411 × 731 dp (a short Android screen)", "Clear the app data", L1, "Tap 「Get Started」", "Tap 「Allow」 on the notification prompt", "Tap 「More subscription plan」", "Look at the banner title"],
      res="The banner is cut to a short strip and the bottom of 「Special」 (the descender of 「p」) is clipped.",
      res_zh="短螢幕下 IAP 橫幅被壓縮，「Special」底部（p 的下緣）被裁切。",
      exp="On the short screen the whole title 「Christmas Special」 shows, as the short-device frame draws it.",
      exp_zh="短螢幕下應完整顯示「Christmas Special」，不被裁切。",
      imgs=[("TC-143-02", "xma10_short_iap", [(0, 0, 1080, 255)]), ("TC-143-02-title", "xma10_title_crop", [(4, 90, 576, 146)])],
      links=[ds("IAP & Credit", "2750-19947", "(短裝置 IAP_year, Pixel 2 411×731)")]),

 dict(iss="ISS-XMA-11", title="Landscape: the Launcher shows no Christmas top banner",
      cls="Functional", sev=3, owner="RD", cases=["TC-144"], rep=(1, 1), feat="Christmas Sale (Launcher)",
      short="[Landscape] Launcher shows no Christmas top banner",
      note="R-059 (Design Landscape: the campaign top banner and pill over the landscape Launcher). The run turned the phone with auto-rotate off and user_rotation 1 (the app follows: w832dp h387dp); restored after. The pill (Santa hat, 「Pro」, ISS-XMA-08) shows; no banner image or title at all. Landscape IAP (TC-146) is right.",
      steps=[L1, "Tap X on the Christmas interstitial", "Turn the phone to landscape", "Look at the top of the Launcher"],
      res="In landscape the Launcher shows the pill, the tool row and My Projects, but no Christmas top banner.",
      res_zh="橫向時 Launcher 沒有聖誕頂部橫幅。",
      exp="In landscape the Christmas top banner and pill show over the Launcher, as the Design draws it.",
      exp_zh="橫向時應顯示聖誕頂部橫幅與膠囊。",
      imgs=[("TC-144-01", "xma11_landscape", [(40, 20, 2380, 420)])],
      links=[ds("Landscape", "2750-27885", "(Launcher landscape with the campaign banner)")]),

 dict(iss="ISS-XMA-12", title="IAP plan card: tag 「Special Offer」 and 「57% OFF」, not 「Christmas Treat」 and 「Save 57%」; monthly price not struck",
      cls="UI", sev=2, owner="RD", cases=[], extra="O-4", rep=(3, 3), feat="Christmas Sale (IAP)",
      short="Tag 「Special Offer」 and 「57% OFF」 instead of 「Christmas Treat」, 「Save xx%」",
      note="R-035 / R-037 (PM 1104 Update, ruling Q-10: the PM 1104 version wins over the older Design 「Special Offer」 / 「67% OFF」). Seen on every IAP entry (TC-006, TC-019, TC-087, TC-096, TC-146); recorded at TC-100, which is Blocked only because its US prices need Play Billing Lab: the tag text, the % wording and the missing struck price do not depend on the store. Also differs on the page: CTA 「Continue」 (Design 「Get 7-Day Free Trial」) and the feature strip is a carousel with 「No Watermark」 rather than the three cards — left to the reviewer, not in this entry.",
      steps=[L1, "Tap X on the Christmas interstitial", "Tap the top pill on the Launcher", "Look at the annual and monthly plan cards"],
      res="The tag reads 「Special Offer」, the card 「57% OFF」, and the monthly price is not struck through.",
      res_zh="年方案標籤為「Special Offer」、顯示「57% OFF」，月方案無劃掉原價。",
      exp="Tag 「Christmas Treat」, 「Save <xx>%」, and the monthly card's original price struck through (PM 1104).",
      exp_zh="標籤應為「Christmas Treat」、「Save xx%」，月方案顯示劃掉的原價。",
      imgs=[("TC-100-01", "xma12_iap_card", [(740, 1290, 1060, 1380), (870, 1370, 1020, 1500), (45, 1555, 1035, 1705)]), ("TC-019-01", "xma12_iap_from_interstitial", [(740, 1290, 1060, 1380), (45, 1555, 1035, 1705)])],
      links=[pm("pm-xmas-launch", "(1104 Update, IAP: 「Christmas Treat」, struck monthly price, no 「Offer」)"), ds("IAP & Credit", "2750-19947", "(IAP_year plan cards)")]),
]

NOT_RAISED = [
 ("TC-095", "Mine Free card reads 「15+ Benefits」, the Design draws 「20+ Benefits」", "Already ruled by a ticket: DRA262608-0134 (16.6.0, closed) changed Mine to 「15+ Benefits」 on purpose (DRA262608-0146 for other languages); the Christmas Design copies the old figure. Cited, not filed (ebugs.md step 1). The row's other checks passed."),
 ("TC-124", "Christmas 500-credit pack missing for the Free user; the pack page shows 「First Purchase Discount」 1000 +1000", "Held: the row needs a signed-in Free account and the run was signed out (sign-in 403, O-9); credit offers are account-tied, so recheck signed in in the R1-d rerun. The sale price is also undecided (Q-13)."),
 ("O-1", "ToS / Privacy Policy open the Traditional Chinese pages on an English app", "Spec silent; likely chosen by region (Taiwan). Report only."),
 ("O-2", "First Restore after a fresh launch returns with no message after the accounts permission", "TC-028 passed on the second tap; report only (candidate for a later row)."),
 ("O-6", "Play Billing Lab not signed in (needs Google's terms accepted)", "Environment; the user's go-ahead is needed."),
 ("O-8", "AI Mini Drama intro sits between the Open intro and the interstitial on the 2nd launch", "TC-009 passed; another feature's intro. Report only."),
 ("O-9", "Stage sign-in after pm clear fails: bindMember HTTP 403", "Same OS, same build already filed: DRA262611P0200 (Sign in CL account fail, Assigned) and DRA262611P0253 (Sign in fail if install AP via APK, 2611201): dedupe.txt only."),
 ("O-10", "「Unofficial Version」 「We couldn't verify your app installation. Purchases are unavailable.」 on every subscription CTA", "Environment: build sideloaded with adb (installer not Google Play); related to DRA262611P0253. Blocks R1-d; report only."),
]
FOLDED = {"O-3": "6. ISS-XMA-06", "O-4": "12. ISS-XMA-12", "O-5": "9. ISS-XMA-09", "O-7": "1–5. ISS-XMA-01…05"}
OBS_ALL = [f"O-{i}" for i in range(1, 11)]

DUPS_TXT = [
 ("O-9 (Stage sign-in after pm clear: bindMember HTTP 403)", "DRA262611P0200", "Assigned, RD, S1, 16.9.0.2611161: 「SIgn In: Sign in CL account fail」"),
 ("O-9 / O-10 (sign-in and purchases on the adb-installed 2611201)", "DRA262611P0253", "BugNeedReview, RD, 16.9.0.2611201: 「SIgn In: Sign in fail if install AP via APK」"),
 ("TC-095 (「15+ Benefits」 vs Design 「20+ Benefits」)", "DRA262608-0134", "Close, 16.6.0: 「[UX] Mine: Mine page shows \"20+ Benefits\" instead of \"15+ Benefits\"」 — the app's 15+ is the ruled state; cited"),
]


def shot(src, dst, boxes):
    im = Image.open(src).convert("RGB")
    d = ImageDraw.Draw(im)
    w = max(4, im.size[0] // 160)
    for b in boxes:
        d.rectangle(b, outline=(255, 0, 0), width=w)
    im.thumbnail((1400, 1400))
    im.save(dst, "JPEG", quality=82)


def main():
    rows = list(csv.DictReader(open(f"{RUN}/results.csv", encoding="utf-8-sig")))
    tally = {}
    for r in rows:
        tally[r["Result"]] = tally.get(r["Result"], 0) + 1
    fails = [r["ID"] for r in rows if r["Result"] == "Fail"]
    disp = {r["ID"]: r["Disposition"] for r in rows}
    obs_file = open(f"{RUN}/observations.md", encoding="utf-8").read()
    obs = [o for o in OBS_ALL if re.search(rf"^- \*\*{o}\*\*", obs_file, re.M)]
    if len(obs) != 10:
        sys.exit(f"observations found: {obs}")
    MAP = {}
    for n, e in enumerate(E, 1):
        for c in e["cases"]:
            MAP.setdefault(c, []).append(f"{n}. {e['iss']}")
    for k, _, why in NOT_RAISED:
        MAP.setdefault(k, []).append("held: recheck signed in" if why.startswith("Held") else ("cited " + re.search(r"DRA\S+", why).group(0).rstrip(",") if why.startswith("Already") else "not raised" + (" (existing ticket, dedupe.txt)" if "DRA" in why and k == "O-9" else "")))
    for k, v in FOLDED.items():
        MAP.setdefault(k, []).append(f"folded into {v}")
    MAP = {k: "; ".join(dict.fromkeys(v)) for k, v in MAP.items()}
    missing = [k for k in fails + obs if k not in MAP]
    extra = [k for k in MAP if k not in fails and k not in obs]
    if missing or extra:
        sys.exit(f"reconciliation incomplete: missing {missing}, extra {extra}")

    img_root = f"{OUT}/{NAME}_images"
    if os.path.isdir(img_root):
        shutil.rmtree(img_root)
    os.makedirs(img_root)
    L = []
    w = L.append
    w(f"# Christmas & New Year Sales (Android) — eBug drafts, round R1 (table v2, Christmas rows), PDR-A {V} build {B}")
    w("")
    w(f"**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-23-r1-christmas/` — round R1 of draft `drafts/20261120-165128` (table v2, Christmas rows, {len(rows)} cases), 2026-11-23 11:09 → 14:06, on {DEVICE[8:]} (adb R5CN8194YSN) through Appium / UiAutomator2, build 16.9.0.{B} (SR DRA261109-01, installed with adb), Stage server with the RD test date inside the Christmas window, Free account signed out (Stage sign-in after pm clear fails, KP-093), Google Play store Taiwan. Tally: " + ", ".join(f"{v} {k}" for k, v in tally.items()) + ".")
    w("")
    w("**Status:** nothing filed, uploaded or commented. First batch of this feature (`ebug-defaults.ts pdr/christmas-new-year-sale android`: no filed batch); no TR is named for 2611201 yet, so Creator, TRCode, source tag and method are for the reviewer. Dedupe: read-only eBug Search, Android pool only (per OS, user 2026-10-28): no open or resolved Android ticket matches an entry; the Christmas tickets in the pool are all from the 2025 campaign (15.9.x, closed). `dedupe.txt`.")
    w("")
    w("Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, no video; no entry rests on a log); `[AIAgent]` / `[AIAgent][UI]` owner RD for defects; text with no spec source and open questions to PM (BugBelong PM), `[AIAgent][UX]` for the one user-experience decision (2026-11-11). Design first unless the PM item is newer (PM 1104 Update wins for the IAP card, ruling Q-10). Every row's precondition is a signed-in Free account; the run was signed out, so each entry names that condition and the account-tied pack row (TC-124) is held. Severity is proposed.")
    w("")
    w(f"**What is drafted:** {len(E)} entries (ISS-XMA-01…{len(E):02d}): " + ", ".join(f"{sum(1 for e in E if e['owner'] == o and e['cls'] == c)} {o} {c}" for o, c in (("RD", "Functional"), ("RD", "UI"), ("PM", "UI"), ("PM", "UX")) if any(e['owner'] == o and e['cls'] == c for e in E)) + ". Entry 12 comes from observation O-4 (seen on every IAP entry; its row TC-100 is Blocked only for the US store).")
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
        tagtype = "" if e["cls"] == "Functional" else f"[{e['cls']}]"
        short = f"PDR-A {V} - [{TAG}]{tagtype} {e['feat']}: {e['short']}"
        if len(short) > 125:
            sys.exit(f"{e['iss']} short description {len(short)} > 125")
        for s in e["steps"]:
            if ">" in s or "›" in s:
                sys.exit(f"{e['iss']} step has a chain: {s}")
        rs = ", ".join(e["cases"]) if len(e["cases"]) < 6 else f"{e['cases'][0]} – {e['cases'][-1]} ({len(e['cases'])} rows)"
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
        w(""); w("Result:"); w(e["res"]); w(f"摘要：{e['res_zh']}"); w(" ".join("{" + x + "}" for x in names))
        w(""); w("Expect Result:"); w(e["exp"]); w(f"摘要：{e['exp_zh']}")
        w(""); w("Note:"); w(DEVICE); w(STATE)
        for label, url in e["links"]:
            w(label); w(url)
        if e.get("basis"):
            w(e["basis"])
        w("<Claude Reviewed>"); w("```"); w("")
        w(f"**Images:** `{NAME}_images/{folder}/`"); w("")

    w("---"); w("")
    w("# Not raised (for the record)")
    w("")
    w("| Item | What was seen | Why not raised |")
    w("|---|---|---|")
    for k, a, b in NOT_RAISED:
        w(f"| {k} | {a} | {b} |")
    blocked = [r for r in rows if r["Result"] == "Blocked"]
    bd = {}
    for r in blocked:
        bd[r["Disposition"]] = bd.get(r["Disposition"], 0) + 1
    w(f"| Blocked ({len(blocked)}) | " + ", ".join(f"{v} {k}" for k, v in sorted(bd.items())) + " | No verdict (reasons in report.md and blocked-reasons.json): R1-d not run (purchases unavailable, sign-in 403), Play Billing Lab terms, RD date fixed, no old build, portrait-only interstitial. |")
    w("")
    w("## Reconciliation against the run")
    w("")
    w(f"{len(fails)} Fail (all defect), {len(blocked)} Blocked, {len(obs)} observations (O-1 … O-10).")
    w("")
    w("| Step | Count | Running total |")
    w("|---|---|---|")
    tot = len(fails) + len(obs)
    nr = [k for k, v in MAP.items() if v.startswith(("not raised", "held", "cited"))]
    fold = [k for k, v in MAP.items() if v.startswith("folded")]
    w(f"| Fail rows + observations | {tot} | {tot} |")
    run = tot - len(nr); w(f"| → not raised, held or cited (TC-095 cited, TC-124 held, {len(nr) - 2} observations) | −{len(nr)} | {run} |")
    run -= len(fold); w(f"| → observations folded into entries (O-3, O-4, O-5, O-7) | −{len(fold)} | {run} |")
    w(f"| → merged: {run} rows share 11 defects or questions; entry 12 rests on O-4 | | **{len(E)} entries** |")
    w("")
    w("### Row-by-row map")
    w("")
    w("| Item | Result | Disposition | Became |")
    w("|---|---|---|---|")
    for k in fails:
        w(f"| {k} | Fail | {disp[k]} | {MAP[k]} |")
    for k in obs:
        w(f"| {k} | observation | — | {MAP[k]} |")
    w("")
    w("### Owner split")
    w("")
    w("| Owner | Entries |")
    w("|---|---|")
    for o in ("RD", "PM"):
        w(f"| {o} | {', '.join(str(i) for i, e in enumerate(E, 1) if e['owner'] == o) or '—'} |")
    w("")
    w("### Filing order")
    w("")
    w("By severity: " + ", ".join(f"**{i}**" for s in (1, 2, 3, 4) for i, e in enumerate(E, 1) if e["sev"] == s) + ". Nothing is filed until the review page's decisions come back.")
    w("")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(L))
    D = ["# Dedupe — Christmas & New Year Sales Android R1 (16.9.0.2611201), read-only eBug Search, PowerDirector Mobile for Android only", "",
         "Searched 2026-11-23: --text Christmas / Interstitial / Holiday / Benefits / Special Offer / Try Pro / Unofficial / Sale / subscription plan / banner, and every open 16.9.0 ticket (86).",
         "No entry repeats an Android ticket. The Christmas tickets in the pool are the 2025 campaign's (15.9.x, closed / NAB / Won't Fix).", "",
         "Kept here only (not drafted):"]
    for a, b, c in DUPS_TXT:
        D.append(f"- {a}: {b} — {c}")
    D += ["", "Related, other campaigns (closed, not the same bug): DRA262607-0038 (Obon 「Save up to」 not localized), DRA252511-0129 (15.9.1 Back from plans briefly shows the interstitial)."]
    open(f"{OUT}/dedupe.txt", "w", encoding="utf-8").write("\n".join(D) + "\n")
    print(f"wrote {len(E)} entries → {OUT}/{NAME}.md")


if __name__ == "__main__":
    main()
