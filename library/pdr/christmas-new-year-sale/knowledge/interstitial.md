# Campaign interstitial

## KF-001 Showing the once-a-day interstitial again
- kind: howto · platform: android · use: run · tags: interstitial, reset, locale
- source: Christmas & New Year Sales Android run 2026-11-23-r1-christmas O-7 · verified: 16.9.0 build 2611201 (2026-11-23)

The interstitial shows once a day (R-012), so a plain relaunch after it was seen goes to the Launcher. To see it again
the same day, `adb shell pm clear` the app (Stage sign-in is then lost, KP-093) and relaunch; for a language row set
the per-app locale first (`cmd locale set-app-locales`, run-android.md), leaving the system language alone.

## KF-002 The sale's legal links open Traditional Chinese pages
- kind: quirk · platform: android · use: run, ebug · tags: interstitial, credits, links, locale
- source: Christmas & New Year Sales Android run 2026-11-23-r1-christmas O-1; run 2026-11-23-r1r-recheck O-8 · verified: 16.9.0 build 2611201 (2026-11-23)

With the app in English, 「Terms of Service」 and 「Privacy Policy」 on the interstitial and on the credit page open
`privacy.cyberlink.com/stat/policy/cht/tos.html` and `…/cht/app/privacy.html`, on the Taiwan Play store and also with
the Play country set to United States (Play Billing Lab). So the store country does not pick the language (perhaps
the SIM/network region or the account); no spec states which language they should be.

## KF-003 The phone's date drives the campaign window (android)
- kind: howto · platform: android · use: run, analysis · tags: campaign, date, window, interstitial, countdown
- source: user 2026-11-25 (chat, REQ-006, inbox I-035); Christmas & New Year Sales Android run 2026-11-25-r2-newyear O-4, O-5, O-7, O-10, O-15; run 2026-11-26-r3-lowbalance O-1, O-4 · verified: 16.9.0 build 2611251 (2026-11-26)

On Stage the app picks the Christmas or New Year campaign from the phone's system date (local time): no RD test date
is needed. Set it in Settings › General management › Date and time with automatic date off (`adb shell am start -a
android.settings.DATE_SETTINGS`; `cmd alarm set-time` has no permission): 「Set date」 › the day's content-desc
(「Tuesday, December 29, 2026」, 「Next month」 / 「Previous month」) › Done; 「Set time」 › tap the hour field, `input
keyevent MOVE_END DEL DEL DEL`, `input text HH`, the same for minutes, Done. Seen: 12/27 23:59 Christmas → 12/28 00:00
New Year, 1/5 23:59 New Year → 1/6 regular. The once-a-day interstitial comes back by moving the date to another day
(12/29 ↔ 12/30) instead of `pm clear` (KF-001), which keeps the Stage sign-in (KP-093); moving the clock backwards can
also bring it back the same day. The Samsung 「Software update」 screen (com.wssyncmldm) comes up a few seconds after a
date change, also over the time picker or the app: wait ~3 s, close it with Back (never install), then launch. Logcat
lines carry the phone's shifted time, so `log-slice.ts` by-case windows (host time) come out empty: read
`logcat-live.txt` by phone time. Put the phone back to the run's base date after each row.

## KF-004 New Year countdowns count to the end of 1/5 (android)
- kind: fact · platform: android · use: run, analysis · tags: countdown, launcher, iap, credits, mine
- source: Christmas & New Year Sales Android run 2026-11-25-r2-newyear O-3, O-9, TC-129 · authority: observed · verified: 16.9.0 build 2611231 (2026-11-25)

In the New Year window the Launcher pill, the IAP CTA and the credit page count to 2027-01-06 00:00:00 local (Q-18's
assumption). The Launcher pill reads 「On Sale!」 (gift icon) until fewer than 7 days remain; its countdown first shows
at a launch on 12/30 00:00 (「6D 23:59:30」), not while the app stays open over midnight. The IAP CTA counts from
12/28. Mine's pill never counts (ISS-XMA-35). The Christmas credit page also counts (to 12/28 00:00), against ruling
Q-11 (ISS-XMA-40).

