# Observations — R3 (2026-11-26)

- O-1 (R3-a, closest TC-134; screenshots/r3a-i2v-price.png). With the phone date at 2026-12-24 (KF-003), Image to Video › Custom
  loads no model: the Model row is empty, Video Quality / Duration have no options and 「Generate」 stays disabled with no
  price, also after 15 s. Logcat (tag GW, phone 14:29:24 and 14:29:54): `SSLHandshakeException: Chain validation failed …
  CertificateExpiredException: Certificate expired at Fri Dec 04 07:59:59 GMT+08:00 2026 (compared to Thu Dec 24 14:29:24
  GMT+08:00 2026)`. A server certificate used by the app expires on 2026-12-04, so with the clock moved past that date the
  model list (and with it the Not Enough Credit dialog, reached only through Generate) cannot be reached on 12/24 or 12/30,
  whatever the tier or balance. Test-setup limit of changing the phone date, not an app defect. The Not Enough Credit rows
  need either a phone date before 12/04 with the RD test date on the stage server, or a renewed certificate.
- O-2 (R3-a). acda.test9 is still Pro at R3-a start, ~25 h after the R2-d New Year test subscription
  (annualsubscription_newyear_2611, bought 2026-11-25 13:02 phone time): Mine 「Pro」 after a relaunch and logcat
  `updateSubscribingStatus: true` on every launch. KP-068 expected a lapse within ~3.5–5.5 h; O-2 contradicts KP-068
  (this subscription kept renewing, or the phone date shift affects it). Balance 4 (totalRemain=4, Credit Pack (2000
  credits) row with 4 left).
- O-3 (R3-b, closest TC-132; screenshots/r3b-launcher-realdate.png, r3b-i2v-realdate.png, r3b-nec-realdate.png). On the real
  date (automatic date and time on, 2026-11-26 14:32) the Stage Launcher shows no Christmas or New Year theme (regular
  banner, regular 「Pro」 tab icon) and there is no certificate error: Image to Video › Custom loads Kling 4.0 and
  「Generate」 shows 70 (balance 4). Generate then opens a **Black Friday** Not Enough Credit dialog: purple card, gift box
  and coins, 「Black Friday」 「SALE」, 「More Credits Needed!」, 「You don’t have enough credits to use this feature. Get
  credits now!」, 「Grab Discount Now!」; ⓧ closed it with the balance unchanged. So Stage on 11/26 runs Black Friday, not
  the Christmas window seen in R1 on 11/23. The dialog is not in the accessibility tree (page source empty while it
  shows), so its texts are read from screenshots.
- O-4 (R3-b, workaround for O-1; TC-132, 133, 141, 136, 137). The I2V page keeps its loaded model and price when the phone
  date is changed while it stays open: load Image to Video › Custom on the real date (photo + prompt), set the date in
  Settings (automatic off), return with `activate` (no relaunch), tap Generate: the dialog takes the campaign of the new
  phone date (12/24 Christmas, 12/30 New Year) and its CTA opens that campaign's credit page. Logcat still logs the GW
  CertificateExpiredException on 12/30 and after the final relaunch on 12/24, so a relaunch on a shifted date brings O-1
  back. Use this route for any Not Enough Credit row until the certificate is renewed.
- O-5 (R3-b, TC-133). Opening the Christmas credit page (phone 12/24) showed the toast 「3 Credits Received」 「Daily free
  credits are valid for 7 days. Check back again tomorrow for more!」 and the balance went 4 → 7 (「Expiring within 7 days:
  3 credits」). A Pro account gets the daily free credits on the credit page; each new phone day may add 3 more, so
  later low-balance rows should read the balance again (still far below the I2V price 70).
- O-6 (R3-b). After the final relaunch on 12/24 the Launcher showed 「Good news! Your AI Video Enhance task has been
  completed. Tap here to view your results.」 (View / Close) for a task this run did not start (shared account); closed
  with Close.
- O-7 (R3-a re-run, TC-142; screenshots/TC-142-after-back.png, TC-142-after-back2.png, r3a2-ny-dialog-back-after.png;
  logs/R3-a2-20261126-153110). On the Free Not Enough Credit dialog (Christmas 12/24, three times; New Year 12/30, once)
  one system Back closes the dialog and the Image to Video page together and lands on the Launcher (Project2Activity);
  ⓧ closes only the dialog. Logcat: the key reaches ViewRootImpl[ImageToVideoActivity] (`ViewPostIme key 0/1`, phone
  15:24:33.430), then Project2Activity becomes visible. On 12/30 the Launcher then showed the once-a-day New Year
  interstitial (new date). Recorded TC-142 Fail defect; not filed. The Pro dialog's Back was not tried (no row; account Free).
- O-8 (R3-a re-run). acda.test9 is now Free (Mine 「Free」 「Claim Holiday Deal」, user REQ-008), balance 7 (no daily credits
  added for Free on 12/24: logcat `checkDailyBonus, hasReceivedToday: 1, dailyCredit: 3`). The O-4 workaround worked for
  Free too: each date move brought the Samsung 「Software update」 screen up (closed with Back, KF-003) and `activate`
  returned to the loaded I2V page. Reopening Image to Video on 12/24 in the same process (no relaunch) loaded no model
  (O-1 is per page load, not only per launch), so each new setup went back to the real date.
- O-9 (R3-a re-run). The Launcher on the real date 2026-11-26 shows a 「6D 08:39:30」 countdown pill (Black Friday window
  on Stage, O-3), and moving the phone date back from 12/30 to 12/24 brought a once-a-day interstitial at the relaunch
  (「SAVE 57%」, closed with ✕).
