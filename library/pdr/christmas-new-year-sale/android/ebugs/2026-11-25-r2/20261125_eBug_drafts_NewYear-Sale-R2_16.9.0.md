# Christmas & New Year Sales (Android) — eBug drafts, round R2 (New Year rows, phone date in the New Year window), PDR-A 16.9.0 build 2611231

**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-25-r2-newyear/` — round R2 of draft `drafts/20261120-165128` (table v2; the 57 New Year rows plus TC-129 and TC-151, REQ-006), 2026-11-25 11:49 → 13:09, on Samsung Galaxy A51 SM-A516B / Android 13 (adb R5CN8194YSN) through Appium / UiAutomator2, build 16.9.0.2611231 installed with adb by the user, Stage server, the campaign driven by the phone's system date (user, REQ-006), acda.test9 signed in (Free; Pro from R2-d after buying the New Year annual test subscription), Play store Taiwan (US through Play Billing Lab for TC-020/021/003/103). Tally: 38 Fail, 17 Pass, 4 Blocked.

**Status:** nothing filed, uploaded or commented. Third batch of this feature; R1 (P0264–P0275) and R1r (P0254–P0263) are filed, all titled for the Christmas sale. The New Year repeats of those bugs are new entries whose Note names the related Christmas ticket; new bugs have none. Dedupe: per OS, read-only (`dedupe.txt`).

Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` / `[AIAgent][UI]` owner RD for defects; text the spec must supply to PM (BugBelong PM), 2026-11-11. Severity is proposed.

**What is drafted:** 17 entries (ISS-XMA-24…40): 4 RD Functional, 12 RD UI, 1 PM UI.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.

---

## 1. ISS-XMA-24 — New Year interstitial (US store): 「SAVE 52%」 and 「vs. paying $7.99/mo × 12」 come from the regular monthly plan, not the campaign $6.99  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-020, O-2  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-006 / R-018 / R-036, ruling Q-3 (REQ-002): the % and 「vs. paying …/mo」 come from the campaign SKUs' store prices (annualsubscription_newyear_2611 $45.99, monthlysubscription_newyear_2611 $6.99 → 45%). Logcat 2027-01-01 12:00:28: the interstitial asked Play for monthly_sub_usd6.99_202209 ($7.99, regular) and the New Year annual. The IAP page reads $6.99 and 45% (O-2). Same as P0254 on the Christmas interstitial; P0254's steps and title name the Christmas sale only.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] New Year Sale (Interstitial): US store: SAVE 52% from the regular $7.99 monthly, not $6.99 (45%)
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2027-01-01 in Settings (automatic date and time off)
2. Set the Play country to United States in Play Billing Lab
3. Force-stop the APP
4. Launch the APP
5. Look at the 「SAVE」 line and the 「vs. paying」 line
6. Check the result

Result:
The interstitial reads 「SAVE 52%」 「vs. paying $7.99/mo × 12」; the IAP page shows $6.99 and 45%.
摘要：新年插頁以一般月訂 $7.99 算出 52%，IAP 頁為 $6.99、45%。
{16.9.0_xma24_interstitial_us.jpg} {16.9.0_xma24_log.txt}

