# Run state — R5 Round 5: light-mode rechecks (TC-102 NY IAP annual card, TC-146 landscape IAP) and the Mine Credits bar measurement, 16.9.0 (2611251)

Table: library/pdr/christmas-new-year-sale/android/drafts/20261126-154459/draft.csv
Started: 2026-11-26T09:19:50.723Z

## Environment
(build, server, device, tier, credit balance, Pink toggles, Log stage timings, Write Log)

## Checkpoints

### 2026-11-26T09:36:51.778Z · all recorded
{"Fail":2}

R5-a done: TC-102 Fail defect (NY annual card navy in light = dark art; Christmas follows), TC-146 Fail defect (landscape: NY annual card, white link separators invisible in light, monthly border fixed grey). C measured: mine-credit-bar.json. Account acda.test9 Free, 22 credits. App Appearance restored to Light Mode (was set to Device Settings for the run). Phone 2026-12-24 ~17:36 automatic off, system light, portrait (user_rotation 0, auto-rotate on as before), app English (system locale, no per-app locale), PowerDirector on the Launcher Home. Logs logs/R5-a-20261126-173555. Nothing bought, generated or filed.

### 2026-11-26T09:45:30.000Z · R5-c done

R5-c (request C, Pro card): acda.test9 bought the Pro test subscription (annualsubscription_christmas_2611, Google Play 「Test card, always approves」), now Pro with 122 credits. Mine Pro captured light (app Appearance Light Mode) and dark (Dark Mode) with page source: card 996×529, bar 996×207, ratios 0.391 / 0.208 vs Figma 0.311 / 0.163; bar content centred, extra padding (mine-credit-bar.json bar_content). App Appearance restored to Light Mode; phone 2026-12-24 17:45 automatic off, system light, portrait, en-US, PowerDirector on the Launcher Home. Logs logs/R5-c-20261126-174503. Nothing generated or filed; nothing bought beyond the one test subscription.
