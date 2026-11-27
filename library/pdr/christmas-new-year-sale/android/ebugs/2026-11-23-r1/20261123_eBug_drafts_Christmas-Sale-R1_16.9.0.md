# Christmas & New Year Sales (Android) — eBug drafts, round R1 (table v2, Christmas rows), PDR-A 16.9.0 build 2611201

**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-23-r1-christmas/` — round R1 of draft `drafts/20261120-165128` (table v2, Christmas rows, 94 cases), 2026-11-23 11:09 → 14:06, on Samsung Galaxy A51 SM-A516B / Android 13 (adb R5CN8194YSN) through Appium / UiAutomator2, build 16.9.0.2611201 (SR DRA261109-01, installed with adb), Stage server with the RD test date inside the Christmas window, Free account signed out (Stage sign-in after pm clear fails, KP-093), Google Play store Taiwan. Tally: 18 Pass, 41 Blocked, 35 Fail.

**Status:** filed 2026-11-23 by ANGOL_HUANG over the IF3 API on TR261123-0015 (12 bugs, DRA262611P0264 – P0275, `filed_bugcodes.md`); no existing ticket commented on. At drafting: first batch of this feature (`ebug-defaults.ts pdr/christmas-new-year-sale android`: no filed batch); no TR is named for 2611201 yet, so Creator, TRCode, source tag and method are for the reviewer. Dedupe: read-only eBug Search, Android pool only (per OS, user 2026-10-28): no open or resolved Android ticket matches an entry; the Christmas tickets in the pool are all from the 2025 campaign (15.9.x, closed). `dedupe.txt`.

Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, no video; no entry rests on a log); `[AIAgent]` / `[AIAgent][UI]` owner RD for defects; text with no spec source and open questions to PM (BugBelong PM), `[AIAgent][UX]` for the one user-experience decision (2026-11-11). Design first unless the PM item is newer (PM 1104 Update wins for the IAP card, ruling Q-10). Every row's precondition is a signed-in Free account; the run was signed out, so each entry names that condition and the account-tied pack row (TC-124) is held. Severity is proposed.

**What is drafted:** 12 entries (ISS-XMA-01…12): 2 RD Functional, 8 RD UI, 1 PM UI, 1 PM UX. Entry 12 comes from observation O-4 (seen on every IAP entry; its row TC-100 is Blocked only for the US store).

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.

---

## 1. ISS-XMA-01 — Interstitial: 「SAVE」 and 「vs. paying …/mo × 12」 stay English in all 26 other languages  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0264](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0264) · 2026-11-23 · TR261123-0015

**Report step:** TC-030 – TC-055 (26 rows), O-7  ·  **Reproduce:** 26/26  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-022 (PM rules 底圖 & 價格 + 多國文案 sheet; ruling Q-16: all 27 languages ship): the lines under the title art (Save, vs., CTA) are localized text made by RD per the sheet. Seen in all 26 non-English languages (TC-030 – TC-055), each run on pm clear + per-app locale (system language untouched). The CTA, disclaimer and bottom links are translated; only these lines and 「/year」 / 「More subscription plan」 (ISS-XMA-02) stay English. The app follows the Design layout (「SAVE」 「57」 「%」, 「vs. paying …/mo × 12」), the sheet gives one line 「Save 57%」 / 「vs. $6.79/mo」 per language, so the sheet's Save and vs. strings are the translations to use (with the store's % and monthly price, ruling Q-3). In Arabic and Persian the English line even takes local digits (「× ١٢」, 「× ۱۲」). Older campaigns had the same class of bug (DRA262607-0038 「Save up to」 not localized, closed).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][MUI] Christmas Sale (Interstitial): 「SAVE」 and 「vs. paying …/mo × 12」 are not localized
```

**Description:**

```
Repro Steps:
1. Clear the app data
2. Set the app language to 中文（台灣）
3. Launch the APP
4. Tap 「Get Started」
5. Tap 「Allow」 on the notification prompt
6. Look at the lines under the title art
7. Check the result

Result:
In every non-English language (26 of 26) 「SAVE」 and 「vs. paying NT$240/mo × 12」 stay in English.
摘要：所有非英文語系（26 種）的插頁仍顯示英文「SAVE」與「vs. paying NT$240/mo × 12」。
{16.9.0_xma01_cht.jpg} {16.9.0_xma01_rus.jpg} {16.9.0_xma01_ara_digits.jpg}

Expect Result:
Both lines use the 多國文案 sheet's Save and vs. text for the app language, with the store's % and price.
摘要：兩行文字應依多國文案表翻譯成該語系（百分比與月價依商店價格），例如繁中「現省 xx%」「相較於每月NT$240」。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (底圖 & 價格: lines under the art localized by RD per the linked 多國文案 sheet, Save and vs. rows) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/01_ISS-XMA-01/`

