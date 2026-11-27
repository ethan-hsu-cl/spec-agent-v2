# Run state — R1 Round 1: Christmas rows of Android v2 on 16.9.0 (2611201), Samsung SM-A516B

Table: library/pdr/christmas-new-year-sale/android/cases.csv
Started: 2026-11-23T03:09:42.655Z

## Environment
(build, server, device, tier, credit balance, Pink toggles, Log stage timings, Write Log)

## Checkpoints

### 2026-11-23T03:24:44.268Z · next TC-029 (R1-b)
{"Pass":10,"Blocked":8,"Not run":76}

R1-a done. App: 16.9.0 (2611201) after pm clear at 11:11 (fresh first launch done; GDPR accepted, notifications allowed, Google accounts permission allowed for Restore). Free, signed out (Stage sign-in after pm clear fails, KP-093); credits totalRemain=0. Stage (yellow bar). Launch count 3: the interstitial now shows straight at each launch (2nd launch had the Open intro first). Phone on Launcher Home. Play store Taiwan (NT$1,210/NT$240); Play Billing Lab NOT signed in: its first screen needs accepting Google's terms (user's go-ahead) — US/other store rows wait for it (TC-013, TC-014 Blocked). Fix this segment: device-android.ts back/home fall back to the W3C keycode route / adb (UiAutomator2 5.7 has no mobile: pressKey). Logs pulled 11:24 (logs/R1-a-20261123-112426).

### 2026-11-23T03:47:31.898Z · next TC-083 (R1-c)
{"Pass":11,"Blocked":8,"Fail":26,"Not run":49}

R1-b done (11:25–11:48). Interstitial is once a day (R-012): a plain relaunch at 11:26 went to the Launcher, so each language ran on pm clear + per-app locale (Android 13: cmd locale set-app-locales; system language never changed). After the last pm clear (uk-UA) the app had 2 launches; ended with locale reset (get-app-locales [], system en-US), a 2nd launch in en-US (Open intro → AI Mini Drama intro → interstitial, O-8) and X → Launcher Home. App: fresh state from pm clear at ~11:45, GDPR accepted, notifications allowed (Google accounts permission NOT yet granted for Restore since this pm clear), Free, signed out (KP-093), Stage yellow bar, Taiwan store, Play Billing Lab not signed in. Interstitial already shown today. Results of TC-034–TC-055 were recorded in batches after their runs, so log-slice windows for them are coarse; the case markers in activity.log give the exact starts. Logs logs/R1-b-20261123-114701. Note for scripts: device-android.ts waitfor matches text only ("id:…" always times out).

### 2026-11-23T04:17:42.307Z · next TC-148 (R1-d)
{"Pass":18,"Blocked":19,"Fail":35,"Not run":22}

R1-c done (11:49–12:17; 7 Pass, 9 Fail defect, 11 Blocked test-data). App: pm clear at ~12:13 (for TC-145/TC-143/TC-109): fresh state, GDPR accepted, notifications allowed, interstitial shown today and closed via More subscription plan › Back; Free, signed out (Google sign-in fails twice: bindMember HTTP 403, O-9 / KP-093; every signed-out paid action and Mine › Credits open 「Sign in to get your credits back」). Credits 0 (totalRemain=0); daily credits shown 「Claimed」, not claimed by the run. Media permissions granted (phone-settings grant-all). Stage yellow bar, Taiwan store, Play Billing Lab not signed in. BLOCKER for R1-d: since ~11:56 every subscription CTA on the IAP page shows 「Unofficial Version」 「We couldn’t verify your app installation. Purchases are unavailable.」 instead of the Google Play panel (O-10; R1-a's interstitial CTA did open the Play test sheet before that). Phone settings restored: light mode (night no), wm size reset (1080x2400), user_rotation 0, accelerometer_rotation 1. Logs logs/R1-c-20261123-121720. Script notes: device-android.ts id continueBtn once hung past 120 s (tap by coordinates worked); lbl "Sign In" matches the dialog title first (tap the button by coordinates).

### 2026-11-23T06:06:51.190Z · all recorded
{"Pass":18,"Blocked":41,"Fail":35}

R1 closed at the user's decision (Wrap up R1 now): R1-d's 22 rows recorded Blocked test-data (purchases unavailable on the adb install, O-10; Stage sign-in 403, O-9 / KP-093). Phase wrap-up next.

### 2026-11-23T06:18:33.230Z · all recorded
{"Pass":18,"Blocked":41,"Fail":35}

R1 closed; phase wrap-up done (2026-11-23). 18 Pass, 35 Fail, 41 Blocked. eBug drafts: 12 entries (ISS-XMA-01…12) in library/pdr/christmas-new-year-sale/android/ebugs/2026-11-23-r1/ with review page 20261123_eBug_review_Christmas-Sale-R1_16.9.0.html (format check 0 errors); nothing filed. blocked-reasons.json written (41 rows). Coverage page coverage.html built (no taps.jsonl on this Android run: 0 presses matched). report.md text handed to the orchestrator (the subagent harness refused report files). Re-run of R1-d needs purchases on the install (O-10), Stage sign-in (O-9) and the user's OK for Play Billing Lab terms. Knowledge pass due (O-9 confirms KP-093).
