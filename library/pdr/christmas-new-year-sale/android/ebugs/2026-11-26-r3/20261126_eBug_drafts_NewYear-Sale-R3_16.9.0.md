# Christmas & New Year Sales (Android) — eBug drafts, round R3 (low-balance Not Enough Credit rows), PDR-A 16.9.0 build 2611251

**Source:** pdr-spec-casebook run `library/pdr/christmas-new-year-sale/android/runs/2026-11-26-r3-lowbalance/` — round R3 of draft `drafts/20261120-165128` (table v2; the 10 low-balance Not Enough Credit rows, REQ-007, R3-a re-run REQ-008), 2026-11-26, on Samsung Galaxy A51 SM-A516B / Android 13 through Appium / UiAutomator2, build 16.9.0.2611251 updated on the phone by the user, Stage server, the campaign driven by the phone's system date (KF-003), acda.test9 signed in (Pro in R3-b; Free, balance 7, in the R3-a re-run), Image to Video Custom (Kling 4.0, 5 s) 70 credits. Tally: 9 Pass, 1 Fail, 0 Blocked.

**Status:** nothing filed, uploaded or commented. Fourth batch of this feature (R1, R1r, R2 filed: P0254–P0275, P0299–P0313). Dedupe: per OS, read-only (`dedupe.txt`).

Rules: reviewer rules 2026-10-21 (one action per Repro step, a Spec Link on every entry with the URL on its own line, an image on every entry, the log excerpt on every failure-related entry, no video); `[AIAgent]` owner RD for defects, no `[UX]`. Severity is proposed.

**What is drafted:** 1 entry (ISS-XMA-41): 1 RD Functional.

Legend — Class: Functional / UI / UX · Severity: S1 critical and blocking only, S2 important, S3 moderate, S4 minor · Owner: RD or PM.

---

## 1. ISS-XMA-41 — Not Enough Credit dialog (Free, 「Upgrade to Pro」): one system Back closes the dialog and Image to Video together; photo, prompt and model are lost  ·  Class: Functional  ·  Severity: S2  ·  Owner: RD

**Report step:** TC-142, O-7  ·  **Reproduce:** 3/3  ·  **Verified on:** 16.9.0.2611251

> **QA note — not pasted into eBug.** R-062 (team rule, Android system Back: Back on the Not Enough Credit dialog closes it like ⓧ) with R-057 (PM pm-xmas-credit: ⓧ closes it, back on the feature page). Seen on 12/24 two times in results.csv (three per O-7; Appium pressKey and adb keyevent 4) and on the New Year dialog on 12/30 once (O-7). Logcat 2026-12-24 15:24:33.430: the Back key goes to ViewRootImpl[ImageToVideoActivity] (ViewPostIme key 0/1), 15:24:33.473 Project2Activity (Launcher) becomes visible, then ImageToVideoActivity stops: the dialog does not consume the key. Phone-date note: with the date after 2026-12-04 a Stage certificate error leaves Image to Video with no model when the page loads (O-1, environment), so the run loaded the page on the real date and moved the date before Generate (O-4); the campaign follows the phone date (KF-003). Pro dialog Back: no row, not tried.

**Short Description:**

```
PDR-A 16.9.0 - [AIAgent] Christmas & New Year Sale (Not Enough Credit): Free dialog: one Back also closes Image to Video
```

**Description:**

```
Repro Steps:
1. Launch the APP
2. Tap 「Image to Video」 on the Launcher
3. Tap 「Custom」
4. Tap the photo area
5. Select a photo
6. Enter a prompt
7. Set the phone date to 2026-12-24 in Settings (automatic date and time off)
8. Return to the APP
9. Tap 「Generate」 (70 credits)
10. Wait until the 「Upgrade to Pro」 dialog shows
11. Press system Back once
12. Check the result

Result:
One Back closes the dialog and Image to Video: the Launcher shows, photo and prompt lost. ⓧ closes only the dialog.
摘要：按一次返回鍵，對話框與 Image to Video 一起關閉回到首頁，輸入遺失；ⓧ 只關對話框。
{16.9.0_xma41_dialog.jpg} {16.9.0_xma41_after_back.jpg} {16.9.0_xma41_after_x.jpg} {16.9.0_xma41_log.txt}

Expect Result:
One Back closes only the dialog, back on Image to Video with the inputs kept, as ⓧ does.
摘要：按一次返回鍵應如 ⓧ 只關閉對話框，留在 Image to Video，輸入保留。

Note:
Device: Samsung Galaxy A51 SM-A516B / Android 13
Related: Christmas sale window (Stage server, phone date 2026-12-24) and New Year sale window (phone date 2026-12-30); build 2611251; Free account, signed in, balance 7 credits (below the price); Image to Video Custom (Kling 4.0, 5 s) costs 70
Related: same on the New Year dialog (phone date 2026-12-30); the same dialog's ⓧ closes only the dialog (TC-142 third setup, TC-141 on the paid dialog); Back on the paid 「More Credits Needed!」 dialog was not tried
Spec Link: Christmas & New Year PM spec (PDRM-MX, Christmas Sale), pm-xmas-credit board (free user without enough credits: 「Upgrade to Pro」 dialog; ⓧ closes it, back on the feature page; Android system Back acts as ⓧ, QA rule R-062) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3226-21365
Spec Link: Christmas & New Year PM spec (PDRM-MX, New Year Sale), pm-ny-credit board (New Year Not Enough Credit dialog, same logic) -
https://www.figma.com/design/3urWYejMUP2uaglb4s73M5/PDRM-MX?node-id=3271-4161
<Claude Reviewed>
```

**Images:** `20261126_eBug_drafts_NewYear-Sale-R3_16.9.0_images/01_ISS-XMA-41/`

---

## Not raised (for the record)

| Item | What was seen | Why not raised |
|---|---|---|
| O-1 | Image to Video loads no model with the phone date after 2026-12-04 (Stage GW certificate) | Environment (server certificate), not an app defect. |
| O-2 | acda.test9 still Pro ~25 h after the R2 New Year test subscription | Account state; knowledge (I-031). |
| O-3 | Black Friday Not Enough Credit dialog on the real date; missing from the page source | Other campaign; tooling note. |
| O-4 | Workaround: load the page on the real date, then move the date | Tooling note. |
| O-5 | 「3 Credits Received」 on opening the Christmas credit page | Daily credit, expected. |
| O-6 | AI Video Enhance task banner from another session on the shared account | Shared account. |
| O-8 | acda.test9 now Free, balance 7; Samsung update screen after date moves | Account state; tooling note. |
| O-9 | Black Friday countdown pill on the real date; interstitial after moving the date back | Other campaign / artifact of moving the clock. |
| TC-133 countdown | Christmas credit page countdown 3D 09:23 | Already DRA262611P0313 (ISS-XMA-40, R2). |

## Reconciliation against the run

1 Fail (all defect), 0 Blocked, 9 observations (O-1 … O-9).

### Row-by-row map

| Item | Result | Disposition | Became |
|---|---|---|---|
| TC-142 | Fail | defect | 1. ISS-XMA-41 |
| O-1 | observation | — | not raised |
| O-2 | observation | — | not raised |
| O-3 | observation | — | not raised |
| O-4 | observation | — | not raised |
| O-5 | observation | — | not raised |
| O-6 | observation | — | not raised |
| O-7 | observation | — | folded into 1. ISS-XMA-41 |
| O-8 | observation | — | not raised |
| O-9 | observation | — | not raised |

### Owner split

| Owner | Entries |
|---|---|
| RD | 1 |

### Filing order

**1**. Nothing is filed until the review page's decisions come back.
