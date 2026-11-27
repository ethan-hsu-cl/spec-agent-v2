# Decisions — Christmas & New Year Sales Android, R2 New Year, 16.9.0 build 2611231

The reviewer's decisions (2026-11-25), as signed off in chat.

Account: ANGOL_HUANG
Method: API
Source tag: [AIAgent]
TRCode: TR261123-0070

| # | ISS | Sev | Belong | Type | Action | Short Description | Note |
|---|---|---|---|---|---|---|---|
| F-1 | ISS-XMA-24 | 2 | RD | Functional | file | PDR-A 16.9.0 - [AIAgent] New Year Sale (Interstitial): US store: SAVE 52% from the regular $7.99 monthly, not $6.99 (45%) |  |
| F-2 | ISS-XMA-25 | 4 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Interstitial): Trial terms read 「until cancelled」, not 「until canceled」 |  |
| F-3 | ISS-XMA-26 | 3 | RD | Functional | file | PDR-A 16.9.0 - [AIAgent] New Year Sale (Interstitial): First system Back is ignored; a second Back closes it |  |
| F-4 | ISS-XMA-27 | 2 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Launcher): Top banner title is not 「Bring New Year moments to life」 |  |
| F-5 | ISS-XMA-28 | 2 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): 「SAVE」 and 「vs. paying …/mo × 12」 are not localized |  |
| F-6 | ISS-XMA-29 | 2 | PM | UI | file | PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): 「/year」 and 「More subscription plan」 are not localized |  |
| F-7 | ISS-XMA-30 | 2 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI][FRA/ITA/UKR/ESP] New Year Sale (Interstitial): Title art not in the app language |  |
| F-8 | ISS-XMA-31 | 3 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI][MUI] New Year Sale (Interstitial): CTA text differs from the 多國文案 sheet in 12 languages | 在Note也附上Sheet CTA vs app的比對表 |
| F-9 | ISS-XMA-32 | 3 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI][RUS/FRA/UKR/POL] New Year Sale (Interstitial): Bottom links overlap each other or separators |  |
| F-10 | ISS-XMA-33 | 3 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI][POL] New Year Sale (Interstitial): CTA wraps to two lines with no side padding in the button |  |
| F-11 | ISS-XMA-34 | 3 | RD | Functional | file | PDR-A 16.9.0 - [AIAgent] New Year Sale (IAP): Discount shows 57% though NT$1,210 vs NT$240 × 12 gives 57.99% |  |
| F-12 | ISS-XMA-35 | 3 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Mine): Mine top pill has no clock or countdown |  |
| F-13 | ISS-XMA-36 | 2 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (IAP): Tag 「Special Offer」 and 「57% OFF」 instead of 「New Year Treat」, 「Save xx%」 |  |
| F-14 | ISS-XMA-37 | 2 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Mine): Pro VIP card lacks New Year decoration |  |
| F-15 | ISS-XMA-38 | 2 | RD | Functional | file | PDR-A 16.9.0 - [AIAgent] New Year Sale (Credit): Pro: New Year 2000-credit pack never offered; no 「Get 2000 credits for …」 |  |
| F-16 | ISS-XMA-39 | 3 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI] New Year Sale (Credit): No Auto Pass: CTA not 「Subscribe for 3000 free credits!」 |  |
| F-17 | ISS-XMA-40 | 3 | RD | UI | file | PDR-A 16.9.0 - [AIAgent][UI] Christmas Sale (Credit): Countdown 「2D 23:56:30」 shows above the CTAs on 12/25 |  |

F-8 note applied: the Note carries a 「Comparison:」 block, sheet CTA vs app for the 12 languages (from the R2 run results).
