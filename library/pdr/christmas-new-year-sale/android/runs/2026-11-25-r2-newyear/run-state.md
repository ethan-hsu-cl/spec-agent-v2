# Run state — R2 Round 2: New Year rows of Android v2 on 16.9.0 (2611231), Samsung SM-A516B

Table: library/pdr/christmas-new-year-sale/android/cases.csv
Started: 2026-11-25T03:48:22.912Z

## Environment
(build, server, device, tier, credit balance, Pink toggles, Log stage timings, Write Log)

## Checkpoints

### 2026-11-25T04:14:31.473Z · next TC-056 (R2-b)
{"Fail":4,"Pass":6,"Not run":49}

R2-a done (11:49–12:14 host time; 6 Pass, 4 Fail defect, 0 Blocked). Start of R2 read: build 16.9.0 (2611231, adb install by the user 2026-12-29 11:43 phone time, fresh install), Stage (yellow bar), signed in acda.test9, Free (Mine 「Free」 「Claim Holiday Deal」), credits 3720 (Mine and logcat totalRemain=3720), phone date 2026-12-29 11:49 Asia/Taipei, automatic date off. Purchases: Play sheet opened from the interstitial CTA on this adb build (no 「Unofficial Version」), cancelled with Back; nothing bought. Phone clock moved for rows (12/30, 12/31, 1/1, 1/2, 12/27 23:59, 12/28 00:00, 1/5 00:03 and 23:58, past 1/6 00:00) and RESTORED to 2026-12-29 12:13 (current time of day). Play Billing Lab: US config added for TC-020/021/003/004, then deleted (store back to Taiwan, NT$ prices on the relaunch). App left on the 「New Year Special」 interstitial (12/29, Taiwan store; it showed again after the clock went back, O-4). Logs logs/R2-a-20261125-121401 (by-case excerpts empty: phone clock shifted, causes read from logcat-live by phone time). Findings: TC-020 52%/$7.99 (regular monthly SKU), TC-021 「cancelled」, TC-023 first Back ignored, TC-003 banner title 「Turn one photo to cinematic reel」. Script notes O-5: date via Settings (helpers: Set date calendar content-desc, time picker EditTexts move up with the keyboard), Samsung update screen pops up after date changes (Back). Next R2-b TC-056.

### 2026-11-25T04:31:20.129Z · next TC-085 (R2-c)
{"Fail":30,"Pass":7,"Not run":22}

R2-b done (12:16–12:31 host time; 1 Pass TC-056, 26 Fail defect, 0 Blocked). Phone date alternated 12/29 ↔ 12/30 in Settings per language (no pm clear; account still acda.test9 Free, logcat totalRemain=3720 at 12/29 12:30), per-app locale per row; ended with phone 2026-12-29 12:30 Asia/Taipei (automatic off), app per-app locales [] (en-US), app on the Launcher (interstitial already shown today 12/29, closed with X; R2-c needs it back: move the date to 12/30 and back, or rely on O-4). Stage, Taiwan store. Logs logs/R2-b-20261125-123056 (by-case excerpts empty: clock shifted). Findings O-6: four English strings in every language; FR/IT title art English, UK shows Russian art, es-ES uses ESP (MX) title+CTA; CTA wording off in 12 languages; RU overlap, FR/UK/PL separators, PL CTA two lines. O-7: Samsung update screen after each 12/30 move (wait 3 s, Back, then launch). Next R2-c TC-085.

### 2026-11-25T04:58:22.353Z · next TC-151 (R2-d)
{"Fail":34,"Pass":16,"Blocked":2,"Not run":7}

R2-c done (12:31–12:57 host time; 8 Pass, 5 Fail defect, 2 Blocked test-data). acda.test9 Free, 3720 credits throughout (logcat totalRemain=3720 at 12:55), Stage, build 2611231. Phone date moved for TC-089 (2027-01-03 12:00), TC-152 (12/28 00:05, then 12/29 23:59 → 12/30 00:00) and RESTORED to 2026-12-29 12:51 (current time of day; automatic off). Dark mode only for TC-085, back to light. Play Billing Lab US config added for TC-103 then deleted (Taiwan NT$ prices back on relaunch). Play sheets opened for TC-106 (monthlysubscription_newyear_2611) and TC-107 (annualsubscription_newyear_2611), cancelled; nothing bought. App en-US on the Launcher (interstitial already shown 12/29). Fails: TC-085/086 banner title 「Turn one photo to cinematic reel」; TC-089 Mine pill has no countdown; TC-102 Special Offer / 57% OFF / no struck monthly / CTA 「Continue」 / feature cards. Countdowns all target 1/6 00:00:00; Launcher pill countdown starts at 12/30 00:00 (O-9). TC-138/139 Blocked: balance 3720. Logs logs/R2-c-20261125-125755 (by-case excerpts empty: clock shifted). Next R2-d TC-151.

### 2026-11-25T05:09:56.778Z · all recorded
{"Fail":38,"Pass":17,"Blocked":4}

R2-d done (12:58–13:09 host time; 1 Pass TC-151, 4 Fail defect TC-116/121/123/129, 2 Blocked test-data TC-136/137). acda.test9 made Pro: New Year annual test subscription annualsubscription_newyear_2611 bought 13:02 phone time on the Play test sheet (Test card, always approves; no Unofficial Version on the adb build 2611231, O-11); credits 3755 (3720 + 35 free-trial bonus), no Credit Auto Pass (R1r Auto Pass expired 11/23). Phone date moved 12/15, 12/30, 12/25 00:03 and RESTORED to 2026-12-29 13:09 (automatic off). Play sheet for 2000 credits (pdrm_2000_credits_paiduser) opened and cancelled; nothing else bought. App en-US on the Launcher (Pro tab), Stage, Taiwan store. Logs logs/R2-d-20261125-130931 (by-case excerpts empty: clock shifted). Findings: TC-116 VIP card no New Year decoration; TC-121/123 Auto Pass card instead of campaign 2000 pack, CTA/text differences; TC-129 countdown on the Christmas credit page. Phase R2 complete; wrap-up next.
