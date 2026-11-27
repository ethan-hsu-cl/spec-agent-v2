# R1r report: Christmas & New Year Sales Android, recheck of the rows R1 skipped

Round R1r of draft 20261120-165128 (table v2, 151 rows; the 35 rows R1 skipped), REQ-005.
- Build 16.9.0 (2611201), downloaded from the Play Store (test track, installer com.android.vending, installed 14:42). The adb install from R1 fails the new 「Unofficial Version」 purchase check; only test builds downloaded from Play pass it (user, REQ-005).
- Phone: SM-A516B / Android 13 (R5CN8194YSN).
- Stage server, with the RD test date inside the Christmas window.
- acda.test9 was signed in throughout: it was already signed in on the Play build, so no pm clear was needed. The account was Free until TC-147, then Pro.
- The Play country was set with Play Billing Lab (terms accepted on acda.test9, with the user's OK): US, India, Indonesia, Philippines and Japan; Taiwan otherwise.
- Nothing was filed, uploaded or commented.

## Tally
10 Pass, 14 Fail (defect), 11 Blocked (8 test-data, 3 defect), 35 total.

| Segment | Rows | Pass | Fail | Blocked | Test time |
|---|---|---|---|---|---|
| R1r-a Play Billing Lab countries (Free) | 7 | 1 | 6 | – | 9 min |
| R1r-b Free, credits and CTAs | 7 | 2 | 1 | 4 (3 test-data, 1 defect) | 10 min |
| R1r-c Subscribe and the Pro rows | 21 | 7 | 7 | 7 (4 test-data, 3 defect) | 18 min |

Passed rows:
- TC-101: the US IAP page computes the % (45).
- TC-104 / TC-105: the Play sheets are the Christmas annual and monthly SKUs.
- TC-147: the Christmas annual plan was bought; the account is Pro.
- TC-119: the Pro pill opens the credit page.
- TC-127: the Auto Pass sheet opens.
- TC-130: Back on the credit page works.
- TC-131: the footer links open.
- TC-140: with enough credits, −70 and no dialog.
- TC-150: Auto Pass was bought, +2000, 「Auto Pass activated」.

## Findings: 11 new eBug drafts, 2 additions to R1 entries
The batch is `ebugs/2026-11-23-r1r/` (ISS-XMA-13…23, continuing the numbering of the unfiled R1 batch). The format check has 0 errors. Review page: `20261123_eBug_review_Christmas-Sale-R1r_16.9.0.html`.
1. ISS-XMA-13, S2 RD: on the US store the interstitial compares $45.99 with the regular monthly SKU ($7.99). It reads 「SAVE 52%」 「vs. paying $7.99/mo × 12」, while the IAP page reads the campaign $6.99 and 45% (TC-013, O-1).
2. ISS-XMA-14, S4 RD: the trial terms say 「until cancelled」 where the spec says 「canceled」 (TC-014).
3. ISS-XMA-15, S2 RD: in India, Indonesia and the Philippines the IAP page opens on the annual plan, not the monthly plan (TC-111–113).
4. ISS-XMA-16, S2 RD: a signed-in Free user gets no Christmas 500 pack. 「First Purchase Discount」 1000 +1000 shows instead, although the app fetches pdrm_500_credit_freeuser_christmas (TC-124, TC-148; R1 had held TC-124).
5. ISS-XMA-17, S2 RD: the Pro VIP card has no Christmas decoration and no JP 「Merry Christmas! Enjoy...」 banner. There is no separate VIP Benefits page (TC-114, TC-115, TC-117).
6. ISS-XMA-18, S2 RD: the credit page banner is the regular image collage, not 「Christmas Special」 (TC-120, TC-118).
7. ISS-XMA-19, S3 RD: without Auto Pass the CTA reads 「Continue with the best deal」, not 「Subscribe for 3000 free credits!」 (TC-125, TC-120).
8. ISS-XMA-20, S4 PM (decision): the app shows the footer 「Terms of Service | Privacy Policy」 and 「unused credits」; the Design has 「Privacy Policy | Terms of Use」 and 「consumed credits」 (TC-120).
9. ISS-XMA-21, S2 RD: Pro users are never offered the Christmas 2000-credit pack, with or without Auto Pass, although the app fetches pdrm_2000_credit_paiduser_christmas (TC-126, TC-122, TC-149).
10. ISS-XMA-22, S3 PM (question): the Christmas monthly costs ₱485 against the regular ₱469 in the Philippines, and the same NT$240 as the regular plan in Taiwan. Is 15% off meant for every store? (O-2, O-6)
11. ISS-XMA-23, S3 PM (text): in 日本語 the Pro pill stays English 「Credit Special Offer」, and the spec has no translation for it (TC-114, O-9).

Additions to R1 entries (same bug, new evidence; listed in the batch's *Cited* table and on its review page):
- ISS-XMA-06: the app truncates the % rather than rounding it. Indonesia's 58.68% shows 「58% OFF」 (TC-112); the US shows 45% (TC-101).
- ISS-XMA-12: the same plan card on the US store, signed in: 「Special Offer」, 「45% OFF」, no struck monthly price, and CTA 「Continue」 (TC-100).

Not raised:
- O-3, O-4, O-5: run and tooling notes.
- O-8: ToS and Privacy open in Traditional Chinese with the Play country set to US. The spec is silent, as with R1's O-1.
- O-11: account state.

Dedupe: read-only search of the Android pool with 22 terms; every 16.9.0 hit was read. No Android ticket matches; the related closed tickets are in `dedupe.txt`.

## Still Blocked and why
- Low-balance account (6): TC-134, TC-135, TC-142 (Free) and TC-132, TC-133, TC-141 (Pro).
  - acda.test9 has 3545–5510 credits and is the only Google account on the phone.
  - No other account can sign in without a password.
  - These rows need a low-balance test account on the phone. Burning about 3,440 credits instead was not done.
- RD stage test date (2):
  - TC-129 needs 2026-12-25 00:03 (New Year countdown).
  - TC-151 step 3 needs 2026-12-30 (New Year window). Steps 1–2 were seen: a Pro launch goes straight to the Launcher.
- No VIP Benefits page (1, defect): TC-117 (ISS-XMA-17).
- Christmas packs not offered (2, defect): TC-148 (Free 500) and TC-149 (Pro 2000) (ISS-XMA-16, ISS-XMA-21). Nothing was bought in their place.

blocked-reasons.json groups: low-balance account 6, RD date 2, no VIP Benefits page 1, pack not offered 2.

## State left on the account and phone
- acda.test9 is Pro: annualsubscription_christmas_2611, bought 15:13 on the test track, renews every 30 min.
- It also has Credit Auto Pass (pdrm_2000_credit_paiduser_yr_autopass, bought 15:25) and 5510 credits.
- Free and no-Auto-Pass rows need both to lapse: cancel them in Play or let the test subscriptions end.
- The Play Billing Lab country is back to Taiwan (set 15:25, active until 17:25). The app language is en-US.
- The Play test build 16.9.0 (2611201) is still installed from the Play Store. Never adb-install over it.
- An Image to Video task from TC-140 (Kling 4.0, 5 s, −70) was left processing.

## Open questions touched
- Q-3: partly settled. The % is computed from store prices and truncated (ISS-XMA-06 addition).
- Q-13: the free 500 pack's sale price is still undecided, and the pack is not shown at all (ISS-XMA-16).
- Q-14: with Auto Pass the page shows 「Auto Pass activated」 (Pass) but no 2000-pack sale (ISS-XMA-21).
- Q-17: switching the country in Play Billing Lab works (prices change), but the monthly landing does not follow (ISS-XMA-15).

## Time, tokens and usage
- Wall 37 min (06:50–07:27 UTC, 14:50–15:27 local), all of it test time, with no idle gap over 15 min.
- Tokens for the run (06:49:11Z–07:27:30Z, session plus subagents): 216 messages, 31.8 M processed (472 in, 0.48 M cache write, 31.2 M cache read, 93 k out). Including the wrap-up: about 34.2 M.
- Usage card (1× Pro, shared account):
  - 5-hour: 73% at the R1r-a start → 82% → 88% at the R1r-c start; the window reset at 07:50 UTC.
  - Weekly: 26 → 28%.

## Coverage
coverage.html, built from runs r1-christmas and r1r-recheck:
- Controls: 25 ran, 4 blocked, 94 n/a.
- Arrows: 6 ran, 6 not run, 6 n/a.
- Notes: 125 ran, 14 blocked, 41 not run, 65 n/a, of 245.
- Board images: 16 of 19.
- There is no taps.jsonl on these Android runs.

## Follow-ups
- Review the R1 and R1r batches together (23 entries). Filing waits for the reviewer's decisions, Creator, TRCode and source tag; there is no filed batch to prefill them from.
- Knowledge pass (O-4 / O-5 Play Billing Lab and SKU reading, O-8 contradicts KF-002, O-10 no VIP Benefits page).
- verify_ebug_drafts.py reports "unknown sheet" and "never names Christmas" on the Spec Links, the same as on R1. Its string-sheet checks do not apply here; the format check passes.
