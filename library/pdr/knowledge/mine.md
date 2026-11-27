# Mine tab

## KP-029 Mine on a paid account
- kind: fact · platform: ios · use: analysis, run · tags: mine, tier, layout
- source: exploration KB mine-page.md (deep dive 2026-09-01, 16.8.0 build 188407, TestFlight, Developer Server, VIP)

No page title (ISS-MP-20) and no scrolling: the bell, an entitlement card (「VIP」 on VIP, 「Pro」 after subscribing
Pro) with a 「Credits N >」 row, rows My Artwork · My Cloud · Demo Videos · User Sign in, then 「Your VIP Features」 and
「More VIP Benefits」, both empty on 16.8.0 although Design F12/F13 fill them (ISS-MP-01/02).

## KP-030 Mine on a Free account
- kind: fact · platform: ios · use: analysis, run · tags: mine, tier, credits
- source: exploration KB mine-page.md (MX-03 run 2026-09-07, PDRM TestFlight, Free, signed out); exploration KB mine-page.md (2026-09-29, 16.9.0 build 189315)

A top chip 「Try Pro+ 7 days for free」; a Free card 「Free」 · 「20+ Benefits >」 (「15+ Benefits」 before 16.9.0) ·
「Claim offer」 with four padlocked benefits (AI Storytelling, Video Object Removal, Video Enhance, Advanced Cutout);
My Credits with the Credits row, 「Buy More」, 「Expiring within 7 days: N credit」, the daily-claim block (KP-041) and a
「Join the Pro+!」 card with 「Subscribe Now」.

## KP-031 Credits row opens My Credits from its right half
- kind: quirk · platform: ios · use: run · tags: mine, credits
- source: exploration KB mine-page.md (verify run 2026-09-02)

「Credits N >」 opens the 「My Credits」 page (Details, Buy More, expiry line) since its fix, but only the balance and
chevron respond; the label and row centre do nothing (ISS-MP-26). Tap the balance number.

## KP-032 My Artwork switches tab
- kind: quirk · platform: ios · use: run · tags: mine, navigation
- source: exploration KB mine-page.md (deep dive 2026-09-01, 16.8.0 build 188407, TestFlight, Developer Server, VIP)

Mine › 「My Artwork >」 does not push a page: it switches to the AI Magic tab with its 「AI Magic | My Artwork」 control
on My Artwork, with no back control (ISS-MP-05). Return by tapping Mine. 「Demo Videos >」 does push a page with ‹.

## KP-033 Demo Videos open a throw-away project
- kind: quirk · platform: ios · use: analysis, run · tags: mine, demo, editor, credits
- source: exploration KB mine-page.md (deep dive 2026-09-01, 16.8.0 build 188407, TestFlight, Developer Server, VIP)

Tapping a Demo Videos card body opens that tool live on sample media (「Try Now」 is a separate target). Applying a
preset there costs 0 credits. Its ✕ lands in the full editor with the demo as a project; leaving with ⌂ returns to
Mine without a save prompt and the project is not kept in the Project tab (ISS-MP-12, ISS-MP-14).

## KP-034 My Cloud needs the corporate Wi-Fi
- kind: quirk · platform: ios · use: analysis, run · tags: mine, cloud, network, wifi
- source: exploration KB mine-page.md (Wi-Fi check 2026-09-03)

On 「17F_QA_Wifi_5G」 My Cloud shows 「Server is busy. Please try again later.」, may open and then eject back to Mine
after about 9 s, and shows the fallback 「0 KB of 1 GB used」. On 「CL-WiFi」 it loads every time (「Upload projects and
media to cloud.」, Project / Media tabs, 「0 KB of 100 GB used」). Recheck any cloud finding on CL-WiFi before writing it.

## KP-035 Sign In validation
- kind: rule · platform: ios · use: analysis, run · tags: mine, sign-in, copy · authority: observed
- source: exploration KB mine-page.md (deep dive 2026-09-01, 16.8.0 build 188407, TestFlight, Developer Server, VIP)

