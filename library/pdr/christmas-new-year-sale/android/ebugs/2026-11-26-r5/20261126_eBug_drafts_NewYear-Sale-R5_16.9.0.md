# Christmas & New Year Sales (Android) — eBug drafts, round R5 (light mode and the Mine / Pro Credits bar), PDR-A 16.9.0 build 2611251

**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-26-r5-light-mine/` — round R5 (2026-11-26 17:20–17:45, REQ-010: A. New Year IAP annual card in light mode, TC-102; B. landscape IAP in light mode, TC-146; C. Mine / Pro Credits bar proportion, O-5 / O-8), on Samsung Galaxy A51 SM-A516B / Android 13 through Appium / UiAutomator2, build 16.9.0.2611251, Stage server, acda.test9 (Free 22 credits, then Pro 122 by the test subscription), light/dark by the system switch with the app's Appearance on 「Device Settings」. R5 tally: 0 Pass, 2 Fail (TC-102, TC-146), 0 Blocked; 8 observations.

**Status:** nothing filed, uploaded or commented. Seventh batch of this feature (R1, R1r, R2, R3, R4, R4-b filed: P0254–P0275, P0299–P0313, P0327–P0329). Dedupe: per OS, read-only (`dedupe.txt`). Plan-card texts are NAB by the user's ruling on DRA262611P0309 and are not re-raised.

Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` owner RD for defects, no `[UX]`. Severity is proposed. Visual findings: no logs.

**What is drafted:** 3 entries (ISS-XMA-44 – ISS-XMA-46): 3 RD UI.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.

---

## 1. ISS-XMA-44 — New Year IAP page: the annual plan card keeps its dark-mode navy background in light mode (portrait and landscape)  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-102, TC-146, O-1  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611251

