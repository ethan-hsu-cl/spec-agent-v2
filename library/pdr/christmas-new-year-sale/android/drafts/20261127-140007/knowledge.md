# Domain knowledge for pdr/christmas-new-year-sale (android), for analysis

## rule

### KP-007 A failed generation refunds its credits (authority team)
A failed item costs nothing net; a partial failure costs only the items that succeeded. A missing or wrong refund is
a defect with its own eBug, even when the failure itself is already filed.

### KP-066 Android text is held to the Android equivalent of the iOS font (android, authority spec, unverified)
The Design Figma is drawn for iOS in SF Pro. On Android the standard is Roboto: SF Pro Regular 400 → Roboto Regular
400, Medium 500 → Roboto Medium 500, Semibold 600 → Roboto Medium 500 (the board labels it 「Semibold/500」). Figma's
variable SF Pro weights between these (Medium 510) count as the nearest named weight. The board gives no size mapping,
so a size in pt is the same number in sp. The design check (`scripts/design.ts`, `ANDROID_WEIGHT`) judges Android
weights this way.

## risk

### KP-077 AI Style Transfer turns portrait photos sideways (android)
AI Cartoon (Elf) and AI Sketch (Oil Painting) on an upright portrait photo (DSC_0047.JPG) return the image turned 90°
in the preview and the export; likely EXIF orientation. Use portrait photos with EXIF rotation when testing them.

## question

### KP-028 No Design for the notification centre
No Design sheet covers the notification centre. Open for PM/Design: what 「Try Now」 may open (external sites, a mark
or confirmation), per-entry unread state, multi-open accordions, refresh frequency and paging.

### KP-037 VIP or Pro+
The top tier is called 「VIP」 on the Mine card and in Design F13 but 「Pro+」 on the My Cloud storage badge, the
paywall and Design F14/F17 (which also draw the subscribed bottom tab as 「Pro+」; the build keeps 「Mine」). Whether
they are one tier is for PM (ISS-MP-25); don't file the mix as a defect meanwhile.

### KP-061 Completion and error states the specs leave open
CineStory F17 says inform users 「when the task is done」 without saying server-done or downloaded. The banner button
is 「View」 in CineStory F02 and 「View Result」 in Video Object Removal F116 (the build says View). The F15 error
states 「Retry」 and 「View Details」 were never reached.

## howto

### KF-003 The phone's date drives the campaign window (android) (android)
On Stage the app picks the Christmas or New Year campaign from the phone's system date (local time): no RD test date
is needed. Set it in Settings › General management › Date and time with automatic date off (`adb shell am start -a
android.settings.DATE_SETTINGS`; `cmd alarm set-time` has no permission): 「Set date」 › the day's content-desc
(「Tuesday, December 29, 2026」, 「Next month」 / 「Previous month」) › Done; 「Set time」 › tap the hour field, `input
keyevent MOVE_END DEL DEL DEL`, `input text HH`, the same for minutes, Done. Seen: 12/27 23:59 Christmas → 12/28 00:00
New Year, 1/5 23:59 New Year → 1/6 regular. The once-a-day interstitial comes back by moving the date to another day
(12/29 ↔ 12/30) instead of `pm clear` (KF-001), which keeps the Stage sign-in (KP-093); moving the clock backwards can
also bring it back the same day. The Samsung 「Software update」 screen (com.wssyncmldm) comes up a few seconds after a
date change, also over the time picker or the app: wait ~3 s, close it with Back (never install), then launch. Logcat
lines carry the phone's shifted time, so `log-slice.ts` by-case windows (host time) come out empty: read
`logcat-live.txt` by phone time. Put the phone back to the run's base date after each row.

## quirk

### KP-069 The Sony XQ-BT52 cannot play 4K 60fps (android)
The Sony XQ-BT52 (Xperia 10 III, Snapdragon 690) hardware decoders stop at 3840×2160 30 fps (4096×2160 24, 1080p
120); a 4K 60 H.264 clip fails at decoder setup (`InsufficientResources`, 「Failed to initialize decoder」) in any
player, while 4K 30 plays. A 4K 60/120 result that will not play on it is a phone limit, not an app bug; check
4K 60 playback on the Samsung SM-A5360. Whether the app should offer 4K 60 on such phones is a PM question.
On 2611251 one Produce of two 4K clips (HEVC main + 4K overlay) failed once with 「…error while decoding the video」
(`OMX.qcom.video.decoder.avc ERROR(0x80001000)`) and worked twice after: use 1080p fixtures for export rows on the Sony.