Expect Result:
The interstitial uses the New Year monthly $6.99: 「SAVE 45%」 「vs. paying $6.99/mo × 12」.
摘要：插頁應以新年活動月訂 $6.99 計算：SAVE 45%。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store United States (Play Billing Lab)
Related: DRA262611P0254 (same calculation on the Christmas interstitial, filed for the Christmas sale)
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-rules board (➊ monthly plan SKU monthlysubscription_newyear_2611, SKU 表 US $6.99; ➍ 年價格 vs 月價格*12個月的價差%) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Interstitial board (「SAVE」 「<xx>」 「%」, 「vs. paying <monthly price>/mo × 12」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5895
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/01_ISS-XMA-24/`

---

## 2. ISS-XMA-25 — New Year interstitial: trial terms read 「until cancelled」, the spec 「until canceled」  ·  Class: UI  ·  Severity: S4  ·  Owner: RD

**Report step:** TC-021  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-020: 「…Subscription renews automatically until canceled. Cancel in Google Play…」. The annual price in the terms matches the big price ($45.99). The spec states the string and the app shows another: RD (text rule 2026-11-11). The interstitial is likely shared with Christmas (P0255); the ticket names the Christmas sale only.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Interstitial): Trial terms read 「until cancelled」, not 「until canceled」
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2027-01-01 in Settings (automatic date and time off)
2. Launch the APP
3. Look at the trial terms under the yellow button
4. Check the result

Result:
The New Year trial terms use the British spelling with a double 「l」, not the spec's US spelling.
摘要：新年插頁試用條款拼字為英式（雙 l）。
{16.9.0_xma25_terms.jpg}

Expect Result:
The terms read 「…Subscription renews automatically until canceled. …」 as the spec states.
摘要：條款應為規格文字「until canceled」。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store United States (Play Billing Lab)
Related: DRA262611P0255 (same string on the Christmas interstitial, filed for the Christmas sale)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Interstitial board (trial terms 「…renews automatically until canceled…」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5895
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/02_ISS-XMA-25/`

---

## 3. ISS-XMA-26 — New Year interstitial: the first system Back does nothing; a second Back closes it  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-023  ·  **Reproduce:** 2/3  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-025, ruling Q-5 (REQ-002): system Back on the interstitial does what X does, one press, back to the Launcher. Seen 12/31 11:58 (Appium Back) and 1/2 12:01 (adb keyevent 4, ~10 s after the interstitial showed: dumpsys still topResumed PromotionInterstitialActivity; the second keyevent reached the Launcher). Once (1/1 12:00) a single Back left the app entirely. X closes it in one tap (TC-022 Pass). No log line for the ignored Back.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] New Year Sale (Interstitial): First system Back is ignored; a second Back closes it
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-31 in Settings (automatic date and time off)
2. Launch the APP
3. Wait until the New Year Special interstitial shows
4. Press system Back once
5. Look at the screen
6. Press system Back again
7. Check the result

Result:
After the first Back the interstitial is still on screen; the second Back closes it to the Launcher.
摘要：第一次按系統返回鍵插頁不關閉，第二次才回到首頁。
{16.9.0_xma26_after_first_back.jpg} {16.9.0_xma26_after_second_back.jpg}

Expect Result:
One system Back closes the interstitial and shows the Launcher, as X does.
摘要：按一次系統返回鍵即應如 X 關閉插頁回到首頁。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: R1 on build 2611201 closed the Christmas interstitial with one Back (TC-016)
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-launch board (New Year interstitial, X closes to the Launcher; Android system Back acts as X per ruling Q-5) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/03_ISS-XMA-26/`

---

## 4. ISS-XMA-27 — Launcher (New Year): the top banner title is 「Turn one photo to cinematic reel」, not 「Bring New Year moments to life」  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-003, TC-085, TC-086  ·  **Reproduce:** 3/3  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-027 (Design New Year Launcher & dialog, dark and light): the New Year banner title is 「Bring New Year moments to life」 ›. The New Year banner image shows (fireworks, woman with a sparkler) and reads well in dark and light, but the title (tv_banner_tagline) is the regular 「Turn one photo to cinematic reel」 ›. Seen at the 12/28 00:00 switch (TC-003), 12/29 light (TC-086) and dark (TC-085).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Launcher): Top banner title is not 「Bring New Year moments to life」
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Launch the APP
3. Tap X on the New Year Special interstitial
4. Look at the top banner title
5. Check the result

Result:
The New Year banner shows the title 「Turn one photo to cinematic reel」 ›, in light and dark mode.
摘要：新年橫幅標題顯示為一般文案「Turn one photo to cinematic reel」。
{16.9.0_xma27_light.jpg} {16.9.0_xma27_dark.jpg}

Expect Result:
The banner title reads 「Bring New Year moments to life」 ›.
摘要：橫幅標題應為「Bring New Year moments to life」。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: DRA262611P0270 (Christmas banner title 「Make Christmas magic with AI」 missing, filed for the Christmas sale)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Launcher & dialog board (Launcher dark / light: 「Bring New Year moments to life」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-23135
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/04_ISS-XMA-27/`

---

## 5. ISS-XMA-28 — New Year interstitial: 「SAVE」 and 「vs. paying …/mo × 12」 stay English in all 26 other languages  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-057, TC-058, TC-059, TC-060, TC-061, TC-062, TC-063, TC-064, TC-065, TC-066, TC-067, TC-068, TC-069, TC-070, TC-071, TC-072, TC-073, TC-074, TC-075, TC-076, TC-077, TC-078, TC-079, TC-080, TC-081, TC-082, O-6  ·  **Reproduce:** 26/26  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-022 (PM rules 底圖 & 價格 + 多國文案 sheet; ruling Q-16): the lines under the title art are localized by RD per the sheet. All 26 non-English languages (TC-057–TC-082), per-app locale, interstitial brought back by moving the phone date 12/29 ↔ 12/30. In Arabic and Persian the English line takes local digits (「× ١٢」, 「× ۱۲」).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): 「SAVE」 and 「vs. paying …/mo × 12」 are not localized
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Set the app language of PowerDirector to 中文（台灣）
3. Launch the APP
4. Look at the lines under the title art
5. Check the result

Result:
In all 26 non-English languages 「SAVE」 and 「vs. paying NT$240/mo × 12」 stay in English.
摘要：新年插頁在 26 種非英文語系仍顯示英文「SAVE」與「vs. paying NT$240/mo × 12」。
{16.9.0_xma28_cht.jpg} {16.9.0_xma28_rus.jpg} {16.9.0_xma28_ara.jpg}

Expect Result:
Both lines use the 多國文案 sheet's Save and vs. text for the app language (繁中「現省 xx%」).
摘要：兩行應依多國文案表翻譯成該語系。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: DRA262611P0264 (same lines on the Christmas interstitial, filed for the Christmas sale)
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-rules board (底圖 & 價格: lines under the art localized by RD per the linked 多國文案 sheet) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
Spec Link: 多國文案 sheet (linked from the PM rules board), block 「New Year Special」 (Save and vs. rows) -
https://docs.google.com/spreadsheets/d/1_rJf-7ljc0c_HO0P4isuyn-AOt6mIlbXsmyRW9xcGSk/edit?gid=1226976055
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/05_ISS-XMA-28/`

---

## 6. ISS-XMA-29 — New Year interstitial: 「/year」 and 「More subscription plan」 stay English in all 26 other languages; the sheet has no translation  ·  Class: UI  ·  Severity: S2  ·  Owner: PM

**Report step:** TC-057, TC-058, TC-059, TC-060, TC-061, TC-062, TC-063, TC-064, TC-065, TC-066, TC-067, TC-068, TC-069, TC-070, TC-071, TC-072, TC-073, TC-074, TC-075, TC-076, TC-077, TC-078, TC-079, TC-080, TC-081, TC-082, O-6  ·  **Reproduce:** 26/26  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** The Design draws 「/year」 and 「More subscription plan」; the 多國文案 sheet has no row for either, so no translation exists in the spec: PM supplies it (text rule 2026-11-11), as P0265 for Christmas.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): 「/year」 and 「More subscription plan」 are not localized
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Set the app language of PowerDirector to Русский
3. Launch the APP
4. Look at the annual price and the link under the trial terms
5. Check the result

Result:
「/year」 and 「More subscription plan」 are English in all 26 non-English languages.
摘要：「/year」與「More subscription plan」在 26 種語系皆為英文，多國文案表無此兩列。
{16.9.0_xma29_rus.jpg} {16.9.0_xma29_jpn.jpg}

Expect Result:
PM supplies both strings for each app language; the interstitial shows them translated.
摘要：請 PM 提供兩字串各語系翻譯。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: DRA262611P0265 (same strings on the Christmas interstitial, filed for the Christmas sale)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Interstitial board (「/year」, 「More subscription plan」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5895
Spec Link: 多國文案 sheet (linked from the PM rules board), block 「New Year Special」 (no row for 「/year」 or 「More subscription plan」) -
https://docs.google.com/spreadsheets/d/1_rJf-7ljc0c_HO0P4isuyn-AOt6mIlbXsmyRW9xcGSk/edit?gid=1226976055
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/06_ISS-XMA-29/`

---

## 7. ISS-XMA-30 — New Year interstitial: title art English in French and Italian, Russian in Ukrainian; es-ES shows the Mexican Spanish title and CTA  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-059, TC-063, TC-082, TC-066, O-6  ·  **Reproduce:** 4/4  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-022 / multilang sheet (block 「New Year Special」): FRA 「Vente du Nouvel An」, ITA 「Capodanno Speciale」, UKR 「Новорічна пропозиція」, ESP title 「Especial Año Nuevo」 and CTA 「Prueba 7 días gratis」. The app shows the English art in fr-FR (TC-059) and it-IT (TC-063), the Russian art 「Новогодняя акция」 in uk-UA (TC-082), and in es-ES the ESP (MX) title 「Especial de Año Nuevo」 and CTA 「Prueba gratis por 7 días」 (TC-066; es-MX's own CTA 「Inicia tu prueba gratuita de 7 días」 is in ISS-XMA-31). Titles in the other 22 languages match the sheet.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][FRA/ITA/UKR/ESP] New Year Sale (Interstitial): Title art not in the app language
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Set the app language of PowerDirector to Français
3. Launch the APP
4. Look at the title art
5. Check the result

Result:
FRA and ITA show the English title art, UKR the Russian art, es-ES the Mexican Spanish title and CTA.
摘要：法文、義大利文顯示英文標題圖；烏克蘭文顯示俄文標題圖；西班牙文（西班牙）顯示墨西哥西文標題與按鈕。
{16.9.0_xma30_fra.jpg} {16.9.0_xma30_ita.jpg} {16.9.0_xma30_ukr.jpg} {16.9.0_xma30_esp.jpg}

Expect Result:
The title art is the sheet's title for the app language (FRA 「Vente du Nouvel An」, UKR 「Новорічна пропозиція」).
摘要：標題圖應為該語系多國文案（法、義、烏、西）。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: new on the New Year art; the Christmas art was French, Italian and Ukrainian in R1 (TC-032, TC-036, TC-055)
Spec Link: 多國文案 sheet (linked from the PM rules board), block 「New Year Special」 (title rows FRA, ITA, UKR, ESP; CTA row ESP) -
https://docs.google.com/spreadsheets/d/1_rJf-7ljc0c_HO0P4isuyn-AOt6mIlbXsmyRW9xcGSk/edit?gid=1226976055
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Interstitial board (title art 「New Year Special」, 多國 title per language) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5895
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/07_ISS-XMA-30/`

---

## 8. ISS-XMA-31 — New Year interstitial: CTA wording differs from the 多國文案 sheet in 12 languages  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-057, TC-058, TC-059, TC-063, TC-064, TC-065, TC-066, TC-069, TC-071, TC-072, TC-075, TC-078, O-6  ·  **Reproduce:** 12/12  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** Sheet CTA vs app: CHT 「７天免費試用」/「7 天免費試用」, CHS 「7天免费试用」/「7 天免费试用」, FRA 「Essai gratuit de 7 jours」/「Recevoir 7 jours d'essai gratuits」, ITA 「Prova Gratis per 7 Giorni」/「Prova Gratuita di 7gg.」, JPN 「7 日間無料で試す」/「７日間無料お試し」, KOR 「7일 무료 체험 시작하기」/「7일 무료 체험」, ESP (see ISS-XMA-30), ESP (MX) 「Prueba gratis por 7 días」/「Inicia tu prueba gratuita de 7 días」, RUS 「Попробовать 7 дней бесплатно」/「7-дн. беспл. пробное」, Viet 「Dùng thử miễn phí 7 ngày」/「Dùng Thử Miễn Phí 7 Ngày」, Arabic 「بدء تجربة مجانية لمدة 7 أيام」/「ابدأ تجربة مجانية لمدة 7 أيام」, Hebrew (TC-078). The same 12 as P0266.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): CTA text differs from the 多國文案 sheet in 12 languages
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Set the app language of PowerDirector to Русский
3. Launch the APP
4. Look at the yellow button
5. Check the result

Result:
In 12 languages the CTA reads differently from the sheet (e.g. RUS 「7-дн. беспл. пробное」).
摘要：12 種語系按鈕文字與多國文案表不同。
{16.9.0_xma31_rus.jpg} {16.9.0_xma31_fra.jpg} {16.9.0_xma31_jpn.jpg}

Expect Result:
The CTA shows the sheet's string for each language (RUS 「Попробовать 7 дней бесплатно」).
摘要：按鈕應為多國文案表文字。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: DRA262611P0266 (same CTA strings on the Christmas interstitial, filed for the Christmas sale)
Comparison: CTA, 多國文案 sheet vs app (build 2611231)
- CHT: sheet 「７天免費試用」 / app 「7 天免費試用」
- CHS: sheet 「7天免费试用」 / app 「7 天免费试用」
- FRA: sheet 「Essai gratuit de 7 jours」 / app 「Recevoir 7 jours d'essai gratuits」
- ITA: sheet 「Prova Gratis per 7 Giorni」 / app 「Prova Gratuita di 7gg.」
- JPN: sheet 「7 日間無料で試す」 / app 「７日間無料お試し」
- KOR: sheet 「7일 무료 체험 시작하기」 / app 「7일 무료 체험」
- ESP: sheet 「Prueba 7 días gratis」 / app 「Prueba gratis por 7 días」
- ESP (MX): sheet 「Prueba gratis por 7 días」 / app 「Inicia tu prueba gratuita de 7 días」
- RUS: sheet 「Попробовать 7 дней бесплатно」 / app 「7-дн. беспл. пробное」
- Viet: sheet 「Dùng thử miễn phí 7 ngày」 / app 「Dùng Thử Miễn Phí 7 Ngày」
- Arabic: sheet 「بدء تجربة مجانية لمدة 7 أيام」 / app 「ابدأ تجربة مجانية لمدة 7 أيام」
- Hebrew: sheet 「ניסיון חינם ל-7 ימים」 / app 「נסה בחינם למשך 7 ימים」
Spec Link: 多國文案 sheet (linked from the PM rules board), block 「New Year Special」 (CTA row) -
https://docs.google.com/spreadsheets/d/1_rJf-7ljc0c_HO0P4isuyn-AOt6mIlbXsmyRW9xcGSk/edit?gid=1226976055
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/08_ISS-XMA-31/`

---

## 9. ISS-XMA-32 — New Year interstitial: bottom links run into each other or the separators in RUS, FRA, UKR and Polish  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-069, TC-059, TC-082, TC-076, O-6  ·  **Reproduce:** 4/4  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** Design bottom bar 「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」 with clear separators. RUS: the three links overlap (x 78–366, 344–738, 720–996) and cover both separators; FRA 「Politique de confidentialité」 (388–694) touches both separators (381, 698); UKR 「Політика конфіденційності」 (376–706) runs into both; Polish 「Warunki korzystania z usługi」 (63–385) runs into the left one.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][RUS/FRA/UKR/POL] New Year Sale (Interstitial): Bottom links overlap each other or separators
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Set the app language of PowerDirector to Русский
3. Launch the APP
4. Look at the three links at the bottom
5. Check the result

Result:
In Russian the bottom links overlap; in French, Ukrainian and Polish a link runs into the separators.
摘要：俄文底部連結互相重疊；法、烏、波蘭文連結壓到分隔線。
{16.9.0_xma32_rus.jpg} {16.9.0_xma32_fra.jpg} {16.9.0_xma32_ukr.jpg} {16.9.0_xma32_pol.jpg}

Expect Result:
The three links fit with space around each separator, as the Design draws.
摘要：三個連結應與分隔線保持間距。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: DRA262611P0267 (same bar on the Christmas interstitial, filed for the Christmas sale)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Interstitial board (「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5895
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/09_ISS-XMA-32/`

---

## 10. ISS-XMA-33 — New Year interstitial (Polish): the CTA wraps to two lines that fill the button edge to edge  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-076  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** Sheet CTA 「Rozpocznij 7-dniowy bezpłatny okres próbny」 matches; the text box spans the whole button (63–1017) in two lines. The Design draws a one-line CTA with side padding.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][POL] New Year Sale (Interstitial): CTA wraps to two lines with no side padding in the button
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Set the app language of PowerDirector to Polski
3. Launch the APP
4. Look at the yellow button
5. Check the result

Result:
The Polish CTA wraps to two lines and touches both sides of the button.
摘要：波蘭文按鈕文字換成兩行且貼齊按鈕左右。
{16.9.0_xma33_pol_cta.jpg}

Expect Result:
The CTA fits with side padding (smaller text or one line), as the Design draws.
摘要：按鈕文字應保有左右留白。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: DRA262611P0268 (same button on the Christmas interstitial, filed for the Christmas sale)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Interstitial board (CTA 「Get 7-Day Free Trial」, one line) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5895
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/10_ISS-XMA-33/`

---

## 11. ISS-XMA-34 — New Year interstitial and IAP show 57% where NT$1,210 vs NT$240 × 12 gives 57.99% (58%)  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-102, O-6  ·  **Reproduce:** 27/27  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-036 (PM ➍ 年價格 vs 月價格*12個月的價差%, ruling Q-3): (NT$240 × 12 − NT$1,210) ÷ (NT$240 × 12) = 57.99% → 58 rounded; the app truncates to 57 on the New Year interstitial in all 27 languages (TC-056–TC-082) and on the IAP card 「57% OFF」 (TC-102). Store prices in logcat 2026-12-29 11:50:29.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] New Year Sale (IAP): Discount shows 57% though NT$1,210 vs NT$240 × 12 gives 57.99%
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Launch the APP
3. Look at the big percentage
4. Tap X
5. Tap the Mine tab
6. Tap 「Claim Holiday Deal」
7. Look at the annual plan card
8. Check the result

Result:
Both pages show 57% for NT$1,210 / NT$240 (57.99%).
摘要：兩頁皆顯示 57%（實際 57.99%）。
{16.9.0_xma34_interstitial_57.jpg} {16.9.0_xma34_iap_57.jpg} {16.9.0_xma34_log.txt}

Expect Result:
The % is rounded from the store prices: 58%.
摘要：百分比應四捨五入為 58%。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: DRA262611P0269 (same truncation on the Christmas pages, filed for the Christmas sale)
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-rules board (➍ 年價格 vs 月價格*12個月的價差%) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Interstitial board (「SAVE」 「<xx>」 「%」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5895
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/11_ISS-XMA-34/`

---

## 12. ISS-XMA-35 — Mine (Free, New Year): the top pill shows no countdown; the Launcher pill does  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-089, O-9  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-029, ruling Q-9 (REQ-003): in the New Year campaign the Launcher and Mine top pill show a clock icon and a countdown 「<d>D hh:mm:ss」 (Design 「2D 23:56:18」, PM 「6D 23:56:18」). At 2027-01-03 12:00 the Launcher pill counts 「2D 11:59:40」 to 1/6 00:00 (Q-18 assumption); Mine's pill reads only 「Try Pro 7 days for free」 with the gift icon (watched 12:00:43–12:00:50; also 12/29 12:34). The IAP CTA and the credit page count to the same target.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Mine): Mine top pill has no clock or countdown
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2027-01-03 in Settings (automatic date and time off)
2. Launch the APP
3. Tap X on the New Year Special interstitial
4. Look at the pill at the top of the Launcher
5. Tap the Mine tab
6. Look at the pill at the top of Mine
7. Check the result

Result:
The Launcher pill shows 「2D 11:59:40」 counting down; Mine's pill shows only 「Try Pro 7 days for free」.
摘要：首頁膠囊有倒數，Mine 頁膠囊無時鐘與倒數。
{16.9.0_xma35_launcher_pill.jpg} {16.9.0_xma35_mine_pill.jpg}

Expect Result:
Mine's top pill shows the clock icon and the same countdown as the Launcher.
摘要：Mine 頁膠囊應與首頁同樣顯示時鐘與倒數。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: none on the Christmas sale (it has no countdown)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Launcher & dialog board (Launcher and Mine top pill with clock and 「2D 23:56:18」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-23135
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-launch board (Mine pill countdown 「6D 23:56:18」) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/12_ISS-XMA-35/`

---

## 13. ISS-XMA-36 — IAP (New Year): tag 「Special Offer」 and 「57% OFF」, not 「New Year Treat」 and 「Save 57%」; monthly not struck; CTA 「Continue」; other feature cards  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-102  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-035 / R-037 / R-040 (PM New Year 1104 Update; Design New Year IAP & Credit): annual card tag 「New Year Treat」 with a small decoration, 「Save <xx>%」 on its right half, no 「Offer」 on the page; monthly card with the original price struck; CTA 「Get 7-Day Free Trial」; feature cards 「Auto Edit」, 「4K Output」, 「Remove Watermark」. App: 「Special Offer」 (balloon/star), 「57% OFF」, 「NT$240/Month」 only, CTA 「Continue」 with the countdown under it, cards 「No Watermark」, 「100 Monthly Credits」, 「Video Enhance」, 「15K+ Music Tracks」, 「4K Output」. The New Year header art and countdown are right.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (IAP): Tag 「Special Offer」 and 「57% OFF」 instead of 「New Year Treat」, 「Save xx%」
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-29 in Settings (automatic date and time off)
2. Launch the APP
3. Tap X on the New Year Special interstitial
4. Tap the Mine tab
5. Tap 「Claim Holiday Deal」
6. Look at the plan cards and the yellow button
7. Check the result

Result:
Tag 「Special Offer」, 「57% OFF」, monthly price not struck, CTA 「Continue」, other feature cards.
摘要：年訂卡標籤為「Special Offer」「57% OFF」，月訂無劃線原價，按鈕為「Continue」，功能卡不同。
{16.9.0_xma36_iap_card.jpg}

Expect Result:
Tag 「New Year Treat」, 「Save 57%」, struck monthly price, CTA 「Get 7-Day Free Trial」, the Design's cards.
摘要：應為 New Year Treat、Save xx%、月訂劃線原價與 Get 7-Day Free Trial 按鈕。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Free account, signed in; Play store Taiwan
Related: DRA262611P0275 (same card on the Christmas IAP page, filed for the Christmas sale)
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-launch board (1104 Update, IAP: 「New Year Treat」, struck monthly price, no 「Offer」) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year IAP & Credit board (IAP_year plan cards, CTA, feature cards) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5521
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/13_ISS-XMA-36/`

---

## 14. ISS-XMA-37 — Mine (Pro, New Year): the VIP card has no New Year decoration  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-116, O-13  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-043 (PM rules ➍ Paid: VIP Welcome Banner decorated; New Year decoration in the New Year campaign). On 2611231 the Pro Mine opens on the plain card (crown 「Pro」, 「You're on the highest plan…」, Credits) with no decoration; tapping it opens nothing (no separate VIP Benefits page). The only New Year touch is the tab icon. 「Your VIP Features」 and 「More VIP Benefits」 stayed empty (O-13).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Mine): Pro VIP card lacks New Year decoration
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-30 in Settings (automatic date and time off)
2. Launch the APP
3. Tap the 「Pro」 tab
4. Look at the VIP card at the top
5. Tap the VIP card
6. Check the result

Result:
The Pro VIP card is the plain card with no New Year decoration; tapping it opens nothing.
摘要：Pro 的 VIP 卡片無新年裝飾，點擊無反應。
{16.9.0_xma37_vip.jpg}

Expect Result:
The VIP welcome banner carries New Year decoration.
摘要：VIP 歡迎橫幅應有新年裝飾。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Pro account (New Year annual plan), signed in, no Credit Auto Pass; Play store Taiwan
Related: DRA262611P0258 (Pro VIP card lacks Christmas decoration, filed for the Christmas sale)
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-rules board (➍ Paid: VIP Welcome Banner with New Year decoration) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/14_ISS-XMA-37/`

---

## 15. ISS-XMA-38 — Credit page (Pro, New Year): the 2000-credit Special Offer pack is never offered; the Auto Pass card takes its place  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-121, TC-123  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-046 / R-008: for a paid user the Special Offer pack 「1000+1000」 (white 1000, green +1000) with the CTA 「Get 2000 credits for <price>」 buys pdrm_2000_credit_paiduser_christmas (the New Year campaign uses the same SKU, PM New Year rules). On 12/30 (no Auto Pass) the special card is the Auto Pass card 「Annual Auto Pass Discount」 「1000 +1000」 「NT$2490」 (ISS-XMA-39); selecting the regular 2000 card gives 「Get 2000 Credits for NT$3350」, whose Play sheet is pdrm_2000_credits_paiduser (TC-123, cancelled). Logcat 2026-12-30 13:04:56 fetches pdrm_2000_credit_paiduser_christmas (NT$2,740.00) and never shows it.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] New Year Sale (Credit): Pro: New Year 2000-credit pack never offered; no 「Get 2000 credits for …」
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-30 in Settings (automatic date and time off)
2. Launch the APP
3. Tap the 「Pro」 tab
4. Tap 「Credit Special Offer」
5. Look at the top card
6. Tap the 2000 pack
7. Tap 「Get 2000 Credits for NT$3350」
8. Check the result

Result:
No 2000-credit Special Offer pack; the 2000 card opens the regular SKU pdrm_2000_credits_paiduser.
摘要：無新年 2000 點特惠包；2000 點卡開啟一般會員 SKU。
{16.9.0_xma38_page.jpg} {16.9.0_xma38_regular_2000.jpg} {16.9.0_xma38_play_regular.jpg} {16.9.0_xma38_log.txt}

Expect Result:
The 「1000+1000」 pack with 「Get 2000 credits for <price>」 opens pdrm_2000_credit_paiduser_christmas.
摘要：應顯示 1000+1000 特惠包並開啟活動 SKU。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Pro account (New Year annual plan), signed in, no Credit Auto Pass; Play store Taiwan
Related: DRA262611P0261 (Christmas 2000-credit pack never offered, filed for the Christmas sale)
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-rules board (➎ Credit IAP: paid Special Offer pack 1000+1000, SKU pdrm_2000_credit_paiduser_christmas) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year IAP & Credit board (credit purchase page: Special Offer 1000+1000, 「Get 2000 credits for $166.99」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5521
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/15_ISS-XMA-38/`

---

## 16. ISS-XMA-39 — Credit page (Pro, no Auto Pass, New Year): no 「Subscribe for 3000 free credits!」; 「Continue with the best deal」 and 「Cancel anytime.」 instead  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-121  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-048 / R-052, ruling Q-14: without Credit Auto Pass the page leads with the Auto Pass sale under 「Subscribe for 3000 free credits!」 and 「Each credit for about <price>」. App: 「Annual top-up automatically!」, CTA 「Continue with the best deal」, 「Each credit for about NT$1.24. Cancel anytime.」. The footer 「Terms of Service | Privacy Policy」 and 「unused credits」 vs the Design's 「Privacy Policy | Terms of Use」 and 「consumed credits」 were held by the reviewer as ISS-XMA-20 (not filed) and are not raised again. The 「New Year Special」 banner and the countdown are right.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Credit): No Auto Pass: CTA not 「Subscribe for 3000 free credits!」
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-30 in Settings (automatic date and time off)
2. Launch the APP
3. Tap the 「Pro」 tab
4. Tap 「Credit Special Offer」
5. Look at the lines above and under the CTA
6. Check the result

Result:
CTA 「Continue with the best deal」 and 「Each credit for about NT$1.24. Cancel anytime.」
摘要：自動續購按鈕文字與規格不同。
{16.9.0_xma39_autopass_cta.jpg}

Expect Result:
「Subscribe for 3000 free credits!」 and 「Each credit for about <price>」, as the Design draws.
摘要：應為 Subscribe for 3000 free credits! 與 Each credit for about。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date inside 2026-12-28 to 2027-01-05); build 2611231 installed with adb; Pro account (New Year annual plan), signed in, no Credit Auto Pass; Play store Taiwan
Related: DRA262611P0260 (same CTA on the Christmas credit page, filed for the Christmas sale)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year IAP & Credit board (credit purchase page: 「Subscribe for 3000 free credits!」, 「Each credit for about $0.1」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-5521
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-credit board (no-subscription Credit Auto Pass version of the credit purchase page) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/16_ISS-XMA-39/`

---

## 17. ISS-XMA-40 — Credit page (Christmas window): a countdown shows above the CTAs; only the New Year page should have one  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-129  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611231

> **QA note — not pasted into eBug.** R-049, ruling Q-11 (REQ-003): only the New Year credit page shows the countdown; the Christmas credit page has none (the Design draws 「2D 23:56:18」 there, overruled). At 2026-12-25 00:03:29 the page (「Christmas Special」 banner) shows the clock and 「2D 23:56:30」, counting to 12/28 00:00. The New Year countdown itself is right (TC-121).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Credit): Countdown 「2D 23:56:30」 shows above the CTAs on 12/25
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-25 00:03 in Settings (automatic date and time off)
2. Launch the APP
3. Tap the 「Pro」 tab
4. Tap 「Credit Special Offer」
5. Look above the CTA
6. Check the result

Result:
The Christmas credit page shows a clock icon and 「2D 23:56:30」 above the CTAs.
摘要：聖誕節點數購買頁 CTA 上方出現倒數。
{16.9.0_xma40_xmas_countdown.jpg}

Expect Result:
No clock icon and no countdown on the Christmas credit page (ruling Q-11).
摘要：聖誕節點數頁不應有時鐘與倒數。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, phone date 2026-12-25 00:03); build 2611231 installed with adb; Pro account (New Year annual plan), signed in, no Credit Auto Pass; Play store Taiwan
Related: R1r (build 2611201, RD test date) saw no countdown on the Christmas credit page; no ticket
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), IAP & Credit board (Christmas credit purchase page; its 「2D 23:56:18」 countdown removed by ruling Q-11) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19947
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-rules board (➎ New Year credit page countdown, New Year only) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
<Claude Reviewed>
```

**Images:** `20261125_eBug_drafts_NewYear-Sale-R2_16.9.0_images/17_ISS-XMA-40/`

---

## Not raised (for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-1 | Toast 「PiP video was enabled before.」 at some launches after a date change | No spec; app debug toast after clock changes; report only. |
| O-3 | IAP CTA and Launcher pill countdowns run to the end of 1/5 | Pass in TC-089 / TC-152. |
| O-4 | Interstitial again on 12/29 after the clock went back | Artifact of moving the clock backwards. |
| O-5 | Settings date tooling; Samsung update screen; log-slice windows empty | Tooling note. |
| O-7 | Samsung 「Software update」 screen after each date move | Phone, not the app. |
| O-8 | New Year Mine icon selected state outline vs Design filled disc | TC-092 passed; left for the design check. |
| O-10 | Time picker tooling, dark mode, Play Billing Lab expiry display | Tooling note. |
| O-11 | Pro test purchase worked on the adb build 2611231 (no 「Unofficial Version」) | Account / build state; knowledge. |
| O-12 | Christmas credit page banner is 「Christmas Special」 on 2611231 (P0259 looked fixed) | Not a recheck of P0259; no comment on tickets. |
| O-14 | Google Play's own 「Here’s a related item」 upsell after cancelling | Google's sheet. |
| O-15 | Samsung update screen interrupted the time picker | Tooling note. |
| TC-121 footer | 「Terms of Service | Privacy Policy」, 「unused credits」 | Same as ISS-XMA-20, held by the reviewer in R1r; not raised again. |
| Blocked test-data (4) | TC-138, TC-139, TC-136, TC-137 | No verdict: a balance below the Image to Video (Custom) price is needed (acda.test9 holds 3720–3755 credits); reasons in report.md and blocked-reasons.json. |

## Reconciliation against the run

38 Fail (all defect), 4 Blocked (0 defect, 4 test-data), 15 observations (O-1 … O-15).

### Row-by-row map

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-020 | Fail | defect | 1. ISS-XMA-24 |
| TC-021 | Fail | defect | 2. ISS-XMA-25 |
| TC-023 | Fail | defect | 3. ISS-XMA-26 |
| TC-003 | Fail | defect | 4. ISS-XMA-27 |
| TC-057 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-058 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-059 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 7. ISS-XMA-30; 8. ISS-XMA-31; 9. ISS-XMA-32; 11. ISS-XMA-34 (57 vs 58) |
| TC-060 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-061 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-062 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-063 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 7. ISS-XMA-30; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-064 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-065 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-066 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 7. ISS-XMA-30; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-067 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-068 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-069 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 9. ISS-XMA-32; 11. ISS-XMA-34 (57 vs 58) |
| TC-070 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-071 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-072 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-073 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-074 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-075 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-076 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 9. ISS-XMA-32; 10. ISS-XMA-33; 11. ISS-XMA-34 (57 vs 58) |
| TC-077 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-078 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 8. ISS-XMA-31; 11. ISS-XMA-34 (57 vs 58) |
| TC-079 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-080 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-081 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 11. ISS-XMA-34 (57 vs 58) |
| TC-082 | Fail | defect | 5. ISS-XMA-28; 6. ISS-XMA-29; 7. ISS-XMA-30; 9. ISS-XMA-32; 11. ISS-XMA-34 (57 vs 58) |
| TC-085 | Fail | defect | 4. ISS-XMA-27 |
| TC-086 | Fail | defect | 4. ISS-XMA-27 |
| TC-089 | Fail | defect | 12. ISS-XMA-35 |
| TC-102 | Fail | defect | 11. ISS-XMA-34; 13. ISS-XMA-36 |
| TC-116 | Fail | defect | 14. ISS-XMA-37 |
| TC-121 | Fail | defect | 15. ISS-XMA-38; 16. ISS-XMA-39 |
| TC-123 | Fail | defect | 15. ISS-XMA-38 |
| TC-129 | Fail | defect | 17. ISS-XMA-40 |
| O-1 | observation | — | not raised |
| O-2 | observation | — | folded into 1. ISS-XMA-24 |
| O-3 | observation | — | not raised |
| O-4 | observation | — | not raised |
| O-5 | observation | — | not raised |
| O-6 | observation | — | folded into 5–10. ISS-XMA-28…33 |
| O-7 | observation | — | not raised |
| O-8 | observation | — | not raised |
| O-9 | observation | — | folded into 12. ISS-XMA-35 |
| O-10 | observation | — | not raised |
| O-11 | observation | — | not raised |
| O-12 | observation | — | not raised |
| O-13 | observation | — | folded into 14. ISS-XMA-37 |
| O-14 | observation | — | not raised |
| O-15 | observation | — | not raised |

### Related Christmas tickets

| Entry | Related ticket |
|---|---|
| 1. ISS-XMA-24 | [DRA262611P0254](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0254) |
| 2. ISS-XMA-25 | [DRA262611P0255](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0255) |
| 3. ISS-XMA-26 | — (new) |
| 4. ISS-XMA-27 | [DRA262611P0270](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0270) |
| 5. ISS-XMA-28 | [DRA262611P0264](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0264) |
| 6. ISS-XMA-29 | [DRA262611P0265](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0265) |
| 7. ISS-XMA-30 | — (new) |
| 8. ISS-XMA-31 | [DRA262611P0266](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0266) |
| 9. ISS-XMA-32 | [DRA262611P0267](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0267) |
| 10. ISS-XMA-33 | [DRA262611P0268](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0268) |
| 11. ISS-XMA-34 | [DRA262611P0269](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0269) |
| 12. ISS-XMA-35 | — (new) |
| 13. ISS-XMA-36 | [DRA262611P0275](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0275) |
| 14. ISS-XMA-37 | [DRA262611P0258](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0258) |
| 15. ISS-XMA-38 | [DRA262611P0261](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0261) |
| 16. ISS-XMA-39 | [DRA262611P0260](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0260) |
| 17. ISS-XMA-40 | — (new) |

### Owner split

| Owner | Entries |
|---|---|
| RD | 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 |
| PM | 6 |

### Filing order

By severity: **1**, **4**, **5**, **6**, **7**, **13**, **14**, **15**, **3**, **8**, **9**, **10**, **11**, **12**, **16**, **17**, **2**. Nothing is filed until the review page's decisions come back.
