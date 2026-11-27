# Run state — R3 Round 3: low-balance Not Enough Credit rows on 16.9.0 (2611251), Samsung SM-A516B

Table: library/pdr/christmas-new-year-sale/android/cases.csv
Started: 2026-11-26T06:26:25.806Z

## Environment
(build, server, device, tier, credit balance, Pink toggles, Log stage timings, Write Log)

## Checkpoints

### 2026-11-26T06:30:48.436Z · next TC-132 (R3-b)
{"Blocked":5,"Not run":5}

R3-a done (14:27–14:31 host time; 5 Blocked test-data, nothing else run). Start read after a relaunch: build 16.9.0 (2611251), Stage (yellow bar), acda.test9 signed in, tier PRO (Mine 「Pro」 「You're on the highest plan…」, pill 「Credit Special Offer」, logcat updateSubscribingStatus: true), credits 4 (Mine, I2V pill, totalRemain=4 at 14:29 phone). I2V Custom price NOT readable: Model row empty, Generate disabled without a price, because a server certificate expired 2026-12-04 and the phone date is 12/24 (O-1: CertificateExpiredException in logcat GW). No Generate tapped, no dialog, nothing bought, no Play sheet. Phone date unchanged 2026-12-24 (time of day = host time, automatic off). App en-US on the Launcher Home. Logs logs/R3-a-20261126-143027. R3-b (Pro) can run on the tier but is likely blocked the same way by O-1 on 12/24 and 12/30.

### 2026-11-26T06:39:22.973Z · all recorded
{"Blocked":5,"Pass":5}

R3-b done (14:31–14:39 host). 5 Pass (TC-132, 133, 141, 136, 137); run 5 Pass / 5 Blocked (R3-a Free rows). Real date 11/26: Stage runs Black Friday (O-3), no cert error, I2V Custom Kling 4.0 = 70. Pro rows reached via O-4 workaround (load I2V on the real date, shift phone date, activate, Generate). acda.test9 Pro, balance 7 (4 + 3 daily free credits on the credit page, O-5). Nothing generated, nothing bought, no Play sheet. Phone left 2026-12-24 (current time of day, automatic off), app relaunched in en-US on the Launcher Home (Christmas theme). Samsung Software update activity still in the background stack (not installed). Logs logs/R3-b-20261126-143851. Run complete: 0 Not run.

### 2026-11-26T07:32:16.126Z · all recorded
{"Pass":9,"Fail":1}

R3-a re-run done (15:19–15:31 host). acda.test9 Free, balance 7, I2V Custom Kling 4.0 = 70. TC-134, 135, 138, 139 Pass; TC-142 Fail defect (system Back on the Free dialog leaves Image to Video for the Launcher, O-7). Reached via the O-4 workaround (three setups). Nothing generated, nothing bought, no Play sheet. Phone 2026-12-24 15:31 (automatic off), app relaunched en-US on the Launcher Home. Logs logs/R3-a2-20261126-153110. Run: 9 Pass, 1 Fail.
