# R3 report: Christmas & New Year Sales Android, the low-balance rows

Round R3 of draft 20261120-165128 (table v2), REQ-007: the 10 Not Enough Credit rows blocked on balance in R1, R1r and R2.
- Build 16.9.0 (2611251), updated on the phone by the user. Phone SM-A516B / Android 13. Stage server.
- acda.test9: **Pro** (the R2 New Year annual test subscription is still active), balance 4 → 7 (3 daily free credits, O-5). Image to Video (Custom, Kling 4.0, 5 s) costs 70.
- Nothing generated, bought, filed, uploaded or commented.

## Tally
5 Pass, 0 Fail, 5 Blocked (test-data), 10 total. Test time 11 min.

| Segment | Rows | Pass | Blocked |
|---|---|---|---|
| R3-a Free (TC-134, 135, 142, 138, 139) | 5 | – | 5 |
| R3-b Pro (TC-132, 133, 141, 136, 137) | 5 | 5 | – |

Passed:
- TC-132 (12/24): 「More Credits Needed!」, body and 「Grab Discount Now!」 exact; red background, stocking and candy canes as Design I2V_Custom 2754:6631.
- TC-133: the CTA opens the red 「Christmas Special」 credit page.
- TC-141: ⓧ closes the dialog, back on Image to Video with inputs kept, balance unchanged (7).
- TC-136 (12/30): same text on the blue New Year background (champagne glasses), as board 2844:23135; no 「CHRISTMAS SALE」.
- TC-137: the CTA opens the blue 「New Year Special」 credit page.

Not judged here: TC-133's Christmas credit page showed a countdown (3D 09:23), already ISS-XMA-40 (R2, the ruling Q-11 gives Christmas none).

## Still Blocked and why
TC-134, 135, 142, 138, 139 need a **Free** account with a balance below 70. acda.test9 is still Pro: the New Year test subscription bought in R2-d (2026-11-25 13:02 phone time) had not lapsed ~25 h later (O-2, against KP-068). They run once the subscription lapses or a Free low-balance account is signed in.

## Observations
- O-1: with the phone date after 2026-12-04, Image to Video loads no model (GW CertificateExpiredException, a server certificate expires 2026-12-04). Environment, not an app defect.
- O-4: workaround: load Image to Video on the real date, then move the phone date and bring the app back without relaunching; the dialog follows the new date's campaign.
- O-3: on the real date (11/26) Stage shows a Black Friday Not Enough Credit dialog. The dialog is missing from the page source.
- O-5: opening the Christmas credit page gave 「3 Credits Received」 (4 → 7).
- O-6: a 「Good news! Your AI Video Enhance task has been completed…」 banner for a task this run did not start (shared account); closed.

Knowledge parked: I-036 (O-1/O-4), I-031 (O-2/O-3/O-5).

## State left
acda.test9 Pro, balance 7. Phone 2026-12-24 (current time of day, automatic off), app en-US on the Stage Launcher.

## Usage
5-hour 3% → 17%, weekly 0% → 3% (1× Pro, shared account).

## Re-run of R3-a (REQ-008, 2026-11-26 15:0x–15:31)
acda.test9 is now **Free**, balance 7, price 70. Same workaround (O-8: the certificate error returns on every page load, so each setup starts on the real date).
- TC-134 Pass (12/24): 「Upgrade to Pro」, 「You don’t have enough credits to use this feature. Upgrade to Pro to get free bonus credits every month.」, 「Grab Discount Now!」, red Christmas card.
- TC-135 Pass: the CTA opens the 「Christmas Special」 IAP page (no Play sheet opened).
- TC-138 Pass (12/30): same text on the blue New Year card.
- TC-139 Pass: the CTA opens the 「New Year Special」 IAP page.
- **TC-142 Fail (defect):** one system Back on the Free dialog closes the dialog *and* the Image to Video page; the app lands on the Launcher and the photo, prompt and model are lost. ⓧ closes only the dialog. Seen twice on 12/24 and once on the New Year dialog on 12/30 (O-7). Expected: Back closes the dialog, back on Image to Video, as ⓧ does (R-062). Screenshots TC-142-after-back.png, TC-142-after-x.png; logs logs/R3-a2-20261126-153110.

**R3 total: 9 Pass, 1 Fail, 0 Blocked.** TC-142 filed 2026-11-26 as DRA262611P0327 (ISS-XMA-41, S2 RD) on TR261125-0064 (`ebugs/2026-11-26-r3/`).
