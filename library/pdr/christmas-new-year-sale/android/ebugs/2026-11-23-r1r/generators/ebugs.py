#!/usr/bin/env python3
"""Build the Christmas & New Year Sales Android eBug draft batch for round R1r (the R1 recheck on the Play test build,
16.9.0 2611201, draft 20261120-165128).

Writes library/pdr/christmas-new-year-sale/android/ebugs/2026-11-23-r1r/20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0.md,
the sibling _images/ folder (one NN_ISS-ID folder per entry: red-boxed JPEGs and log excerpts named 16.9.0_<slug>.*),
dedupe.txt and review.json. Entries continue the R1 batch's numbering (ISS-XMA-13 on). Findings that are the same bug
as an R1 entry are listed as additions to that entry, not drafted again. Every Fail row, every defect Blocked row and
every observation of the run is mapped; the script stops when one is missing. Nothing is filed.

Usage: python3 library/pdr/christmas-new-year-sale/android/ebugs/2026-11-23-r1r/generators/ebugs.py
"""
import csv, json, os, re, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(OUT, *[".."] * 6))
ROOT = f"{REPO}/library/pdr/christmas-new-year-sale/android"
RUN = f"{ROOT}/runs/2026-11-23-r1r-recheck"
LOGA = f"{RUN}/logs/R1r-a-20261123-150024/logcat-live.txt"
LOGB = f"{RUN}/logs/R1r-b-20261123-151009/logcat-live.txt"
LOGC = f"{RUN}/logs/R1r-c-20261123-152640/logcat-live.txt"
NAME = "20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0"
R1 = "ebugs/2026-11-23-r1/20261123_eBug_drafts_Christmas-Sale-R1_16.9.0.md"
V, B = "16.9.0", "2611201"
TAG = "AIAgent"
DEVICE = "Device: Samsung Galaxy A51 SM-A516B / Android 13"

DS = "https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id="
PM = "https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id="


def ds(board, node, what):
    return (f"Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), {board} board {what} -", DS + node)


def pm(board, what, node="3226-21365"):
    return (f"Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), {board} board {what} -", PM + node)


def state(acct, store):
    return f"Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; {acct}; Play store {store} (Play Billing Lab)"


FREE, PRO, PRO_AP = "Free account, signed in", "Pro account (Christmas annual plan), signed in, no Credit Auto Pass", "Pro account with Credit Auto Pass, signed in"

# full-resolution boxes (1080 x 2400 portrait)
INT_SAVE = (200, 690, 875, 1125)
INT_VS = (285, 1200, 795, 1285)
INT_TERMS = (55, 1880, 1025, 2020)
IAP_YEAR = (50, 1335, 1030, 1525)
IAP_MONTH = (50, 1560, 1030, 1705)
CR_BANNER = (4, 4, 1076, 360)
CR_TOP = (60, 510, 1020, 725)
CR_PACKS = (60, 760, 1020, 1300)
CR_LINE = (260, 1700, 820, 1765)
CR_CTA = (60, 1775, 1020, 1910)
CR_EXP = (160, 1995, 915, 2040)
CR_FOOT = (290, 2130, 765, 2180)
VIP_EN = (40, 235, 1040, 775)
VIP_JA = (40, 235, 1040, 840)
PILL = (40, 110, 455, 195)

PRICE = r"GoogleBillingWrapper: getProductDetails: \S+ price:"

L1 = "Launch the APP"


def pbl(country):
    return [f"Set the Play country to {country} in Play Billing Lab", "Force-stop the APP", L1]


