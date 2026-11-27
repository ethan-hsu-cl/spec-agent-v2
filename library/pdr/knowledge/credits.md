# Credits

## KP-007 A failed generation refunds its credits
- kind: rule · platform: both · use: analysis, run, ebug · tags: credits, refund · authority: team
- source: run.md step 8 (user, 2026-10-19); AIGC Watermark Android run 2026-11-17-r1-full O-7; AIGC Watermark Android run 2026-11-23-r2-changed O-7 · verified: 16.9.0 build 2611193 (2026-11-23)

A failed item costs nothing net; a partial failure costs only the items that succeeded. A missing or wrong refund is
a defect with its own eBug, even when the failure itself is already filed.

## KP-008 Reading the credits ledger
- kind: howto · platform: both · use: run · tags: credits, refund, ledger
- source: run.md step 8 (user, 2026-10-19); Video Enhance Android run 2026-11-10-r1-full O-16, O-17, O-25 · verified: 16.9.0 build 2611231 (2026-11-24)

Mine › Credits › Details lists charge rows by tool (Text to Image / Text to Speech / AI Video Generator / Video
Enhancer) with the platform (「PowerDirector (Android)」) and a refund row 「Generation failed, credits returned +N」.
The account is shared: rows nobody in the run made appear (a 「Credit Pack (2000 credits) +2000」 on 2026-11-10), so
match rows by time and amount, never by balance difference alone. Balances lag: the credit pill is stale until its
screen is reopened, and the Pro tab can trail one charge behind the ledger (Android); quote the next fresh pill.

## KP-041 Daily free credits
- kind: fact · platform: both · use: analysis, run · tags: credits, claim
- source: exploration KB mine-page.md (2026-09-07 PDRM TestFlight, and 2026-09-29, 16.9.0 build 189315, Free); Android: Video Enhance run 2026-11-10-r1-full O-27 (offer seen, not claimed); Christmas & New Year Sales Android run 2026-11-26-r3-lowbalance O-5 (inbox I-031) · verified: android 16.9.0 build 2611251 (2026-11-26)

My Credits carries 「Complimentary daily credits / Claim once every 24 hours / Claim」; a claim gives 5 credits
(toast 「5 Credits Received · valid for 7 days」). Yet 「Expiring within 7 days」 stays 「0 credit」 after it
(ISS-MP-27, DRI261893-0042). Android's Mine › Credit page shows the same 「Complimentary daily credits ‹Claim›」
offer (16.9.0 build 2611091). On Android (Pro, Stage, Christmas credit page, 16.9.0 build 2611251) merely opening the
credit page granted 3 credits with no tap: toast 「3 Credits Received」 「Daily free credits are valid for 7 days. Check
back again tomorrow for more!」, 「Expiring within 7 days: 3 credits」. Each new phone day may add 3 more, so re-read the
balance before a low-balance row.

## KP-067 Credits can read 「--」 or 0 right after a launch
- kind: quirk · platform: android · use: run · tags: credits, billing, logs, launch
- source: Video Enhance Android run 2026-11-10-r1-full O-1; AIGC Watermark Android run 2026-11-17-r1-full O-1, O-20 (seen without a purchase: corrected); AIGC Watermark Android run 2026-11-26-e1-entries O-4 (inbox I-012) · verified: 16.9.0 build 2611251 (2026-11-26)

At some launches (right after a Google Play purchase, but also after a plain relaunch or a `locale reset`),
CreditSystemManager logs `getCreditRemain error, creditSystemUUID is null`, `refreshMemberToken error` and
`checkFeatureCredit … JsonSyntaxException` right after the Play Integrity (StandardIntegrity) call: the pill shows
「--」, AI Magic may say 「No Internet Connection」 and tool pages 0 credits while online, or a wrong price (2611251: Text to
Video Kling 4.0 「Generate ◆ 25」 instead of ◆70 once). A plain relaunch fixes it;
relaunch before reading prices or the pill.

## KP-070 Credit Details drops the current month after local midnight
- kind: quirk · platform: android · use: run, ebug · tags: credits, ledger, date
- source: Video Enhance Android run 2026-11-18-r2-full O-25, O-31; Video Enhance Android run 2026-11-24-r3-full O-17; Video Enhance Android run 2026-11-26-r4-full O-25 · verified: 16.9.0 build 2611251 (2026-11-27)

Between local midnight (UTC+8) and the server's UTC date change, Mine › Credits › Details opened on the previous
month's group with no current-month group, also after a relaunch, while logcat `getCreditHistory` listed the new
charges; before midnight they showed. Read ledger rows in daytime or from logcat; recheck across a month boundary
before filing.

## KP-071 Buying credits is followed by an offer and a backup dialog
- kind: fact · platform: android · use: analysis, run · tags: credits, buy-more, dialog
- source: Video Enhance Android run 2026-11-18-r2-full O-12; Video Enhance Android run 2026-11-24-r3-full O-5; Video Enhance Android run 2026-11-26-r4-full O-12 · verified: 16.9.0 build 2611251 (2026-11-26)