> **QA note — not pasted into eBug.** REQ-010 (user, 2026-11-26): 「但在Light mode下New Year Sales IAP年方案卡片的背景顏色不對(用到Dark mode圖樣)」. Background only: the plan-card texts (Special Offer / 57% OFF / NT$1210/Year) follow the Design and were ruled NAB by the user on DRA262611P0309, so they are not raised here and P0309 is not a duplicate (it is about text, this is the card's background); P0309 is not commented on. Measured (R5-a, 12/30, Mine 「Claim Holiday Deal」, Free, acda.test9): the annual card is navy (3,24,114) at the left edge to (19,49,152) on the right in LIGHT mode, pixel-identical to DARK mode; the page background follows the mode (249,251,255 light / 12,12,12 dark). Design New Year IAP & Credit board: light IAP_year 2855:39936 draws a pale cream card (251,246,221), dark IAP_year 2855:39855 a dark navy card (9,18,55). Control: Christmas on 12/24 follows the mode, light cream (251,246,223)-(251,247,231) = Design light, dark burgundy (64,7,10)-(76,9,12) = Design dark. Merge (ebugs.md step 1, one defect per entry): TC-146's landscape New Year annual card (17,47,149) in light is the same card and the same art in another orientation, so it is folded in here rather than into ISS-XMA-45, whose defects (separators, monthly border) are landscape-only and affect both seasons. Class UI, RD: the Design states the light card and the app shows the dark one. S3: the whole selected plan card is the wrong scheme on the purchase page in light mode, readable, nothing blocked. O-1: the app's Appearance (☰ › Preferences) overrides the system dark mode; the run used 「Device Settings」. Visual finding: no log (overlay rule 3).

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (IAP): Annual plan card uses the dark-mode background in light mode
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-30 in Settings (automatic date and time off)
2. Set the phone to light mode in Settings
3. Launch the APP
4. Tap 「Mine」
5. Tap 「Claim Holiday Deal」
6. Look at the annual plan card
7. Check the result

Result:
In light mode the annual card has the dark-mode navy background, the same pixels as in dark mode.
摘要：淺色模式下年方案卡片仍是深色模式的深藍背景，與深色模式完全相同。
{16.9.0_xma44_light.jpg} {16.9.0_xma44_dark.jpg} {16.9.0_xma44_land_light.jpg} {16.9.0_xma44_design.jpg}

Expect Result:
In light mode the annual card has the light background the Design draws (pale cream), as Christmas does.
摘要：淺色模式下年方案卡片應為設計稿的淺色（米白）背景，與聖誕節一致。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: New Year sale window (Stage server, phone date 2026-12-30); build 2611251; Free account, signed in; app Appearance 「Device Settings」 with the system in light mode (also with Appearance 「Light Mode」)
Related: the Christmas IAP annual card follows the mode (cream in light, burgundy in dark)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year IAP & Credit board (IAP_year, light: cream annual card) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2855-39936
<Claude Reviewed>
```

**Images:** `20261126_eBug_drafts_NewYear-Sale-R5_16.9.0_images/01_ISS-XMA-44/`

---

## 2. ISS-XMA-45 — Landscape IAP page: link separators and monthly card border keep fixed colours, separators invisible in light mode  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-146  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611251

> **QA note — not pasted into eBug.** REQ-010 (user, 2026-11-26): 「TC-146 Landscape mode下的Light mode的UI，雖然Design spec沒有畫出來，但配色應該也要follow light mode設定」. The Design draws landscape in the dark scheme only (Christmas board 2750:27885, New Year 2844:22907), so the basis is the app's own portrait IAP page in each mode plus the user's ruling (Basis: In-product); Class UI, owner RD, not [UX] (rule 5). Measured (R5-a, both seasons identical): the 「|」 separators between Terms of Service / Privacy Policy / Restore Purchase are white (255,255,255) in light and in dark, so they vanish on the light background (249,251,255); portrait draws them (176,186,204) light / (89,97,110) dark. The monthly card border is (204,213,225) in both modes; portrait (176,186,204) light / (54,59,67) dark, so in light it is fainter than portrait and in dark it becomes a bright outline. Landscape follows the mode for the right-side background, monthly fill, prices, disclaimer and link text (same values as portrait). The New Year annual card in landscape is ISS-XMA-44 (same card as portrait). Closed same-OS tickets from last year's sale (15.9.1) fixed other landscape IAP colours: DRA252511-0121 / 0122 (the selected monthly plan's highlight, light / dark) and DRA252512-0005 (prices, discount and terms text colours; RD added landscape colours for the Christmas / New Year period); the separators and the unselected monthly border were not named, so this stays a new entry naming them as related (overlay rule 7, closed tickets). The two elements are merged: one screen, one cause (the landscape layout's fixed colours), the same Repro steps. S3: the links lose their separators in light mode and the border is wrong in both, nothing blocked. Visual finding: no log.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Christmas & New Year Sale (Landscape IAP): Separators invisible in light, border not themed
```

**Description:**

```
Repro Steps:
1. Set the phone date to 2026-12-24 in Settings (automatic date and time off)
2. Set the phone to light mode in Settings
3. Turn auto-rotate off
4. Launch the APP
5. Tap the sale pill at the top of the Launcher
6. Turn the phone to landscape
7. Look at the links and the monthly card
8. Check the result

Result:
In landscape the 「|」 separators are white in both modes (invisible in light) and the monthly border is a fixed grey.
摘要：橫向時連結間的「|」分隔線在兩種模式都是白色（淺色下看不見），月方案外框顏色固定不變。
{16.9.0_xma45_xmas_land_light.jpg} {16.9.0_xma45_ny_land_light.jpg} {16.9.0_xma45_xmas_land_dark.jpg} {16.9.0_xma45_portrait_light.jpg}

Expect Result:
Separators and monthly border follow light/dark mode with the colours portrait uses.
摘要：分隔線與月方案外框應跟隨淺色／深色模式，使用直向畫面的顏色。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas (phone date 2026-12-24) and New Year (2026-12-30) sale windows, Stage server; build 2611251; Free account, signed in; auto-rotate off, landscape; app Appearance 「Device Settings」; closed 15.9.1 landscape IAP colour tickets: DRA252511-0121 / 0122 (selected monthly highlight), DRA252512-0005 (text colours)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Christmas Landscape board (IAP, dark only) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2750-27885
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), New Year Landscape board (IAP, dark only) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2844-22907
Basis: In-product — IAP page in portrait: light mode draws the 「|」 separators and the monthly card border grey (176,186,204), dark mode (89,97,110) / (54,59,67)
<Claude Reviewed>
```

**Images:** `20261126_eBug_drafts_NewYear-Sale-R5_16.9.0_images/02_ISS-XMA-45/`

---

## 3. ISS-XMA-46 — Mine / Pro page: the Credits bar under the Free / Pro card is 27 % taller than the Design  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** O-5, O-8  ·  **Reproduce:** 4/4  ·  **Verified on:** 16.9.0.2611251

> **QA note — not pasted into eBug.** REQ-010 (user, 2026-11-26): 「Mine / Pro頁裡 Free/Pro卡片下方Credits橫條的高度比例看起來與Design Figma上面比例不符，這個請你額外測量比例後去列隻Mine / Pro 頁的bug」. No casebook row covers the bar's height (O-5, O-8), so the Report step names the observations. Figma (figma-design get_metadata, specs/2026-11-20/extracted/figma-mine-credit-bar.json): mine_free 2682:13540 card 343×232, credit bar 343×56 (y 176 in the card); mine_vip 2718:4363 card 343×180, bar 343×56 (y 124); bar content icon+「Credits」 y 16 h 24, value+chevron y 18 h 20. App (page source, mine-credit-bar.json): Free card 996×778, Pro card 996×529, credit_remain_area 996×207 in both, light and dark identical (Free/Pro light and dark = 4 of 4). Content is vertically centred within 1 px; the extra height is padding (icon row 77 px above and below vs 46.5; value row 68 vs 52.3) while the content itself is smaller (icon 53 vs 69.7 px). Free card 778 vs 673.7 (+15.5 %) mostly from the bar; Pro card 529 vs 522.7 (+1.2 %), so the Pro card's top part is shorter and the bar takes 39 % of the card instead of 31 %. The Design draws Mine in dark only and calls the paid card 「VIP」; the app's tab reads 「Mine」 for Free and 「Pro」 for Pro (O-7), so the feature is named 「Mine / Pro Page」 as the user did. Class UI, RD: the Design states the size. S3 like the other layout tickets of this batch (reviewer may lower to S4: proportion only, nothing hidden or blocked). Comparison block in the Note as ISS-XMA-31 (DRA262611P0304 convention). Visual finding: no log.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI] Mine / Pro Page (Credits Bar): Credits bar 27% taller than Design, card proportions off
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap 「Mine」 (「Pro」 for a Pro account)
3. Look at the Credits bar under the Free / Pro card
4. Check the result

Result:
The Credits bar is 207 px tall against 163 px from the Design (+27 %), so it takes too much of the card.
摘要：Credits 橫條高 207 px，設計稿換算為 163 px（高 27%），占卡片比例過大。
{16.9.0_xma46_free_vs_figma.jpg} {16.9.0_xma46_pro_vs_figma.jpg} {16.9.0_xma46_free_light.jpg} {16.9.0_xma46_pro_light.jpg}

Expect Result:
The bar keeps the Design's height (56 of the card's 343 width, 163 px here): 0.241 of the Free card, 0.311 of Pro.
摘要：Credits 橫條應為設計稿高度（此機 163 px），約占 Free 卡 0.241、Pro 卡 0.311。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Free (balance 22) and Pro (122) on acda.test9, light and dark the same; build 2611251; Stage server
Comparison: Credits bar, Figma vs app (1 Figma px = 2.904 px: card 343 px = 996 px)
- Bar height: Figma 56 (= 162.6 px) / app 207 px (+27.3 %)
- Bar height / Free card height: Figma 56/232 = 0.241 / app 207/778 = 0.266
- Bar height / Pro card height: Figma 56/180 = 0.311 / app 207/529 = 0.391
- Bar height / card width: Figma 0.163 / app 0.208
- Space above and below the icon row: Figma 16 (= 46.5 px) / app 77 px
- Credits icon: Figma 24 (= 69.7 px) / app 53 px (-24 %)
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Launcher & dialog board (mine_free: card 343×232, Credits bar 56) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2682-13540
Spec Link: Christmas & New Year Design spec ([MX] Christmas & New Year, page 2026), Launcher & dialog board (mine_vip: card 343×180, Credits bar 56) -
https://www.figma.com/design/HpkQG91Rm4POCXpzjC1QbT/-MX--Christmas---New-Year?node-id=2718-4363
<Claude Reviewed>
```

**Images:** `20261126_eBug_drafts_NewYear-Sale-R5_16.9.0_images/03_ISS-XMA-46/`

---

## Not raised (for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-1 | The app's Appearance 「Light Mode」 overrides the system dark switch; the run used 「Device Settings」 | Intended setting; tooling note (folded into the ISS-XMA-44 QA note). |
| O-2 | Start state: acda.test9 Free with 22 credits, phone date 2027-01-01 | Account state. |
| O-3 | Mine's top pill counts down in the New Year window (contradicts KF-004) | Knowledge correction for KF-004, not a spec defect; parked for the knowledge wrap-up. |
| O-4 | IAP page opened from the Launcher pill is outside the page source; system Back reaches the Launcher | Tooling limit; Back behaviour already covered by earlier tickets (R1). |
| O-6 | New Year interstitial shown after the date change | Expected (KF-003). |
| O-7 | Pro test subscription bought; tab label reads 「Pro」 | Setup for request C. |
| TC-102 texts | Plan-card texts Special Offer / 57% OFF / NT$1210/Year | Ruled NAB by the user (DRA262611P0309 follows the Design); not re-raised. |

## Reconciliation against the run

2 Fail in R5 (TC-102, TC-146), 0 Blocked, 8 observations (O-1 … O-8). TC-102 and TC-146's landscape New Year card are one defect (ISS-XMA-44); TC-146's separators and monthly border are a second (ISS-XMA-45); request C (O-5, O-8) is ISS-XMA-46. 2 Fail rows + 1 request → 3 entries.

### Row-by-row map

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-102 | Fail | defect | 1. ISS-XMA-44 |
| TC-146 | Fail | defect | 1. ISS-XMA-44 (New Year annual card); 2. ISS-XMA-45 (separators, monthly border) |
| O-1 | observation | — | not raised; folded into 1. ISS-XMA-44 (QA note) |
| O-2 | observation | — | not raised |
| O-3 | observation | — | not raised |
| O-4 | observation | — | not raised |
| O-5 | observation | — | folded into 3. ISS-XMA-46 |
| O-6 | observation | — | not raised |
| O-7 | observation | — | not raised |
| O-8 | observation | — | folded into 3. ISS-XMA-46 |

### Owner split

| Owner | Entries |
|---|---|
| RD | 1, 2, 3 |

### Filing order

**1**, **2**, **3**. Nothing is filed until the review page's decisions come back.