E = [
 dict(iss="ISS-XMA-13", title="Interstitial (US store): 「SAVE 52%」 and 「vs. paying $7.99/mo × 12」 come from the regular monthly plan, not the campaign $6.99",
      cls="Functional", sev=2, owner="RD", cases=["TC-013", "TC-101"], extra="O-1", rep=(1, 1), feat="Christmas Sale (Interstitial)",
      short="US store: SAVE 52% from the regular $7.99 monthly, not $6.99 (45%)",
      state=state(FREE, "United States"),
      note="R-006 / R-018 / R-036, ruling Q-3 (REQ-002): the interstitial's % and 「vs. paying …/mo」 are computed from the campaign SKUs' store prices (annualsubscription_christmas_2611 $45.99, monthlysubscription_christmas_2611 $6.99 → 45%). Logcat 14:52:28: the interstitial asked Play only for monthly_sub_usd6.99_202209 ($7.99, the regular monthly) and the Christmas annual: ($7.99×12 − $45.99) ÷ ($7.99×12) = 52.03% → 52. The IAP page a minute later (14:53:30) read the campaign monthly $6.99 and shows 45% (TC-101 Pass), so the two screens disagree. On the Taiwan store both monthly SKUs cost NT$240, which hid this in R1. Rounding vs truncation is a separate entry (R1 ISS-XMA-06): 52.03 gives 52 either way. Precondition: first launch of the day (the interstitial is daily).",
      steps=pbl("United States") + ["Tap 「Continue」 on the AI Mini Drama intro", "Look at the 「SAVE」 line and the 「vs. paying」 line"],
      res="The interstitial reads 「SAVE 52%」 「vs. paying $7.99/mo × 12」 (regular monthly); the IAP page shows $6.99 and 45%.",
      res_zh="插頁以一般月訂 $7.99 算出 52%，IAP 頁為 $6.99、45%。",
      exp="The interstitial uses the campaign monthly $6.99: 「SAVE 45%」 「vs. paying $6.99/mo × 12」.",
      exp_zh="插頁應以活動月訂 $6.99 計算：SAVE 45%。",
      imgs=[("TC-013-interstitial-us", "xma13_interstitial_us", [INT_SAVE, INT_VS]), ("TC-100-iap-us", "xma13_iap_us_45", [IAP_YEAR, IAP_MONTH])],
      log=("xma13_log", LOGA, [r"14:52:2[0-9]", r"14:53:3[0-2]"], r"getProductDetails: (monthly\S*|annualsubscription_christmas_2611) price:"),
      links=[pm("pm-xmas-rules", "(➊ monthly plan SKU monthlysubscription_christmas_2611, SKU 表 US $6.99; ➍ formula 年價格 vs 月價格*12個月的價差%)"), ds("Interstitial", "2750-19946", "(「SAVE」 「<xx>」 「%」, 「vs. paying <monthly price>/mo × 12」)")]),

 dict(iss="ISS-XMA-14", title="Interstitial: trial terms read 「until cancelled」, the spec 「until canceled」",
      cls="UI", sev=4, owner="RD", cases=["TC-014"], rep=(2, 2), feat="Christmas Sale (Interstitial)",
      short="Trial terms read 「until cancelled」, not 「until canceled」",
      state=state(FREE, "United States"),
      note="R-020 (Design and PM 1104 interstitial text): 「…Subscription renews automatically until canceled. Cancel in Google Play…」. The annual price in the terms matches the big price ($45.99), so that half of TC-014 passes; only the spelling differs. Same on the Taiwan store in R1. The spec states the string and the app shows another, so RD (text rule 2026-11-11). The IAP page's own terms use 「cancelled」 too (not part of this spec text).",
      steps=[L1, "Tap 「Continue」 on the AI Mini Drama intro", "Look at the trial terms under the yellow button"],
      res="The trial terms use the British spelling with a double 「l」, not the spec's US spelling.",
      res_zh="試用條款拼字為英式（雙 l），與規格美式拼字不同。",
      exp="The terms read 「…Subscription renews automatically until canceled. …」 as the spec states.",
      exp_zh="條款應為規格文字「until canceled」。",
      imgs=[("TC-013-interstitial-us", "xma14_terms", [INT_TERMS])],
      links=[ds("Interstitial", "2750-19946", "(trial terms 「…renews automatically until canceled…」)")]),

 dict(iss="ISS-XMA-15", title="IAP (India, Indonesia, Philippines): the page opens on the annual plan, not the monthly plan",
      cls="Functional", sev=2, owner="RD", cases=["TC-111", "TC-112", "TC-113"], rep=(3, 3), feat="Christmas Sale (IAP)",
      short="India, Indonesia, Philippines: IAP opens on the annual plan, not monthly",
      state=state(FREE, "India, Indonesia, Philippines"),
      note="R-007 (PM rules ➊: India, Indonesia and the Philippines keep the default landing on the monthly plan), ruling Q-17 (REQ-002): testers set the country with Play Billing Lab. The store did switch (logcat: annualsubscription_christmas_2611 ₹3,850 / IDR 590,000 / ₱2,500; monthlysubscription_christmas_2611 ₹750 / IDR 119,000 / ₱485), yet iap_radioBtn_yearly is checked when the page opens in all three. The phone's system locale is en-US and its SIM/network Taiwan; if the app picks the landing from something other than the Play country, RD can say so (Q-17 names Play Billing Lab as the test method).",
      steps=pbl("India") + ["Tap the Mine tab", "Tap 「Claim Holiday Deal」", "Look at which plan card is selected"],
      res="In India, Indonesia and the Philippines the IAP page opens with the annual plan selected.",
      res_zh="印度、印尼、菲律賓開啟 IAP 頁皆預設選年方案。",
      exp="In India, Indonesia and the Philippines the IAP page opens with the monthly plan selected.",
      exp_zh="這三國應預設選取月方案。",
      imgs=[("TC-111-iap-india", "xma15_india", [IAP_YEAR, IAP_MONTH]), ("TC-112-iap-indonesia", "xma15_indonesia", [IAP_YEAR, IAP_MONTH]), ("TC-113-iap-philippines", "xma15_philippines", [IAP_YEAR, IAP_MONTH])],
      links=[pm("pm-xmas-rules", "(➊ India / Indonesia / Philippines land on the monthly plan)")]),

 dict(iss="ISS-XMA-16", title="Credit page (Free): no Christmas 500-credit Special Offer; 「First Purchase Discount」 1000 +1000 shown instead",
      cls="Functional", sev=2, owner="RD", cases=["TC-124", "TC-148"], extra="O-7", rep=(2, 2), feat="Christmas Sale (Credit)",
      short="Free user: no Christmas 500-credit offer; First Purchase pack instead",
      state=state(FREE, "Taiwan"),
      note="R-047 (PM rules ➎: for a free user the Special Offer pack shows only a white 「500」 with the original price struck through and the sale price; SKU pdrm_500_credit_freeuser_christmas, ➊). PM-only: no Design frame; the sale price is not given (Q-13, open), so the Expect names the SKU, not a price. Logcat 15:02:36: the page fetched pdrm_500_credit_freeuser_christmas (NT$1,960.00) and pdrm_2000_credit_freeuser_firstpurchase (NT$5,600.00) and shows only the second. R1 held this row (signed out, sign-in 403); signed in on the Play build it is the same, so it is drafted now (TC-148, buying the pack, is Blocked by it). Side note (O-7): acda.test9 has bought 1000 and 2000 packs before, yet still gets 「First Purchase Discount」.",
      steps=[L1, "Tap the Mine tab", "Tap 「Credits」", "Tap 「Buy More」", "Swipe up to the end of the page", "Look at the credit packs"],
      res="The page shows 「First Purchase Discount」 1000 +1000 NT$5600 and no Christmas 「500」 Special Offer.",
      res_zh="Free 點數頁只有首購 1000+1000，沒有聖誕 500 點特惠。",
      exp="A Free user sees the Special Offer 「500」, original price struck, sale price beside it.",
      exp_zh="應顯示聖誕 500 點特惠（原價劃掉並顯示特價）。",
      imgs=[("TC-124-buymore", "xma16_free_buymore", [CR_TOP, CR_PACKS])],
      log=("xma16_log", LOGB, [r"15:02:36"], r"GoogleBillingWrapper: getProductDetails: \S*(christmas|firstpurchase|500_credit)\S* price:"),
      links=[pm("pm-xmas-rules", "(➎ Credit IAP: free user Special Offer pack, white 500 with the original price struck; ➊ SKU pdrm_500_credit_freeuser_christmas)")]),

 dict(iss="ISS-XMA-17", title="Mine (Pro): the VIP card has no Christmas decoration, and no JP 「Merry Christmas! Enjoy...」 banner",
      cls="UI", sev=2, owner="RD", cases=["TC-115", "TC-114", "TC-117"], extra="O-10", rep=(2, 2), feat="Christmas Sale (Mine)",
      short="Pro VIP card lacks Christmas decoration and JP 「Merry Christmas!」 banner",
      state=state(PRO, "United States and Japan"),
      note="R-043 (PM rules ➍ Paid: VIP Welcome Banner decorated, US and JP versions; PM launch board frame 「Pro+ VIP Benefits Page」 3271:3807: JP 「Merry Christmas! Enjoy...」 with 「20+ VIP features, 1000+ templates, and 250 free credits every month.」, US a decorated VIP card). On 16.9.0 (2611201) the VIP banner is the card at the top of Mine; tapping it opens nothing, so there is no separate VIP Benefits page (O-10; a 「VIP Benefits」 page existed in 15.9.0, DRA252510-0140), and TC-117 (system Back from that page) is Blocked by it. The only Christmas touches on the Pro Mine are the Santa tab icon and the 「Credit Special Offer」 pill. JP: Play Billing Lab country Japan, app 日本語.",
      steps=[L1, "Tap the 「Pro」 tab", "Look at the VIP card at the top", "Tap the VIP card"],
      res="The Pro VIP card is the plain card in English and 日本語; no decoration, no 「Merry Christmas! Enjoy...」.",
      res_zh="Pro 的 VIP 卡片英日文皆無聖誕裝飾與日本版橫幅。",
      exp="The VIP card carries Christmas decoration (US) and, in Japan, the 「Merry Christmas! Enjoy...」 banner.",
      exp_zh="VIP 卡片應有聖誕裝飾，日本版顯示 Merry Christmas 橫幅。",
      imgs=[("TC-115-vip", "xma17_vip_us", [VIP_EN]), ("TC-114-mine", "xma17_vip_jp", [VIP_JA])],
      links=[pm("pm-xmas-launch", "(「Pro+ VIP Benefits Page」 JP and US versions)", "3271-3807"), pm("pm-xmas-rules", "(➍ Paid: VIP Welcome Banner with Christmas decoration, US and JP)")]),

 dict(iss="ISS-XMA-18", title="Credit page: the top banner is the regular image collage, not the 「Christmas Special」 banner",
      cls="UI", sev=2, owner="RD", cases=["TC-120", "TC-118"], rep=(3, 3), feat="Christmas Sale (Credit)",
      short="Credit page banner is the regular collage, not 「Christmas Special」",
      state=state(PRO, "United States and Japan"),
      note="R-045 (PM rules ➎: static top banner 「Christmas Sale」, renamed 「Christmas Special」 by the 1104 update, the same in every language; Design IAP & Credit board draws it). Seen in English on the US store (TC-120, from the 「Credit Special Offer」 pill and from Mine › Credits › Buy More), in 日本語 on the Japan store (TC-118) and on the Free user's page (TC-124, Taiwan store): always the regular collage of portraits (iv_banner). TC-118's step 1 (the IAP banner on a Pro account) has no entry: a Pro account has no IAP entry (O-10); the IAP banner was seen on Free and is the Christmas art.",
      steps=[L1, "Tap the 「Pro」 tab", "Tap 「Credit Special Offer」", "Look at the top banner"],
      res="The credit page's top banner is the regular portrait collage, in English and in 日本語.",
      res_zh="點數頁頂部橫幅為一般人像拼貼圖（英日文皆同）。",
      exp="The credit page shows the static 「Christmas Special」 banner, the same in every language.",
      exp_zh="應為靜態「Christmas Special」聖誕橫幅，各語系相同。",
      imgs=[("TC-120-page", "xma18_banner_en", [CR_BANNER]), ("TC-118-credit-ja", "xma18_banner_ja", [CR_BANNER])],
      links=[pm("pm-xmas-rules", "(➎ Credit IAP: static top banner, renamed 「Christmas Special」 by 1104, not localized)"), ds("IAP & Credit", "2750-19947", "(credit purchase page, 「Christmas Special」 banner)")]),

 dict(iss="ISS-XMA-19", title="Credit page (Pro, no Auto Pass): the Auto Pass offer has no 「Subscribe for 3000 free credits!」; it reads 「Continue with the best deal」",
      cls="UI", sev=3, owner="RD", cases=["TC-125", "TC-120"], rep=(2, 2), feat="Christmas Sale (Credit)",
      short="No Auto Pass: CTA not 「Subscribe for 3000 free credits!」",
      state=state(PRO, "United States"),
      note="R-048 / R-051, ruling Q-14 (REQ-002): a user without Credit Auto Pass sees the Auto Pass credit sale, led by the Design's 「Subscribe for 3000 free credits!」, which opens the Credit Auto Pass panel. The app does lead with Auto Pass (its CTA opens the 「Credit Auto Pass (2000 Credits)」 sheet, pdrm_2000_credit_paiduser_yr_autopass, TC-127 Pass) but with the regular Auto Pass card: 「Annual Auto Pass Discount」 「1000 +1000」 「$84.99」, 「Annual top-up automatically!」 and 「Continue with the best deal」. For comparison the Free page reads 「Subscribe for 1200 free credits!」 (TC-124), so the string exists. The missing Christmas 2000 pack on the same page is ISS-XMA-21.",
      steps=[L1, "Tap the 「Pro」 tab", "Tap 「Credit Special Offer」", "Look at the top card and the buttons under the packs"],
      res="Without Auto Pass the CTA reads 「Continue with the best deal」; no 「Subscribe for 3000 free credits!」.",
      res_zh="未訂 Auto Pass 時按鈕為 Continue with the best deal。",
      exp="Without Auto Pass the page shows 「Subscribe for 3000 free credits!」, opening the Auto Pass panel.",
      exp_zh="應顯示「Subscribe for 3000 free credits!」按鈕。",
      imgs=[("TC-120-page", "xma19_autopass_cta", [CR_TOP, CR_LINE, CR_CTA])],
      links=[ds("IAP & Credit", "2750-19947", "(credit purchase page: 「Subscribe for 3000 free credits!」)"), pm("pm-xmas-credit", "(無訂閱 Credit Auto Pass version of the credit purchase page)")]),

 dict(iss="ISS-XMA-20", title="Credit page: footer 「Terms of Service | Privacy Policy」 and 「unused credits」 differ from the Design's 「Privacy Policy | Terms of Use」 and 「consumed credits」: which ships?",
      cls="UI", sev=4, owner="PM", cases=["TC-120"], rep=(3, 3), feat="Christmas Sale (Credit)",
      short="Credit page footer and expiry line differ from the Design; which ships?",
      state=state(PRO, "United States"),
      note="R-052 (Design IAP & Credit board): 「The expiration period for consumed credits is one year.」 and 「Privacy Policy」 | 「Terms of Use」. The app keeps the regular credit page's strings (「…for unused credits is one year.」, 「Terms of Service | Privacy Policy」) on every account and store. The Design's 「consumed credits」 reads as a slip (consumed credits cannot expire), and the footer is the app's standard order, so this is a decision for PM (text rule 2026-11-11: PM when the spec's own text must change), not an RD fix. Not raised from the same row: 「Each credit for about $0.04」 (Design 「$0.1」) is computed from the store price ($84.99 ÷ 2000), the Design's is a mockup value.",
      steps=[L1, "Tap the 「Pro」 tab", "Tap 「Credit Special Offer」", "Look at the two lines under the button and the links at the bottom"],
      res="The page reads 「…for unused credits is one year.」 and 「Terms of Service | Privacy Policy」.",
      res_zh="點數頁為 unused credits 與 Terms of Service | Privacy Policy。",
      exp="PM decides: the Design's 「consumed credits」 and 「Privacy Policy | Terms of Use」, or the app's text.",
      exp_zh="請 PM 決定到期說明與頁尾文字。",
      imgs=[("TC-120-page", "xma20_footer", [CR_EXP, CR_FOOT])],
      links=[ds("IAP & Credit", "2750-19947", "(credit purchase page: expiry line and 「Privacy Policy」 | 「Terms of Use」)")]),

 dict(iss="ISS-XMA-21", title="Credit page (Pro): the Christmas 2000-credit pack is never offered, with or without Auto Pass, though its SKU is fetched",
      cls="Functional", sev=2, owner="RD", cases=["TC-126", "TC-122", "TC-149"], rep=(2, 2), feat="Christmas Sale (Credit)",
      short="Pro: Christmas 2000-credit pack never offered, with or without Auto Pass",
      state=state(PRO_AP, "Taiwan (also United States without Auto Pass)"),
      note="R-046 / R-048, ruling Q-14 (REQ-002): for a paid user the Special Offer pack 「1000+1000」 with the CTA 「Get 2000 credits for <price>」 buys pdrm_2000_credit_paiduser_christmas (PM rules ➎, Design IAP & Credit board, US mockup $166.99); a user with Auto Pass sees 「Auto Pass activated」 and the 2000-pack sale. With Auto Pass (bought 15:25, TC-150) the balance line does read 「Auto Pass activated」, but only the six regular member packs show (TC-126). Without Auto Pass (US store, TC-122) the special card is the Auto Pass card (ISS-XMA-19) and selecting the regular 2000 pack gives 「Get 2000 Credits for $99.99」 (pdrm_2000_credits_paiduser). Logcat: pdrm_2000_credit_paiduser_christmas is fetched every time (US $84.99, JP ¥14,300, TW NT$2,740.00) and never shown, so TC-149 (buying it) is Blocked. The store price ($84.99) is not the mockup's $166.99; the store sets it.",
      steps=[L1, "Tap the 「Pro」 tab", "Tap 「Credit Special Offer」", "Look at the balance line and the credit packs"],
      res="With 「Auto Pass activated」 only the regular packs show; no 「1000+1000」 Christmas pack, though fetched.",
      res_zh="已訂 Auto Pass 仍只有一般點數包，沒有聖誕 2000 點特惠。",
      exp="A Pro user gets the Christmas 「1000+1000」 pack with 「Get 2000 credits for <price>」.",
      exp_zh="Pro 應看到聖誕 1000+1000 特惠包與購買按鈕。",
      imgs=[("TC-126-page", "xma21_with_autopass", [(70, 410, 860, 515), (55, 535, 1025, 1080), CR_CTA]), ("TC-122-2000", "xma21_without_autopass", [CR_TOP, (720, 1045, 1015, 1300), CR_CTA])],
      log=("xma21_log", LOGC, [r"15:17:16\.31", r"15:26:12\.35", r"15:25:5[25]"], r"(GoogleBillingWrapper: getProductDetails: pdrm_2000_credit_paiduser_(christmas|yr_autopass) price:|totalRemain=)"),
      links=[pm("pm-xmas-rules", "(➎ Credit IAP: paid Special Offer pack 1000+1000; Auto Pass subscribers see the 2000-pack sale)"), ds("IAP & Credit", "2750-19947", "(credit purchase page: Special Offer 1000+1000, 「Get 2000 credits for $166.99」)")]),

 dict(iss="ISS-XMA-22", title="IAP (Philippines, Taiwan): the Christmas monthly plan is not cheaper than the regular monthly plan; is 15% off meant for every store?",
      cls="Functional", sev=3, owner="PM", cases=["TC-113", "TC-105"], extra="O-2, O-6", rep=(2, 2), feat="Christmas Sale (IAP)",
      short="Philippines: Christmas monthly ₱485 costs more than the regular ₱469",
      state=state(FREE, "Philippines and Taiwan"),
      note="PM rules ➊: the Android monthly plan is 15% off (monthlysubscription_christmas_2611). Store prices read by the app (logcat): Philippines campaign monthly ₱485.00 vs the regular monthly_sub_usd6.99_202209 ₱469.00 (the campaign is 3% dearer); Taiwan both NT$240.00 (the SKU 表 itself sets the campaign monthly to NT$240); US $6.99 vs $7.99 (12.5% off). The SKU 表 lists no regular monthly price to check against. A store-price question the run cannot settle, so filed to PM (rule 2026-11-11): should the campaign monthly be discounted in every store, and should the Play prices for the Philippines and Taiwan change? TC-113's own failure (annual card selected) is ISS-XMA-15; TC-105 passed (the Play sheet is the campaign SKU).",
      steps=pbl("Philippines") + ["Tap the Mine tab", "Tap 「Claim Holiday Deal」", "Look at the monthly plan price"],
      res="Philippines: the Christmas monthly is ₱485, the regular monthly ₱469; Taiwan: both NT$240.",
      res_zh="菲律賓聖誕月訂比一般貴；台灣兩者同價。",
      exp="PM decides whether the Christmas monthly must be cheaper in every store (15% off) and sets the prices.",
      exp_zh="請 PM 決定各商店月訂是否都要打折並調整價格。",
      imgs=[("TC-113-iap-philippines", "xma22_philippines_monthly", [IAP_MONTH])],
      log=("xma22_log", None, None, None),
      links=[pm("pm-xmas-rules", "(➊ Android Monthly 15% off, SKU monthlysubscription_christmas_2611; linked SKU 表)")]),

 dict(iss="ISS-XMA-23", title="Mine (Pro, 日本語): the top pill stays English 「Credit Special Offer」; the spec gives no translation",
      cls="UI", sev=3, owner="PM", cases=["TC-114"], extra="O-9", rep=(1, 1), feat="Christmas Sale (Mine)",
      short="[JPN] Pro top pill stays English 「Credit Special Offer」",
      state=state(PRO, "Japan"),
      note="R-044 (Design Launcher & dialog board, mine_vip: 「Credit Special Offer」 pill with a gift icon, ruling Q-12). The 多國文案 sheet has no row for the pill, so no translation exists in the spec (text rule 2026-11-11: PM supplies it); plainly wrong on screen (English in a Japanese Mine), so filed, not held. Only 日本語 was run on the Pro account; other languages likely the same. Same class as R1 ISS-XMA-02.",
      steps=["Set the app language to 日本語", L1, "Tap the 「Pro」 tab", "Look at the pill at the top left"],
      res="In 日本語 the Pro Mine's top pill reads 「Credit Special Offer」 in English.",
      res_zh="日文介面下 Pro Mine 頁膠囊仍為英文。",
      exp="PM supplies 「Credit Special Offer」 for each app language; the pill shows it translated.",
      exp_zh="請 PM 提供各語系翻譯。",
      imgs=[("TC-114-mine", "xma23_pill_jp", [PILL])],
      links=[ds("Launcher & dialog", "2772-10246", "(mine_vip: 「Credit Special Offer」 pill)")]),
]

