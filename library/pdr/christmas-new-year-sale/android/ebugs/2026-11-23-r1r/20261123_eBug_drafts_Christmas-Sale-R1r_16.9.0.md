# Christmas & New Year Sales (Android) — eBug drafts, round R1r (recheck of the rows R1 skipped, Play test build), PDR-A 16.9.0 build 2611201

**Filed by:** ANGOL_HUANG on 2026-11-23 — API, TR261123-0015, 16.9.0 build 2611201: 10 filed (DRA262611P0254–P0263), ISS-XMA-20 held; see `filed_bugcodes.md`.

**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-23-r1r-recheck/` — round R1r of draft `drafts/20261120-165128` (table v2, 35 rows R1 skipped), 2026-11-23 14:50 → 15:27, on Samsung Galaxy A51 SM-A516B / Android 13 (adb R5CN8194YSN) through Appium / UiAutomator2, build 16.9.0.2611201 downloaded from the Play Store (test track; the adb install of R1 is refused by the new 「Unofficial Version」 purchase check, REQ-005), Stage server with the RD test date inside the Christmas window, acda.test9 signed in (Free, then Pro after TC-147 and Credit Auto Pass after TC-150), Play country set with Play Billing Lab (US, India, Indonesia, Philippines, Japan; Taiwan otherwise). Tally: 14 Fail, 10 Pass, 11 Blocked.

**Status:** nothing filed, uploaded or commented. Second batch of this feature; the R1 batch (`ebugs/2026-11-23-r1/`, ISS-XMA-01…12) is not filed either, so this batch continues its numbering and both go to the reviewer together. `ebug-defaults.ts`: no filed batch, so Creator, TRCode, source tag and method are for the reviewer. Dedupe: read-only eBug Search, Android pool only (per OS): no Android ticket matches an entry (`dedupe.txt`); against the R1 drafts, two findings are the same bugs as R1 entries and are listed under *Cited — additions to R1 entries* instead of drafted.

Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` / `[AIAgent][UI]` owner RD for defects; text the spec must supply or change and open questions to PM (BugBelong PM), 2026-11-11. Each entry's Note names its account and Play store. Severity is proposed.

**What is drafted:** 11 entries (ISS-XMA-13…23): 4 RD Functional, 4 RD UI, 1 PM Functional, 2 PM UI. Additions to R1 entries: ISS-XMA-06 (TC-112 truncation) and ISS-XMA-12 (TC-100, US store); R1's held TC-124 is drafted here as ISS-XMA-16.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.

---

## 1. ISS-XMA-13 — Interstitial (US store): 「SAVE 52%」 and 「vs. paying $7.99/mo × 12」 come from the regular monthly plan, not the campaign $6.99  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-013, TC-101, O-1  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-006 / R-018 / R-036, ruling Q-3 (REQ-002): the interstitial's % and 「vs. paying …/mo」 are computed from the campaign SKUs' store prices (annualsubscription_christmas_2611 $45.99, monthlysubscription_christmas_2611 $6.99 → 45%). Logcat 14:52:28: the interstitial asked Play only for monthly_sub_usd6.99_202209 ($7.99, the regular monthly) and the Christmas annual: ($7.99×12 − $45.99) ÷ ($7.99×12) = 52.03% → 52. The IAP page a minute later (14:53:30) read the campaign monthly $6.99 and shows 45% (TC-101 Pass), so the two screens disagree. On the Taiwan store both monthly SKUs cost NT$240, which hid this in R1. Rounding vs truncation is a separate entry (R1 ISS-XMA-06): 52.03 gives 52 either way. Precondition: first launch of the day (the interstitial is daily).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] Christmas Sale (Interstitial): US store: SAVE 52% from the regular $7.99 monthly, not $6.99 (45%)
```

**Description:**

```
Repro Steps:
1. Set the Play country to United States in Play Billing Lab
2. Force-stop the APP
3. Launch the APP
4. Tap 「Continue」 on the AI Mini Drama intro
5. Look at the 「SAVE」 line and the 「vs. paying」 line
6. Check the result

