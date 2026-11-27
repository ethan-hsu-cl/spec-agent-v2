# Christmas & New Year Sales Android — R1 (table v2, Christmas rows) eBugs filed 2026-11-23

Creator ANGOL_HUANG (read back on every bug) · method API (create + attachment upload) · source tag [AIAgent] · TR [TR261123-0015](https://ecl.cyberlink.com/IF3/tr/BPM/FormView/TR261123-0015) · 16.9.0 build 2611201 (TR header: 「16.9.0.2611201 (Deluxe)」) · Stage server · template Generic v16.9 (23176), PowerDirector Mobile for Android · due 2026-12-02 (the TR's) · decisions: `decisions.md`

**Read back:** every bug's Creator, severity, belong, TR, version, build and Short Description match what was sent, every attachment is on its page (`DataJSON.UploadFiles`) and every inline {filename} in its description resolves to one of them. Status on read-back is 「BugNeedReview」. Attachments: red 5px boxes drawn by `make_filing_sheets.py --no-sheet` on unboxed run frames (`upload/boxes.json`) → `upload_filing/`. No existing ticket was commented on.

**F-9 (ISS-XMA-09):** `[AIAgent][UX]` with BugBelong PM, allowed by the 2026-11-11 rule (PM decisions on user experience).

**To do by hand:** OS Language is a required template field the API cannot set — fill it on each ticket's web edit form.

| F | BugCode | ISS | Sev | Belong | Type | Attachments | Short Description |
|---|---|---|---|---|---|---|---|
| F-1 | [DRA262611P0264](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0264) | ISS-XMA-01 | 2 | RD | UI | 3 | PDR-A 16.9.0 - [AIAgent][UI][MUI] Christmas Sale (Interstitial): 「SAVE」 and 「vs. paying …/mo × 12」 are not localized |
| F-2 | [DRA262611P0265](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0265) | ISS-XMA-02 | 2 | PM | UI | 2 | PDR-A 16.9.0 - [AIAgent][UI][MUI] Christmas Sale (Interstitial): 「/year」 and 「More subscription plan」 are not localized |
| F-3 | [DRA262611P0266](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0266) | ISS-XMA-03 | 3 | RD | UI | 4 | PDR-A 16.9.0 - [AIAgent][UI][MUI] Christmas Sale (Interstitial): CTA text differs from the 多國文案 sheet in 12 languages |
| F-4 | [DRA262611P0267](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0267) | ISS-XMA-04 | 3 | RD | UI | 4 | PDR-A 16.9.0 - [AIAgent][UI][RUS/FRA/UKR/POL] Christmas Sale (Interstitial): Bottom links overlap each other or separators |
| F-5 | [DRA262611P0268](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0268) | ISS-XMA-05 | 3 | RD | UI | 1 | PDR-A 16.9.0 - [AIAgent][UI][POL] Christmas Sale (Interstitial): CTA wraps to two lines with no side padding in the button |
| F-6 | [DRA262611P0269](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0269) | ISS-XMA-06 | 3 | RD | Functional | 2 | PDR-A 16.9.0 - [AIAgent] Christmas Sale (IAP): Discount shows 57% though NT$1,210 vs NT$240 × 12 gives 57.99% |
| F-7 | [DRA262611P0270](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0270) | ISS-XMA-07 | 2 | RD | UI | 2 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Launcher): Top banner title is not 「Make Christmas magic with AI」 |
| F-8 | [DRA262611P0271](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0271) | ISS-XMA-08 | 2 | RD | UI | 2 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Launcher): Top pill reads 「Pro」, not 「Try Pro 7 days for free」 |
| F-9 | [DRA262611P0272](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0272) | ISS-XMA-09 | 3 | PM | UX | 2 | PDR-A 16.9.0 - [AIAgent][UX] Christmas Sale (IAP): Back from IAP opened via 「More subscription plan」 skips the interstitial |
| F-10 | [DRA262611P0273](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0273) | ISS-XMA-10 | 3 | RD | UI | 2 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (IAP): [Short screen] Banner title 「Christmas Special」 is clipped at the bottom |
| F-11 | [DRA262611P0274](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0274) | ISS-XMA-11 | 3 | RD | Functional | 1 | PDR-A 16.9.0 - [AIAgent] Christmas Sale (Launcher): [Landscape] Launcher shows no Christmas top banner |
| F-12 | [DRA262611P0275](https://ecl.cyberlink.com/IF3/ebug/BPM/FormView/DRA262611P0275) | ISS-XMA-12 | 2 | RD | UI | 2 | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (IAP): Tag 「Special Offer」 and 「57% OFF」 instead of 「Christmas Treat」, 「Save xx%」 |

| Feature | Platform | AI Found # | Created # | Known # |
|---|---|---|---|---|
| Christmas & New Year Sales | Android | 12 | 12 | 0 |

OS Language set to 24 Languages on the web edit form, 2026-11-23 (user's choice). Not on DRA262611P0274: cancelled by ANGOL_HUANG at 16:48 before the pass, so it has no Edit form.

Short Description of P0264–P0268 edited on the web form, 2026-11-25 (user): [MUI] / language tags moved before the feature name; read back.
