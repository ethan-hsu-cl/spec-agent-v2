# Christmas & New Year Sales Android — R1r eBugs filed 2026-11-23

Creator ANGOL_HUANG (read back) · method API (create + attachment upload) · source tag [AIAgent] · TR [TR261123-0015](https://ecl.cyberlink.com/IF3/tr/BPM/FormView/TR261123-0015) · 16.9.0 build 2611201 (TR header 「16.9.0.2611201 (Deluxe)」) · Stage server · template Generic v16.9 (23176) · due 2026-12-02 · decisions: `decisions.md`

Verified in R1r (`runs/2026-11-23-r1r-recheck`, Play test build 2611201). ISS-XMA-20 (F-8) held by the reviewer, not filed. The R1 batch (`ebugs/2026-11-23-r1/`) is not part of this filing.

**Read back:** Product, Creator, Severity, BugBelong, TR, Version 16.9.0, Build 2611201 and Short Description match what was sent; every attachment is on its page (`DataJSON.UploadFiles`) and every inline `{filename}` matches one. Status 「BugNeedReview」. Frames red-boxed 5px by `make_filing_sheets.py --no-sheet` (`upload/boxes.json`). No existing ticket was commented on.

**Still to do on the web form:** OS Language (the API cannot set it).

| # | BugCode | ISS | Sev | Belong | Files | Short Description |
|---|---|---|---|---|---|---|
| F-1 | [DRA262611P0254](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0254) | ISS-XMA-13 | 2 | RD | 3 | PDR-A 16.9.0 - [AIAgent] Christmas Sale (Interstitial): US store: SAVE 52% from the regular $7.99 monthly, not $6.99 (45%) |
| F-2 | [DRA262611P0255](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0255) | ISS-XMA-14 | 4 | RD | 1 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Interstitial): Trial terms read 「until cancelled」, not 「until canceled」 |
| F-3 | [DRA262611P0256](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0256) | ISS-XMA-15 | 2 | RD | 3 | PDR-A 16.9.0 - [AIAgent] Christmas Sale (IAP): India, Indonesia, Philippines: IAP opens on the annual plan, not monthly |
| F-4 | [DRA262611P0257](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0257) | ISS-XMA-16 | 2 | RD | 2 | PDR-A 16.9.0 - [AIAgent] Christmas Sale (Credit): Free user: no Christmas 500-credit offer; First Purchase pack instead |
| F-5 | [DRA262611P0258](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0258) | ISS-XMA-17 | 2 | RD | 2 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Mine): Pro VIP card lacks Christmas decoration and JP 「Merry Christmas!」 banner |
| F-6 | [DRA262611P0259](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0259) | ISS-XMA-18 | 2 | RD | 2 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Credit): Credit page banner is the regular collage, not 「Christmas Special」 |
| F-7 | [DRA262611P0260](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0260) | ISS-XMA-19 | 3 | RD | 1 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Credit): No Auto Pass: CTA not 「Subscribe for 3000 free credits!」 |
| F-9 | [DRA262611P0261](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0261) | ISS-XMA-21 | 2 | RD | 3 | PDR-A 16.9.0 - [AIAgent] Christmas Sale (Credit): Pro: Christmas 2000-credit pack never offered, with or without Auto Pass |
| F-10 | [DRA262611P0262](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0262) | ISS-XMA-22 | 3 | PM | 2 | PDR-A 16.9.0 - [AIAgent] Christmas Sale (IAP): Philippines: Christmas monthly ₱485 costs more than the regular ₱469 |
| F-11 | [DRA262611P0263](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0263) | ISS-XMA-23 | 3 | PM | 1 | PDR-A 16.9.0 - [AIAgent][UI][JPN] Christmas Sale (Mine): Pro top pill stays English 「Credit Special Offer」 |

Not filed: F-8 ISS-XMA-20 — 不開單（審核者裁示：hold）.

OS Language set to 24 Languages on the web edit form, 2026-11-23 (user's choice).

Short Description of P0263 edited on the web form, 2026-11-25 (user): [MUI] / language tags moved before the feature name; read back.
