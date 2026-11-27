# (MX) Christmas & New Year Sales (Android) — what the phone needs before a run

The repository holds everything a run reads on the computer (table, `phases.json`, run plans, scripts). This list is
what has to be on the phone or the account instead, because it can't be committed.

## Phone, build and server
- Phone: Samsung Galaxy A51 SM-A516B, adb serial R5CN8194YSN, Android 13, 1080 × 2400 (Round 1, 2026-11-23).
- UiAutomator2 server 5.7.0: Google Play Protect blocks it on this phone (「Unsafe app blocked」); the user allowed it
  once on the phone (2026-11-23). The run never overrides Play Protect itself: if it is blocked again, stop for the user.
- Appium needs JAVA_HOME set to the installed JDK 17 (`/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home`;
  the script's Homebrew default is not on this Mac) and the Android SDK build-tools (installed 2026-11-23).
- Build under test: 16.9.0 (2611201). A clean install uses the APK the user gave:
  `/Users/biaggi_li/Downloads/PowerDirector Mobile for Android-DRA261109-01-16.9.0.2611201.apk` (`adb install -r`, or
  `pm clear` for a fresh first launch with the same build).
- Server: Stage, from the empty `/sdcard/cyberlink/PDR/testserver.config` (KP-005); the Launcher bar is yellow.
- Campaign window: the stage server's RD test date is set inside the Christmas window (user, 2026-11-23, Q-1 ruling).
  Rows needing another date (before 12/11, midnight boundaries, the next day, the New Year window, another time zone)
  are Blocked test-data until RD changes it.

## Accounts and store
- Google account on the phone: acda.test9@gmail.com. Its Play store showed Taiwan prices (NT$1,210/year) on the
  interstitial. Rows expecting US prices, India / Indonesia / Philippines and Japan set the Play country in
  **Play Billing Lab** (installed) and restore it after the row (Q-17 ruling).
- Purchases (TC-147 – TC-150): the agent buys the Pro test subscription and credit packs without asking when the
  Google Play sheet shows a test purchase (license tester, 「Test card, always approves」; AGENTS.md). A sheet with a
  real payment method stops for the user. Never type a password.
- Free rows run before the purchases; TC-147 makes the account Pro. Low-balance rows (Not Enough Credit dialog) need a
  balance below the Image to Video (Custom) price; record the balance read.
- No earlier build is on the computer, so the upgrade rows (TC-011, TC-012) are Blocked test-data.

## Phone settings (the run sets and restores them, run step 4)
- The user sets: USB debugging on, this computer allowed; Stay awake on; no PIN; on the USB cable.
- Dark / light mode, display size (short screen), auto-rotate, app language, Play Billing Lab country.
