# R6 — DRA262611P0311 recheck: New Year 2000-credit pack with and without Credit Auto Pass (2026-11-27)

Phone SM-A516B (R5CN8194YSN), build 16.9.0 (2611251), Stage (yellow bar), acda.test9, app English, light.
Nothing filed, commented or status-changed. Screenshots and logs local only.

## Setup
- Phone came up with automatic time ON (2026-11-27); turned it off and set 2026-12-30 (Samsung Software update popup Backed, KF-003).
- Mine showed **Free** (the earlier test sub had lapsed). Bought the New Year annual Pro test subscription
  (annualsubscription_newyear_2611, Play sheet 「Test card, always approves」) → Pro, 2839 credits.

## State A — Pro, no Auto Pass, 12/30 (screenshots/r6-A-credit-ny-1.png + source)
「New Year Special」; balance 2839, no Auto Pass line; card 「Annual Auto Pass Discount」 1000 +1000 NT$2490; packs
50…2000 struck through with member prices; 「Annual top-up automatically!」 + CTA 「Continue with the best deal」 →
Play 「Credit Auto Pass (2000 Credits)」 NT$2,490/30 min (pdrm_2000_credit_paiduser_yr_autopass). No 1000+1000 sale
pack, no 「Get 2000 credits for …」 — correct per R-048 / Q-14.

## Auto Pass purchase
Play sheet 「Test card, always approves」 → subscribed 12:14 (logcat doVerifySubscribe productId
pdrm_2000_credit_paiduser_yr_autopass). Balance stayed 2839 (no +2000 seen; R1r saw +2000) — side observation, possibly the
shifted clock: logcat shows SocketTimeout / certificate-expired errors to apptest.cyberlink.com at the 12/30 date.

## State B — Pro + Auto Pass, 12/30 (r6-B-credit-ny-1.png, r6-B-credit-ny-relaunch.png, r6-B-play-2000-ny.png)
「Auto Pass activated」 ⓘ on the balance line; 「Special Offer」 1000 +1000 NT$2740; 「Enjoy lower prices as a Premium
user !」; CTA 「Get 2000 Credits for NT$2740」. Same after a relaunch. CTA → Play 「2000 Credits」 NT$2,740.00 (test card);
cancelled with Back. launchBillingFlow does not log the SKU; NT$2,740 is unique to pdrm_2000_credit_paiduser_christmas
(pdrm_2000_credits_paiduser = NT$3,350, yr_autopass = NT$2,490).

## State B — 12/15 Christmas (r6-B-credit-xmas.png, r6-B-play-2000-xmas.png)
「Christmas Special」, otherwise identical: 「Auto Pass activated」, Special Offer 1000 +1000 NT$2740, 「Get 2000 Credits
for NT$2740」 → Play 「2000 Credits」 NT$2,740.00 (christmas SKU by price); cancelled.

## Verdict
P0311: **not a bug** under R-048 / Q-14 — with Auto Pass the 2000 pack (1000+1000, 「Get 2000 Credits for …」, christmas
SKU) is offered; the ticket's no-Auto-Pass repro shows the correct Auto Pass sale. Same holds for DRA262611P0261 (Christmas).
Text note: the app writes 「Get 2000 **C**redits for NT$2740」 (capital C) vs the table/Design 「Get 2000 credits for …」.
TC-121 (table expects the 2000 pack without Auto Pass) is out of date against R-048 — recorded Fail spec-addition.

## End state
acda.test9 Pro (annualsubscription_newyear_2611 test sub, renews every 30 min) + Credit Auto Pass (test sub), 2839
credits; nothing else bought. Phone 2026-12-24, automatic time off, light, portrait, app English on the Launcher Home.
Logs: logs/ (pull-logs R6-a).