## fact

### KF-004 New Year countdowns count to the end of 1/5 (android) (android, authority observed)
In the New Year window the Launcher pill, the IAP CTA and the credit page count to 2027-01-06 00:00:00 local (Q-18's
assumption). The Launcher pill reads 「On Sale!」 (gift icon) until fewer than 7 days remain; its countdown first shows
at a launch on 12/30 00:00 (「6D 23:59:30」), not while the app stays open over midnight. The IAP CTA counts from
12/28. Mine's pill never counts (ISS-XMA-35). The Christmas credit page also counts (to 12/28 00:00), against ruling
Q-11 (ISS-XMA-40).

### KP-003 Android debug controls (android)
Android has no Pink, no fault switches, no tier switch, no Write Log and no developer-server switch. Launcher ☰ ›
Menu ends with a QA block (download all contents, scoped-storage migration, 「QA: consume all non-consumables」, 「QA:
show all subscription plans」, 「QA: purchase SKU test」, region): never tap the consume or purchase rows. Fault
switches are planned for a later build (user, 2026-10-28): recheck on each new build.

### KP-006 Android tiers and chat limits (android)
Android sells Pro, not Pro+, through Google Play billing; the tier comes from the signed-in account. Daily chat limits
are server-configured: Free 10, Pro 100.

### KP-011 Design 8/E is the leading Launcher sheet (unverified)
Of the Launcher Design sheets, 「Template Page - Launcher supports banner (TBD) (8_E)」 matches the build (three content
rows, five bottom tabs, 「View more」). Older sheets drawing 「See All」, four tabs or two rows are superseded: never
file against them. The big-shortcut list follows 8/E F14 (…Video Enhance), not F04 (…Cinematic Reel Creator).

### KP-012 Shortcut tiles come from the CMS (unverified)
Which tools the Launcher's small shortcuts show (and in what order) is set on the CMS (Design: 「Shortcut on CMS」), up to
16 tiles over two pages. A tile list that differs from the Design is not a defect; reach a tool through AI Magic when
it is not on the first page.

### KP-041 Daily free credits
My Credits carries 「Complimentary daily credits / Claim once every 24 hours / Claim」; a claim gives 5 credits
(toast 「5 Credits Received · valid for 7 days」). Yet 「Expiring within 7 days」 stays 「0 credit」 after it
(ISS-MP-27, DRI261893-0042). Android's Mine › Credit page shows the same 「Complimentary daily credits ‹Claim›」
offer (16.9.0 build 2611091). On Android (Pro, Stage, Christmas credit page, 16.9.0 build 2611251) merely opening the
credit page granted 3 credits with no tap: toast 「3 Credits Received」 「Daily free credits are valid for 7 days. Check
back again tomorrow for more!」, 「Expiring within 7 days: 3 credits」. Each new phone day may add 3 more, so re-read the
balance before a low-balance row.

### KP-071 Buying credits is followed by an offer and a backup dialog (android)
After a 500-credit test purchase the app offers another pack, which varies between purchases (「Want to get 50
Credits, too?」 「NT$170.00」 on 2611091 and 2611251, 「Want to get 1000 Credits, too?」 「NT$2,010.00」 on 2611231), with
「Not now」;
「Not now」 then opens 「Check Backup Protection」 over My Credits (「Back up now」, 「Later」, 「Don't show again」
unticked). The pack page opens on a pre-selected server-set promotion: 「Annual Auto Pass Discount」 1000 +1000 NT$2490
(「Continue with the best deal」) on 2611231, a 「BLACK FRIDAY SALE」 header with a countdown and 「Special Offer」 1000 +1000
NT$2740 (「Get 2000 Credits for NT$2740」) on 2611251: tap the wanted pack tile first. None of this is in a feature spec; close both dialogs before the next step.

### KP-072 What a Pro purchase or sign-in changes on Android (android)
A Pro purchase adds 「Monthly Credit Bonus (for Pro Subscribers) +100」 (iOS: +50, KP-043), turns the Launcher's last
tab into 「Pro」 with a VIP icon instead of 「Mine」, and the next Launcher shows a 「Use credits to enjoy AI features /
Congrats! 100 monthly credits have been added with your Pro subscription」 dialog (system Back closes it). The tier
follows the Play account, so after `pm clear` the app reads Pro before sign-in. Google-button sign-in opens
「Welcome! Enter your email to get started」 with a marketing box ticked by default and adds 「Loyalty Credit Bonus
(for PowerDirector Subscribers) +30」. Logcat's `acknowledgePurchaseResponse 2 Server error` at purchase has no
visible effect.

