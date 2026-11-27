# Observations — R4 (2026-11-26)

- O-1 (R4-a, TC-153 – TC-165; screenshots/r4a-zhTW-ready.png, TC-154-CHS.png, r4a-zhCN-after-locale.png). Cheaper route
  than KP-144's per-dialog setup: the Image to Video page needs the real date only once. Load I2V › Custom on the real
  date (photo + inspiration prompt, Generate 70), move the phone to 2026-12-24, `activate`, then for each language run
  `device-android.ts locale <tag>` (per-app locale, `cmd locale set-app-locales`) with the page still open: the activity
  is recreated in the new language and keeps Kling 4.0, the photo, the prompt and the price 70, and Generate opens the
  Christmas dialog in that language. 13 languages took 15:52–15:54 host (~12 s each) after one ~3 min setup. The prompt
  filled from the inspiration chip stays in the first language (Traditional Chinese) on later languages; the dialog
  texts are not affected. Extends KP-144: the expired-certificate failure is per page load, and a locale recreation is
  not a page load.
- O-2 (R4-a, TC-161 / TC-160 / TC-162). Wording choices recorded per Q-19, rows passed: Korean body has no 「free」
  (보너스 크레딧, no 무료), the title writes 프로 while the body writes Pro, and the body breaks 받으세요 with 「요.」 alone
  on its last line; Japanese (毎月無料クレジット) and Spanish (créditos gratis) render 「free bonus credits」 without
  「bonus」. French title 「Mettre à niveau à Pro」 is literal; its CTA 「Obtenez maintenant une réduction」 wraps to two
  lines inside the button (not clipped).
- O-3 (R4-a). acda.test9 Free (Mine 「Free」 「Claim Holiday Deal」), balance 7 at start and end (logcat totalRemain=7 on
  every reading); Stage on the real date still shows the Black Friday pill 「6D 08:10:15」 on the Launcher.
- O-4 (R4-a second half, TC-166 – TC-178). The O-1 route held for a second setup: real date → `launch --lang th-TH` →
  I2V › Custom (intro 「ลองใช้เลย」, inspiration chip, photo) → 12/24 → `activate` → 13 languages 16:00–16:02 host. No
  Software update screen this time. Balance 7 throughout (logcat totalRemain=7). Two Fail defects in R4-a now carry
  「Pro+」 in the body: Italian (TC-159) and Vietnamese (TC-168, also mostly left in English: 「You don't have enough
  tín dụng to use this feature. Nâng cấp lên Pro+ to get free bonus tín dụng every month.」), so the body string
  looks reused from a Pro+ variant in those locales.
- O-5 (R4-a, wording per Q-19, rows passed). Thai and Persian titles spell the plan out (โปร; 「نسخهٔ حرفه‌ای」 =
  professional version) while their bodies write Pro, like Korean (O-2). Polish says 「Przejdź na plan Pro」 in the body;
  Dutch and Swedish/Danish/Norwegian render credits as tegoed / krediter / kreditter. Arabic, Persian and Hebrew dialog
  texts run right to left; the I2V page behind them is not mirrored (back arrow left, Kling row left-aligned) in
  Arabic/Persian/Hebrew, outside these rows.
- O-6 (R4-b, TC-179 – TC-204; screenshots/r4b-iap.png, r4b-play-sheet.png, r4b-mine-pro.png). Pro purchase at phone
  2026-12-24 16:06: Mine 「Claim Holiday Deal」 › Christmas Special IAP (Special Offer 57% OFF, NT$1210/Year, Continue,
  countdown 「3D 07:54:25」) › Continue → Play sheet 「PowerDirector Yearly Subscription」 「NT$1,210.00/30 min」 「Test card,
  always approves」 「This is a test subscription. It will recur according to this schedule. You will not be charged.」 ›
  Subscribe (tapped by bounds 540,2164, O-11 of R2) → onPurchasesUpdated annualsubscription_christmas_2611
  (GPA.3314-8789-2130-90557), updateSubscribingStatus true, doVerifySubscribe OK (one acknowledgePurchaseResponse 2
  「Server error」 logged, then OK). The Mine tab is labelled 「Pro」 afterwards. Balance 7 → 107: the Pro subscription
  grants 100 giveaway_monthly credits at once (no 35 trial bonus this time, unlike R2-d's 3755), so a fresh Pro
  purchase can never leave a balance below the 70-credit Image to Video price: the paid dialog rows need credits spent
  (without a video generation) or a balance set by RD. All 26 rows Blocked test-data.
- O-7 (R4-b, script). After the purchase the bottom tab reads 「Pro」, so `lbl Pro` / `lbl Mine` match other elements
  (`lbl Pro` opened New Project's Add Media → an empty project's editor; left with TimeLine_Home, an empty project may
  be in Recent Projects). Tap the tab by pixels (972,2190). The Mine 「Credits」 row opened nothing; a stray tap opened
  Demo Videos (left by its back arrow). Logs logs/R4-b-20261126-160831.
- O-8 (R4-b re-run, TC-179 – TC-204; screenshots/r4b2-mine.png, r4b2-zhTW-ready.png). After the user lowered the
  balance (REQ-009 follow-up): acda.test9 Pro (Mine 「Pro」 「You're on the highest plan.」), balance 22. The two
  spends that lowered it are in the credit history before this segment (ImageToVideo −60 at 16:16:10 and −25 at
  16:16:32 host, the user's); logcat showed a cached totalRemain=47 until 16:19, then 22 on every reading to the end:
  nothing was generated in the segment. A 「Good news! Your Image to Video task has been completed」 toast was on the
  Launcher at the start (Close). The O-1 route held a third time: real date → `launch --lang zh-TW` → I2V › Custom
  (inspiration chip, cat photo, Kling 4.0, Generate 70) → 12/24 → Samsung Software update screen (Back) → `activate` →
  26 languages 16:21–16:27 host. The paid dialog's height varies by language, so its ⓧ moves between y ≈ 750 and 790;
  a tap at (937,770) closed it every time.
- O-9 (R4-b re-run, wording per Q-19). 25 of 26 paid dialogs are fully translated. Vietnamese (TC-194, Fail defect) is
  the one left in English: body 「You don't have enough tín dụng to use this feature. Get tín dụng now!」, the same
  half-translated pattern as the Free dialog's body (TC-168); the Vietnamese title and CTA are translated, so it is the
  body string only. Italian's paid body has no plan name (TC-159's 「Pro+」 is in the Free body only). Recorded
  wording: Japanese body asks to buy (クレジットを購入してください) for 「Get credits now」; Spanish CTA drops
  「now」 (Aprovechar el descuento); Spanish (MX) title ends with a period (Necesitas más créditos.); French CTA wraps
  to two lines inside the button; Dutch uses tegoed and 「Koop nu tegoed!」. Arabic, Persian and Hebrew run right to
  left.
