# Observations — R1r recheck (Android, Play test build 16.9.0 2611201, SM-A516B)

- **O-1** (TC-013, TC-101) On the US store the interstitial and the IAP page disagree: the interstitial reads
  「SAVE 52%」 「vs. paying $7.99/mo × 12」 from the regular monthly SKU `monthly_sub_usd6.99_202209` ($7.99), while
  the IAP page reads the campaign `monthlysubscription_christmas_2611` ($6.99) and 「45% OFF」. On the Taiwan store
  both monthly SKUs cost NT$240, which hid it in R1. The Save % is computed by the app and truncated, not rounded:
  Indonesia 58.68% shows 「58% OFF」 (TC-112), Taiwan 57.99% showed 57 (R1 O-3, now settled).
- **O-2** (TC-113) Philippines store: the regular monthly SKU `monthly_sub_usd6.99_202209` is ₱469.00, cheaper than
  the campaign monthly `monthlysubscription_christmas_2611` ₱485.00 (logcat 14:58:26). A store-price matter for PM.
- **O-3** (segment start) The Play test build (installed 14:42) was already signed in as acda.test9 (Free, 3545
  credits) on Stage; no sign-in was needed. The first relaunch at 14:52 still showed the interstitial (after the AI
  Mini Drama intro), so the once-a-day count had not been used on this install; no `pm clear` was needed.
- **O-4** (setup) Play Billing Lab: terms accepted with 「Continue as Acd」 on acda.test9 (user OK 2026-11-23). Its
  first screen asks 「Continue as …」 again after each relaunch; a configuration lasts 2 hours (「Active until …」).
  Country suggestions are not in the accessibility tree: tap the first suggestion by position (y≈662; India is the
  second, y≈788). Restored to Taiwan at 14:59 (active until 16:59, Introductory offer: Yes).
- **O-5** (TC-104, TC-105; script) The Play sheet's SKU is not in the app's logcat at launch (`launchBillingFlow:
  BillingResponse 0` only). While the sheet is open, `adb shell dumpsys activity activities | grep -o "iabData:[^ ]*"`
  prints it (`iabData:subs:<package>:<sku>`); use it for every 「SKU (logcat)」 check.
- **O-6** (TC-105) Taiwan store: monthlysubscription_christmas_2611 and the regular monthly_sub_usd6.99_202209 are
  both NT$240.00, so the Christmas monthly is no cheaper in Taiwan (annual christmas NT$1,210.00). Store pricing; for
  PM if the monthly should be discounted in every country.
- **O-7** (TC-124, TC-148) Signed in (acda.test9, Free) the Buy More page still shows 「First Purchase Discount」
  1000 +1000 NT$5600 and no Christmas 500 pack, although the app fetches pdrm_500_credit_freeuser_christmas
  (NT$1,960.00) and the account has bought 1000 and 2000 packs before (ledger), so 「First Purchase」 should arguably not
  apply either.
- **O-8** (TC-131; contradicts KF-002's guess) With the Play country set to United States in Play Billing Lab and
  the app in English, the credit page's 「Privacy Policy」 and 「Terms of Service」 still open the Traditional Chinese
  pages (`privacy.cyberlink.com/stat/policy/cht/app/privacy.html`, `…/cht/tos.html`). So the language is not picked
  by the Play store country; perhaps by the SIM/network region (Taiwan) or the account. No spec states it.
- **O-9** (TC-114) In 日本語 the Pro Mine's top pill stays English 「Credit Special Offer」 while the rest of Mine is
  Japanese. The spec gives the pill only in English; whether it should be localized is a PM question.
- **O-10** (TC-147, TC-115) No separate 「VIP Benefits」 page exists on 16.9.0 (2611201): for a Pro account the VIP
  banner is the card at the top of Mine and tapping it opens nothing; also no upgrade (IAP) entry for Pro, so the IAP
  page's banner can only be seen on Free.
- **O-11** (segment end, 15:26) Purchases made on acda.test9 (test track): annualsubscription_christmas_2611 at
  15:13 (Pro; renews every 30 min, KP-068) and Credit Auto Pass pdrm_2000_credit_paiduser_yr_autopass at 15:25
  (+2000; balance 5510). The account is now Pro with Auto Pass; Free and no-Auto-Pass rows need these to lapse. An
  Image to Video (Kling 4.0, 5 s, −70) task from TC-140 was still 「Processing…」 at 15:22 (left to finish).