After a 500-credit test purchase the app offers another pack, which varies between purchases (「Want to get 50
Credits, too?」 「NT$170.00」 on 2611091 and 2611251, 「Want to get 1000 Credits, too?」 「NT$2,010.00」 on 2611231), with
「Not now」;
「Not now」 then opens 「Check Backup Protection」 over My Credits (「Back up now」, 「Later」, 「Don't show again」
unticked). The pack page opens on a pre-selected server-set promotion: 「Annual Auto Pass Discount」 1000 +1000 NT$2490
(「Continue with the best deal」) on 2611231, a 「BLACK FRIDAY SALE」 header with a countdown and 「Special Offer」 1000 +1000
NT$2740 (「Get 2000 Credits for NT$2740」) on 2611251: tap the wanted pack tile first. None of this is in a feature spec; close both dialogs before the next step.

## KP-091 Credit prices seen on Android (Free, Stage)
- kind: fact · platform: android · use: analysis, run · tags: credits, price
- source: AIGC Watermark Android run 2026-11-17-r1-full O-2..O-25 (charges matched pill and log); AIGC Watermark Android run 2026-11-23-r2-changed O-9, O-14 · verified: 16.9.0 build 2611193 (2026-11-23)

Text to Image 3, AI Art 6, Text to Speech 2, Talking Avatar 10, AI Music Generator 5 a song; Image to Video Veo 3.1
4 s 32, Vidu Q2 15, Kling O3 25, Pixverse V6 20, Wan 2.7 40; Text to Video Kling O3 30, Veo 3.1 4 s Fast 28, Wan 2.7
720p 25; AI Anime Video Vivid 10 s 40; Video Edit by Chat Gemini Omni Flash 1.1 72, Kling O3 45; Character Motion Swap
Wan 2.2 Animate 39, Kling Motion Control 60; Cinematic Reel 70. AI Cartoon and AI Sketch charged nothing although the
feature list prices them at 1. On 2611193: Text to Video Veo 3.1 4 s Fast 28, Kling O3 5 s 1080p 30, Wan 2.7 5 s 1080p 40;
Video Edit by Chat Gemini Omni Flash 1.1 8 a second (40 for 5 s), Kling O3 5 a second (25); Motion Swap Wan 2.2
Animate 3 a second (39), Kling Motion Control 6 a second (60); Cinematic Reel Horror Movie 70, Micro Cinema / Handheld
Camera / One-Take Shot / Time Lapse 48, Fast Cut 72; Pro Seedance 2.0 5 s 40 (I2V Standard, T2V Fast 720p); I2V Gemini
Omni Flash 1.1 5 s 25. Prices are server-set: recheck on each build (Image / Text to Video on 2611251: KP-135).

## KP-092 Reading the balance from the Android log
- kind: howto · platform: android · use: run · tags: credits, logs
- source: AIGC Watermark Android run 2026-11-17-r1-full O-1, O-7, O-18, O-25; AIGC Watermark Android run 2026-11-23-r2-changed · verified: 16.9.0 build 2611231 (2026-11-25)

CreditSystemManager logs `totalRemain=<n>` after each launch and each charge; it matched the credit pill every time,
so a charge can be checked by clock time in logcat without opening Mine › Credits.

## KP-095 The credit-history log line names each charge's model
- kind: howto · platform: android · use: run, ebug · tags: credits, logs, models, cinematic-reel
- source: AIGC Watermark Android run 2026-11-23-r2-changed O-7, O-9, O-14 · verified: 16.9.0 build 2611193 (2026-11-23)

The ledger's log line (`getCreditHistory … actionId=…`) names each charge's provider and model (e.g.
AICinematicShorts genvideo_1_sec_kling_o3pro_enable_1080p, bytedance seedance2.0fast). It is the only place Cinematic
Reel's model shows.

## KP-135 Video generation prices on 2611251
- kind: fact · platform: android · use: analysis, run · tags: credits, price, image-to-video, text-to-video, video-edit-by-chat
- source: Recent Task Model Info Android run 2026-11-26-r1-full (inbox I-024, I-027); AIGC Watermark Android run 2026-11-26-e1-entries O-3 (inbox I-009) · verified: 16.9.0 build 2611251 (2026-11-26)

Image to Video 5 s: Kling 4.0 70, Kling O3 25, Pixverse V6 20, Wan 3.0 50, Gemini Omni Flash 1.1 25, Happy Horse 1.1
40, Seedance 2.5 150, Seedance 2.0 40, Veo 3.1 32, Vidu Q2 15, Wan 2.7 40; templates 15 or 25. Text to Video 9:16 5 s
1080p: Kling 4.0 70, Wan 3.0 50, Seedance 2.5 150, Seedance 2.0 40, Gemini Omni Flash 25, Happy Horse 1.1 40, Wan 2.7
40, Veo 3.1 28, Kling O3 30. Video Edit by Chat Seedance 2.5 14 a second, Kling O3 5. Others as KP-091.

## KP-145 Stage ran a Black Friday Not Enough Credit dialog on 2026-11-26
- kind: fact · platform: android · use: run, analysis · tags: credits, campaign, server, date · authority: observed
- source: Christmas & New Year Sales Android run 2026-11-26-r3-lowbalance O-3 (inbox I-031; scope: seen from Image to Video, the dialog is the app's credit gate) · verified: 16.9.0 build 2611251 (2026-11-26)

On the real date 2026-11-26 Stage showed no Christmas or New Year theme, and Generate with too few credits opened a
Black Friday dialog (purple card, 「Black Friday」 「SALE」, 「More Credits Needed!」, 「Grab Discount Now!」, ⓧ closes it
with no charge). So a real-date run on Stage is not a "regular" baseline while another campaign is live. The dialog is
not in the accessibility tree: read its texts from the screenshot. Version-bound; check the date's campaign first.