# PH / TW regular vs campaign monthly prices: lines picked by exact text, both logs
PH_TW = [(LOGA, r"14:58:26", r"getProductDetails: (monthlysubscription_christmas_2611|monthly_sub_usd6\.99_202209) price:"),
         (LOGB, r"15:03:15", r"getProductDetails: (monthlysubscription_christmas_2611|monthly_sub_usd6\.99_202209) price:")]

ADDITIONS = [
 ("ISS-XMA-06 (R1)", "TC-112 (Indonesia) and TC-101 (US), O-1", "New evidence, Play test build, signed in: the app truncates. Indonesia IDR 590,000 / IDR 119,000 × 12 = 58.68% shows 「58% OFF」 (rounded 59); Taiwan 57.99% → 57 (R1). US 45.17% → 45 (TC-101 Pass). Add to ISS-XMA-06 the Indonesia screenshot (runs/2026-11-23-r1r-recheck/screenshots/TC-112-iap-indonesia.png) and that the % is computed, not fixed."),
 ("ISS-XMA-12 (R1)", "TC-100 (US store, signed in)", "Same bug on the US store, signed in on the Play test build: tag 「Special Offer」 with a Santa hat, 「45% OFF」 not 「Save 45%」, monthly 「$6.99/Month」 with no struck original although the page fetched the regular $7.99; also CTA 「Continue」 and the 「No Watermark」 carousel (left to the reviewer in R1). Add TC-100's screenshot (screenshots/TC-100-iap-us.png); not a new entry."),
 ("R1 held TC-124", "TC-124, TC-148", "R1 held the missing Christmas 500 pack until a signed-in recheck; signed in it is the same, so it is now drafted as ISS-XMA-16 (no R1 entry to add to)."),
]

