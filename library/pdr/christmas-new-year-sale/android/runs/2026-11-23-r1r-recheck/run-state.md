# Run state — R1r Round 1 recheck: rows R1 skipped, on the Play test build 16.9.0 (2611201), Samsung SM-A516B

Table: library/pdr/christmas-new-year-sale/android/cases.csv
Started: 2026-11-23T06:49:11.627Z

## Environment
(build, server, device, tier, credit balance, Pink toggles, Log stage timings, Write Log)

## Checkpoints

### 2026-11-23T07:00:38.911Z · next TC-134 (R1r-b)
{"Fail":6,"Pass":1,"Not run":28}

R1r-a done (14:50–15:00; 1 Pass, 6 Fail defect). App: Play test build 16.9.0 (2611201, installer com.android.vending), not cleared (no pm clear this segment). Signed in acda.test9@gmail.com (already signed in at start), Free, credits 3545 (Mine pill 14:55), Stage (yellow bar). Interstitial shown today at 14:52 (closed with X), so the next launches go to the Launcher. Play Billing Lab: terms accepted on acda.test9 (Continue as Acd, user OK); country RESTORED to Taiwan at 14:59 (config active until 16:59, Introductory offer: Yes; prices back to NT$ at the 15:00 relaunch). No purchase made, no Play sheet opened. Phone on the Launcher. Logs pulled 15:00 (logs/R1r-a-20261123-150024). Findings: interstitial uses the regular monthly SKU ($7.99 → 52%, O-1), Save % truncated (Indonesia 58.68 → 58), monthly-first landing missing for IN/ID/PH. Script note: Play Billing Lab country suggestions are not in the accessibility tree; tap by position (O-4).

### 2026-11-23T07:10:24.692Z · next TC-147 (R1r-c)
{"Fail":7,"Pass":3,"Blocked":4,"Not run":21}

R1r-b done (15:01–15:10; 2 Pass, 1 Fail defect, 3 Blocked test-data, 1 Blocked defect). App: Play test build 16.9.0 (2611201), not cleared. Signed in acda.test9, Free (Mine 「Claim Holiday Deal」), credits 3545 (Mine 15:02, logcat totalRemain=3545). Stage (yellow bar). No purchase made: two Play sheets opened (annual, monthly) and cancelled with Back (responseCode 1, updateSubscribingStatus false); Christmas 500 pack not offered so TC-148 not bought. Play Billing Lab country untouched: Taiwan (active until 16:59). Phone on Mine. Logs pulled 15:10 (logs/R1r-b-20261123-151009). TC-134/135/142 Blocked: balance 3545, only acda.test9 on the phone. Script note O-5: Play sheet SKU via dumpsys activity iabData. Next R1r-c TC-147 (subscribes, one-way).

### 2026-11-23T07:27:04.820Z · all recorded
{"Fail":14,"Pass":10,"Blocked":11}

R1r-c done (15:11–15:27; 7 Pass, 7 Fail defect, 4 Blocked test-data, 3 Blocked defect). Phase R1r: all 35 rows recorded (0 Not run). App: Play test build 16.9.0 (2611201), not cleared. Signed in acda.test9. PURCHASES (test track, 「Test card, always approves」): annualsubscription_christmas_2611 at 15:13:45 via Mine pill 「Try Pro 7 days for free」 → IAP → Continue (interstitial already used today); Credit Auto Pass pdrm_2000_credit_paiduser_yr_autopass at 15:25:47 (+2000). Account now Pro + Auto Pass, credits 5510 (logcat 15:25:55). Stage (yellow bar). Play Billing Lab country RESTORED to Taiwan at 15:25 (active until 17:25, Introductory offer Yes); app locale back to en-US (launch). Image to Video Kling 4.0 task from TC-140 (−70) left processing. Logs pulled 15:26 (logs/R1r-c-20261123-152640). Findings: Pro Mine VIP card has no Christmas decoration / JP banner, no VIP Benefits page; credit page has no Christmas banner and no Christmas 2000 pack (paid SKU fetched, never shown) with or without Auto Pass; Auto Pass card wording differs. Script notes: lbl Subscribe on the Play sheet hits the Google Pay ToS link (tap the button by position, y≈2165); lbl Generate hits 「Generate Sound by AI」 (tap 540,2143); lbl Pro opens New Project (id tv_premium). Next: phase wrap-up (orchestrator).

### 2026-11-23T08:02:14.553Z · all recorded
{"Fail":14,"Pass":10,"Blocked":11}

Phase R1r wrap-up done (phase closed). Tally 10 Pass, 14 Fail (defect), 11 Blocked (8 test-data: low-balance account 6, RD date 2; 3 defect: TC-117 no VIP Benefits page, TC-148/149 Christmas packs not offered). blocked-reasons.json written. Coverage page rebuilt with runs r1-christmas + r1r-recheck. eBug batch ebugs/2026-11-23-r1r/ (11 drafts ISS-XMA-13…23, format check 0 errors, review page built; additions to R1 ISS-XMA-06 and ISS-XMA-12; R1 held TC-124 now ISS-XMA-16); nothing filed. Account acda.test9 left Pro (Christmas annual, test track) + Credit Auto Pass, 5510 credits; Play Billing Lab country Taiwan; app en-US; Play test build installed. Next: reviewer decisions on the R1 + R1r batches; Blocked rows need a low-balance account and the RD New Year date.
