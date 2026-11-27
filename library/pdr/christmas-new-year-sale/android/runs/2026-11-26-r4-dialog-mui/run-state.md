# Run state — R4 Round 4: Not Enough Credit dialog in 26 languages (draft 20261126-154459) on 16.9.0 (2611251), Samsung SM-A516B

Table: library/pdr/christmas-new-year-sale/android/drafts/20261126-154459/draft.csv
Started: 2026-11-26T07:47:11.190Z

## Environment
(build, server, device, tier, credit balance, Pink toggles, Log stage timings, Write Log)

## Checkpoints

### 2026-11-26T07:56:33.759Z · next TC-166 (R4-a)
{"Pass":12,"Fail":1,"Not run":39}

R4-a first half done (15:48–15:56 host). TC-153 – TC-165: 12 Pass, 1 Fail defect (TC-159 ITA body 「Passa Pro+」). acda.test9 Free, balance 7, I2V Custom Kling 4.0 = 70. One I2V load on the real date, then phone 12/24 and per-app locale switched in place per language (O-1). Nothing generated, nothing bought, no Play sheet, nothing filed. Phone 2026-12-24 15:55 (automatic off), app locale reset (English US, app-locales []), relaunched on the Launcher Home. Logs logs/R4-a-20261126-155541. Next: TC-166 (Thai), same O-1 route: real date → I2V load → 12/24 → locale per row.

### 2026-11-26T08:03:51.365Z · next TC-179 (R4-b)
{"Pass":24,"Fail":2,"Not run":26}

R4-a second half done (15:57–16:03 host). TC-166 – TC-178: 12 Pass, 1 Fail defect (TC-168 VIE body mostly English, 「Pro+」). R4-a total 24 Pass, 2 Fail defect (TC-159, TC-168). acda.test9 Free, balance 7. Nothing generated, bought or filed. Phone 2026-12-24 16:03 (automatic off), app locale reset (app-locales []), Launcher Home. Logs logs/R4-a2-20261126-160306. Next: R4-b TC-179 (Pro purchase on the Play test sheet first).

### 2026-11-26T08:09:25.126Z · all recorded
{"Pass":24,"Fail":2,"Blocked":26}

R4-b (16:04–16:09 host): acda.test9 bought Pro (annualsubscription_christmas_2611, Play test sheet 「Test card, always approves」); balance 7 → 107 (100 monthly Pro grant) ≥ 70, so TC-179 – TC-204 all Blocked test-data (O-6). Nothing generated, nothing else bought, nothing filed. Phone 2026-12-24 (automatic off), app locale en-US (system), Launcher Home. Logs logs/R4-b-20261126-160831. R4 done: 24 Pass, 2 Fail defect, 26 Blocked.

### 2026-11-26T08:29:23.479Z · all recorded
{"Pass":49,"Fail":3}

R4-b re-run (16:18–16:30 host): acda.test9 Pro, balance 22 (lowered by the user). TC-179 – TC-204: 25 Pass, 1 Fail defect (TC-194 VIE body left in English), Blocked results replaced, blocked-reasons.json emptied. Nothing generated, bought or filed. Phone 2026-12-24 (automatic off), app locale [] (system en-US), Launcher Home. Logs logs/R4-b2-20261126-162818. R4 done: 49 Pass, 3 Fail defect.