### KP-076 AI Anime Video from the editor is slow and adds a clip (android)
AI Anime Video started from the editor (Vivid 10 s) took about 22 minutes (「17 minutes left…」); 「Add to Timeline」
puts the result after the source clip, not in its place. Start it early in a segment.

### KP-079 Some tools save their result to the gallery by themselves (android)
Video Edit by Chat, AI Anime Video and Talking Avatar write the result to the gallery when the task finishes, with no
「Save」 tap and before the result is opened (2611193; R2 read Talking Avatar as writing at first open, R3 O-4 saw it
write at finish with the result unopened; on 2611251 one AI Anime Video copy from a PIP clip was written
20 min late, when the app returned to the Launcher). Text to Image's 「Add to Timeline」 also writes a gallery copy, which a later
「Save」 reuses (KP-080). Character Motion Swap, Cinematic Reel Creator and Text to Video do not, nor does Image to
Video's 「Full Editor」 from a never-saved result. Whether this is
intended is not in any spec.

### KP-080 What a second Save does (android)
A Text to Image result saved once is never written again: a second 「Save」 says 「Saved to Gallery」 and leaves the
first file as it was. AI Art, Image to Video and Text to Video write a new file on every Save. In Image to Video file
names the number after the date counts saves, not tasks. On an Image to Video result every share target (YouTube,
TikTok, Instagram, Facebook, More) first writes a new file too; YouTube / Facebook then warn 「Before sharing to … music
copyright」 although no music was chosen.

### KP-085 AI Storytelling results live in its own history (android)
AI Storytelling results are not in My Artwork: they are under AI Storytelling › history 「Generated Story」 and are
exported, not saved. A Free account gets one free story; more need Pro.

### KP-086 AI Music Generator on Android (android)
Android has AIMusicGeneratorV2 (log: Google Lyria 3 Pro): Genre / Mood / Theme chips, song length and number of songs
(default 2, 「Generate for ◆ 10」, 5 credits a song); no description box and no lyrics path, unlike the PM board
(「Generate for ◆ 6」). Opening it from AI Magic creates an editor project 「AI Music Generator <MM-DD>」 behind it.

### KP-088 AI Voice Changer on a Free account (android)
On Free only the 「Effect」 tab applies: Radio 1 / Radio 2 free, Telephone / Chipmunk Pro. Every Professional /
Mellow / Bright AI voice is Pro (a tap plays a 10 s preview with 「Unlock the 10-second limit now」). An Effect voice
charges nothing.

### KP-091 Credit prices seen on Android (Free, Stage) (android)
Text to Image 3, AI Art 6, Text to Speech 2, Talking Avatar 10, AI Music Generator 5 a song; Image to Video Veo 3.1
4 s 32, Vidu Q2 15, Kling O3 25, Pixverse V6 20, Wan 2.7 40; Text to Video Kling O3 30, Veo 3.1 4 s Fast 28, Wan 2.7
720p 25; AI Anime Video Vivid 10 s 40; Video Edit by Chat Gemini Omni Flash 1.1 72, Kling O3 45; Character Motion Swap
Wan 2.2 Animate 39, Kling Motion Control 60; Cinematic Reel 70. AI Cartoon and AI Sketch charged nothing although the
feature list prices them at 1. On 2611193: Text to Video Veo 3.1 4 s Fast 28, Kling O3 5 s 1080p 30, Wan 2.7 5 s 1080p 40;
Video Edit by Chat Gemini Omni Flash 1.1 8 a second (40 for 5 s), Kling O3 5 a second (25); Motion Swap Wan 2.2
Animate 3 a second (39), Kling Motion Control 6 a second (60); Cinematic Reel Horror Movie 70, Micro Cinema / Handheld
Camera / One-Take Shot / Time Lapse 48, Fast Cut 72; Pro Seedance 2.0 5 s 40 (I2V Standard, T2V Fast 720p); I2V Gemini
Omni Flash 1.1 5 s 25. Prices are server-set: recheck on each build (Image / Text to Video on 2611251: KP-135).

### KP-098 Gemini Omni Flash 1.1 in Image to Video always generates sound (android)
With 「Gemini Omni Flash 1.1」 picked in Image to Video, 「Generate Sound by AI」 is On and its Off is greyed out; the
result has an audio track (5 s, 25 credits).

