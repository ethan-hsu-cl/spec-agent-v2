# R1 report: Christmas & New Year Sales Android, Christmas rows of table v2

Round R1 of draft 20261120-165128 (table v2, 151 rows; 94 Christmas rows this round).
- Build 16.9.0 (2611201, SR DRA261109-01), installed with adb.
- Phone: SM-A516B / Android 13, Play store Taiwan.
- Stage server, RD test date inside the Christmas window.
- Every row ran with the Free account signed out (Stage sign-in after pm clear fails: O-9, KP-093).
- The user closed R1 before R1-d (purchases unavailable, O-10). Nothing filed.

## Tally
18 Pass, 35 Fail (defect), 41 Blocked (test-data), 94 total.

| Segment | Pass | Fail | Blocked | Test time |
|---|---|---|---|---|
| R1-z | – | – | 6 | – |
| R1-a | 10 | – | 2 | 15 min |
| R1-b | 1 | 26 | – | 21 min |
| R1-c | 7 | 9 | 11 | 31 min |
| R1-d | – | – | 22 (not run) | – |

## Main findings: 12 eBug drafts (ebugs/2026-11-23-r1/, format check 0 errors)
1. S2 RD: 「SAVE」 and 「vs. paying NT$240/mo × 12」 stay English in all 26 non-English languages. In Arabic and Persian the English line takes local digits.
2. S2 PM: 「/year」 and 「More subscription plan」 stay English in all 26 languages. The 多國文案 sheet has no text for either, so PM must supply it.
3. S3 RD: the CTA wording differs from the sheet in 12 languages (CHT, CHS, FRA, ITA, JPN, KOR, ESP, ESP (MX), RUS, Viet, Arabic, Hebrew).
4. S3 RD: the bottom links overlap in RUS. In FRA, UKR and Polish the separators touch or cover the text.
5. S3 RD: the Polish CTA wraps to two lines, edge to edge.
6. S3 RD: 57% is shown, but NT$1,210 vs NT$240 × 12 gives 57.99%. Either truncated or fixed text; the US store (45%) would tell which (O-3).
7. S2 RD: the Launcher banner title reads 「Turn one photo to cinematic reel」, not 「Make Christmas magic with AI」 (TC-083, TC-084). The Stage CMS content may be the cause.
8. S2 RD: the Launcher pill reads 「Pro」, not 「Try Pro 7 days for free」; the Mine pill is right (TC-087, TC-090).
9. S3 PM [AIAgent][UX], a decision: Back and ‹ on the IAP page opened from the interstitial go to the Launcher (TC-109, O-5).
10. S3 RD: at 411×731 dp the IAP banner title is clipped (TC-143).
11. S3 RD: the landscape Launcher has no Christmas banner (TC-144).
12. S2 RD: the IAP card shows 「Special Offer」 / 「57% OFF」, not 「Christmas Treat」 / 「Save xx%」, and the monthly price is not struck through (O-4; row TC-100 is Blocked for the US store only).

Not filed:
- TC-095: cites DRA262608-0134 (15+ Benefits is the ruled state).
- TC-124: held for a signed-in recheck; Q-13 also open.
- O-1, O-2, O-6, O-8, O-10: report only.
- O-9: already filed on Android as DRA262611P0200 and DRA262611P0253 (in dedupe.txt only).

Dedupe: read-only search of the Android pool plus all 86 open 16.9.0 Android tickets. No duplicate found; the Christmas tickets in the pool are the 2025 campaign's (15.9.x, resolved).

## Blockers and what re-running R1-d needs
- Purchases on the install (O-10): every subscription CTA shows 「Unofficial Version」. Needs a Play internal-test-track install or an RD bypass (related DRA262611P0253).
- Stage sign-in after pm clear (O-9): needed for R1-d's Pro rows, TC-124, TC-134, TC-135 and TC-142.
- The user's OK for the Play Billing Lab terms: TC-013, TC-014, TC-100, TC-101 (US store), TC-111–113 (India, Indonesia, Philippines), TC-114 (JP).
- Other Blocked rows: RD date fixed (TC-001, 002, 005, 010); no old build (TC-011, 012); the interstitial stays portrait on this phone, needs a tablet (TC-145).

blocked-reasons.json groups: purchases 24, Play Billing Lab terms 7, RD date 4, sign-in 3, old build 2, tablet 1.

## Open questions touched
- Q-7: the banner title is wrong, so where it leads was not judged.
- Q-13: TC-124 held.
- Q-18: not in this round.

## Time, tokens and usage
- Wall 2 h 57 min: test 1 h 08 min, idle 1 h 49 min (waiting for the R1-d decision).
- Tokens (since 03:09:42Z, session plus subagents): 383 messages, 64.6 M processed (836 in, 0.90 M cache write, 63.5 M cache read, 181 k out).
- Usage card (1× Pro, shared account): 5-hour 12 → 51 → 54%, weekly 18 → 24%.

## Coverage
coverage.html: controls 29 not run / 94 n/a, arrows 12 not run / 6 n/a, notes 180 not run / 65 n/a of 245, board images 16 of 19. No taps.jsonl on this Android run, so 0 presses matched.

## Follow-ups
- Knowledge pass is due (O-9 confirms KP-093).
- verify_ebug_drafts.py "unknown sheet" and the entry 9 basis warnings remain; the format check passes.
