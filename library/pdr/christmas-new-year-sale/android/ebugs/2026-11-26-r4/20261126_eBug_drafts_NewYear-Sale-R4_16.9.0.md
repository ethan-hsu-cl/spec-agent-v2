# Christmas & New Year Sales (Android) — eBug drafts, round R4 (Not Enough Credit dialog in 26 languages), PDR-A 16.9.0 build 2611251

**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-26-r4-dialog-mui/` — round R4 of draft `drafts/20261126-154459` (in review, not yet saved; R-070, Q-19, TC-153 – TC-204, REQ-009), 2026-11-26, on Samsung Galaxy A51 SM-A516B / Android 13 through Appium / UiAutomator2, build 16.9.0.2611251, Stage server, phone date 2026-12-24 (Christmas window, KF-003; Image to Video loaded on the real date first, KP-144), per-app language switched with the page open, acda.test9 Free, balance 7, Image to Video Custom (Kling 4.0, 5 s) 70 credits. Tally: 24 Pass, 2 Fail, 26 Blocked (test-data: the paid dialog rows, O-6).

**Status:** nothing filed, uploaded or commented. Fifth batch of this feature (R1, R1r, R2, R3 filed: P0254–P0275, P0299–P0313, P0327). Dedupe: per OS, read-only (`dedupe.txt`).

Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` owner RD for defects, no `[UX]`. Severity is proposed.

**What is drafted:** 1 entry (ISS-XMA-42, TC-159 and TC-168 merged): 1 RD UI.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.

---

## 1. ISS-XMA-42 — Not Enough Credit dialog (Free, 「Upgrade to Pro」): the body names Pro+ in Italian and Vietnamese; the Vietnamese body is mostly English  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-159, TC-168, O-4  ·  **Reproduce:** 2/2  ·  **Verified on:** 16.9.0.2611251

> **QA note — not pasted into eBug.** One ticket, not two: both fails are the same string (the free dialog body) in two locales, and both put Pro+ where the English and the title say Pro, so the localized body looks taken from a Pro+ variant of the string (O-4); the Vietnamese one is also left largely untranslated. The fix is the same resource in two locale files, like ISS-XMA-30 grouping four languages. Owner RD (text rule, 2026-11-11): the PM spec states the English text (R-055, pm-xmas-credit: 「Upgrade to Pro」 / 「… Upgrade to Pro to get free bonus credits every month.」), the plan name Pro is not open, and R-070 says the dialog is in the app language and not left in English; the spec gives no translation (Q-19, open), but Q-19's own assumption makes a text left in English a defect, and naming another plan is wrong whatever the wording decision, so it is filed, not held (ebugs.md step 1). Note for the reviewer: on filing, the team moved the R1/R2 「not localized」 tickets P0264 / P0301 to PC-Doc (and P0316, P0319, P0320 on Cinematic Reel are PC-Doc); the casebook rule says RD or PM, never Doc, so RD is proposed and the reviewer may choose. Expect quotes no translation of our own beyond the plan name. Pro+ is the top tier (VIP, KP-037), a different, dearer plan than the CTA's Pro offer: misleading in a purchase prompt, hence S3 (S2 if the reviewer counts a wrong plan in a paywall as important). Reached by the KP-144 workaround: Image to Video loaded on the real date (Stage certificate fails after 2026-12-04), phone moved to 2026-12-24, per-app language switched with the page open (cmd locale set-app-locales; the activity recreates and keeps photo, prompt, model, price), Generate (O-1, O-4). Bodies read: ITA 「Non disponi di sufficienti crediti per usare questa funzione. Passa Pro+ per ricevere crediti bonus gratuiti ogni mese.」 (Pro+, and 「a」 missing: title 「Passa a Pro」); VIE 「You don't have enough tín dụng to use this feature. Nâng cấp lên Pro+ to get free bonus tín dụng every month.」 (title 「Nâng Cấp Lên Pro」, CTA 「Nhận Ưu Đãi Ngay!」); ENG 「You don’t have enough credits to use this feature. Upgrade to Pro to get free bonus credits every month.」 (TC-134, R3). Text finding: no log (overlay rule 3). New Year window and the paid dialog (TC-179 – TC-204, Blocked test-data) not seen in these languages.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][ITA/VIE] Christmas Sale (Not Enough Credit): Free dialog body says Pro+; VIE mostly English
```

**Description:**

```
Repro Steps:
1. Launch the APP with the phone on the real date
2. Tap 「Image to Video」 on the Launcher
3. Tap 「Custom」
4. Tap the photo area
5. Select a photo
6. Enter a prompt
7. Set the phone date to 2026-12-24 in Settings (automatic date and time off)
8. Set the app language of PowerDirector to Italiano in Settings (per-app language)
9. Return to the APP (Image to Video still open)
10. Tap 「Genera」 (70 credits)
11. Wait until the 「Passa a Pro」 dialog shows
12. Read the dialog body
13. Tap ⓧ
14. Set the app language of PowerDirector to Tiếng Việt in Settings
15. Return to the APP
16. Tap 「Tạo」 (70 credits)
17. Wait until the 「Nâng Cấp Lên Pro」 dialog shows
18. Read the dialog body
19. Check the result