NOT_RAISED = [
 ("O-3", "Play test build already signed in as acda.test9; interstitial still unused today", "Run state, no finding."),
 ("O-4", "Play Billing Lab terms accepted; country suggestions not in the accessibility tree", "Tooling note."),
 ("O-5", "Play sheet SKU only visible in dumpsys activity iabData", "Tooling note."),
 ("O-8", "ToS / Privacy Policy open the Traditional Chinese pages with the Play country United States", "Spec silent (R1 O-1, not raised); not the Play country; report only."),
 ("O-11", "Purchases made: Christmas annual (15:13) and Credit Auto Pass (15:25); account Pro + Auto Pass, 5510 credits", "Account state left for the next run."),
]
FOLDED = {"O-1": "1. ISS-XMA-13; addition to R1 ISS-XMA-06", "O-2": "10. ISS-XMA-22", "O-6": "10. ISS-XMA-22", "O-7": "4. ISS-XMA-16",
          "O-9": "11. ISS-XMA-23", "O-10": "5. ISS-XMA-17"}
OBS_ALL = [f"O-{i}" for i in range(1, 12)]
ROW_ADDITIONS = {"TC-100": "addition to R1 ISS-XMA-12", "TC-112": "3. ISS-XMA-15; addition to R1 ISS-XMA-06"}

