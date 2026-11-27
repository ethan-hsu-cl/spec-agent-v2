# Christmas & New Year Sales (Android) — eBug drafts, round R4-b (paid More Credits Needed dialog in 26 languages), PDR-A 16.9.0 build 2611251

**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-26-r4-dialog-mui/` — R4-b re-run (2026-11-26 16:19–16:28) of round R4, draft `drafts/20261126-154459` (in review, not yet saved; R-070, R-053, Q-19, TC-179 – TC-204, REQ-009), on Samsung Galaxy A51 SM-A516B / Android 13 through Appium / UiAutomator2, build 16.9.0.2611251, Stage server, phone date 2026-12-24 (Christmas window, KF-003; Image to Video loaded on the real date first, KP-144), per-app language switched with the page open, acda.test9 Pro, balance 22, Image to Video Custom (Kling 4.0, 5 s) 70 credits. R4-b tally: 25 Pass, 1 Fail (TC-194). R4 total: 49 Pass, 3 Fail, 0 Blocked; TC-159 / TC-168 already filed as DRA262611P0328 (batch 2026-11-26-r4).

**Status:** nothing filed, uploaded or commented. Sixth batch of this feature (R1, R1r, R2, R3, R4 filed: P0254–P0275, P0299–P0313, P0327, P0328). Dedupe: per OS, read-only (`dedupe.txt`).

Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` owner RD for defects, no `[UX]`; no comment on DRA262611P0328 (related only). Severity is proposed.

**What is drafted:** 1 entry (ISS-XMA-43, TC-194): 1 RD UI.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.

---

## 1. ISS-XMA-43 — More Credits Needed dialog (paid, Christmas): the Vietnamese body is English except 「tín dụng」  ·  Class: UI  ·  Severity: S3  ·  Owner: RD

**Report step:** TC-194, O-9  ·  **Reproduce:** 1/1  ·  **Verified on:** 16.9.0.2611251

> **QA note — not pasted into eBug.** A new ticket, not a comment on DRA262611P0328 (no comments on existing eBugs, AGENTS.md): P0328 names the Free 「Upgrade to Pro」 dialog and its body string (TC-159, TC-168); this is the paid 「More Credits Needed!」 dialog (R-053), a different string, shown to a subscribed user. The pattern is the same (the Vietnamese body keeps English around 「tín dụng」), so the Note lists P0328 as related. Owner RD (text rule, 2026-11-11): the PM spec states the English body (R-053, pm-xmas-credit: 「You don’t have enough credits to use this feature. Get credits now!」) and R-070 says title, body and CTA are in the app language and not left in English; the spec gives no translation (Q-19, open), but Q-19's own assumption makes a text left in English a defect, so it is filed, not held (ebugs.md step 1). The Expect quotes no translation of our own. Class UI, as ISS-XMA-42 / P0328. Note for the reviewer: the team moved earlier 「not localized」 tickets (P0264 / P0301) to PC-Doc; the casebook rule says RD or PM, never Doc, so RD is proposed and the reviewer may choose. S3 like P0328: a purchase prompt half in English for Vietnamese users; the meaning still reads and the CTA and title are Vietnamese, nothing is blocked. Reached by the KP-144 route (O-1, O-8): Image to Video loaded on the real date (Stage certificate fails after 2026-12-04), photo and prompt (inspiration chip) entered, Kling 4.0, phone moved to 2026-12-24, per-app language switched with the page open (cmd locale set-app-locales), Generate. Read 2026-11-26 16:25 host. Vietnamese: title 「Cần Thêm Tín Dụng!」, body 「You don't have enough tín dụng to use this feature. Get tín dụng now!」, CTA 「Nhận Ưu Đãi Ngay!」. English (TC-132, R3, 12/24): 「More Credits Needed!」 / 「You don’t have enough credits to use this feature. Get credits now!」 / 「Grab Discount Now!」. Italian paid body has no plan name and passes (TC-185). Text finding: no log (overlay rule 3). New Year window not seen in Vietnamese.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent][UI][VIE] Christmas Sale (Not Enough Credit): Paid dialog body mostly English
```

**Description:**

```
Repro Steps:
1. Launch the APP with the phone on the real date
2. Tap 「Image to Video」 on the Launcher
3. Tap 「Custom」
4. Tap the photo area
5. Select a photo
6. Tap an inspiration chip to fill the prompt
7. Set the phone date to 2026-12-24 in Settings (automatic date and time off)
8. Set the app language of PowerDirector to Tiếng Việt in Settings (per-app language)
9. Return to the APP (Image to Video still open)
10. Tap 「Tạo」 (70 credits)
11. Wait until the 「Cần Thêm Tín Dụng!」 dialog shows
12. Read the dialog body
13. Check the result