User Sign in › Sign In (Email/Password, Sign Up, Forgot Password, Google / Facebook / Apple): an empty submit shows
「Please enter your Email.」 and 「Please enter your password.」, a bad address 「Please enter a valid email address.」;
fields and errors are cleared on re-entry.

## KP-036 Setting the appearance
- kind: howto · platform: ios · use: run · tags: appearance, dark-mode, settings
- source: exploration KB mine-page.md (deep dive 2026-09-01, 16.8.0 build 188407, TestFlight, Developer Server, VIP)

Home ☰ › Preferences › Appearance: 「Light mode」 / 「Dark mode」 / 「Device Settings」 (default Device Settings).

## KP-037 VIP or Pro+
- kind: question · platform: both · use: analysis, ebug · tags: mine, tier, naming
- source: exploration KB mine-page.md (deep dive 2026-09-01, 16.8.0 build 188407, TestFlight, Developer Server, VIP)

The top tier is called 「VIP」 on the Mine card and in Design F13 but 「Pro+」 on the My Cloud storage badge, the
paywall and Design F14/F17 (which also draw the subscribed bottom tab as 「Pro+」; the build keeps 「Mine」). Whether
they are one tier is for PM (ISS-MP-25); don't file the mix as a defect meanwhile.

## KP-038 Advanced Cutout and AI Smart Cutout
- kind: term · platform: both · use: analysis, ebug · tags: mine, subscription, naming
- source: exploration KB mine-page.md (MX-03 run 2026-09-07, PDRM TestFlight, Free, signed out)

One capability: the Mine Free card calls it 「Advanced Cutout」, the paywall's Compare plans 「AI Smart Cutout」.

## KP-094 Google sign-in goes through Chrome on Android
- kind: howto · platform: android · use: run · tags: sign-in, google, chrome
- source: AIGC Watermark Android run 2026-11-17-r1-full O-27, O-28, O-29 (user approved 「Continue as Acda」, 2026-11-18); Christmas & New Year Sales Android run 2026-11-23-r1-christmas O-9 · verified: 16.9.0 build 2611231 (2026-11-24)

Mine › User Sign in › Google opens Chrome (not the Android account chooser): first Chrome's 「Sign in to Chrome」 sheet
(「Continue as <name>」 / 「Skip」). 「Continue as …」 signs Chrome into the phone's account and goes on without a
password (Stage lands on mauth-stage.cyberlink.com 「You Are All Set!」); 「Skip」 leads to an empty Google 「Email or
phone」 page, which needs the user. Any other account needs its password typed by the user. Once Chrome is signed
in, the button goes straight to 「You Are All Set!」 with no sheet.

## KP-127 Two My Artwork pages on Android
- kind: fact · platform: android · use: analysis, run, ebug · tags: my-artwork, navigation, layout
- source: Recent Task Model Info Android run 2026-11-26-r1-full O-9 (inbox I-026); AIGC Watermark Android run 2026-11-26-e1-entries O-17 · verified: 16.9.0 build 2611251 (2026-11-27)

☰ › My Artwork switches to the AI Magic tab's My Artwork (46 px side gutter), like iOS (KP-032). Pro / Mine › 「My
Artwork」 opens a separate page whose titles and tiles start at x = 0 with no side margin and its ‹ / title row at
y = 0. Not in a spec; compare with the Design's My Artwork board before filing.

## KP-143 No VIP Benefits page on Android Mine
- kind: fact · platform: android · use: analysis, run · tags: mine, tier, vip, iap
- source: Christmas & New Year Sales Android run 2026-11-23-r1r-recheck O-10 · verified: 16.9.0 build 2611201 (2026-11-23)

On a Pro account the VIP banner is the card at the top of Mine and tapping it opens nothing: there is no separate
「VIP Benefits」 page. Pro also has no upgrade (IAP page) entry, so the IAP page and its banner can only be reached on
Free.
