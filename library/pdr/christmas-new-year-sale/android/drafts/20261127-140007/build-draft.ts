// Builds draft.csv and requirements.md for pdr/christmas-new-year-sale (android), update of v3.
// Run: node library/pdr/christmas-new-year-sale/android/drafts/20261127-140007/build-draft.ts
// User, 2026-11-27 (REQ-011): DRA262611P0311 re-verified under R-048 (Q-14): without Credit Auto Pass the page leads with the
// Auto Pass sale, with Auto Pass it shows the 2000-credit pack sale. v3's TC-120 / TC-121 expected the 2000 pack without
// Auto Pass, and TC-122 / TC-123 tap 「Get 2000 credits」 with no Auto Pass precondition. New TC-205: New Year with Auto Pass.
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
const why = 'REQ-011: R-048 (Q-14) — without Credit Auto Pass the Auto Pass sale leads; the 2000-credit pack sale only with Auto Pass (DRA262611P0311 NAB)';

const [head, ...v3] = parseCsv(readFileSync(join(here, '../../cases.csv'), 'utf8').replace(/^﻿/, '')).filter(r => r.length > 1);
const page = (season: 'Christmas' | 'New Year') => [
  `Top banner 「${season} Special」, the same image in every language`,
  'The top card is the Auto Pass credit sale (Credit Auto Pass, 2000 credits a year)',
  'No 「1000+1000」 Special Offer pack and no 「Get 2000 credits for …」 (they need Auto Pass, TC-126 / TC-205)',
  'Packs 50, 100, 200, 500, 1000, 2000 credits, each with its original price struck through and the member price',
  '「Subscribe for 3000 free credits!」',
  '「Each credit for about $0.1」 and 「The expiration period for consumed credits is one year.」',
  '「Privacy Policy」 | 「Terms of Use」',
  season === 'Christmas' ? 'No countdown above the CTA' : 'Above the CTA a clock icon and a countdown 「<d>D hh:mm:ss」 (TC-089 checks its value)',
].join('\n');
const ref = 'R-045, R-048, R-050, R-052, R-049';
const out: string[][] = [];
for (const r of v3) {
  const id = r[0];
  if (id === 'TC-120' || id === 'TC-121') {
    const season = id === 'TC-120' ? 'Christmas' : 'New Year';
    const notes = r[7].replace(/^US mockup prices: [^.]*\. /, 'US mockup prices: $9.99→$4.99, $17.99→$8.99, $31.99→$15.99, $69.99→$34.99, $119.99→$59.99, $199.99→$99.99. ');
    out.push([id, r[1], r[2], r[3], page(season), r[5], ref, `${notes} Without Auto Pass: Q-14 ruling (REQ-002), REQ-011.`, 'modified', why]);
  } else if (id === 'TC-122' || id === 'TC-123') {
    const pre = r[2].split('\n').map(l => l.replace(/^\d+\. /, ''));
    pre.splice(2, 0, 'Credit Auto Pass subscribed (the 2000-credit pack sale shows only then, R-048)');
    out.push([id, r[1], pre.map((s, i) => `${i + 1}. ${s}`).join('\n'), r[3], r[4], r[5], r[6].includes('R-048') ? r[6] : `${r[6]}, R-048`,
      [r[7], 'Run after the Auto Pass purchase row (TC-150).'].filter(Boolean).join(' '), 'modified', why]);
  } else {
    out.push([...r, 'unchanged', '']);
  }
  if (id === 'TC-126') {
    out.push(['TC-205', 'Credit purchase page', '1. Pro account (subscribed) signed in\n2. New Year window: stage server, RD test date 2026-12-30\n3. Credit Auto Pass subscribed',
      'Open the credit purchase page', 'Top banner 「New Year Special」\nThe balance line reads 「Auto Pass activated」\nThe 2000-credit pack sale shows: 「1000+1000」 「$166.99」 and 「Get 2000 credits for $166.99」\nNo Auto Pass sale card and no 「Subscribe for 3000 free credits!」',
      'P1', 'R-048, R-046, R-045', 'New Year counterpart of TC-126. Run after the Auto Pass purchase row. Q-14 ruling (REQ-002), REQ-011.', 'new', why]);
  }
}

