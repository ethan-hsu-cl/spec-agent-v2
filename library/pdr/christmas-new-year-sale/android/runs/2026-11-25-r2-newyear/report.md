# R2 report: Christmas & New Year Sales Android, the New Year rows

Round R2 of draft 20261120-165128 (table v2, 151 rows), REQ-006: the 57 New Year rows plus TC-129 and TC-151.
- Build 16.9.0 (2611231), installed by the user with adb (installer null). Purchases still worked: no 「Unofficial Version」 dialog on this build (O-11, KP-138 updated).
- Phone: SM-A516B / Android 13 (R5CN8194YSN).
- Stage server. The campaign followed the phone's system date (user, REQ-006). The base date was 2026-12-29; rows moved it when they needed another day.
- acda.test9 was signed in throughout. It was Free for R2-a to R2-c. In R2-d it became Pro: the New Year annual test subscription was bought on the Play test sheet (「Test card, always approves」).
- The Play store was Taiwan. United States was set through Play Billing Lab for TC-020, TC-021, TC-003 and TC-103, then removed.
- Nothing was filed, uploaded or commented.

## Tally
17 Pass, 38 Fail (defect), 4 Blocked (test-data), 59 total.

| Segment | Rows | Pass | Fail | Blocked | Test time |
|---|---|---|---|---|---|
| R2-a New Year interstitial and window edges (Free) | 10 | 6 | 4 | – | 24 min |
| R2-b Interstitial in 27 languages | 27 | 1 | 26 | – | 18 min |
| R2-c Launcher, Mine and IAP (Free) | 15 | 8 | 5 | 2 | 28 min |
| R2-d Pro rows | 7 | 1 | 4 | 2 | 10 min |

Passed rows:
- TC-024, TC-106, TC-107: the CTAs open the New Year SKUs on the Play sheet (annualsubscription_newyear_2611, monthlysubscription_newyear_2611).
- TC-025, TC-026, TC-022, TC-007: interstitial details and its close.
- TC-004: from 1/6 the Launcher, Mine and IAP are back to regular.
- TC-056: English interstitial.
- TC-088, TC-092 (the Mine icon has a selected-state note, O-8), TC-094, TC-097, TC-099: Launcher and Mine.
- TC-103: US IAP, 45%.
- TC-152: the Launcher countdown starts at 12/30.
- TC-151: a Pro user gets no interstitial on 12/15 or on 12/30.

## Findings: 17 eBug drafts
The batch is `ebugs/2026-11-25-r2/` (ISS-XMA-24…40). The format check has 0 errors. Review page: `20261125_eBug_review_NewYear-Sale-R2_16.9.0.html`.

The filed Christmas tickets (DRA262611P0254–P0275) all name the Christmas sale. So the New Year repeats are new entries, and each names its related ticket.

1. ISS-XMA-24, S2 RD (P0254): on the US store the interstitial reads 「SAVE 52%」 from the regular $7.99 monthly price (TC-020).
2. ISS-XMA-25, S4 RD (P0255): the interstitial says 「until cancelled」 (TC-021).
3. ISS-XMA-26, S3 RD (new): the first system Back on the interstitial does nothing; a second Back closes it (TC-023). R1 on 2611201 closed it with one Back.
4. ISS-XMA-27, S2 RD (P0270): the Launcher banner title is 「Turn one photo to cinematic reel」, not 「Bring New Year moments to life」 (TC-003, TC-085, TC-086).
5. ISS-XMA-28, S2 RD (P0264): 「SAVE」 and 「vs. paying …」 stay in English in 26 languages (TC-057–082).
6. ISS-XMA-29, S2 PM (P0265): 「/year」 and 「More subscription plan」 stay in English, and the sheet has no translation for them.
7. ISS-XMA-30, S2 RD (new): the title art is wrong in four languages (TC-059, 063, 082, 066):
   - French and Italian show the English art.
   - Ukrainian shows the Russian art.
   - es-ES shows the Mexican Spanish title and CTA.
8. ISS-XMA-31, S3 RD (P0266): the CTA differs from the sheet in 12 languages.
9. ISS-XMA-32, S3 RD (P0267): the bottom links overlap in RUS, FRA, UKR and Polish.
10. ISS-XMA-33, S3 RD (P0268): the Polish CTA wraps to two lines.
11. ISS-XMA-34, S3 RD (P0269): the % shows 57 where the prices give 57.99% (58), on the interstitial and the IAP page.
12. ISS-XMA-35, S3 RD (new): Mine's top pill has no countdown; the Launcher, IAP and credit page do (TC-089).
13. ISS-XMA-36, S2 RD (P0275): the IAP plan card is wrong (TC-102):
    - 「Special Offer」 and 「57% OFF」 appear, and the monthly price is not struck through.
    - The CTA reads 「Continue」, and the feature cards differ from the Design.