### KP-107 The toolbar sheet places every editor tool (unverified)
The sheet lists the editor's toolbars: Global (nothing selected), Video, PIP Video, Photo, PIP Photo, Audio and Text.
Each column is a first-layer button and the items under it are what that button opens. Many tools sit in several
places: Video Enhance is under Video and PIP Video › Enhance, Cinematic Reel Creator under Global › AI Magic and
Photo / PIP Photo › Effects. The newest dated tab is the reference. `node scripts/entry-points.ts pdr fetch` saves it
and `node scripts/entry-points.ts pdr "<tool>"` lists one tool's places. The primary place gets the full table and every
other place a UI pass (spec-casebook `analysis.md` pass 12). Launcher, AI Magic tab, Mine and banner entries are not in the sheet.

The sheet marks platform-specific places and behaviours (user, 2026-11-27): 「(4/E IOS)」 and 「(iOS)」 are iOS only,
「Android沒有」 / 「Andorid 沒有」 are not on Android, 「only Android」 / 「android only」 are Android only, and
「(iOS 11/M; And 12/E)」 ships on both at different releases. A note 「(iOS) … (Android) …」 describes each platform
separately. An Android table never checks an iOS-only place (AI Remove, Quick Actions, Magnifier, Opacity on Video,
Face Smoother / Body Reshape / Face Reshape on Video, Mask on Text), and an iOS table never checks an Android-only one
(HSL, Skin Smoother). `node scripts/entry-points.ts pdr "<tool>" --platform ios|android` applies it.

### KP-112 AI tools started from the editor leave the timeline alone (android)
From the editor, Generate in AI Anime Video, Talking Avatar, AI Art, Text to Image, Cinematic Reel Creator or Video
Edit by Chat goes to the tool's task list or result; results land there and in My Artwork, and Back returns to the
unchanged editor (only a result's 「Add to Timeline」 adds a clip, KP-076). Cinematic Reel Creator and Video Edit by
Chat never take the selected clip; AI Anime Video from a clip's Effects goes straight to trimming that clip, Talking
Avatar from an audio clip takes it as the voice. Leaving Text to Image clears the clip selection (RTMI Q-10).
Editor ⋯ › My Artwork › a result, then system Back ×3, lands on the Launcher, not the editor.

### KP-113 AI Style Transfer on 2611251 (android)
Photo / PIP Photo › Portrait › 「AI Style Transfer」 is back (2611193 had none): tabs Favorites | AI Anime (Custom =
description box) / AI Cartoon / AI Sketch ⓘ / Tempo Effects, opening on AI Anime. No price, no charge (Pro); a result
replaces the photo in place and Undo restores it. Launcher › AI Magic › AI Cartoon / AI Sketch: intro › Try It Now ›
Add Media, then a new project 「AI Cartoon <MM-DD>」 (「…(1)」 next) opens on that panel; results are not in My Artwork.
On Free one Pro style previewed with 「Pro Only / Upgrade Now」, then even free styles opened 「Upgrade to Pro」.

### KP-114 Completion banners and notifications on Android (android)
Each finished task raises its own 「Good news! Your <tool> task has been completed. Tap here to view your results.」
banner (Close / View) over any screen, editor and Launcher included, queued one per task; a system notification comes
with it (not always: none for one Cinematic Reel task). Image to Video holds its banner while its own pages are open.
Each finish logs FcmInstanceIDService 「key = Msg, value = Good news!…」 with `pdr://click_<tool>?oid=…`, usable to time
it; the notification's tap deep-links to the result and drops the page stack. `DownloadUriTask … URI is not absolute`
at a finish has no visible effect. Android counterpart of KP-055.

### KP-116 Text to Image runs only in the foreground (android)
‹ during a Text to Image generation asks 「Images Generating … Leaving this page will cancel the process, and the used
credits will not be restored.」 (Leave / Cancel). It sends no completion message, so it never gets a banner. Once a
label tap on 「Cancel」 left the dialog up after the image had finished; tap it by position.

### KP-117 Models offered on Android (2611251) (android)
Image to Video (11): Kling 4.0 (default), Kling O3, Pixverse V6, Wan 3.0, Gemini Omni Flash 1.1, Happy Horse 1.1,
Seedance 2.5, Seedance 2.0, Veo 3.1, Vidu Q2, Wan 2.7; Seedance 2.5 / 2.0 read 「Subscribe Pro to Unlock」 on Free.
Text to Video (9): Kling 4.0 (default), Wan 3.0, Seedance 2.5, Seedance 2.0, Gemini Omni Flash, Happy Horse 1.1, Wan
2.7, Veo 3.1, Kling O3. Video Edit by Chat as KP-082 (2611193, not reread). No Video Object Removal. The picker is a
bottom sheet opened scrolled to the current model; a downward drag closes it. Server-set: reread each build.

### KP-118 Video Edit by Chat rounds the source length up (android)
The page shows the source length rounded up to the second and bills each rounded second: 8.28 s reads 「00:09」 (◆126,
Seedance 2.5), 5.397 s 「00:06」 (◆30, Kling O3). Leaving the page with inputs filled asks 「Leave this page?」.

### KP-122 AI Art and Text to Image result pages (2611251) (android)
AI Art results cannot be opened in the editor: no 「Full Editor」 (feedback, share, download, 「Turn the image into a
video」, which opens Image to Video with the image filled in); a rule naming 「Full Editor」 for every image result
(AIGC R-024) applies to AI Art without that step. Text to Image right after Generate shows download, share, feedback,
「Image to Video」 and 「Generate ◆3」, no 「Full Editor」, 「Add to Timeline」 or You might also like; opened from My
Artwork (editor) it adds 「Add to Timeline」. 2611193 showed 「Full Editor」 for Text to Image: recheck per build.

### KP-123 Image and Text to Video tool pages on Android (android)
Both show a 「Try It Now」 intro at every open until 「Don't show again」 is ticked (Text to Video from Editor › AI Magic
skips it). Generate goes straight to Recent tasks with a processing card already tagged with the model. Text to Video
has no ‹ (only a home icon, back to AI Magic or the editor) and after Generate its page is replaced by Recent tasks, so
‹ from a Home entry goes to Home; Image to Video keeps its page. Text to Video has no Template tab; Image to Video
template tasks are named after the template (「Breakthrough 1」).