Result:
The VIE body reads 「You don't have enough tín dụng to use this feature. Get tín dụng now!」 (English).
摘要：越南文付費對話框內文除了「tín dụng」外仍是英文（標題與按鈕已翻譯）。
{16.9.0_xma43_vie.jpg} {16.9.0_xma43_eng.jpg}

Expect Result:
The body is fully in Vietnamese, saying 「…enough credits… Get credits now!」 like the title and CTA.
摘要：內文應完整翻譯成越南文，意思與英文內文相同。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, phone date 2026-12-24); build 2611251; Pro account (subscribed), signed in, balance 22 credits (below the price); Image to Video Custom (Kling 4.0, 5 s) costs 70; app language set per app
Related: DRA262611P0328 covers the Free dialog 「Nâng Cấp Lên Pro」 (its body says Pro+ and is mostly English); this is the paid dialog 「Cần Thêm Tín Dụng!」, another string. The other 25 languages translate the paid body (TC-179 – TC-204)
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-credit board (paid user without enough credits: 「More Credits Needed!」 dialog, English body 「You don’t have enough credits to use this feature. Get credits now!」) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
<Claude Reviewed>
```

**Images:** `20261126_eBug_drafts_NewYear-Sale-R4b_16.9.0_images/01_ISS-XMA-43/`

---

## Not raised (for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-8 | R4-b setup: acda.test9 Pro, balance 22 after the user's two spends; KP-144 route held; dialog ⓧ moves with height | Account state and tooling note. |
| O-9 (rest) | JPN body asks to buy credits; ESP CTA drops 「now」; ESP (MX) title ends with a period; FRA CTA on two lines; NLD 「tegoed」 | Wording per Q-19 (same meaning, fits); rows passed. |

## Reconciliation against the run

3 Fail in R4 (TC-159, TC-168 filed as DRA262611P0328 from batch 2026-11-26-r4; TC-194 here), 0 Blocked, 9 observations (O-1 … O-9; O-1 – O-7 belong to the R4 batch).

### Row-by-row map

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-159 | Fail | defect | filed in 2026-11-26-r4 as DRA262611P0328 |
| TC-168 | Fail | defect | filed in 2026-11-26-r4 as DRA262611P0328 |
| TC-194 | Fail | defect | 1. ISS-XMA-43 |
| O-1 | observation | — | covered by batch 2026-11-26-r4 |
| O-2 | observation | — | covered by batch 2026-11-26-r4 |
| O-3 | observation | — | covered by batch 2026-11-26-r4 |
| O-4 | observation | — | covered by batch 2026-11-26-r4 |
| O-5 | observation | — | covered by batch 2026-11-26-r4 |
| O-6 | observation | — | covered by batch 2026-11-26-r4 |
| O-7 | observation | — | covered by batch 2026-11-26-r4 |
| O-8 | observation | — | not raised |
| O-9 | observation | — | not raised (rest); folded into 1. ISS-XMA-43 |

### Owner split

| Owner | Entries |
|---|---|
| RD | 1 |

### Filing order

**1**. Nothing is filed until the review page's decisions come back.
