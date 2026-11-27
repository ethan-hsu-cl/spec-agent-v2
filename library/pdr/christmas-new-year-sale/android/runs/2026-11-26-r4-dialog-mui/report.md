# R4 report: Not Enough Credit dialog in 26 languages (REQ-009)

Draft 20261126-154459 (in review): R-070, Q-19, TC-153 – TC-204. Build 16.9.0 (2611251), SM-A516B Android 13, Stage, phone date 2026-12-24 (Christmas window; Image to Video loaded on the real date first, KP-144; languages switched in place, O-1).

## Tally
24 Pass, 2 Fail (defect), 26 Blocked (test-data), 52 total.

| Segment | Rows | Pass | Fail | Blocked |
|---|---|---|---|---|
| R4-a Free 「Upgrade to Pro」 dialog | 26 | 24 | 2 | – |
| R4-b Paid 「More Credits Needed!」 dialog | 26 | – | – | 26 |

## Fails
- TC-159 ITA: body 「Non disponi di sufficienti crediti per usare questa funzione. Passa Pro+ per ricevere crediti bonus gratuiti ogni mese.」 names Pro+ (and lacks 「a」); title and English say Pro. Screenshot TC-159-ITA.png.
- TC-168 Viet: body 「You don't have enough tín dụng to use this feature. Nâng cấp lên Pro+ to get free bonus tín dụng every month.」 is mostly English and names Pro+. Screenshot TC-168-VIE.png.

Wording notes (recorded per Q-19, not failed): JPN and ESP drop 「bonus」; KOR drops 「free」; KOR / Thai / Persian titles spell the plan out while the body writes Pro; KOR body leaves 「요.」 alone on the last line; FRA CTA wraps to two lines inside the button; in RTL languages the page behind the dialog is not mirrored (outside these rows).

## Blocked
TC-179 – TC-204: buying the Pro test subscription (annualsubscription_christmas_2611, test card) added the 100 monthly credits at once, 7 → 107, at or above the 70 price (O-6). They need 38+ credits spent or a lower balance set by RD.

## State left
acda.test9 Pro (renewing test subscription), 107 credits. Phone 2026-12-24, automatic off, app English (US) on the Launcher. An empty project may be in Recent Projects (O-7). Nothing generated or filed.

## Filed
TC-159 / TC-168 filed 2026-11-26 as DRA262611P0328 (ISS-XMA-42, S3 RD [UI]) on TR261125-0064 (`ebugs/2026-11-26-r4/`).

## R4-b re-run (2026-11-26 16:19–16:28, after the user lowered the balance)
acda.test9 Pro, balance 22, price 70. All 26 paid-dialog rows ran: 25 Pass, 1 Fail.
- **TC-194 Viet Fail (defect):** body 「You don't have enough tín dụng to use this feature. Get tín dụng now!」 is English except 「tín dụng」; title 「Cần Thêm Tín Dụng!」 and CTA 「Nhận Ưu Đãi Ngay!」 are Vietnamese. Same pattern as TC-168 (free dialog, DRA262611P0328, which covers the free dialog only). Screenshot TC-194-VIE.png.
- ITA paid dialog (TC-185) has no plan name and passes: the Pro+ text is only in the free dialog.
- Wording notes (Q-19, not failed): JPN body asks to buy credits; ESP CTA drops 「now」; ESP (MX) title ends with a period; FRA CTA wraps to two lines inside the button.

**R4 total: 49 Pass, 3 Fail (TC-159, TC-168 filed as DRA262611P0328; TC-194 filed as DRA262611P0329), 0 Blocked.** State: acda.test9 Pro, 22 credits; phone 2026-12-24, automatic off; app English (US) on the Launcher.