### KP-124 Text to Image has two history pages (android)
The tool's history icon opens ‹ + home, 「Manage」 (edit mode with 「Select All」 / 「Deselect All」), date groups and
prompt rows whose copy icon refills the prompt; closing a preview returns to it. My Artwork › Text to Image opens X +
home, 「Select」 and 「Images were created」; closing a preview returns to My Artwork. From the editor a preview is an
import page (「Import 1 Image」).

### KP-125 Cinematic Reel Creator tasks (android)
Tasks are named by template and a counter (「Micro Cinema 01」, 「02」…), not by date. Generate switches to the task
list; system Back on 「Analyzing & Generating」 returns to the preview while the task runs on. From any editor entry it
opens the template carousel as from the Launcher and never brings in the selected photo.

### KP-126 Talking Avatar's entries and voice check (android)
From an audio clip's toolbar it takes that clip as the voice (Step 2 「Edit the Voice and Format」, no By Text / By
Voice switch). A near-silent voice is refused at Generate with 「Please use speech or spoken audio, not music or singing
files.」, no charge; /sdcard/Music/Recorded_Voices/VoiceOver_20220214_180613.wav (8 s) passes. No Launcher › AI Magic
tile: the other entry is Editor › AI Magic. Its task list once read 「No Generated Videos」 though older tasks existed.

### KP-127 Two My Artwork pages on Android (android)
☰ › My Artwork switches to the AI Magic tab's My Artwork (46 px side gutter), like iOS (KP-032). Pro / Mine › 「My
Artwork」 opens a separate page whose titles and tiles start at x = 0 with no side margin and its ‹ / title row at
y = 0. Not in a spec; compare with the Design's My Artwork board before filing.

### KP-128 Android Home on 2611251 (android)
Shortcut tiles (CMS, KP-012) page 1: Image to Video, Character Motion Swap, Cinematic Reel Creator, AI Mini Drama, AI
Storytelling, AI Video Upscaler, Text To Video, Auto Captions; page 2: Auto Edit, Photo Enhance, Replace BG, Fix Shake,
AI Anime Video, Adjust Speed, Facial Mosaic, Voice Changer. AI-Powered Creation: Movie-Style Reels, Describe & Edit,
Create with Veo3.1, Text To Video, 60s Vlog Master, Animate your image (= Image to Video); What's Trending holds Image
to Video templates (Ghost Step 15, Breakthrough / Tiny Darling 25 credits). No Text to Image entry on Home.

