// Builds draft.csv and requirements.md for pdr/christmas-new-year-sale (android), update of v2.
// Run: node library/pdr/christmas-new-year-sale/android/drafts/20261126-154459/build-draft.ts
// User, 2026-11-26 (REQ-009): 「Not Enough Credit這個dialog有檢查MUI的case嗎？如果沒有，請新增相關case並執行測試」.
// v2 has no language row for the Not Enough Credit dialog. New R-070 (dialog texts in every shipped language) and
// Q-19 (no translation in the spec); one row per non-English language for the free and the paid dialog, Christmas
// window (the New Year dialog uses the same texts; its theme is TC-136 / TC-138). Every v2 row is unchanged.
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));

const parseCsv = (t: string) => {
  const out: string[][] = []; let row: string[] = [], f = '', q = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (q) { if (c === '"') { if (t[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += c; continue; }
    if (c === '"') q = true; else if (c === ',') { row.push(f); f = ''; }
    else if (c === '\n') { row.push(f); out.push(row); row = []; f = ''; } else if (c !== '\r') f += c;
  }
  if (f || row.length) { row.push(f); out.push(row); }
  return out;
};
const esc = (s: string) => /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;

// The 26 non-English languages, as the interstitial language rows name them (TC-030 – TC-055).
const LANGS: [string, string][] = [
  ['中文（台灣）', 'CHT'], ['中文（简体）', 'CHS'], ['Français', 'FRA'], ['Deutsch', 'DEU'], ['हिन्दी', 'Hindi'],
  ['Bahasa Indonesia', 'IND'], ['Italiano', 'ITA'], ['日本語', 'JPN'], ['한국어', 'KOR'], ['Español (España)', 'ESP'],
  ['Bahasa Melayu', 'Malay'], ['Português (Brasil)', 'PTB'], ['Русский', 'RUS'], ['ไทย', 'Thai'],
  ['Español (México)', 'ESP (MX)'], ['Tiếng Việt', 'Viet'], ['Nederlands', 'Dutch'], ['Türkçe', 'Turkish'],
  ['العربية', 'Arabic'], ['Polski', 'Polish'], ['فارسی', 'Persian'], ['עברית', 'Hebrew'], ['Svenska', 'SVE'],
  ['Dansk', 'DAN'], ['Norsk bokmål', 'NOR'], ['Українська', 'UKR'],
];
const RTL = new Set(['Arabic', 'Persian', 'Hebrew']);
const XMAS = 'Christmas window: stage server, RD test date 2026-12-15';
const LOW = 'Credit balance below the price of Image to Video (Custom)';
const KIND = {
  free: { who: 'Free account (not subscribed) signed in', name: 'Upgrade to Pro', ref: 'R-070, R-055', en: 'TC-134',
          texts: '「Upgrade to Pro」 / 「You don’t have enough credits to use this feature. Upgrade to Pro to get free bonus credits every month.」 / 「Grab Discount Now!」' },
  paid: { who: 'Pro account (subscribed) signed in', name: 'More Credits Needed!', ref: 'R-070, R-053', en: 'TC-132',
          texts: '「More Credits Needed!」 / 「You don’t have enough credits to use this feature. Get credits now!」 / 「Grab Discount Now!」' },
};
const why = 'REQ-009: no language row for the Not Enough Credit dialog; new R-070';

const [head, ...v2] = parseCsv(readFileSync(join(here, '../../cases.csv'), 'utf8').replace(/^﻿/, '')).filter(r => r.length > 1);
let next = Math.max(...v2.map(r => +r[0].slice(3))) + 1;
const fresh: string[][] = [];
for (const k of ['free', 'paid'] as const) {
  const K = KIND[k];
  for (const [lang, code] of LANGS) {
    const exp = [
      `The 「${K.name}」 dialog: title, body and CTA in ${lang}, saying what the English ${K.texts} says`,
      'No text clipped, overlapped or left in English',
      ...(RTL.has(code) ? ['Texts aligned right to left'] : []),
      'Christmas background and image as in English (the art has no text)',
    ].join('\n');
    fresh.push([`TC-${String(next++).padStart(3, '0')}`, 'Not Enough Credit dialog',
      [K.who, XMAS, LOW, `App language ${lang} (phone or app language setting)`].map((s, i) => `${i + 1}. ${s}`).join('\n'),
      '1. Open Image to Video › Custom\n2. Enter a prompt\n3. Tap 「Generate」', exp, 'P2', K.ref,
      `${code}. Q-19: the spec has no translation of the dialog; the app's wording is recorded. English: ${K.en}.`,
      'new', why]);
  }
}
const at = v2.findIndex(r => r[0] === 'TC-142') + 1;
const out = [...v2.slice(0, at).map(r => [...r, 'unchanged', '']), ...fresh, ...v2.slice(at).map(r => [...r, 'unchanged', ''])];
writeFileSync(join(here, 'draft.csv'), [[...head, 'Change', 'Change Reason'], ...out].map(r => r.map(esc).join(',')).join('\n') + '\n');

let req = readFileSync(join(here, '../../requirements.md'), 'utf8');
const r70 = '- R-070 [Rule: localization; ruling Q-16, REQ-002; request REQ-009] The Not Enough Credit dialog, free (R-055) and paid (R-053), shows its title, body and CTA in the app language in every shipped language (all 27, Q-16), complete, not clipped or overlapped and not left in English, right to left in Arabic, Persian and Hebrew; the campaign art has no text and is the same in every language. Wording: Q-19.';
const q19 = '- Q-19 The spec gives no translation of the Not Enough Credit dialog (the 多國文案 sheet covers only the interstitial; the PM and Design draw the dialog in English only). Assumption: the app\'s own translation of the English texts is accepted when it says the same thing, is complete and fits; the wording read on each language is recorded, and a text left in English, clipped or overlapping is a defect. R-070, TC-153 – TC-204.';
const variants = [['free', 'TC-134'], ['paid', 'TC-132']].flatMap(([k, en]) => [`| R-070 | ${k} · ENG | ${en} |`,
  ...fresh.filter(r => r[6].includes(k === 'free' ? 'R-055' : 'R-053')).map(r => `| R-070 | ${k} · ${r[7].split('.')[0]} | ${r[0]} |`)]);
req = req.replace(/(### Variants\n\| Requirement \| Variant \| Rows \|\n\|---\|---\|---\|\n)/, `$1${variants.join('\n')}\n`);
req = req.replace(/(- R-058[^\n]*\n)/, `$1${r70}\n`).replace(/(## Open questions\n)/, `$1${q19}\n`);
if (!req.includes('R-070') || !req.includes('Q-19')) throw new Error('requirements anchors not found');
writeFileSync(join(here, 'requirements.md'), req);
console.log(`draft.csv: ${out.length} rows (${fresh.length} new: ${fresh[0][0]} – ${fresh.at(-1)![0]})`);
