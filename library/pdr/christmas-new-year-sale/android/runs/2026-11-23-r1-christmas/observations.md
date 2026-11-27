# Observations — R1 Christmas (Android, 16.9.0 2611201, SM-A516B)

- **O-1** (TC-027) The interstitial's 「Terms of Service」 and 「Privacy Policy」 open the Traditional Chinese pages
  (`privacy.cyberlink.com/stat/policy/cht/tos.html`, `…/cht/app/privacy.html`) while the phone locale and the app are
  en-US. Possibly chosen by the Play/region (Taiwan) rather than the language; no spec states which language. Evidence
  screenshots/TC-027-01.png, TC-027-03.png.
- **O-2** (TC-028) On a fresh launch the first 「Restore Purchase」 › OK asks Google's 「Get a list of Google accounts on
  the device」 permission; after Allow the app returns to the interstitial with no result message (log: GoogleAuthUtil
  `NEED_PERMISSION`, no toast). Only a second tap shows 「Your current Google Play Store account has no purchases.」.
  Evidence screenshots/TC-028-03.png, TC-028-toast-2.png.
- **O-3** (TC-013, interstitial and IAP on the Taiwan store) 「SAVE 57%」 / 「57% OFF」 while the PM formula (R-036,
  ruling Q-3) on the store prices NT$1,210/year vs NT$240 × 12 = NT$2,880 gives 57.99 → 58% (requirements Q-3 says
  "with TW 58%"). Either the % is truncated or it is the mockups' fixed 57. The US store (45%) tells them apart:
  check it once Play Billing Lab is set up (TC-013).
- **O-4** (TC-019, TC-006) The Christmas IAP plan card shows the tag 「Special Offer」 and 「57% OFF」; R-035 (PM 1104,
  ruling Q-10) expects 「Christmas Treat」 and 「Save <xx>%」 with no 「Offer」 copy. For the IAP rows of R1-c.
  Evidence screenshots/TC-019-01.png.
- **O-5** (TC-019) From the interstitial, 「More subscription plan」 › IAP back arrow (`[AID]IAP_Back`) lands on the
  Launcher, not back on the interstitial. No spec states where it should return.
- **O-6** (TC-013) Play Billing Lab is installed but not signed in: its first screen needs 「Continue as Acd」, which
  accepts Google's terms of service. The US / India / Indonesia / Philippines / Japan store rows need the user to
  accept it (or allow the agent to) first.
- **O-7** (TC-030 – TC-055, R-022) In every non-English app language the interstitial keeps four English strings:
  「SAVE」, 「vs. paying NT$240/mo × 12」, 「/year」 and 「More subscription plan」, while the CTA, disclaimer and
  bottom links are translated. One cause for all language rows (likely one eBug for the untranslated strings, plus
  separate items for wrong CTA wording per language and the bottom-bar overlap in RU / FR). The app also follows the
  Design layout (「SAVE」 「xx」 「%」, 「vs. paying …/mo × 12」) rather than the sheet's one-line 「Save 57%」 / 「vs.
  $6.79/mo」, so the sheet's 「Save」 and 「vs.」 strings are the translations to use for those two lines (PM to
  confirm). Plain relaunch did not bring the interstitial back today (once a day, R-012), so each language ran on
  `pm clear` + per-app locale (`cmd locale set-app-locales`), system language untouched.
- **O-8** (after TC-055) Second launch after `pm clear`, app language back to the device's en-US: 「Welcome to
  PowerDirector」 「Get Started」 (Open intro) → an AI Mini Drama intro (「Turn your ideas and characters into captivating
  mini dramas.」 「Continue」, then 「Try It Now」 with 「Don't show again」) → back arrow → the Christmas interstitial.
  R-011 names only Open intro → interstitial; the AI Mini Drama pages sit between them. Evidence
  screenshots/R1-b-end.png (Launcher after X).
- **O-9** (R1-c, before TC-095) Sign-in tried for the Free rows: Mine › User Sign in › Google button → Chrome went
  straight to mauth-stage 「You Are All Set!」 (Chrome already signed in), but back in the app Mine still shows 「User
  Sign in」 and the Free card; logcat 11:53:45 `bindMember, Exception: retrofit2.HttpException: HTTP 403` /
  `[updateAfterLogin] bindMember failed.` and no on-screen message this time (KP-093 saw 「Account Not Found」). R1-c
  rows ran signed out; the Free card and campaign entries are the same either way. Evidence screenshots/signin-02.png,
  signin-03.png.
- **O-10** (TC-104, TC-105; blocks R1-d purchases) From about 11:56 every subscription CTA on the Christmas IAP page
  opens the app's own dialog 「Unofficial Version」 「We couldn’t verify your app installation. Purchases are
  unavailable.」 「Understood」 instead of the Google Play panel; no billing or SKU line in logcat. In R1-a (11:1x,
  right after `pm clear`) the interstitial CTA opened the Play test sheet. In between: two more `pm clear`s (R1-b) and a
  Google sign-in that failed with bindMember HTTP 403 (O-9, KP-093 also blames the device identity after the Play
  Integrity call). The build was sideloaded with `adb install` (installer not Google Play), so a Play Integrity
  verdict is the likely cause. Needs the user / RD: how this build passes the installation check (install through
  Play internal testing, or an RD bypass) before any purchase row (R1-d) can run. Evidence screenshots/TC-104-01.png,
  TC-105-03.png.