Result:
The interstitial reads 「SAVE 52%」 「vs. paying $7.99/mo × 12」 (regular monthly); the IAP page shows $6.99 and 45%.
摘要：插頁以一般月訂 $7.99 算出 52%，IAP 頁為 $6.99、45%。
{16.9.0_xma13_interstitial_us.jpg} {16.9.0_xma13_iap_us_45.jpg} {16.9.0_xma13_log.txt}

Expect Result:
The interstitial uses the campaign monthly $6.99: 「SAVE 45%」 「vs. paying $6.99/mo × 12」.
摘要：插頁應以活動月訂 $6.99 計算：SAVE 45%。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Free account, signed in; Play store United States (Play Billing Lab)
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (➊ monthly plan SKU monthlysubscription_christmas_2611, SKU 表 US $6.99; ➍ formula 年價格 vs 月價格*12個月的價差%) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Interstitial board (「SAVE」 「<xx>」 「%」, 「vs. paying <monthly price>/mo × 12」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19946
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/01_ISS-XMA-13/`

---

## 2. ISS-XMA-14 — Interstitial: trial terms read 「until cancelled」, the spec 「until canceled」  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Report step:** TC-014  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-020 (Design and PM 1104 interstitial text): 「…Subscription renews automatically until canceled. Cancel in Google Play…」. The annual price in the terms matches the big price ($45.99), so that half of TC-014 passes; only the spelling differs. Same on the Taiwan store in R1. The spec states the string and the app shows another, so RD (text rule 2026-11-11). The IAP page's own terms use 「cancelled」 too (not part of this spec text).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Interstitial): Trial terms read 「until cancelled」, not 「until canceled」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap 「Continue」 on the AI Mini Drama intro
3. Look at the trial terms under the yellow button
4. Check the result

Result:
The trial terms use the British spelling with a double 「l」, not the spec's US spelling.
摘要：試用條款拼字為英式（雙 l），與規格美式拼字不同。
{16.9.0_xma14_terms.jpg}

Expect Result:
The terms read 「…Subscription renews automatically until canceled. …」 as the spec states.
摘要：條款應為規格文字「until canceled」。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Free account, signed in; Play store United States (Play Billing Lab)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Interstitial board (trial terms 「…renews automatically until canceled…」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19946
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/02_ISS-XMA-14/`

---

## 3. ISS-XMA-15 — IAP (India, Indonesia, Philippines): the page opens on the annual plan, not the monthly plan  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-111, TC-112, TC-113  ·  **Reproduce:** 3/3  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-007 (PM rules ➊: India, Indonesia and the Philippines keep the default landing on the monthly plan), ruling Q-17 (REQ-002): testers set the country with Play Billing Lab. The store did switch (logcat: annualsubscription_christmas_2611 ₹3,850 / IDR 590,000 / ₱2,500; monthlysubscription_christmas_2611 ₹750 / IDR 119,000 / ₱485), yet iap_radioBtn_yearly is checked when the page opens in all three. The phone's system locale is en-US and its SIM/network Taiwan; if the app picks the landing from something other than the Play country, RD can say so (Q-17 names Play Billing Lab as the test method).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] Christmas Sale (IAP): India, Indonesia, Philippines: IAP opens on the annual plan, not monthly
```

**Description:**

```
Repro Steps:
1. Set the Play country to India in Play Billing Lab
2. Force-stop the APP
3. Launch the APP
4. Tap the Mine tab
5. Tap 「Claim Holiday Deal」
6. Look at which plan card is selected
7. Check the result

Result:
In India, Indonesia and the Philippines the IAP page opens with the annual plan selected.
摘要：印度、印尼、菲律賓開啟 IAP 頁皆預設選年方案。
{16.9.0_xma15_india.jpg} {16.9.0_xma15_indonesia.jpg} {16.9.0_xma15_philippines.jpg}

Expect Result:
In India, Indonesia and the Philippines the IAP page opens with the monthly plan selected.
摘要：這三國應預設選取月方案。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Free account, signed in; Play store India, Indonesia, Philippines (Play Billing Lab)
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (➊ India / Indonesia / Philippines land on the monthly plan) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/03_ISS-XMA-15/`

---

## 4. ISS-XMA-16 — Credit page (Free): no Christmas 500-credit Special Offer; 「First Purchase Discount」 1000 +1000 shown instead  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-124, TC-148, O-7  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-047 (PM rules ➎: for a free user the Special Offer pack shows only a white 「500」 with the original price struck through and the sale price; SKU pdrm_500_credit_freeuser_christmas, ➊). PM-only: no Design frame; the sale price is not given (Q-13, open), so the Expect names the SKU, not a price. Logcat 15:02:36: the page fetched pdrm_500_credit_freeuser_christmas (NT$1,960.00) and pdrm_2000_credit_freeuser_firstpurchase (NT$5,600.00) and shows only the second. R1 held this row (signed out, sign-in 403); signed in on the Play build it is the same, so it is drafted now (TC-148, buying the pack, is Blocked by it). Side note (O-7): acda.test9 has bought 1000 and 2000 packs before, yet still gets 「First Purchase Discount」.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] Christmas Sale (Credit): Free user: no Christmas 500-credit offer; First Purchase pack instead
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap the Mine tab
3. Tap 「Credits」
4. Tap 「Buy More」
5. Swipe up to the end of the page
6. Look at the credit packs
7. Check the result

Result:
The page shows 「First Purchase Discount」 1000 +1000 NT$5600 and no Christmas 「500」 Special Offer.
摘要：Free 點數頁只有首購 1000+1000，沒有聖誕 500 點特惠。
{16.9.0_xma16_free_buymore.jpg} {16.9.0_xma16_log.txt}

Expect Result:
A Free user sees the Special Offer 「500」, original price struck, sale price beside it.
摘要：應顯示聖誕 500 點特惠（原價劃掉並顯示特價）。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Free account, signed in; Play store Taiwan (Play Billing Lab)
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (➎ Credit IAP: free user Special Offer pack, white 500 with the original price struck; ➊ SKU pdrm_500_credit_freeuser_christmas) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/04_ISS-XMA-16/`

---

## 5. ISS-XMA-17 — Mine (Pro): the VIP card has no Christmas decoration, and no JP 「Merry Christmas! Enjoy...」 banner  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-115, TC-114, TC-117, O-10  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-043 (PM rules ➍ Paid: VIP Welcome Banner decorated, US and JP versions; PM launch board frame 「Pro+ VIP Benefits Page」 3271:3807: JP 「Merry Christmas! Enjoy...」 with 「20+ VIP features, 1000+ templates, and 250 free credits every month.」, US a decorated VIP card). On 16.9.0 (2611201) the VIP banner is the card at the top of Mine; tapping it opens nothing, so there is no separate VIP Benefits page (O-10; a 「VIP Benefits」 page existed in 15.9.0, DRA252510-0140), and TC-117 (system Back from that page) is Blocked by it. The only Christmas touches on the Pro Mine are the Santa tab icon and the 「Credit Special Offer」 pill. JP: Play Billing Lab country Japan, app 日本語.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Mine): Pro VIP card lacks Christmas decoration and JP 「Merry Christmas!」 banner
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap the 「Pro」 tab
3. Look at the VIP card at the top
4. Tap the VIP card
5. Check the result

Result:
The Pro VIP card is the plain card in English and 日本語; no decoration, no 「Merry Christmas! Enjoy...」.
摘要：Pro 的 VIP 卡片英日文皆無聖誕裝飾與日本版橫幅。
{16.9.0_xma17_vip_us.jpg} {16.9.0_xma17_vip_jp.jpg}

Expect Result:
The VIP card carries Christmas decoration (US) and, in Japan, the 「Merry Christmas! Enjoy...」 banner.
摘要：VIP 卡片應有聖誕裝飾，日本版顯示 Merry Christmas 橫幅。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Pro account (Christmas annual plan), signed in, no Credit Auto Pass; Play store United States and Japan (Play Billing Lab)
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-launch board (「Pro+ VIP Benefits Page」 JP and US versions) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-3807
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (➍ Paid: VIP Welcome Banner with Christmas decoration, US and JP) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/05_ISS-XMA-17/`

---

## 6. ISS-XMA-18 — Credit page: the top banner is the regular image collage, not the 「Christmas Special」 banner  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-120, TC-118  ·  **Reproduce:** 3/3  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-045 (PM rules ➎: static top banner 「Christmas Sale」, renamed 「Christmas Special」 by the 1104 update, the same in every language; Design IAP & Credit board draws it). Seen in English on the US store (TC-120, from the 「Credit Special Offer」 pill and from Mine › Credits › Buy More), in 日本語 on the Japan store (TC-118) and on the Free user's page (TC-124, Taiwan store): always the regular collage of portraits (iv_banner). TC-118's step 1 (the IAP banner on a Pro account) has no entry: a Pro account has no IAP entry (O-10); the IAP banner was seen on Free and is the Christmas art.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Credit): Credit page banner is the regular collage, not 「Christmas Special」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap the 「Pro」 tab
3. Tap 「Credit Special Offer」
4. Look at the top banner
5. Check the result

Result:
The credit page's top banner is the regular portrait collage, in English and in 日本語.
摘要：點數頁頂部橫幅為一般人像拼貼圖（英日文皆同）。
{16.9.0_xma18_banner_en.jpg} {16.9.0_xma18_banner_ja.jpg}

Expect Result:
The credit page shows the static 「Christmas Special」 banner, the same in every language.
摘要：應為靜態「Christmas Special」聖誕橫幅，各語系相同。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Pro account (Christmas annual plan), signed in, no Credit Auto Pass; Play store United States and Japan (Play Billing Lab)
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (➎ Credit IAP: static top banner, renamed 「Christmas Special」 by 1104, not localized) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), IAP & Credit board (credit purchase page, 「Christmas Special」 banner) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19947
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/06_ISS-XMA-18/`

---

## 7. ISS-XMA-19 — Credit page (Pro, no Auto Pass): the Auto Pass offer has no 「Subscribe for 3000 free credits!」; it reads 「Continue with the best deal」  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-125, TC-120  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-048 / R-051, ruling Q-14 (REQ-002): a user without Credit Auto Pass sees the Auto Pass credit sale, led by the Design's 「Subscribe for 3000 free credits!」, which opens the Credit Auto Pass panel. The app does lead with Auto Pass (its CTA opens the 「Credit Auto Pass (2000 Credits)」 sheet, pdrm_2000_credit_paiduser_yr_autopass, TC-127 Pass) but with the regular Auto Pass card: 「Annual Auto Pass Discount」 「1000 +1000」 「$84.99」, 「Annual top-up automatically!」 and 「Continue with the best deal」. For comparison the Free page reads 「Subscribe for 1200 free credits!」 (TC-124), so the string exists. The missing Christmas 2000 pack on the same page is ISS-XMA-21.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Credit): No Auto Pass: CTA not 「Subscribe for 3000 free credits!」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap the 「Pro」 tab
3. Tap 「Credit Special Offer」
4. Look at the top card and the buttons under the packs
5. Check the result

Result:
Without Auto Pass the CTA reads 「Continue with the best deal」; no 「Subscribe for 3000 free credits!」.
摘要：未訂 Auto Pass 時按鈕為 Continue with the best deal。
{16.9.0_xma19_autopass_cta.jpg}

Expect Result:
Without Auto Pass the page shows 「Subscribe for 3000 free credits!」, opening the Auto Pass panel.
摘要：應顯示「Subscribe for 3000 free credits!」按鈕。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Pro account (Christmas annual plan), signed in, no Credit Auto Pass; Play store United States (Play Billing Lab)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), IAP & Credit board (credit purchase page: 「Subscribe for 3000 free credits!」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19947
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-credit board (無訂閱 Credit Auto Pass version of the credit purchase page) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/07_ISS-XMA-19/`

---

## 8. ISS-XMA-20 — Credit page: footer 「Terms of Service | Privacy Policy」 and 「unused credits」 differ from the Design's 「Privacy Policy | Terms of Use」 and 「consumed credits」: which ships?  ·  Class: UI  ·  Severity: S4  ·  Owner: PM

**Report step:** TC-120  ·  **Reproduce:** 3/3  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-052 (Design IAP & Credit board): 「The expiration period for consumed credits is one year.」 and 「Privacy Policy」 | 「Terms of Use」. The app keeps the regular credit page's strings (「…for unused credits is one year.」, 「Terms of Service | Privacy Policy」) on every account and store. The Design's 「consumed credits」 reads as a slip (consumed credits cannot expire), and the footer is the app's standard order, so this is a decision for PM (text rule 2026-11-11: PM when the spec's own text must change), not an RD fix. Not raised from the same row: 「Each credit for about $0.04」 (Design 「$0.1」) is computed from the store price ($84.99 ÷ 2000), the Design's is a mockup value.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Credit): Credit page footer and expiry line differ from the Design; which ships?
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap the 「Pro」 tab
3. Tap 「Credit Special Offer」
4. Look at the two lines under the button and the links at the bottom
5. Check the result

Result:
The page reads 「…for unused credits is one year.」 and 「Terms of Service | Privacy Policy」.
摘要：點數頁為 unused credits 與 Terms of Service | Privacy Policy。
{16.9.0_xma20_footer.jpg}

Expect Result:
PM decides: the Design's 「consumed credits」 and 「Privacy Policy | Terms of Use」, or the app's text.
摘要：請 PM 決定到期說明與頁尾文字。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Pro account (Christmas annual plan), signed in, no Credit Auto Pass; Play store United States (Play Billing Lab)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), IAP & Credit board (credit purchase page: expiry line and 「Privacy Policy」 | 「Terms of Use」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19947
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/08_ISS-XMA-20/`

---

## 9. ISS-XMA-21 — Credit page (Pro): the Christmas 2000-credit pack is never offered, with or without Auto Pass, though its SKU is fetched  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-126, TC-122, TC-149  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-046 / R-048, ruling Q-14 (REQ-002): for a paid user the Special Offer pack 「1000+1000」 with the CTA 「Get 2000 credits for <price>」 buys pdrm_2000_credit_paiduser_christmas (PM rules ➎, Design IAP & Credit board, US mockup $166.99); a user with Auto Pass sees 「Auto Pass activated」 and the 2000-pack sale. With Auto Pass (bought 15:25, TC-150) the balance line does read 「Auto Pass activated」, but only the six regular member packs show (TC-126). Without Auto Pass (US store, TC-122) the special card is the Auto Pass card (ISS-XMA-19) and selecting the regular 2000 pack gives 「Get 2000 Credits for $99.99」 (pdrm_2000_credits_paiduser). Logcat: pdrm_2000_credit_paiduser_christmas is fetched every time (US $84.99, JP ¥14,300, TW NT$2,740.00) and never shown, so TC-149 (buying it) is Blocked. The store price ($84.99) is not the mockup's $166.99; the store sets it.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] Christmas Sale (Credit): Pro: Christmas 2000-credit pack never offered, with or without Auto Pass
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap the 「Pro」 tab
3. Tap 「Credit Special Offer」
4. Look at the balance line and the credit packs
5. Check the result

Result:
With 「Auto Pass activated」 only the regular packs show; no 「1000+1000」 Christmas pack, though fetched.
摘要：已訂 Auto Pass 仍只有一般點數包，沒有聖誕 2000 點特惠。
{16.9.0_xma21_with_autopass.jpg} {16.9.0_xma21_without_autopass.jpg} {16.9.0_xma21_log.txt}

Expect Result:
A Pro user gets the Christmas 「1000+1000」 pack with 「Get 2000 credits for <price>」.
摘要：Pro 應看到聖誕 1000+1000 特惠包與購買按鈕。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Pro account with Credit Auto Pass, signed in; Play store Taiwan (also United States without Auto Pass) (Play Billing Lab)
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (➎ Credit IAP: paid Special Offer pack 1000+1000; Auto Pass subscribers see the 2000-pack sale) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), IAP & Credit board (credit purchase page: Special Offer 1000+1000, 「Get 2000 credits for $166.99」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19947
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/09_ISS-XMA-21/`

---

## 10. ISS-XMA-22 — IAP (Philippines, Taiwan): the Christmas monthly plan is not cheaper than the regular monthly plan; is 15% off meant for every store?  ·  Class: Functional  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-113, TC-105, O-2, O-6  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** PM rules ➊: the Android monthly plan is 15% off (monthlysubscription_christmas_2611). Store prices read by the app (logcat): Philippines campaign monthly ₱485.00 vs the regular monthly_sub_usd6.99_202209 ₱469.00 (the campaign is 3% dearer); Taiwan both NT$240.00 (the SKU 表 itself sets the campaign monthly to NT$240); US $6.99 vs $7.99 (12.5% off). The SKU 表 lists no regular monthly price to check against. A store-price question the run cannot settle, so filed to PM (rule 2026-11-11): should the campaign monthly be discounted in every store, and should the Play prices for the Philippines and Taiwan change? TC-113's own failure (annual card selected) is ISS-XMA-15; TC-105 passed (the Play sheet is the campaign SKU).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] Christmas Sale (IAP): Philippines: Christmas monthly ₱485 costs more than the regular ₱469
```

**Description:**

```
Repro Steps:
1. Set the Play country to Philippines in Play Billing Lab
2. Force-stop the APP
3. Launch the APP
4. Tap the Mine tab
5. Tap 「Claim Holiday Deal」
6. Look at the monthly plan price
7. Check the result

Result:
Philippines: the Christmas monthly is ₱485, the regular monthly ₱469; Taiwan: both NT$240.
摘要：菲律賓聖誕月訂比一般貴；台灣兩者同價。
{16.9.0_xma22_philippines_monthly.jpg} {16.9.0_xma22_log.txt}

Expect Result:
PM decides whether the Christmas monthly must be cheaper in every store (15% off) and sets the prices.
摘要：請 PM 決定各商店月訂是否都要打折並調整價格。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Free account, signed in; Play store Philippines and Taiwan (Play Billing Lab)
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (➊ Android Monthly 15% off, SKU monthlysubscription_christmas_2611; linked SKU 表) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/10_ISS-XMA-22/`

---

## 11. ISS-XMA-23 — Mine (Pro, 日本語): the top pill stays English 「Credit Special Offer」; the spec gives no translation  ·  Class: UI  ·  Severity: S3  ·  Owner: PM

**Report step:** TC-114, O-9  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-044 (Design Launcher & dialog board, mine_vip: 「Credit Special Offer」 pill with a gift icon, ruling Q-12). The 多國文案 sheet has no row for the pill, so no translation exists in the spec (text rule 2026-11-11: PM supplies it); plainly wrong on screen (English in a Japanese Mine), so filed, not held. Only 日本語 was run on the Pro account; other languages likely the same. Same class as R1 ISS-XMA-02.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][JPN] Christmas Sale (Mine): Pro top pill stays English 「Credit Special Offer」
```

**Description:**

```
Repro Steps:
1. Set the app language to 日本語
2. Launch the APP
3. Tap the 「Pro」 tab
4. Look at the pill at the top left
5. Check the result