---

## 2. ISS-XMA-02 — Interstitial: 「/year」 and 「More subscription plan」 stay English in all 26 other languages; the sheet has no translation  ·  Class: UI  ·  Severity: S2  ·  Owner: PM

**Filed by:** ANGOL_HUANG · [DRA262611P0265](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0265) · 2026-11-23 · TR261123-0015

**Report step:** TC-030 – TC-055 (26 rows), O-7  ·  **Reproduce:** 26/26  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** Text with no spec source: the 多國文案 sheet translates only the title, Save, vs. and CTA; 「/year」 after the annual price and the link 「More subscription plan」 have no translation anywhere in the spec, so PM must supply them (AGENTS.md text rule 2026-11-11: PM when no sheet states it). Plainly wrong on screen (English in a localized page), so filed, not held. Same 26 rows as ISS-XMA-01.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][MUI] Christmas Sale (Interstitial): 「/year」 and 「More subscription plan」 are not localized
```

**Description:**

```
Repro Steps:
1. Clear the app data
2. Set the app language to Русский
3. Launch the APP
4. Tap 「Get Started」
5. Tap 「Allow」 on the notification prompt
6. Look at the annual price and the link under the trial terms
7. Check the result

Result:
「NT$1,210/year」 and 「More subscription plan」 are English in every non-English app language (26 of 26).
摘要：所有非英文語系中「/year」與「More subscription plan」仍為英文。
{16.9.0_xma02_rus.jpg} {16.9.0_xma02_jpn.jpg}

Expect Result:
PM to supply 「/year」 and 「More subscription plan」 for the 26 languages; then both show translated.
摘要：請 PM 提供 26 種語系的「/year」與「More subscription plan」翻譯。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (linked 多國文案 sheet: no row for 「/year」 or 「More subscription plan」) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Interstitial board (「/year」, 「More subscription plan」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19946
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/02_ISS-XMA-02/`

---

## 3. ISS-XMA-03 — Interstitial: CTA wording differs from the 多國文案 sheet in 12 languages  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0266](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0266) · 2026-11-23 · TR261123-0015

**Report step:** TC-030 – TC-051 (12 rows), O-7  ·  **Reproduce:** 12/12  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-022: the CTA is RD's localized text per the 多國文案 sheet. The app shows the generic trial string instead in 12 languages; the other 14 match. Note ESP shows the ESP (MX) sheet text and ESP (MX) a third wording. App vs sheet: CHT 「7 天免費試用」 vs 「７天免費試用」 (full-width 7, no space); CHS 「7 天免费试用」 vs 「7天免费试用」; FRA 「Recevoir 7 jours d'essai gratuits」 vs 「Essai gratuit de 7 jours」; ITA 「Prova Gratuita di 7gg.」 vs 「Prova Gratis per 7gg.」; JPN 「７日間無料お試し」 vs 「7 日間無料で試す」; KOR 「7일 무료 체험」 vs 「7일 무료 체험 시작하기」; ESP 「Prueba gratis por 7 días」 vs 「Prueba 7 días gratis」; RUS 「7-дн. беспл. пробное」 vs 「Попробовать 7 дней бесплатно」; ESP (MX) 「Inicia tu prueba gratuita de 7 días」 vs 「Prueba gratis por 7 días」; Viet 「Dùng Thử Miễn Phí 7 Ngày」 vs 「Dùng thử miễn phí 7 ngày」; Arabic 「ابدأ تجربة مجانية لمدة 7 أيام」 vs 「بدء تجربة مجانية لمدة 7 أيام」; Hebrew 「נסה בחינם למשך 7 ימים」 vs 「ניסיון חינם ל-7 ימים」.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][MUI] Christmas Sale (Interstitial): CTA text differs from the 多國文案 sheet in 12 languages
```

**Description:**

```
Repro Steps:
1. Clear the app data
2. Set the app language to Français
3. Launch the APP
4. Tap 「Get Started」
5. Tap 「Allow」 on the notification prompt
6. Look at the yellow button
7. Check the result

Result:
The CTA reads 「Recevoir 7 jours d'essai gratuits」 (FRA); 12 languages differ from the sheet.
摘要：12 種語系的 CTA 與多國文案表不同（例如法文、俄文、韓文、日文）。
{16.9.0_xma03_fra.jpg} {16.9.0_xma03_rus.jpg} {16.9.0_xma03_kor.jpg} {16.9.0_xma03_jpn.jpg}

Expect Result:
The CTA uses the sheet's text in each language (FRA 「Essai gratuit de 7 jours」).
摘要：CTA 應使用多國文案表的各語系文字。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (linked 多國文案 sheet, CTA row) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/03_ISS-XMA-03/`

---

## 4. ISS-XMA-04 — Interstitial: bottom links run into each other or into the separators in RUS, FRA, UKR and Polish  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0267](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0267) · 2026-11-23 · TR261123-0015

**Report step:** TC-042, TC-032, TC-055, TC-049, O-7  ·  **Reproduce:** 4/4  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-022 rows check 「No text clipped, overlapped or in another language」. Measured from the page source: RUS 「Условия обслуживания」 (x 78–366), 「Политика конфиденциальности」 (344–738) and 「Восстановить покупку」 (720–996) overlap each other and the separators; FRA both separators touch 「Politique de confidentialité」; UKR 「Політика конфіденційності」 (376–706) under both separators (381, 698), the right one over its last letter; Polish the left separator (381) touches 「Warunki korzystania z usługi」 (63–385).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][RUS/FRA/UKR/POL] Christmas Sale (Interstitial): Bottom links overlap each other or separators
```

**Description:**

```
Repro Steps:
1. Clear the app data
2. Set the app language to Русский
3. Launch the APP
4. Tap 「Get Started」
5. Tap 「Allow」 on the notification prompt
6. Look at the three links at the bottom
7. Check the result