Result:
ITA body says 「Passa Pro+」, VIE 「Nâng cấp lên Pro+」 (titles say Pro); the VIE body is mostly English.
摘要：義大利文與越南文內文寫成 Pro+（標題為 Pro）；越南文內文大多仍是英文。
{16.9.0_xma42_ita.jpg} {16.9.0_xma42_vie.jpg} {16.9.0_xma42_eng.jpg}

Expect Result:
The body names Pro like the title and the English 「Upgrade to Pro」, fully in the app language.
摘要：內文應與標題及英文一致寫 Pro，且完整翻譯成該語言。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, phone date 2026-12-24); build 2611251; Free account, signed in, balance 7 credits (below the price); Image to Video Custom (Kling 4.0, 5 s) costs 70; app language set per app
Related: the other 24 languages and English say Pro in the body (TC-134, TC-153 – TC-178); title and CTA are translated in ITA and VIE
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-credit board (free user without enough credits: 「Upgrade to Pro」 dialog, English body 「… Upgrade to Pro to get free bonus credits every month.」) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261126_eBug_drafts_NewYear-Sale-R4_16.9.0_images/01_ISS-XMA-42/`

---

## Not raised (for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-1 | Cheaper route: per-app language switched with Image to Video open keeps its inputs | Tooling note (extends KP-144). |
| O-2 | KOR / JPN / ESP drop 「free」 or 「bonus」; KOR title 프로, 「요.」 alone; FRA CTA on two lines | Wording per Q-19 (same meaning, fits); rows passed. |
| O-3 | acda.test9 Free, balance 7; Black Friday pill on the real date | Account state; other campaign. |
| O-5 | THA / FAS titles spell the plan out; RTL page behind the dialog not mirrored | Wording per Q-19; the page is outside these rows. |
| O-6 | Pro test purchase adds 100 credits at once (7 → 107); paid dialog rows Blocked | Test data (TC-179 – TC-204 Blocked). |
| O-7 | Bottom tab reads 「Pro」 after purchase; stray taps; empty project left | Tooling note. |

## Reconciliation against the run

2 Fail (all defect, merged into one entry), 26 Blocked (test-data, O-6, not raised), 7 observations (O-1 … O-7).

### Row-by-row map

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-159 | Fail | defect | 1. ISS-XMA-42 |
| TC-168 | Fail | defect | 1. ISS-XMA-42 |
| O-1 | observation | — | not raised |
| O-2 | observation | — | not raised |
| O-3 | observation | — | not raised |
| O-4 | observation | — | folded into 1. ISS-XMA-42 |
| O-5 | observation | — | not raised |
| O-6 | observation | — | not raised |
| O-7 | observation | — | not raised |

### Owner split

| Owner | Entries |
|---|---|
| RD | 1 |

### Filing order

**1**. Nothing is filed until the review page's decisions come back.
