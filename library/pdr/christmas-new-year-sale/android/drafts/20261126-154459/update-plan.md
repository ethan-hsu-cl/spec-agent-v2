# Update plan — v2 → draft 20261126-154459 (REQ-009)

Same spec set (specs/2026-11-20). User, 2026-11-26: 「Not Enough Credit這個dialog有檢查MUI的case嗎？如果沒有，請新增相關case並執行測試」. v2 checks the dialog only in English (TC-132, TC-134).

## Requirements
- New R-070: the Not Enough Credit dialog (free R-055, paid R-053) in every shipped language (27, Q-16): texts in the app language, complete, not clipped or overlapping, right to left in Arabic / Persian / Hebrew, art the same.
- New Q-19: the spec has no translation of the dialog. Assumption: the app's own wording is accepted when it means the same and fits; it is recorded per language.
- Why the analysis missed it: the language variants pass applied Q-16 (27 languages) only to the interstitial, the screen the 多國文案 sheet names; every user-facing text screen shipping in those languages needs a language row, sheet or not.

## Rows
- New TC-153 – TC-178: the free 「Upgrade to Pro」 dialog in the 26 non-English languages.
- New TC-179 – TC-204: the paid 「More Credits Needed!」 dialog in the same 26.
- Placed right after TC-142 in the Not Enough Credit section. Christmas window only: the New Year dialog has the same texts, and its theme is TC-136 / TC-138.
- All 151 v2 rows unchanged.

## Not added
- New Year language rows: the same strings; one season covers the text.
