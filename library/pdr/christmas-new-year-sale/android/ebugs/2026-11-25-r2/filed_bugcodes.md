# Christmas & New Year Sales Android — R2 New Year eBugs filed 2026-11-25

Creator ANGOL_HUANG (read back) · method API (create + attachment upload) · source tag [AIAgent] · TR [TR261123-0070](https://ecl.cyberlink.com/IF3/tr/BPM/FormView/TR261123-0070) · 16.9.0 build 2611231 (TR header 「16.9.0.2611231 (Deluxe)」) · Stage server · template Generic v16.9 (23176) · due 2026-12-02 · decisions: `decisions.md`

Verified in R2 (`runs/2026-11-25-r2-newyear`, build 2611231 installed with adb; phone date in the New Year window). All 17 filed; none held.

**Read back:** Product, Creator, Severity, BugBelong, TR, Version 16.9.0, Build 2611231 and Short Description match what was sent; every attachment is on its page (`DataJSON.UploadFiles`) and every inline `{filename}` matches one. Status 「BugNeedReview」. Frames red-boxed 5px by `make_filing_sheets.py --no-sheet` (`upload/boxes.json`). No existing ticket was commented on.

**F-8 (DRA262611P0304):** the Note carries the reviewer-requested 「Comparison:」 block, sheet CTA vs app for the 12 languages.

**OS Language:** 24 Languages, set on the web edit form (same choice as TR261123-0015).

| # | BugCode | ISS | Sev | Belong | Files | Short Description |
|---|---|---|---|---|---|---|
| F-1 | [DRA262611P0297](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0297) | ISS-XMA-24 | 2 | RD | 2 | PDR-A 16.9.0 - [AIAgent] New Year Sale (Interstitial): US store: SAVE 52% from the regular $7.99 monthly, not $6.99 (45%) |
| F-2 | [DRA262611P0298](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0298) | ISS-XMA-25 | 4 | RD | 1 | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Interstitial): Trial terms read 「until cancelled」, not 「until canceled」 |
| F-3 | [DRA262611P0299](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0299) | ISS-XMA-26 | 3 | RD | 2 | PDR-A 16.9.0 - [AIAgent] New Year Sale (Interstitial): First system Back is ignored; a second Back closes it |
| F-4 | [DRA262611P0300](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0300) | ISS-XMA-27 | 2 | RD | 2 | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Launcher): Top banner title is not 「Bring New Year moments to life」 |
| F-5 | [DRA262611P0301](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0301) | ISS-XMA-28 | 2 | RD | 3 | PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): 「SAVE」 and 「vs. paying …/mo × 12」 are not localized |
| F-6 | [DRA262611P0302](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0302) | ISS-XMA-29 | 2 | PM | 2 | PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): 「/year」 and 「More subscription plan」 are not localized |
| F-7 | [DRA262611P0303](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0303) | ISS-XMA-30 | 2 | RD | 4 | PDR-A 16.9.0 - [AIAgent][UI][FRA/ITA/UKR/ESP] New Year Sale (Interstitial): Title art not in the app language |
| F-8 | [DRA262611P0304](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0304) | ISS-XMA-31 | 3 | RD | 3 | PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): CTA text differs from the 多國文案 sheet in 12 languages |
| F-9 | [DRA262611P0305](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0305) | ISS-XMA-32 | 3 | RD | 4 | PDR-A 16.9.0 - [AIAgent][UI][RUS/FRA/UKR/POL] New Year Sale (Interstitial): Bottom links overlap each other or separators |
| F-10 | [DRA262611P0306](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0306) | ISS-XMA-33 | 3 | RD | 1 | PDR-A 16.9.0 - [AIAgent][UI][POL] New Year Sale (Interstitial): CTA wraps to two lines with no side padding in the button |
| F-11 | [DRA262611P0307](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0307) | ISS-XMA-34 | 3 | RD | 3 | PDR-A 16.9.0 - [AIAgent] New Year Sale (IAP): Discount shows 57% though NT$1,210 vs NT$240 × 12 gives 57.99% |
| F-12 | [DRA262611P0308](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0308) | ISS-XMA-35 | 3 | RD | 2 | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Mine): Mine top pill has no clock or countdown |
| F-13 | [DRA262611P0309](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0309) | ISS-XMA-36 | 2 | RD | 1 | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (IAP): Tag 「Special Offer」 and 「57% OFF」 instead of 「New Year Treat」, 「Save xx%」 |
| F-14 | [DRA262611P0310](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0310) | ISS-XMA-37 | 2 | RD | 1 | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Mine): Pro VIP card lacks New Year decoration |
| F-15 | [DRA262611P0311](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0311) | ISS-XMA-38 | 2 | RD | 4 | PDR-A 16.9.0 - [AIAgent] New Year Sale (Credit): Pro: New Year 2000-credit pack never offered; no 「Get 2000 credits for …」 |
| F-16 | [DRA262611P0312](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0312) | ISS-XMA-39 | 3 | RD | 1 | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Credit): No Auto Pass: CTA not 「Subscribe for 3000 free credits!」 |
| F-17 | [DRA262611P0313](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0313) | ISS-XMA-40 | 3 | RD | 1 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Credit): Countdown 「2D 23:56:30」 shows above the CTAs on 12/25 |