DUPS_TXT = [
 "No entry repeats an Android ticket. Searched the Android pool (PowerDirector Mobile for Android) for Christmas, Credit Special Offer, Auto Pass, VIP, Benefits, Credit Pack, Credit IAP, Credit System, Credit, First Purchase, cancel, Monthly, Special Offer, Holiday, Interstitial, banner, Save, Mine, IAP, Subscription, Purchase, Pro; read every 16.9.0 hit: none is about the campaign, the credit page or the IAP page.",
 "Related, closed, not the same bug: DRA252510-0140 (15.9.0 [MUI] VIP Benefits: page content not localized; shows a VIP Benefits page existed then, ISS-XMA-17); DRA262604-0081 (16.4.0 Pro account shows 「First Purchase Discount」 after subscribing Credit Auto Pass, Close; context for ISS-XMA-16's side note); DRA262605-0051 (16.4.0 Auto Pass default landing pack, Close).",
 "Against the R1 batch (2026-11-23-r1, not filed): TC-100 = ISS-XMA-12 and TC-112's truncation = ISS-XMA-06 (listed as additions, not drafted); every other entry is a different screen or rule.",
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
        if any(re.search(t, line[:30]) for t in times) and re.search(pat, line):
            msg = line[19:].strip()
            key = line[11:19] + re.sub(r"^\S+\s+\d+\s+\d+\s+", "", msg)
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
    obs = [o for o in OBS_ALL if re.search(rf"^- \*\*{o}\*\*", obs_file, re.M)]
    if len(obs) != 11:
        sys.exit(f"observations: {obs}")
    MAP = {}
    for n, e in enumerate(E, 1):
        for c in e["cases"]:
            MAP.setdefault(c, []).append(f"{n}. {e['iss']}")
    for k, v in ROW_ADDITIONS.items():
        MAP.setdefault(k, []).append(v)
    for k, _, _ in NOT_RAISED:
        MAP.setdefault(k, []).append("not raised")
    for k, v in FOLDED.items():
        MAP.setdefault(k, []).append(f"folded into {v}")
    MAP = {k: "; ".join(dict.fromkeys(x for s in v for x in s.split("; "))) for k, v in MAP.items()}
    need = fails + dblk + obs
    missing = [k for k in need if k not in MAP]
    extra = [k for k in MAP if k not in need and disp.get(k, ("",))[0] != "Pass"]
    if missing or extra:
        sys.exit(f"unmapped: {missing}; not in run: {extra}")

    img_root = f"{OUT}/{NAME}_images"
    if os.path.isdir(img_root):
        shutil.rmtree(img_root)
    os.makedirs(img_root)
    L = []
    w = L.append
    w(f"# Christmas & New Year Sales (Android) — eBug drafts, round R1r (recheck of the rows R1 skipped, Play test build), PDR-A {V} build {B}")
    w("")
    w(f"**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-23-r1r-recheck/` — round R1r of draft `drafts/20261120-165128` (table v2, {len(rows)} rows R1 skipped), 2026-11-23 14:50 → 15:27, on {DEVICE[8:]} (adb R5CN8194YSN) through Appium / UiAutomator2, build 16.9.0.{B} downloaded from the Play Store (test track; the adb install of R1 is refused by the new 「Unofficial Version」 purchase check, REQ-005), Stage server with the RD test date inside the Christmas window, acda.test9 signed in (Free, then Pro after TC-147 and Credit Auto Pass after TC-150), Play country set with Play Billing Lab (US, India, Indonesia, Philippines, Japan; Taiwan otherwise). Tally: " + ", ".join(f"{v} {k}" for k, v in tally.items()) + ".")
    w("")
    w("**Status:** nothing filed, uploaded or commented. Second batch of this feature; the R1 batch (`ebugs/2026-11-23-r1/`, ISS-XMA-01…12) is not filed either, so this batch continues its numbering and both go to the reviewer together. `ebug-defaults.ts`: no filed batch, so Creator, TRCode, source tag and method are for the reviewer. Dedupe: read-only eBug Search, Android pool only (per OS): no Android ticket matches an entry (`dedupe.txt`); against the R1 drafts, two findings are the same bugs as R1 entries and are listed under *Cited — additions to R1 entries* instead of drafted.")
    w("")
    w("Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` / `[AIAgent][UI]` owner RD for defects; text the spec must supply or change and open questions to PM (BugBelong PM), 2026-11-11. Each entry's Note names its account and Play store. Severity is proposed.")
    w("")
    owners = ", ".join(f"{sum(1 for e in E if e['owner'] == o and e['cls'] == c)} {o} {c}" for o, c in (("RD", "Functional"), ("RD", "UI"), ("PM", "Functional"), ("PM", "UI")) if any(e['owner'] == o and e['cls'] == c for e in E))
    w(f"**What is drafted:** {len(E)} entries (ISS-XMA-13…{12 + len(E)}): {owners}. Additions to R1 entries: ISS-XMA-06 (TC-112 truncation) and ISS-XMA-12 (TC-100, US store); R1's held TC-124 is drafted here as ISS-XMA-16.")
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
            slug, path, times, pat = e["log"]
            if path is None:
                lines = []
                for pth, t, pt in PH_TW:
                    lines += excerpt(pth, [t], pt)
            else:
                lines = excerpt(path, times, pat)
            if not lines:
                sys.exit(f"{e['iss']}: empty log excerpt")
            txt = "\n".join(lines) + "\n"
            if re.search(r"(?i)bearer|authorization|token=|signature=", txt):
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
        for label, url in e["links"]:
            w(label); w(url)
        w("<Claude Reviewed>"); w("```"); w("")
        w(f"**Images:** `{NAME}_images/{folder}/`"); w("")

    w("---"); w("")
    w("## Cited — additions to R1 entries (same bug, new evidence; not drafted again)")
    w("")
    w("| R1 entry | From R1r | What to add |")
    w("|---|---|---|")
    for a, b, c in ADDITIONS:
        w(f"| {a} | {b} | {c} |")
    w("")
    w("## Not raised (for the record)")
    w("")
    w("| Item | What was seen | Why not raised |")
    w("|---|---|---|")
    for k, a, b in NOT_RAISED:
        w(f"| {k} | {a} | {b} |")
    blocked = [r for r in rows if r["Result"] == "Blocked"]
    tdata = [r["ID"] for r in blocked if r["Disposition"] != "defect"]
    w(f"| Blocked test-data ({len(tdata)}) | {', '.join(tdata)} | No verdict: low-balance account needed (TC-132–135, 141, 142), RD stage date for the New Year window (TC-129, TC-151 step 3); reasons in report.md and blocked-reasons.json. |")
    w("")
    w("## Reconciliation against the run")
    w("")
    w(f"{len(fails)} Fail (all defect), {len(blocked)} Blocked ({len(dblk)} defect, {len(tdata)} test-data), {len(obs)} observations (O-1 … O-11).")
    w("")
    w("### Row-by-row map")
    w("")
    w("| Item | Result | Disposition | Became |")
    w("|---|---|---|---|")
    for k in fails + dblk + [k for k in MAP if disp.get(k, ("",))[0] == "Pass"]:
        w(f"| {k} | {disp[k][0]} | {disp[k][1] or '—'} | {MAP[k]} |")
    for k in obs:
        w(f"| {k} | observation | — | {MAP[k]} |")
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
    w("By severity: " + ", ".join(f"**{i}**" for s in (1, 2, 3, 4) for i, e in enumerate(E, 1) if e["sev"] == s) + ". File with the R1 batch, after its decisions; nothing is filed until the review page's decisions come back.")
    w("")
    open(f"{OUT}/{NAME}.md", "w", encoding="utf-8").write("\n".join(L))
    D = ["# Dedupe — Christmas & New Year Sales Android R1r (16.9.0.2611201), read-only eBug Search, PowerDirector Mobile for Android only", ""] + DUPS_TXT
    open(f"{OUT}/dedupe.txt", "w", encoding="utf-8").write("\n".join(D) + "\n")
    review = {"lede": "Second batch of this feature, from the R1r recheck on the Play test build (signed in, Play Billing Lab countries, Pro and Auto Pass purchases on the test track). It continues the unfiled R1 batch (ISS-XMA-01…12, ebugs/2026-11-23-r1): review both together. Two findings are the same bugs as R1 entries and are listed below as additions (ISS-XMA-06: the app truncates, Indonesia 58.68% → 58; ISS-XMA-12: same card on the US store); R1's held TC-124 is now ISS-XMA-16.",
              "why": {"ISS-XMA-13": "US store only: the interstitial and the IAP page disagree (52% vs 45%).",
                      "ISS-XMA-16": "R1 held this until a signed-in recheck; same signed in.",
                      "ISS-XMA-20": "Design's 「consumed credits」 looks like a slip: PM decides, not RD.",
                      "ISS-XMA-22": "Store-price question for PM (no defect in the app's code).",
                      "ISS-XMA-23": "No translation exists in the spec: PM supplies it."}}
    json.dump(review, open(f"{OUT}/review.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {len(E)} entries → {OUT}/{NAME}.md")


if __name__ == "__main__":
    main()