### KP-130 Text to Speech entries add a title first (android)
Global › Audio › Text to Speech, Global › Text › Text to Speech and Editor › AI Magic › Text to Speech first add a
「Tap to Edit」 title at the playhead and open its text editor; ✓ opens 「Select Voice」 (Preset ◆2 per 1,000
characters; Casual Voice is Pro, 「Generate Voice」 with no price). Leaving Select Voice keeps the title. With a title
selected, Text toolbar › Text to Speech opens Select Voice at once with its text. The label reads 「Text to  Speech」.

### KP-131 A second voice on the same title (android)
When the title already has a voice, Generate asks 「Generate Another Voice? / 2 credits will be used for this
generation.」 with a 「Replace the current voice instead of adding a new one」 tick (button Generate, or Replace when
ticked). Replace moved the voice from audio track 1 to track 2.

### KP-132 AI Voice Changer on a Pro account (android)
One panel from Global › Audio, Video / PIP Video › Audio Tools and Audio clip › Audio Tools: tabs Effect / Professional
/ Mellow / Bright / Deep / Other, a Filter sheet (Type, Gender, Age, Reset, Save filter) and trash. No price shown;
Professional voices applied with no charge. The voice replaces the clip's own audio (no new track). From Global › Audio
with nothing selected it takes the main clip under the playhead and leaves it selected. Free: KP-088.

### KP-135 Video generation prices on 2611251 (android)
Image to Video 5 s: Kling 4.0 70, Kling O3 25, Pixverse V6 20, Wan 3.0 50, Gemini Omni Flash 1.1 25, Happy Horse 1.1
40, Seedance 2.5 150, Seedance 2.0 40, Veo 3.1 32, Vidu Q2 15, Wan 2.7 40; templates 15 or 25. Text to Video 9:16 5 s
1080p: Kling 4.0 70, Wan 3.0 50, Seedance 2.5 150, Seedance 2.0 40, Gemini Omni Flash 25, Happy Horse 1.1 40, Wan 2.7
40, Veo 3.1 28, Kling O3 30. Video Edit by Chat Seedance 2.5 14 a second, Kling O3 5. Others as KP-091.

### KP-140 Intro pages before the Launcher after a reset (android)
On the second launch after `pm clear` (en-US) the app shows 「Welcome to PowerDirector」 「Get Started」 (Open intro),
then an AI Mini Drama intro (「Turn your ideas and characters into captivating mini dramas.」 「Continue」, then 「Try It
Now」 with 「Don't show again」); its back arrow goes on to the next launch page (a campaign interstitial, else the
Launcher). Rows that start from a launch walk past these pages first.

### KP-143 No VIP Benefits page on Android Mine (android)
On a Pro account the VIP banner is the card at the top of Mine and tapping it opens nothing: there is no separate
「VIP Benefits」 page. Pro also has no upgrade (IAP page) entry, so the IAP page and its banner can only be reached on
Free.

### KP-145 Stage ran a Black Friday Not Enough Credit dialog on 2026-11-26 (android, authority observed)
On the real date 2026-11-26 Stage showed no Christmas or New Year theme, and Generate with too few credits opened a
Black Friday dialog (purple card, 「Black Friday」 「SALE」, 「More Credits Needed!」, 「Grab Discount Now!」, ⓧ closes it
with no charge). So a real-date run on Stage is not a "regular" baseline while another campaign is live. The dialog is
not in the accessibility tree: read its texts from the screenshot. Version-bound; check the date's campaign first.

## term

### KP-023 Meme Dance Creator
The Launcher's second row is 「Meme Dance Creator」 in the build. Design 8/E and the more-content-promotion sheet also
say 「Meme Dance Generator」; use the build's name and don't file the difference (a spec self-contradiction for PM).

### KP-038 Advanced Cutout and AI Smart Cutout
One capability: the Mine Free card calls it 「Advanced Cutout」, the paywall's Compare plans 「AI Smart Cutout」.

Not shown: KP-082 (superseded by KP-117), KP-090 (superseded by KP-122), KP-104 (superseded by KP-106), KP-110 (disputed: the sheet (KP-107) puts these tools under Effects / names 「AI Text to Image」; AIGC Watermark Q-22, drafted to PM as ISS-AWA-20), KP-068 (disputed: annualsubscription_newyear_2611 bought 2026-11-25 13:02 (phone time) on acda.test9 was still Pro ~25 h later (Mine 「Pro」 after relaunch, `updateSubscribingStatus: true` every launch, build 2611251); the phone date had been moved forward meanwhile, so either this SKU keeps renewing or the date shift keeps it alive. Until settled, check the tier at each segment start rather than assume a lapse)

<!-- knowledge hash: 0283d4eac9154377 -->