Result:
RUS: the three links overlap each other; FRA, UKR, Polish: separators touch or cover the link text.
摘要：俄文三個連結互相重疊並壓到分隔線；法文、烏克蘭文、波蘭文分隔線碰到或壓到文字。
{16.9.0_xma04_rus_links.jpg} {16.9.0_xma04_fra_links.jpg} {16.9.0_xma04_ukr_links.jpg} {16.9.0_xma04_pol.jpg}

Expect Result:
The three links and their separators sit apart with nothing overlapping (wrap or shrink the links when they do not fit).
摘要：三個連結與分隔線應各自分開、不重疊。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Interstitial board (「Terms of Service」 | 「Privacy Policy」 | 「Restore purchase」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19946
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/04_ISS-XMA-04/`

---

## 5. ISS-XMA-05 — Interstitial (Polish): the CTA wraps to two lines that fill the button edge to edge  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0268](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0268) · 2026-11-23 · TR261123-0015

**Report step:** TC-049  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-022 (Polish CTA 「Rozpocznij 7-dniowy bezpłatny okres próbny」, text matches the sheet). The text box spans x 63–1017, the whole button, so the words touch the rounded ends; the Design draws one line centred with padding.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][POL] Christmas Sale (Interstitial): CTA wraps to two lines with no side padding in the button
```

**Description:**

```
Repro Steps:
1. Clear the app data
2. Set the app language to Polski
3. Launch the APP
4. Tap 「Get Started」
5. Tap 「Allow」 on the notification prompt
6. Look at the yellow button
7. Check the result

Result:
The Polish CTA wraps to two lines that run to both edges of the button.
摘要：波蘭文 CTA 折成兩行，文字貼滿按鈕左右兩端，沒有內距。
{16.9.0_xma05_pol_cta.jpg}

Expect Result:
The CTA text sits inside the button with side padding (one line, smaller text or a taller button).
摘要：CTA 文字應在按鈕內保留左右內距。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Interstitial board (CTA 「Get 7-Day Free Trial」, one line) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19946
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/05_ISS-XMA-05/`

---

## 6. ISS-XMA-06 — Interstitial and IAP show 57% where the store prices give 57.99% (58%)  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0269](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0269) · 2026-11-23 · TR261123-0015

**Report step:** TC-030 – TC-055 (26 rows), O-3  ·  **Reproduce:** 3/3  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-018 / R-036, ruling Q-3 (REQ-002): the % is computed by the app from the store's campaign prices (PM 「Xmas 年價格 vs 月價格*12個月的價差%」); Q-3 itself says TW gives 58%. On the Taiwan store (NT$1,210/year, NT$240/month, both shown on the page) (2880 − 1210) ÷ 2880 = 57.99%, but the interstitial (every language, TC-029 – TC-055) and the IAP card (TC-019, TC-100) show 57: either truncated or the mockups' fixed 57. The US store ($45.99 / $6.99 → 45%) tells them apart; it waits for Play Billing Lab (TC-013, TC-101 Blocked). If truncation is intended, RD forwards it to PM to rule on rounding. Listed on the Fail rows' Report step because each language row noted it; those rows fail on the text items too.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] Christmas Sale (IAP): Discount shows 57% though NT$1,210 vs NT$240 × 12 gives 57.99%
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Close the Christmas interstitial with X
3. Tap the top pill on the Launcher
4. Look at the annual plan card
5. Tap the back arrow
6. Clear the app data
7. Launch the APP
8. Tap 「Get Started」
9. Tap 「Allow」 on the notification prompt
10. Look at the big percentage
11. Check the result

Result:
Both pages show 57% while their own prices, NT$1,210/year and NT$240/month, give 57.99%.
摘要：插頁與 IAP 顯示 57%，但 NT$1,210 與 NT$240×12 計算為 57.99%。
{16.9.0_xma06_interstitial_57.jpg} {16.9.0_xma06_iap_57.jpg}

Expect Result:
The % is computed from the store's campaign prices and rounded: 58% on the Taiwan store, 45% on the US store (Q-3).
摘要：百分比應由商店價格計算並四捨五入：台灣 58%、美國 45%。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-rules board (➍ formula: 年價格 vs 月價格*12個月的價差%) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Interstitial board (「SAVE」 「<xx>」 「%」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19946
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/06_ISS-XMA-06/`

---

## 7. ISS-XMA-07 — Launcher: the top banner shows 「Turn one photo to cinematic reel」, not 「Make Christmas magic with AI」  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0270](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0270) · 2026-11-23 · TR261123-0015

**Report step:** TC-083, TC-084  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-026 (Design Launcher dark / light, PM rules ➌). The banner image is a Christmas picture, so the campaign banner may be on with the wrong title, or the Stage CMS still holds the Cinematic Reel banner text; RD to say which. Unchanged over 15 s (no rotation). Legibility in dark and light mode is fine. Banner target (Q-7) not judged.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Launcher): Top banner title is not 「Make Christmas magic with AI」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap X on the Christmas interstitial
3. Look at the top banner title
4. Check the result

Result:
The top banner shows a Christmas image titled 「Turn one photo to cinematic reel」, in dark and light mode.
摘要：頂部橫幅標題為「Turn one photo to cinematic reel」。
{16.9.0_xma07_dark.jpg} {16.9.0_xma07_light.jpg}

Expect Result:
The top banner is the Christmas banner titled 「Make Christmas magic with AI」 › in dark and light mode.
摘要：頂部橫幅應為聖誕橫幅，標題「Make Christmas magic with AI」。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Launcher & dialog board (Launcher dark / light: 「Make Christmas magic with AI」) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2772-10246
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/07_ISS-XMA-07/`

---

## 8. ISS-XMA-08 — Launcher: the top pill reads only 「Pro」, not 「Try Pro 7 days for free」  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0271](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0271) · 2026-11-23 · TR261123-0015

**Report step:** TC-087, TC-090  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-028 (Design Launcher pill 「Try Pro+ 7 days for free」 with Santa hat; ruling Q-8: Android says Pro, never Pro+). The Santa-hat icon is right and the pill opens the Christmas IAP page; no countdown (as expected for Christmas). The Mine tab's pill in the same state does read 「Try Pro 7 days for free」 (TC-095, TC-098), so only the Launcher pill is short.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Launcher): Top pill reads 「Pro」, not 「Try Pro 7 days for free」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap X on the Christmas interstitial
3. Look at the pill at the top of the Launcher
4. Check the result

Result:
The Launcher pill reads only 「Pro」 with the Santa hat; Mine's pill reads 「Try Pro 7 days for free」.
摘要：Launcher 頂部膠囊只顯示「Pro」（Mine 頁的膠囊則為「Try Pro 7 days for free」）。
{16.9.0_xma08_launcher_pill.jpg} {16.9.0_xma08_mine_pill.jpg}

Expect Result:
The Launcher top pill reads 「Try Pro 7 days for free」 with the Santa-hat icon (Pro, never Pro+).
摘要：Launcher 頂部膠囊應顯示「Try Pro 7 days for free」並有聖誕帽圖示。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Launcher & dialog board (top pill 「Try Pro+ 7 days for free」, Santa hat; Pro per ruling Q-8) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2772-10246
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/08_ISS-XMA-08/`

---

## 9. ISS-XMA-09 — IAP opened from the interstitial: back arrow and system Back go to the Launcher, not back to the interstitial  ·  Class: UX  ·  Severity: S3  ·  Owner: PM

**Filed by:** ANGOL_HUANG · [DRA262611P0272](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0272) · 2026-11-23 · TR261123-0015

**Report step:** TC-109, O-5  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** Question for PM, filed for a decision (AGENTS.md 2026-11-11). R-042 says the IAP back arrow ‹ returns to the page it was opened from, R-061 that system Back does what ‹ does. From the interstitial both land on the Launcher (TC-109, and ‹ in R1-a TC-019 / O-5). Whether closing the interstitial on the way back is intended (it shows once a day) is not stated; an older ticket on 15.9.1 (DRA252511-0129, closed) complained that Back from the plans 「briefly shows interstitial before launcher」.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UX] Christmas Sale (IAP): Back from IAP opened via 「More subscription plan」 skips the interstitial
```

**Description:**

```
Repro Steps:
1. Clear the app data
2. Launch the APP
3. Tap 「Get Started」
4. Tap 「Allow」 on the notification prompt
5. Tap 「More subscription plan」
6. Press system Back
7. Check the result

Result:
System Back (and the ‹ arrow) on the IAP page goes to the Launcher Home; the interstitial is gone.
摘要：從插頁進入 IAP 後，按系統返回鍵（或左上返回）直接回到 Launcher，不回插頁。
{16.9.0_xma09_iap_from_interstitial.jpg} {16.9.0_xma09_after_back.jpg}

Expect Result:
PM to decide: should Back return to the interstitial (R-042) or close both to the Launcher?
摘要：請 PM 決定：從此 IAP 返回應回到插頁，或直接回到 Launcher？

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), IAP & Credit board (IAP_year back arrow ‹) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19947
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-launch board (flow arrow 「More subscription plan」 → IAP_T1) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-31190
Basis: In-product — Christmas IAP page: its back arrow returns to the page it was opened from (R-042); the interstitial case is not stated
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/09_ISS-XMA-09/`

---

## 10. ISS-XMA-10 — Short screen: the IAP banner title 「Christmas Special」 is clipped at the bottom  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0273](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0273) · 2026-11-23 · TR261123-0015

**Report step:** TC-143  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-023 (Design 「短裝置」 Pixel 2 411×731 frames 2750:20070, 2750:20280). The run set wm size 1080×1920 at 420 dpi = 411×731 dp (restored after). The banner shrinks to a 245 px strip and the descender of 「p」 in 「Special」 is cut off; the ‹ arrow sits on a snowflake. The interstitial and the credit pages fit.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (IAP): [Short screen] Banner title 「Christmas Special」 is clipped at the bottom
```

**Description:**

```
Repro Steps:
1. Set the screen to 411 × 731 dp (a short Android screen)
2. Clear the app data
3. Launch the APP
4. Tap 「Get Started」
5. Tap 「Allow」 on the notification prompt
6. Tap 「More subscription plan」
7. Look at the banner title
8. Check the result

Result:
The banner is cut to a short strip and the bottom of 「Special」 (the descender of 「p」) is clipped.
摘要：短螢幕下 IAP 橫幅被壓縮，「Special」底部（p 的下緣）被裁切。
{16.9.0_xma10_short_iap.jpg} {16.9.0_xma10_title_crop.jpg}

Expect Result:
On the short screen the whole title 「Christmas Special」 shows, as the short-device frame draws it.
摘要：短螢幕下應完整顯示「Christmas Special」，不被裁切。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), IAP & Credit board (短裝置 IAP_year, Pixel 2 411×731) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19947
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/10_ISS-XMA-10/`

---

## 11. ISS-XMA-11 — Landscape: the Launcher shows no Christmas top banner  ·  Class: Functional  ·  Severity: S3  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0274](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0274) · 2026-11-23 · TR261123-0015

**Report step:** TC-144  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-059 (Design Landscape: the campaign top banner and pill over the landscape Launcher). The run turned the phone with auto-rotate off and user_rotation 1 (the app follows: w832dp h387dp); restored after. The pill (Santa hat, 「Pro」, ISS-XMA-08) shows; no banner image or title at all. Landscape IAP (TC-146) is right.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] Christmas Sale (Launcher): [Landscape] Launcher shows no Christmas top banner
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap X on the Christmas interstitial
3. Turn the phone to landscape
4. Look at the top of the Launcher
5. Check the result

Result:
In landscape the Launcher shows the pill, the tool row and My Projects, but no Christmas top banner.
摘要：橫向時 Launcher 沒有聖誕頂部橫幅。
{16.9.0_xma11_landscape.jpg}

Expect Result:
In landscape the Christmas top banner and pill show over the Launcher, as the Design draws it.
摘要：橫向時應顯示聖誕頂部橫幅與膠囊。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Landscape board (Launcher landscape with the campaign banner) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-27885
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/11_ISS-XMA-11/`

---

## 12. ISS-XMA-12 — IAP plan card: tag 「Special Offer」 and 「57% OFF」, not 「Christmas Treat」 and 「Save 57%」; monthly price not struck  ·  Class: UI  ·  Severity: S2  ·  Owner: RD

**Filed by:** ANGOL_HUANG · [DRA262611P0275](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0275) · 2026-11-23 · TR261123-0015

**Report step:** O-4  ·  **Reproduce:** 3/3  ·  **Verified on:** 16.9.0.2611201

> **QA note — not pasted into eBug.** R-035 / R-037 (PM 1104 Update, ruling Q-10: the PM 1104 version wins over the older Design 「Special Offer」 / 「67% OFF」). Seen on every IAP entry (TC-006, TC-019, TC-087, TC-096, TC-146); recorded at TC-100, which is Blocked only because its US prices need Play Billing Lab: the tag text, the % wording and the missing struck price do not depend on the store. Also differs on the page: CTA 「Continue」 (Design 「Get 7-Day Free Trial」) and the feature strip is a carousel with 「No Watermark」 rather than the three cards — left to the reviewer, not in this entry.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (IAP): Tag 「Special Offer」 and 「57% OFF」 instead of 「Christmas Treat」, 「Save xx%」
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap X on the Christmas interstitial
3. Tap the top pill on the Launcher
4. Look at the annual and monthly plan cards
5. Check the result

Result:
The tag reads 「Special Offer」, the card 「57% OFF」, and the monthly price is not struck through.
摘要：年方案標籤為「Special Offer」、顯示「57% OFF」，月方案無劃掉原價。
{16.9.0_xma12_iap_card.jpg} {16.9.0_xma12_iap_from_interstitial.jpg}

Expect Result:
Tag 「Christmas Treat」, 「Save <xx>%」, and the monthly card's original price struck through (PM 1104).
摘要：標籤應為「Christmas Treat」、「Save xx%」，月方案顯示劃掉的原價。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, RD test date); Free account, signed out; Play store Taiwan
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-launch board (1104 Update, IAP: 「Christmas Treat」, struck monthly price, no 「Offer」) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), IAP & Credit board (IAP_year plan cards) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-19947
<Claude Reviewed>
```

**Images:** `20261123_eBug_drafts_Christmas-Sale-R1_16.9.0_images/12_ISS-XMA-12/`

---

# Not raised (for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| TC-095 | Mine Free card reads 「15+ Benefits」, the Design draws 「20+ Benefits」 | Already ruled by a ticket: DRA262608-0134 (16.6.0, closed) changed Mine to 「15+ Benefits」 on purpose (DRA262608-0146 for other languages); the Christmas Design copies the old figure. Cited, not filed (ebugs.md step 1). The row's other checks passed. |
| TC-124 | Christmas 500-credit pack missing for the Free user; the pack page shows 「First Purchase Discount」 1000 +1000 | Held: the row needs a signed-in Free account and the run was signed out (sign-in 403, O-9); credit offers are account-tied, so recheck signed in in the R1-d rerun. The sale price is also undecided (Q-13). |
| O-1 | ToS / Privacy Policy open the Traditional Chinese pages on an English app | Spec silent; likely chosen by region (Taiwan). Report only. |
| O-2 | First Restore after a fresh launch returns with no message after the accounts permission | TC-028 passed on the second tap; report only (candidate for a later row). |
| O-6 | Play Billing Lab not signed in (needs Google's terms accepted) | Environment; the user's go-ahead is needed. |
| O-8 | AI Mini Drama intro sits between the Open intro and the interstitial on the 2nd launch | TC-009 passed; another feature's intro. Report only. |
| O-9 | Stage sign-in after pm clear fails: bindMember HTTP 403 | Same OS, same build already filed: DRA262611P0200 (Sign in CL account fail, Assigned) and DRA262611P0253 (Sign in fail if install AP via APK, 2611201): dedupe.txt only. |
| O-10 | 「Unofficial Version」 「We couldn't verify your app installation. Purchases are unavailable.」 on every subscription CTA | Environment: build sideloaded with adb (installer not Google Play); related to DRA262611P0253. Blocks R1-d; report only. |
| Blocked (41) | 41 test-data | No verdict (reasons in report.md and blocked-reasons.json): R1-d not run (purchases unavailable, sign-in 403), Play Billing Lab terms, RD date fixed, no old build, portrait-only interstitial. |

## Reconciliation against the run

35 Fail (all defect), 41 Blocked, 10 observations (O-1 … O-10).

| Step | Count | Running total |
|---|---|---|
| Fail rows + observations | 45 | 45 |
| → not raised, held or cited (TC-095 cited, TC-124 held, 6 observations) | −8 | 37 |
| → observations folded into entries (O-3, O-4, O-5, O-7) | −4 | 33 |
| → merged: 33 rows share 11 defects or questions; entry 12 rests on O-4 | | **12 entries** |

### Row-by-row map

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-030 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-031 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-032 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 4. ISS-XMA-04; 6. ISS-XMA-06 |
| TC-033 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-034 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-035 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-036 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-037 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-038 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-039 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-040 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-041 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-042 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 4. ISS-XMA-04; 6. ISS-XMA-06 |
| TC-043 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-044 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-045 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-046 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-047 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-048 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-049 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 4. ISS-XMA-04; 5. ISS-XMA-05; 6. ISS-XMA-06 |
| TC-050 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-051 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 3. ISS-XMA-03; 6. ISS-XMA-06 |
| TC-052 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-053 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-054 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 6. ISS-XMA-06 |
| TC-055 | Fail | defect | 1. ISS-XMA-01; 2. ISS-XMA-02; 4. ISS-XMA-04; 6. ISS-XMA-06 |
| TC-083 | Fail | defect | 7. ISS-XMA-07 |
| TC-084 | Fail | defect | 7. ISS-XMA-07 |
| TC-087 | Fail | defect | 8. ISS-XMA-08 |
| TC-090 | Fail | defect | 8. ISS-XMA-08 |
| TC-095 | Fail | defect | cited DRA262608-0134 |
| TC-109 | Fail | defect | 9. ISS-XMA-09 |
| TC-124 | Fail | defect | held: recheck signed in |
| TC-143 | Fail | defect | 10. ISS-XMA-10 |
| TC-144 | Fail | defect | 11. ISS-XMA-11 |
| O-1 | observation | — | not raised |
| O-2 | observation | — | not raised |
| O-3 | observation | — | folded into 6. ISS-XMA-06 |
| O-4 | observation | — | folded into 12. ISS-XMA-12 |
| O-5 | observation | — | folded into 9. ISS-XMA-09 |
| O-6 | observation | — | not raised |
| O-7 | observation | — | folded into 1–5. ISS-XMA-01…05 |
| O-8 | observation | — | not raised |
| O-9 | observation | — | not raised (existing ticket, dedupe.txt) |
| O-10 | observation | — | not raised |

### Owner split

| Owner | Entries |
|---|---|
| RD | 1, 3, 4, 5, 6, 7, 8, 10, 11, 12 |
| PM | 2, 9 |

### Filing order

By severity: **1**, **2**, **7**, **8**, **12**, **3**, **4**, **5**, **6**, **9**, **10**, **11**. Nothing is filed until the review page's decisions come back.