Result:
In 日本語 the Pro Mine's top pill reads 「Credit Special Offer」 in English.
摘要：日文介面下 Pro Mine 頁膠囊仍為英文。
{16.9.0_xma23_pill_jp.jpg}

Expect Result:
PM supplies 「Credit Special Offer」 for each app language; the pill shows it translated.
摘要：請 PM 提供各語系翻譯。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Play test build from the Play Store; Pro account (Christmas annual plan), signed in, no Credit Auto Pass; Play store Japan (Play Billing Lab)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Launcher & dialog board (mine_vip: 「Credit Special Offer」 pill) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2772-10246
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1r_16.9.0_images/11_ISS-XMA-23/`

---

## Cited — additions to R1 entries (same bug, new evidence; not drafted again)

| R1 entry | From R1r | What to add |
|---|---|---|
| ISS-XMA-06 (R1) | TC-112 (Indonesia) and TC-101 (US), O-1 | New evidence, Play test build, signed in: the app truncates. Indonesia IDR 590,000 / IDR 119,000 × 12 = 58.68% shows 「58% OFF」 (rounded 59); Taiwan 57.99% → 57 (R1). US 45.17% → 45 (TC-101 Pass). Add to ISS-XMA-06 the Indonesia screenshot (runs/2026-11-23-r1r-recheck/screenshots/TC-112-iap-indonesia.png) and that the % is computed, not fixed. |
| ISS-XMA-12 (R1) | TC-100 (US store, signed in) | Same bug on the US store, signed in on the Play test build: tag 「Special Offer」 with a Santa hat, 「45% OFF」 not 「Save 45%」, monthly 「$6.99/Month」 with no struck original although the page fetched the regular $7.99; also CTA 「Continue」 and the 「No Watermark」 carousel (left to the reviewer in R1). Add TC-100's screenshot (screenshots/TC-100-iap-us.png); not a new entry. |
| R1 held TC-124 | TC-124, TC-148 | R1 held the missing Christmas 500 pack until a signed-in recheck; signed in it is the same, so it is now drafted as ISS-XMA-16 (no R1 entry to add to). |

## Not raised (for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-3 | Play test build already signed in as acda.test9; interstitial still unused today | Run state, no finding. |
| O-4 | Play Billing Lab terms accepted; country suggestions not in the accessibility tree | Tooling note. |
| O-5 | Play sheet SKU only visible in dumpsys activity iabData | Tooling note. |
| O-8 | ToS / Privacy Policy open the Traditional Chinese pages with the Play country United States | Spec silent (R1 O-1, not raised); not the Play country; report only. |
| O-11 | Purchases made: Christmas annual (15:13) and Credit Auto Pass (15:25); account Pro + Auto Pass, 5510 credits | Account state left for the next run. |
| Blocked test-data (8) | TC-134, TC-135, TC-142, TC-151, TC-129, TC-132, TC-133, TC-141 | No verdict: low-balance account needed (TC-132–135, 141, 142), RD stage date for the New Year window (TC-129, TC-151 step 3); reasons in report.md and blocked-reasons.json. |

## Reconciliation against the run

14 Fail (all defect), 11 Blocked (3 defect, 8 test-data), 11 observations (O-1 … O-11).

### Row-by-row map

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-013 | Fail | defect | 1. ISS-XMA-13 |
| TC-014 | Fail | defect | 2. ISS-XMA-14 |
| TC-100 | Fail | defect | addition to R1 ISS-XMA-12 |
| TC-111 | Fail | defect | 3. ISS-XMA-15 |
| TC-112 | Fail | defect | 3. ISS-XMA-15; addition to R1 ISS-XMA-06 |
| TC-113 | Fail | defect | 3. ISS-XMA-15; 10. ISS-XMA-22 |
| TC-124 | Fail | defect | 4. ISS-XMA-16 |
| TC-114 | Fail | defect | 5. ISS-XMA-17; 11. ISS-XMA-23 |
| TC-115 | Fail | defect | 5. ISS-XMA-17 |
| TC-118 | Fail | defect | 6. ISS-XMA-18 |
| TC-120 | Fail | defect | 6. ISS-XMA-18; 7. ISS-XMA-19; 8. ISS-XMA-20 |
| TC-125 | Fail | defect | 7. ISS-XMA-19 |
| TC-122 | Fail | defect | 9. ISS-XMA-21 |
| TC-126 | Fail | defect | 9. ISS-XMA-21 |
| TC-148 | Blocked | defect | 4. ISS-XMA-16 |
| TC-117 | Blocked | defect | 5. ISS-XMA-17 |
| TC-149 | Blocked | defect | 9. ISS-XMA-21 |
| TC-101 | Pass | — | 1. ISS-XMA-13 |
| TC-105 | Pass | — | 10. ISS-XMA-22 |
| O-1 | observation | — | folded into 1. ISS-XMA-13; addition to R1 ISS-XMA-06 |
| O-2 | observation | — | folded into 10. ISS-XMA-22 |
| O-3 | observation | — | not raised |
| O-4 | observation | — | not raised |
| O-5 | observation | — | not raised |
| O-6 | observation | — | folded into 10. ISS-XMA-22 |
| O-7 | observation | — | folded into 4. ISS-XMA-16 |
| O-8 | observation | — | not raised |
| O-9 | observation | — | folded into 11. ISS-XMA-23 |
| O-10 | observation | — | folded into 5. ISS-XMA-17 |
| O-11 | observation | — | not raised |

### Owner split

| Owner | Entries |
|---|---|
| RD | 1, 2, 3, 4, 5, 6, 7, 9 |
| PM | 8, 10, 11 |

### Filing order

By severity: **1**, **3**, **4**, **5**, **6**, **9**, **7**, **10**, **11**, **2**, **8**. File with the R1 batch, after its decisions; nothing is filed until the review page's decisions come back.
