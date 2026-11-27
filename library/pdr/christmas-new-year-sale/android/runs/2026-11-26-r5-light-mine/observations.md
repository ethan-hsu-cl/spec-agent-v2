# Observations — R5 (16.9.0 build 2611251, SM-A516B, Stage)

- **O-1 (TC-102, TC-146) The app's own Appearance overrides the system dark mode.** Launcher ☰ › Preferences ›
  Appearance was 「Light Mode」 at the start, so `cmd uimode night yes` changed Samsung's Display to Dark but the app
  stayed light (also after a relaunch). The run set it to 「Device Settings」 (options: Light Mode / Dark Mode /
  Device Settings), after which the app follows the system switch; restored to 「Light Mode」 at the end. The R4
  captures were dark, so the setting was changed between R4 and R5. Each system switch recreates the app on the
  Launcher Home tab (the open page closes). Evidence: screenshots/r5-app-appearance.png, r5-app-appearance-device.png.
- **O-2 Start state differed from R4's end.** Account acda.test9 was **Free** with 22 credits (Pro at the end of R4;
  the renewing test subscription has lapsed or was cancelled by someone else), and the phone date was 2027-01-01 17:20
  (R4 ended on 12/24). Nothing bought or cancelled in R5.
- **O-3 (contradicts KF-004) Mine's top pill counts down in the New Year window.** On 2027-01-01 Mine showed the gift
  icon with 「4D 06:39:11」, and on 12/30 6D…; KF-004 says Mine's pill never counts (ISS-XMA-35). screenshots/r5-start.png.
- **O-4 The IAP page opened from the Launcher pill is outside the page source.** While it is on screen, `texts` /
  `els` list the Launcher behind it, and system Back went to the Launcher (toast 「Tap the back button again to
  exit.」) with the IAP still drawn; its ‹ arrow (by position) closed it. In landscape after the rotation back to
  portrait the page stayed drawn until ‹ was tapped. screenshots/r5-end-check.png (before it was closed: an earlier
  copy was overwritten).
- **O-5 Mine Credits bar is taller than the Design (user request C).** Card width 996 px = Figma 343 → 2.904 px per
  Figma px. Credits bar (credit_remain_area) 207 px against 162.6 expected (+27.3 %) on Free and Pro, light and dark.
  Free card 778 px against 673.7 (+15.5 %); Pro card 529 px against 522.7 (+1.2 %). Ratios bar/card height: Free
  0.266 vs 0.241 (+10.2 %), Pro 0.391 vs 0.311 (+25.8 %); bar/card width 0.208 vs 0.163 (+27.3 %). mine-credit-bar.json.
- **O-6 Interstitial after the date change.** Moving the date 1/1 → 12/30 brought the New Year interstitial at the next
  launch (KF-003); closed with ✕. screenshots/r5a-ny-interstitial-light.png.
- **O-7 (R5-c) Pro by test subscription.** Mine 「Claim Holiday Deal」 › Christmas Special IAP (57% OFF, NT$1210/Year,
  3D 06:19:20 countdown) › Continue › Google Play sheet 「PowerDirector Yearly Subscription」 NT$1,210.00/30 min,
  「Test card, always approves」, 「This is a test subscription … You will not be charged.」 › Subscribe. SKU
  `annualsubscription_christmas_2611` (logcat). The app returned to the Launcher Home as Pro; Mine 122 credits
  (22 + 100 monthly). The 5th tab's label reads 「Pro」 (it read 「Mine」 while Free). A first `lbl Subscribe` hit the
  sheet's legal paragraph and opened a Google payments legal page in Chrome; Back returned to the unchanged sheet,
  then Subscribe was tapped by position. screenshots/r5d-iap.png, r5d-play-sheet.png, r5d-mine-pro-light.png.
- **O-8 (R5-c, request C) Pro card in light and dark with page source.** banner_view 996×529 at (42,246),
  credit_remain_area 996×207 at (42,568), light and dark identical, equal to the R4 dark pixel measure. Bar/card h
  0.391 vs 0.311 (+25.8 %), bar/card w 0.208 vs 0.163 (+27.3 %); bar 207 px vs 162.6 Figma-scaled (+27.3 %), card
  529 vs 522.7 (+1.2 %). Bar content (icon, 「Credits」, value, chevron) is vertically centred within 1 px on Free and
  Pro; the extra height is padding: icon row 77 px above and below vs 46.5 scaled (Figma 16), value row 68 vs 52.3
  (Figma 18); icon 53 px vs 69.7 scaled. mine-credit-bar.json `bar_content`; r5c-crop-pro-light.png,
  r5c-crop-pro-dark.png.