// REQ-012 (user, 2026-11-27): the Design draws the IAP page and the credit page in dark and light (IAP_year dark / light,
// credit page dark / light); v3 checked only 「seasonal background」 in whatever appearance the phone had (DRA262611P0331).
// New R-071 / R-072 and one row per page × season × appearance, colours read from the Design frames.
const why12 = 'REQ-012: the Design draws this page in dark and light; one row per appearance (DRA262611P0331 was missed with one row)';
const app = (m: 'Dark' | 'Light') => `App Appearance 「${m} Mode」 (☰ › Preferences › Appearance; it overrides the phone setting)`;
const win = (s: 'Christmas' | 'New Year') => s === 'Christmas' ? 'Christmas window: stage server, RD test date 2026-12-15' : 'New Year window: stage server, RD test date 2026-12-30';
const pre = (who: string, s: 'Christmas' | 'New Year', m: 'Dark' | 'Light', open: string) => [who, win(s), app(m), open].map((x, i) => `${i + 1}. ${x}`).join('\n');
const iapExp = (s: 'Christmas' | 'New Year', m: 'Dark' | 'Light') => [
  `Top banner 「${s} Special」 art as in the other appearance`,
  m === 'Dark' ? 'Page background black' : 'Page background white',
  m === 'Dark' ? `Annual card: dark ${s === 'Christmas' ? 'red' : 'navy'} background with a gold border` : 'Annual card: pale cream background with a yellow border, no dark art',
  m === 'Dark' ? 'Monthly card: black with a grey border, its texts white' : 'Monthly card: white with a grey border, its texts dark grey',
  'Texts and prices readable on their background, nothing left in the other appearance\'s colours',
].join('\n');
const crExp = (s: 'Christmas' | 'New Year', m: 'Dark' | 'Light') => [
  `Top banner 「${s} Special」 art as in the other appearance`,
  m === 'Dark' ? 'Page background black, balance and texts white' : 'Page background white, balance and texts dark',
  m === 'Dark' ? 'Pack tiles dark grey with dark price strips' : 'Pack tiles pale blue with grey price strips',
  'The top offer card keeps its green-blue gradient header, its body in the page colour',
  'Texts and prices readable on their background, nothing left in the other appearance\'s colours',
].join('\n');
let nid = 206;
const rowsAfter: Record<string, string[][]> = { 'TC-102': [], 'TC-121': [] };
for (const s of ['Christmas', 'New Year'] as const) for (const m of ['Dark', 'Light'] as const) {
  rowsAfter['TC-102'].push([`TC-${nid++}`, 'Mine and IAP', pre('Free account (not subscribed) signed in', s, m, 'IAP page open from Mine'), 'Look at the page colours',
    iapExp(s, m), m === 'Light' ? 'P1' : 'P2', 'R-071, R-035', `Design IAP_year ${m.toLowerCase()} (${s}). REQ-012.`, 'new', why12]);
}
for (const s of ['Christmas', 'New Year'] as const) for (const m of ['Dark', 'Light'] as const) {
  rowsAfter['TC-121'].push([`TC-${nid++}`, 'Credit purchase page', pre('Pro account (subscribed) signed in', s, m, 'Credit purchase page open (Mine › Credits)'), 'Look at the page colours',
    crExp(s, m), m === 'Light' ? 'P1' : 'P2', 'R-072, R-045', `Design credit page ${m.toLowerCase()} (${s}). REQ-012.`, 'new', why12]);
}
const out2: string[][] = [];
for (const r of out) {
  if (r[0] === 'TC-100' || r[0] === 'TC-102') {
    r[4] = r[4].replace('Annual card: seasonal background,', 'Annual card: seasonal background (colours per appearance: TC-206 – TC-209),');
    if (r[8] === 'unchanged') { r[8] = 'modified'; r[9] = why12; }
  }
  out2.push(r);
  // the Christmas IAP rows go after TC-102 too: TC-100 and TC-102 are neighbours in the Mine and IAP section
  if (rowsAfter[r[0]]) out2.push(...rowsAfter[r[0]]);
}
out.splice(0, out.length, ...out2);

writeFileSync(join(here, 'draft.csv'), [[...head, 'Change', 'Change Reason'], ...out].map(r => r.map(esc).join(',')).join('\n') + '\n');

let req = readFileSync(join(here, '../../requirements.md'), 'utf8');
const sub = (a: string | RegExp, b: string) => { const n = req.replace(a, b); if (n === req) throw new Error(`anchor not found: ${a}`); req = n; };
sub('- R-046 [PM:pm-xmas-rules ➎; DS:ds-xmas-iap-credit] For a paid user the Special Offer pack',
    '- R-046 [PM:pm-xmas-rules ➎; DS:ds-xmas-iap-credit; ruling Q-14, REQ-011] For a paid user with Credit Auto Pass (R-048) the Special Offer pack');
sub('| R-048 | without Auto Pass | TC-125 |\n| R-048 | with Auto Pass | TC-126 |',
    '| R-048 | without Auto Pass, Christmas | TC-125, TC-120 |\n| R-048 | without Auto Pass, New Year | TC-121 |\n| R-048 | with Auto Pass, Christmas | TC-126, TC-122 |\n| R-048 | with Auto Pass, New Year | TC-205, TC-123 |');
sub(/(\| REQ-002 \| Question answers 2026-11-20[^\n]*\n)/, `$1| REQ-011 | DRA262611P0311 re-verified under the Q-14 ruling: the 2000-credit pack sale only with Credit Auto Pass: R-046, R-048 |\n`);
sub(/(- R-070[^\n]*\n)/, `$1- R-071 [DS:ds-xmas-iap-credit; DS:ds-ny-iap-credit; request REQ-012] The IAP page follows the app's appearance as the Design draws IAP_year dark and light: dark — black page, annual card dark seasonal (Christmas red, New Year navy) with a gold border, monthly card black; light — white page, annual card pale cream with a yellow border, monthly card white; the banner art is the same in both.\n- R-072 [DS:ds-xmas-iap-credit; DS:ds-ny-iap-credit; request REQ-012] The credit purchase page follows the app's appearance as the Design draws it: dark — black page, dark grey pack tiles; light — white page, pale blue pack tiles; the banner art and the offer card's gradient header are the same in both.\n`);
sub('| R-048 | without Auto Pass, Christmas |', '| R-071 | Christmas · dark | TC-206 |\n| R-071 | Christmas · light | TC-207 |\n| R-071 | New Year · dark | TC-208 |\n| R-071 | New Year · light | TC-209 |\n| R-072 | Christmas · dark | TC-210 |\n| R-072 | Christmas · light | TC-211 |\n| R-072 | New Year · dark | TC-212 |\n| R-072 | New Year · light | TC-213 |\n| R-048 | without Auto Pass, Christmas |');
sub(/(\| REQ-011 \| [^\n]*\n)/, `$1| REQ-012 | Why DRA262611P0331 was missed: dark / light drawn by the Design became no variant: R-071, R-072 |\n`);
writeFileSync(join(here, 'requirements.md'), req);
console.log(`draft.csv: ${out.length} rows`);