14. ISS-XMA-37, S2 RD (P0258): the Pro VIP card has no New Year decoration (TC-116).
15. ISS-XMA-38, S2 RD (P0261): Pro users are never offered the 2000-credit pack (TC-121, TC-123):
    - The Auto Pass card takes its place.
    - The 2000 card opens the regular SKU pdrm_2000_credits_paiduser.
16. ISS-XMA-39, S3 RD (P0260): with no Auto Pass the CTA is 「Continue with the best deal」 and the text adds 「Cancel anytime.」 (TC-121).
17. ISS-XMA-40, S3 RD (new): on 12/25 the Christmas credit page shows a countdown, 「2D 23:56:30」. Ruling Q-11 gives a countdown to the New Year page only (TC-129).

Not raised:
- TC-121's footer 「Terms of Service | Privacy Policy」 and 「unused credits」: these are ISS-XMA-20, which the reviewer held in R1r.
- O-1: the PiP toast.
- O-4, O-5, O-7, O-10, O-15: date and tooling notes.
- O-8: the Mine icon's selected state. This is left for the design check.
- O-12: the Christmas credit banner looks fixed on 2611231 (P0259). This was not a recheck, so the ticket gets no comment.
- O-14: Google Play's upsell sheet.

Dedupe: read-only. Android only, whole pool, searched for 「New Year」, 「Christmas」, 「Countdown」, 「Credit Special Offer」 and 「Interstitial」. No 16.9.0 ticket names the New Year sale (`dedupe.txt`).

## Still Blocked and why
Low-balance account (4): TC-138 and TC-139 (Free, 3720 credits), TC-136 and TC-137 (Pro, 3755 credits).
- Each needs a balance below the Image to Video (Custom) price.
- Credits were not burned to get there.

These are grouped in blocked-reasons.json.

## State left on the account and phone
- acda.test9 is Pro: annualsubscription_newyear_2611 (test, NT$1,210/30 min, 3-minute trial), bought at 13:02 phone time.
  - It renews every 30 minutes and will lapse within hours (KP-068).
  - There is no Credit Auto Pass. The R1r Auto Pass expired on 11/23.
- Credits: 3755 (3720 plus 35 free-trial bonus).
- Phone date 2026-12-29 13:09 (automatic off), Asia/Taipei.
- App language en-US, on the Launcher. Taiwan store; the Play Billing Lab configs were deleted. Light mode.
- Build 2611231 (adb) is still installed.

## Open questions touched
- Q-18: every countdown counts to 2027-01-06 00:00 local (end of 1/5), as assumed. The Launcher pill shows 「On Sale!」 until fewer than 7 days remain (O-9, KF-004).
- Q-11: the New Year credit page has its countdown. The Christmas credit page has one too, which goes against the ruling (ISS-XMA-40).
- Q-3: the % is computed from the store prices and truncated (ISS-XMA-34). On the US interstitial it uses the regular monthly SKU (ISS-XMA-24).

## Time, tokens and usage
- Wall time 1 h 20 min (03:49–05:09 UTC, 11:49–13:09 local), all of it test time with no idle gap.
- Tokens, run session plus subagents (from 03:48 UTC to the wrap-up): 430 messages, 68.3 M processed (924 in, 0.81 M cache write, 67.3 M cache read, 195 k out).
- Usage card (1× Pro, shared account): 5-hour 6% at the R2-a start → 22% → 32% → 44% at the R2-d start; weekly 36 → 41%.

## Coverage
coverage.html, built from r1-christmas, r1r-recheck and r2-newyear:
- Controls: 25 ran, 4 blocked, 94 n/a.
- Arrows: 12 ran, 6 n/a.
- Notes: 166 ran, 14 blocked, 65 n/a, of 245.
- Board images: 16 of 19.
- There is no taps.jsonl on these Android runs.

## Knowledge pass
Done in the wrap-up, under the domain-knowledge rules:
- KF-003 is new: the phone date drives the campaign window. It covers the Settings steps, the Samsung update screen and the empty log-slice windows. Inbox item I-035 is closed into it.
- KF-004 is new: the New Year countdowns, their target and when each starts.
- KP-138 is updated: the 2611231 adb install was not blocked.
- KP-092, KP-141 and KP-142 are stamped verified on 2611231.
- `--check`: 104 entries OK.

## Follow-ups
- Review the R2 batch. Filing waits for the reviewer's decisions; the page prefills Creator, TRCode and tag from the filed R1r batch. No TR names build 2611231 yet.
- To run the 4 low-balance rows, a low-balance test account is needed on the phone.
- REQ-006 is done.
