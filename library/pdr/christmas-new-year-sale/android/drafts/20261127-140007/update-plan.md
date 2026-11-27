# Update plan — v3 → draft 20261127-140007 (REQ-011, REQ-012)

Same spec set (specs/2026-11-20). User, 2026-11-27: DRA262611P0311 re-checked under the PM rule 「未訂閱 Auto Pass 的用戶會看到 Auto Pass 的 Credit Sales；若已訂閱 Auto Pass，則會看到 2000 Credit Pack 的 Credit Sales」 (R-048, Q-14). Run R6 showed the app follows it: without Auto Pass the page leads with the Auto Pass sale, with Auto Pass it shows 「Auto Pass activated」 and the 1000+1000 pack. The ticket is NAB, and v3 rows that expected the 2000 pack without Auto Pass are wrong.

## Requirements
- R-046 modified: the 1000+1000 Special Offer pack and 「Get 2000 credits for …」 are for a paid user **with** Credit Auto Pass (R-048).
- R-048 variants split by season: without Auto Pass TC-125, TC-120 (Christmas), TC-121 (New Year); with Auto Pass TC-126, TC-122 (Christmas), TC-205, TC-123 (New Year).
- Why the analysis missed it: R-048 (the Q-14 ruling) was applied to TC-125 / TC-126 only; the whole-page rows TC-120 / TC-121 kept the Design frame, which draws both offers on one page. A ruling that splits a screen by state must be carried to every row that looks at that screen.

## Requirements (REQ-012)
- New R-071: the IAP page in the app's dark and light appearance, as the Design draws IAP_year dark and light (page, annual card, monthly card colours).
- New R-072: the credit purchase page in dark and light (page, pack tiles).
- Why the analysis missed it: v2 gave dark / light variants only to the Launcher banner, whose PM line names them; the IAP and credit frames drawn in both appearances got one row each saying 「seasonal background」, which R2 passed on a navy card in light mode (DRA262611P0331). Fixed in analysis.md pass 10, *Every drawn appearance is a variant*.

## Rows
- TC-120, TC-121 modified: the no-Auto-Pass page — Auto Pass sale card on top, no 1000+1000 pack and no 「Get 2000 credits for …」; banner, packs, footer and countdown checks kept. Spec Ref adds R-048, drops R-046.
- TC-122, TC-123 modified: precondition 「Credit Auto Pass subscribed」, run after TC-150.
- New TC-205 (after TC-126): New Year credit page with Auto Pass.
- New TC-206 – TC-209 (after TC-102): IAP page, Christmas / New Year × dark / light, appearance set with the app's Appearance setting.
- New TC-210 – TC-213 (after TC-121): credit purchase page, same four.
- TC-100, TC-102 modified: 「seasonal background」 now points to TC-206 – TC-209 for the colours.
- All other 197 v3 rows unchanged.

## Not added
- The short-device frames (IAP and credit page, drawn dark only): a screen-size variant, not an appearance; no short phone among the fixtures.
- 「Get 2000 **C**redits」 capital C (app) vs 「credits」 (Design): text difference seen in R6, not a row change; for an eBug if wanted.
