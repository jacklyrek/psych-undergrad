// Psych Wiki — views, routing, and the study loop.
//
// The loop is the one from apps/quiz_runner.py, unchanged in substance because the substance is the
// point (learning-science-for-self-study.md):
//     due item -> predict confidence BEFORE seeing anything -> answer -> reveal + the source
//     reading -> self/auto grade -> scheduler update
// The prediction step is what makes the fluency illusion visible later in Stats, so it stays
// mandatory and it stays first.
//
// Rendering is deliberately plain: build an HTML string, assign it, and handle clicks by delegation
// off a data-action attribute. No framework, no build step — this has to be servable as static files
// from GitHub Pages, and the whole app is small enough that the machinery would cost more than it
// saves.

import * as sm2 from './sm2.js';
import * as store from './store.js';
import * as api from './supabase.js';
import * as sess from './session.js';
import * as stats from './analytics.js';

const view = document.getElementById('view');
const topTitle = document.getElementById('topTitle');
const backBtn = document.getElementById('backBtn');
const syncChip = document.getElementById('syncChip');
const tabbar = document.getElementById('tabbar');
const citeSheet = document.getElementById('citeSheet');

// Confidence buckets. Five taps beat a slider on a phone, and the values sit mid-band for the
// 20-point calibration buckets in analytics.js.
const CONFIDENCE = [
  { v: 10, label: 'No idea' },
  { v: 30, label: 'Shaky' },
  { v: 50, label: 'Maybe' },
  { v: 70, label: 'Fairly sure' },
  { v: 90, label: 'Certain' },
];

const GRADES = [
  { g: 'missed', label: 'Missed', hint: 'start over' },
  { g: 'shaky', label: 'Shaky', hint: 'soon again' },
  { g: 'correct', label: 'Got it', hint: 'space it out' },
];

const KIND_LABEL = { concept: 'con', theory: 'thy', unit: 'unit', person: 'who', study: 'std', sources: 'src' };

// ---------------------------------------------------------------- small helpers

const esc = (s) => String(s ?? '').replace(/[&<>"]/g,
  (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

const pct = (x) => (x === null || x === undefined ? '—' : `${Math.round(x * 100)}%`);
const plural = (n, word) => `${n} ${word}${n === 1 ? '' : 's'}`;

function days(n) {
  if (n === 1) return 'tomorrow';
  return `in ${n} days`;
}

function relTime(iso) {
  if (!iso) return 'never';
  const secs = Math.round((Date.now() - Date.parse(iso)) / 1000);
  if (secs < 60) return 'just now';
  if (secs < 3600) return `${Math.floor(secs / 60)}m ago`;
  if (secs < 86400) return `${Math.floor(secs / 3600)}h ago`;
  return `${Math.floor(secs / 86400)}d ago`;
}

function clozePrompt(item) {
  // The {{deletion}} is replaced with a blank so the answer isn't sitting in the question.
  return esc(item.prompt).replace(/\{\{.*?\}\}/g, '<span class="blank"></span>');
}

function promptHTML(item) {
  return item.type === 'cloze' ? clozePrompt(item) : esc(item.prompt);
}

// --- chart components --------------------------------------------------------
// Colour here answers one question: how am I doing on this row. That makes it a *status* encoding,
// not series identity — so it is a small fixed scale with reserved meaning, and it never travels
// alone: every meter also carries the number, a word, and an icon. The hexes behind these three
// names are validated in style.css; see the note there before changing them.

const STATUS_ICON = { good: '✓', warn: '!', bad: '✕' };

const clampPct = (n) => Math.round(Math.max(0, Math.min(100, n)) * 10) / 10;

/** Accuracy → how you're doing. Bands chosen to match the app's own vocabulary: at 80%+ an item is
 *  genuinely retrieved, below 50% it isn't being recalled so much as recognised. */
function accuracyStatus(acc) {
  if (acc >= 0.8) return { s: 'good', word: 'solid' };
  if (acc >= 0.5) return { s: 'warn', word: 'shaky' };
  return { s: 'bad', word: 'weak' };
}

/** Calibration → the gap between how sure you felt and how often you were right. Underconfidence
 *  costs you nothing, so it isn't flagged; overconfidence is the one that hides missing knowledge. */
function calibrationStatus(gap) {
  if (gap < -0.1) return { s: 'good', word: 'underconfident' };
  if (gap <= 0.1) return { s: 'good', word: 'well judged' };
  if (gap <= 0.25) return { s: 'warn', word: 'overconfident' };
  return { s: 'bad', word: 'badly overconfident' };
}

function statusLegend() {
  return `<div class="legend">${Object.entries(
    { good: '80%+ solid', warn: '50–79% shaky', bad: 'under 50% weak' },
  ).map(([s, text]) => `<span class="status" data-s="${s}">
      <i class="status-icon" aria-hidden="true">${STATUS_ICON[s]}</i>${esc(text)}</span>`).join('')}</div>`;
}

/** One meter per row: name and value on top, the bar, then the status word and the sample size.
 *  `marker` (0–100) draws the comparison line the calibration chart needs. */
function meters(rows) {
  return `<div class="meters">${rows.map((r) => `
    <div class="meter">
      <div class="meter-head">
        <span class="meter-name">${esc(r.name)}</span>
        <span class="meter-val">${esc(r.value)}</span>
      </div>
      <div class="meter-track">
        <span class="meter-fill" data-s="${r.status.s}" style="width:${clampPct(r.pct)}%"></span>
        ${r.marker === undefined ? ''
          : `<span class="meter-mark" style="left:${clampPct(r.marker)}%"></span>`}
      </div>
      <div class="meter-sub">
        <span class="status" data-s="${r.status.s}">
          <i class="status-icon" aria-hidden="true">${STATUS_ICON[r.status.s]}</i>${esc(r.status.word)}
        </span>
        ${r.note ? `<span class="sep">·</span><span>${esc(r.note)}</span>` : ''}
      </div>
    </div>`).join('')}</div>`;
}

/** A day-by-day column strip. Cells are { total, overdue?, today? }; `overdue` stacks at the base in
 *  the critical colour so an overdue backlog is visible inside today's column rather than hidden in
 *  its total. Far more compact than one row per day, and it reads as a calendar. */
function columns(cells, axis) {
  const max = Math.max(1, ...cells.map((c) => c.total));
  const h = (v) => `${Math.max(2, Math.round((v / max) * 1000) / 10)}%`;
  return `<div class="cols">${cells.map((c) => {
    if (!c.total) return `<span class="col"><span class="col-seg" data-s="empty" style="height:2px"></span></span>`;
    const overdue = c.overdue || 0;
    return `<span class="col" ${c.today ? 'data-today="1"' : ''} title="${esc(c.title || '')}">
      ${overdue < c.total ? `<span class="col-seg" style="height:${h(c.total - overdue)}"></span>` : ''}
      ${overdue ? `<span class="col-seg" data-s="bad" style="height:${h(overdue)}"></span>` : ''}
    </span>`;
  }).join('')}</div>
  <div class="cols-axis">${axis.map((a) => `<span>${esc(a)}</span>`).join('')}</div>`;
}

function hero(value, label, note, status) {
  return `<div class="hero" ${status ? `data-s="${status}"` : ''}>
    <b>${esc(value)}</b><span>${esc(label)}</span>${note ? `<em>${esc(note)}</em>` : ''}</div>`;
}

function statGrid(cells) {
  return `<div class="stat-grid">${cells.map((c) => `
    <div class="stat" ${c.tone ? `data-tone="${c.tone}"` : ''}>
      <b>${esc(c.value)}</b><span>${esc(c.label)}</span>
    </div>`).join('')}</div>`;
}

// ---------------------------------------------------------------- routing

function parseHash() {
  const raw = (location.hash || '#/study').slice(1);
  const [path, query] = raw.split('?');
  return {
    parts: path.split('/').filter(Boolean),
    params: new URLSearchParams(query || ''),
  };
}

const TITLES = { study: 'Study', read: 'Readings', stats: 'Stats', you: 'You' };

// --- scroll position ---------------------------------------------------------
// The document scrolls, not #view (which has no overflow of its own), so resetting the container's
// scrollTop does nothing — arriving at a new page left you wherever the last one was scrolled to.
//
// It can't be an unconditional window.scrollTo(0, 0) either, because render() runs for two quite
// different reasons: moving to a new view, and re-rendering the one you're on (tapping a filter
// chip, typing in search, a sync event landing). Resetting on the second kind would yank the page to
// the top mid-interaction. viewKey() is what separates them: same key means same view, leave the
// scroll alone.
const scrollMemory = new Map();
let lastViewKey = null;
let restoreScrollNext = false;

// --- tab memory --------------------------------------------------------------
// The tab bar behaves the way a phone app's does, not the way four plain links do. Two rules:
//
//   * tapping a tab you are *not* on returns you to wherever you last were inside it — stepping off
//     a reading to check Stats and coming back lands on the reading, at the place you left it, not
//     at the top of the index;
//   * tapping the tab you *are* on pops back to that tab's own home (the readings index, the study
//     setup), and tapping it again at home scrolls to the top.
//
// Deliberately in memory only, not localStorage: a cold start should open each tab at its home
// rather than resuming a page from last week.
const tabMemory = new Map();

/** The current route with any ?h=<heading> stripped — the identity a tab remembers. */
function currentPath(parts) {
  return `#/${parts.join('/') || 'study'}`;
}

// --- going back --------------------------------------------------------------
// Both the ‹ button and the swipe route through goBack(). A bare history.back() walks off the end of
// the app when the current page is the first one it drew — a deep link into a reading, or a relaunch
// that restored the URL — and lands you on whatever was in the tab beforehand. Easy to do by
// accident once a gesture can trigger it, so each entry is stamped with how deep into the app it is
// and the bottom of the stack falls back to the section's own home instead.
let navDepth = 0;

function trackDepth() {
  const stamped = history.state?.depth;
  if (typeof stamped === 'number') { navDepth = stamped; return; }  // returning to a stamped entry
  navDepth = lastViewKey === null ? 0 : navDepth + 1;               // a new one; the first is the root
  history.replaceState({ depth: navDepth }, '');
}

function goBack() {
  if (navDepth > 0) history.back();
  else location.hash = `#/${parseHash().parts[0] || 'study'}`;
}

function viewKey(parts) {
  if (parts[0] === 'study' && parts[1] === 'run') {
    // Each item, and each stage within an item, is new content that should start at the top.
    const s = store.loadSession();
    return s ? `study/run/${s.idx}/${s.stage}` : 'study/run';
  }
  if (parts[0] === 'read') {
    if (parts[1]) return `read/${parts[1]}`;
    // Search results are a different list from the full index, but keystrokes within a search
    // aren't — otherwise every character typed would scroll you back to the top.
    return searchQuery.trim().length >= 2 ? 'read:search' : 'read';
  }
  return parts[0] || 'study';
}

/** Opening a section low on the screen would reveal its readings below the fold. Bring its header up
 *  under the top bar instead, so the list you just opened is the list you are looking at. */
function scrollUnitIntoView(key) {
  const head = [...view.querySelectorAll('.unit-head')].find((b) => b.dataset.value === key);
  if (!head) return;
  const bar = document.querySelector('.topbar');
  const top = head.getBoundingClientRect().top + window.scrollY - ((bar ? bar.offsetHeight : 0) + 8);
  window.scrollTo(0, Math.max(0, top));
}

/** Scroll a heading clear of the sticky top bar rather than under it. */
function scrollToHeading(id) {
  const target = view.querySelector(`#${CSS.escape(id)}`);
  if (!target) return;
  const bar = document.querySelector('.topbar');
  const clearance = (bar ? bar.offsetHeight : 0) + 8;
  const top = target.getBoundingClientRect().top + window.scrollY - clearance;
  window.scrollTo(0, Math.max(0, top));
}

function render() {
  const { parts, params } = parseHash();
  const tab = parts[0] || 'study';
  trackDepth();
  const key = viewKey(parts);
  const sameView = key === lastViewKey;
  // Remember where the outgoing view was, read before innerHTML changes the page height.
  if (lastViewKey && !sameView) scrollMemory.set(lastViewKey, window.scrollY);

  for (const a of tabbar.querySelectorAll('.tab')) {
    if (a.dataset.tab === tab) a.setAttribute('aria-current', 'page');
    else a.removeAttribute('aria-current');
  }

  let title = TITLES[tab] || 'Psych Wiki';
  let showBack = false;
  let html = '';

  if (tab === 'study') {
    if (parts[1] === 'run') {
      const s = store.loadSession();
      if (!s) { location.hash = '#/study'; return; }
      html = s.stage === 'summary' ? viewSummary(s) : viewRun(s);
      title = s.stage === 'summary' ? 'Session done' : 'Studying';
    } else {
      html = viewStudySetup();
    }
  } else if (tab === 'read') {
    if (parts[1]) {
      const page = store.content.pagesBySlug.get(parts[1]);
      html = viewPage(parts[1], params.get('h'));
      title = page ? page.title : parts[1];
      showBack = true;
    } else {
      html = viewReadIndex();
    }
  } else if (tab === 'stats') {
    html = viewStats();
  } else if (tab === 'you') {
    html = viewYou();
  } else {
    location.hash = '#/study';
    return;
  }

  topTitle.textContent = title;
  backBtn.hidden = !showBack;
  view.innerHTML = html;

  const anchor = params.get('h');
  if (anchor) {
    // Arrived via [[page#heading]] or a contents link — the heading is the destination.
    scrollToHeading(anchor);
  } else if (!sameView) {
    // Back/forward returns you to where you were; anything else is a new page, so start at the top.
    const remembered = restoreScrollNext ? scrollMemory.get(key) : undefined;
    window.scrollTo(0, remembered ?? 0);
  }
  lastViewKey = key;
  restoreScrollNext = false;
  // Recorded after the redirects above, so a tab never remembers a route that bounced.
  tabMemory.set(tab, currentPath(parts));

  if (tab === 'read' && !store.content.readingsLoaded) store.loadReadings();
}

// ---------------------------------------------------------------- study: setup

const prefs = {
  length: 15,
  cram: false,
  filters: { units: [], blooms: [], types: [] },
};

function viewStudySetup() {
  const items = store.content.items;
  if (!items.length) return `<div class="boot">Loading the bank…</div>`;

  const state = store.getState();
  const today = sm2.todayISO();
  const counts = sess.dueCounts(items, state, prefs.filters, today);
  const facets = sess.facets(items);
  const filtering = Object.values(prefs.filters).some((v) => v.length);
  const available = prefs.cram ? counts.total : (filtering ? counts.inFilter : counts.due);
  const n = Math.min(prefs.length, available);
  const pipe = stats.pipeline(items, state);

  const chip = (kind, value, label) => `<button class="chip" data-action="filter"
      data-kind="${kind}" data-value="${esc(value)}"
      aria-pressed="${prefs.filters[kind].includes(value)}">${esc(label)}</button>`;

  // A session outlives leaving the tab (and the app being killed), so this is where you pick it back
  // up. Without it, tapping Study to pop back here would strand a half-finished session with no
  // route to it — and the queue, not just the position, would be gone.
  const saved = store.loadSession();
  const resume = saved && saved.stage !== 'summary' && saved.idx < saved.queue.length ? `
    <div class="card">
      <b>Session in progress</b>
      <p class="meta" style="margin:.3rem 0 .8rem">Left at item ${saved.idx + 1} of
        ${saved.queue.length}.</p>
      <div class="btn-row">
        <button class="btn btn-ghost" data-action="discard">Discard</button>
        <button class="btn btn-primary" data-action="resume">Resume</button>
      </div>
    </div>` : '';

  return `
  ${resume}
  ${counts.due === 0 && !prefs.cram ? `
    <div class="banner banner-good">Nothing is due today — the schedule has you covered.
    You can still cram below, but spacing is what makes it stick.</div>` : ''}

  <div class="card">
    ${statGrid([
      { value: counts.due, label: 'due today', tone: counts.due ? 'warn' : 'good' },
      { value: pipe.new, label: 'unseen' },
      { value: counts.total, label: 'in bank' },
    ])}
    ${filtering && !prefs.cram
      ? `<p class="meta" style="margin:.2rem 0 .8rem">${counts.inFilter} of those match your focus.</p>` : ''}
    <button class="btn btn-primary" data-action="start" ${n ? '' : 'disabled'}>
      ${n ? `Start — ${plural(n, 'item')}` : 'Nothing to serve'}
    </button>
    ${!n && !prefs.cram ? `<p class="next-hint">Switch to cram, or loosen the focus below.</p>` : ''}
  </div>

  <div class="section-title">Mode</div>
  <div class="chips">
    <button class="chip" data-action="mode" data-value="spaced" aria-pressed="${!prefs.cram}">Spaced — what's due</button>
    <button class="chip" data-action="mode" data-value="cram" aria-pressed="${prefs.cram}">Cram — ignore dates</button>
  </div>
  <p class="meta" style="margin-top:.5rem">${prefs.cram
    ? 'Cram is massing — useful the night before something, not as the habit.'
    : 'The default and the healthiest loop.'}</p>

  <div class="section-title">Session length</div>
  <div class="chips">
    ${[5, 10, 15, 25, 40].map((len) => `<button class="chip" data-action="length" data-value="${len}"
        aria-pressed="${prefs.length === len}">${len}</button>`).join('')}
  </div>

  <div class="section-title">Focus <span class="muted" style="text-transform:none;letter-spacing:0">(optional)</span></div>
  <div class="card card-tight">
    <p class="meta" style="margin-bottom:.4rem">Units</p>
    <div class="chips">${facets.units.map((u) => chip('units', u, sess.unitLabel(u))).join('')}</div>
    <p class="meta" style="margin:.8rem 0 .4rem">Bloom level — apply/analyze is where exams concentrate</p>
    <div class="chips">${facets.blooms.map((b) => chip('blooms', b, b)).join('')}</div>
    <p class="meta" style="margin:.8rem 0 .4rem">Item type</p>
    <div class="chips">${facets.types.map((t) => chip('types', t, t)).join('')}</div>
    ${filtering ? `<div style="margin-top:.8rem"><button class="btn btn-ghost btn-sm" data-action="clearfilters">Clear focus</button></div>` : ''}
  </div>`;
}

function startSession(ids) {
  const items = store.content.items;
  const queue = ids || sess.buildQueue(items, store.getState(), {
    filters: prefs.filters,
    length: prefs.length,
    cram: prefs.cram,
    today: sm2.todayISO(),
  });
  if (!queue.length) return;
  store.saveSession({
    queue,
    idx: 0,
    stage: 'prompt',
    results: [],
    startedAt: Date.now(),
    itemStartAt: Date.now(),
    draft: { confidence: null, response: '' },
  });
  location.hash = '#/study/run';
  render();
}

// ---------------------------------------------------------------- study: the loop

function currentItem(s) {
  return store.content.itemsById.get(s.queue[s.idx]);
}

function viewRun(s) {
  const item = currentItem(s);
  if (!item) {
    // The bank changed under a saved session (rebuilt items.json). Skip the vanished item.
    s.idx += 1;
    if (s.idx >= s.queue.length) s.stage = 'summary';
    store.saveSession(s);
    return s.stage === 'summary' ? viewSummary(s) : viewRun(s);
  }

  const head = `
    <div class="progress"><i style="width:${(s.idx / s.queue.length) * 100}%"></i></div>
    <div class="item-meta">
      <span>Item ${s.idx + 1} of ${s.queue.length}</span><span class="dot">·</span>
      <span>${esc(item.type)}</span><span class="dot">·</span>
      <span>${esc(item.bloom_level)}</span><span class="dot">·</span>
      <span>${esc(sess.unitLabel(item.unit))}</span>
    </div>
    <div class="prompt">${promptHTML(item)}</div>`;

  return s.stage === 'reveal' ? head + stageReveal(s, item) : head + stagePrompt(s, item);
}

function stagePrompt(s, item) {
  const d = s.draft;
  let input;
  if (item.type === 'mcq' && item.options) {
    input = `<div class="options">${item.options.map((opt, i) => `
      <button class="option" data-action="pick" data-value="${esc(opt)}"
              aria-pressed="${d.response === opt}">
        <span class="key">${String.fromCharCode(65 + i)}</span>
        <span>${esc(opt)}</span>
      </button>`).join('')}</div>`;
  } else if (item.type === 'cloze') {
    input = `<label class="field"><span>Fill the blank</span>
      <input type="text" id="responseInput" value="${esc(d.response)}"
             autocapitalize="none" autocomplete="off" spellcheck="false"
             enterkeyhint="done" placeholder="the missing words"></label>`;
  } else {
    input = `<label class="field"><span>Answer in your own words</span>
      <textarea id="responseInput" placeholder="Say it out loud or type it — producing the answer is the point."
                >${esc(d.response)}</textarea></label>`;
  }

  const ready = d.confidence !== null;
  return `
    <div class="section-title">Before you answer — how sure are you?</div>
    <div class="confidence">${CONFIDENCE.map((c) => `
      <button class="conf" data-action="conf" data-value="${c.v}" aria-pressed="${d.confidence === c.v}">
        <b>${c.v}%</b><span>${esc(c.label)}</span>
      </button>`).join('')}</div>
    <p class="meta" style="margin:.6rem 0 1rem">Commit to a number first. The gap between this and
      the outcome is the only way to catch material that merely feels familiar.</p>
    ${input}
    <button class="btn btn-primary" data-action="reveal" ${ready ? '' : 'disabled'}>
      ${ready ? 'Reveal answer' : 'Pick a confidence first'}
    </button>`;
}

function stageReveal(s, item) {
  const d = s.draft;
  const auto = sm2.autograde(item, d.response);
  const modelAnswer = item.type === 'mcq' ? (item.correct || item.answer) : item.answer;
  const explanation = item.type === 'mcq' && item.answer && item.answer !== item.correct ? item.answer : '';
  const page = store.pageForItem(item);
  const st = store.itemState(item.id) || {};

  const banner = auto === true
    ? `<div class="banner banner-good">Auto-graded: <b>correct</b>. Override below if you were guessing.</div>`
    : auto === false
      ? `<div class="banner banner-bad">Auto-graded: <b>not a match</b>. Override below if it's the same idea in other words.</div>`
      : '';

  const suggested = auto === true ? 'correct' : auto === false ? 'missed' : null;

  return `
    ${banner}
    <div class="answer-pair">
      <div class="answer-box yours"><b>You said</b>${d.response ? esc(d.response) : '<i class="muted">(blank)</i>'}</div>
      <div class="answer-box model"><b>Model answer</b>${esc(modelAnswer)}
        ${explanation ? `<p class="explain">${esc(explanation)}</p>` : ''}</div>
    </div>

    <details class="source">
      <summary>Source reading — ${esc(page ? page.title : item.source_page)}</summary>
      <div class="reading" data-slug="${esc(page ? page.slug : '')}">
        ${page ? page.html : (store.content.readingsLoaded
          ? `<p class="muted">Reading not in the bundle: ${esc(item.source_page)}</p>`
          : `<p class="muted">Fetching the readings…</p>`)}
      </div>
    </details>

    <div class="section-title">Grade your recall</div>
    <div class="grades">${GRADES.map((g) => `
      <button class="btn grade" data-action="grade" data-g="${g.g}"
              ${suggested === g.g ? 'data-suggested="1"' : ''}>
        ${g.label}<small>${g.hint}</small>
      </button>`).join('')}</div>
    <p class="next-hint">Currently every ${st.interval || 0}d · ease ${(st.ease ?? 2.5).toFixed(2)}</p>`;
}

function viewSummary(s) {
  const res = s.results;
  const by = { correct: 0, shaky: 0, missed: 0 };
  for (const r of res) by[r.outcome] += 1;
  const secs = Math.round((Date.now() - s.startedAt) / 1000);
  const over = res.filter((r) => r.confidence >= 70 && r.outcome !== 'correct');

  return `
    <div class="banner banner-info">Session done — ${plural(res.length, 'item')} in
      ${Math.floor(secs / 60)}m ${secs % 60}s.</div>
    ${statGrid([
      { value: by.correct, label: 'got it', tone: 'good' },
      { value: by.shaky, label: 'shaky', tone: 'warn' },
      { value: by.missed, label: 'missed', tone: 'bad' },
    ])}

    ${over.length ? `
      <div class="section-title">Overconfident misses</div>
      <div class="banner banner-warn">You felt sure and got these wrong — exactly what the fluency
        illusion hides. Re-read them rather than only re-drilling them.</div>
      <div class="list">${over.map((r) => {
        const item = store.content.itemsById.get(r.item_id);
        const page = item ? store.pageForItem(item) : null;
        return `<a class="list-item" href="#/read/${esc(page ? page.slug : '')}">
          <span class="grow"><span class="title">${esc(item ? item.topic : r.item_id)}</span>
          <span class="sub">felt ${r.confidence}% sure · ${esc(r.outcome)}</span></span>
          <span class="arrow">›</span></a>`;
      }).join('')}</div>` : ''}

    <div class="btn-row" style="margin-top:1rem">
      <button class="btn btn-ghost" data-action="donesession">Done</button>
      <button class="btn btn-primary" data-action="again">Another session</button>
    </div>`;
}

function submitGrade(outcome) {
  const s = store.loadSession();
  if (!s || s.stage !== 'reveal') return;
  const item = currentItem(s);
  if (!item) return;

  const timeTaken = Math.round((Date.now() - s.itemStartAt) / 100) / 10;
  store.grade(item, outcome, {
    confidence: s.draft.confidence,
    timeTaken,
    response: s.draft.response,
  });

  s.results.push({ item_id: item.id, outcome, confidence: s.draft.confidence });
  s.idx += 1;
  s.stage = s.idx >= s.queue.length ? 'summary' : 'prompt';
  s.draft = { confidence: null, response: '' };
  s.itemStartAt = Date.now();
  store.saveSession(s);
  render();
}

// ---------------------------------------------------------------- reader

let searchQuery = '';

// Which unit section the index has open. ~100 wiki pages across 14 units is a long scroll if they
// are all listed at once — Unit 8 sits below sixty rows. Collapsed, every unit is one tap away, and
// only one opens at a time so the list never grows past a screen or two again.
//
// In memory, deliberately, like tabMemory: stepping into a reading and coming back should find the
// section still open, but a cold start should open the index closed.
let openUnit = null;

function viewReadIndex() {
  if (!store.content.readingsLoaded) {
    return store.content.readingsError
      ? `<div class="banner banner-bad">Couldn't load the readings: ${esc(store.content.readingsError)}</div>`
      : `<div class="boot">Fetching 123 readings…</div>`;
  }

  const pages = store.content.pages;
  const q = searchQuery.trim().toLowerCase();
  const search = `
    <div class="search-wrap">
      <input type="search" id="searchInput" value="${esc(searchQuery)}" enterkeyhint="search"
             placeholder="Search ${pages.length} readings" autocapitalize="none" autocomplete="off">
    </div>`;

  if (q.length >= 2) {
    const hits = pages
      .map((p) => {
        const inTitle = p.title.toLowerCase().includes(q);
        const at = p.text.toLowerCase().indexOf(q);
        if (!inTitle && at < 0) return null;
        // Rank title matches first; show the sentence the term appears in as the subtitle.
        const snippet = at >= 0 ? p.text.slice(Math.max(0, at - 45), at + 90) : p.text.slice(0, 120);
        return { page: p, rank: inTitle ? 0 : 1, snippet };
      })
      .filter(Boolean)
      .sort((a, b) => a.rank - b.rank || a.page.title.localeCompare(b.page.title))
      .slice(0, 60);

    return search + (hits.length
      ? `<p class="meta" style="margin-bottom:.6rem">${plural(hits.length, 'match')}</p>
         <div class="list">${hits.map((h) => rowFor(h.page, h.snippet)).join('')}</div>`
      : `<div class="empty"><div class="empty-big">∅</div>No reading mentions “${esc(searchQuery)}”.</div>`);
  }

  // Grouped by unit, spine first, then electives, then the sources files. One collapsible section
  // per group, so the whole syllabus fits on screen and any unit is a tap rather than a scroll.
  const wiki = pages.filter((p) => p.collection === 'wiki');
  const research = pages.filter((p) => p.collection === 'research');
  const units = [...new Set(wiki.map((p) => p.unit).filter(Boolean))].sort(sess.compareUnits);

  let html = search;
  for (const unit of units) {
    const group = wiki.filter((p) => p.unit === unit);
    // The unit overview page leads; concepts and theories follow alphabetically.
    group.sort((a, b) => (a.type === 'unit' ? -1 : b.type === 'unit' ? 1 : a.title.localeCompare(b.title)));
    const spine = /^\d+$/.test(unit);
    html += unitSection(unit, spine ? unit : 'elec', unitTopic(unit, group),
                        plural(group.length, 'reading'), group);
  }
  if (research.length) {
    html += unitSection('sources', 'src', 'Sources & evidence base',
                        plural(research.length, 'source file'),
                        research.slice().sort((a, b) => sess.compareUnits(a.unit, b.unit)));
  }
  return html;
}

/** "Unit 8 — Crisis, Risk Assessment & Trauma-Informed Care" → "Crisis, Risk Assessment &
 *  Trauma-Informed Care". The number is already in the badge; the topic is what you scan for. */
function unitTopic(unit, group) {
  const overview = group.find((p) => p.type === 'unit');
  const title = overview ? overview.title : sess.unitLabel(unit);
  return title.replace(/^(unit\s*\d+|elective)\s*[—–-]\s*/i, '');
}

/** A collapsed unit shows only its header row; opening one closes whichever was open. */
function unitSection(key, badge, title, sub, pages) {
  const open = openUnit === key;
  return `<div class="list unit-group">
    <button class="list-item unit-head" data-action="toggleunit" data-value="${esc(key)}"
            aria-expanded="${open}">
      <span class="kind${badge.length > 2 ? ' kind-word' : ''}">${esc(badge)}</span>
      <span class="grow"><span class="title">${esc(title)}</span><span class="sub">${esc(sub)}</span></span>
      <span class="arrow chevron">›</span>
    </button>
    ${open ? pages.map((p) => rowFor(p)).join('') : ''}
  </div>`;
}

function rowFor(page, snippet) {
  const sub = snippet
    ? `…${esc(snippet.trim())}…`
    : (page.tags?.length ? esc(page.tags.slice(0, 4).join(' · ')) : esc(sess.unitLabel(page.unit)));
  return `<a class="list-item" href="#/read/${esc(page.slug)}">
    <span class="kind">${esc(KIND_LABEL[page.type] || page.type.slice(0, 3))}</span>
    <span class="grow"><span class="title">${esc(page.title)}</span><span class="sub">${sub}</span></span>
    <span class="arrow">›</span></a>`;
}

function viewPage(slug) {
  if (!store.content.readingsLoaded) return `<div class="boot">Fetching the readings…</div>`;
  const page = store.content.pagesBySlug.get(slug);
  if (!page) {
    return `<div class="empty"><div class="empty-big">?</div>No reading called
      <code>${esc(slug)}</code>.<div style="margin-top:1rem"><a class="btn btn-ghost" href="#/read">All readings</a></div></div>`;
  }

  const items = store.content.items.filter(
    (it) => String(it.source_page).replace(/^.*\//, '').replace(/\.md$/, '') === slug);
  const chips = [
    page.type,
    page.unit ? sess.unitLabel(page.unit) : null,
    page.cluster ? `cluster: ${page.cluster}` : null,
    page.track === 'elective' ? 'elective' : null,
  ].filter(Boolean);

  const toc = page.headings.length > 2 ? `
    <details class="source"><summary>On this page</summary>
      <div class="toc" style="padding:0 .85rem .6rem">
        ${page.headings.map((h) => `<a href="#/read/${esc(slug)}?h=${esc(h.id)}"
           data-level="${h.level}">${esc(h.text)}</a>`).join('')}
      </div></details>` : '';

  // Offered twice — before the reading and again at the end, so finishing a long page doesn't
  // mean scrolling back up to quiz on it.
  const quizBtn = (margin) => items.length
    ? `<button class="btn btn-primary" data-action="quizpage" data-slug="${esc(slug)}"
         style="${margin}">Quiz me on this — ${plural(items.length, 'item')}</button>`
    : '';

  return `
    <div class="chips" style="margin-bottom:.8rem">
      ${chips.map((c) => `<span class="chip chip-static">${esc(c)}</span>`).join('')}
    </div>
    ${quizBtn('margin-bottom:1rem')}
    ${toc}
    <article class="reading" data-slug="${esc(slug)}">${page.html}</article>
    ${quizBtn('margin:1.4rem 0 .4rem')}

    ${page.backlinks.length ? `
      <div class="section-title">Linked from</div>
      <div class="list">${page.backlinks.map((b) => {
        const p = store.content.pagesBySlug.get(b);
        return p ? rowFor(p) : '';
      }).join('')}</div>` : ''}`;
}

function openCite(slug, key) {
  const page = store.content.pagesBySlug.get(slug);
  const note = page?.sources?.[key];
  document.getElementById('citeLabel').textContent = `Source ${key}`;
  document.getElementById('citeText').textContent = note
    || 'This page cites the source by number; the full note is in the unit’s sources file under Readings.';
  citeSheet.hidden = false;
}

// ---------------------------------------------------------------- stats

function viewStats() {
  const items = store.content.items;
  const state = store.getState();
  const log = store.getLog();
  const today = sm2.todayISO();

  if (!log.length) {
    return `<div class="empty"><div class="empty-big">◌</div>
      No attempts recorded yet.<p class="meta" style="margin-top:.6rem">Study a session and this
      fills in — accuracy, calibration, and what's coming due.</p>
      ${api.configured && !api.signedIn() ? `<p class="meta">Signing in on the <a href="#/you">You</a>
        tab pulls in the history from your laptop.</p>` : ''}</div>`;
  }

  const sum = stats.summarize(log);
  const str = stats.streak(log, today);
  const cal = stats.calibration(log);
  const brier = stats.brierScore(log);
  const forecast = stats.dueForecast(items, state, today, 14);
  const pipe = stats.pipeline(items, state);
  const blooms = stats.byBloom(log, sess.BLOOM_ORDER);
  const weak = stats.weakestClusters(log);
  const act = stats.activity(log, today, 30);
  const stale = stats.daysSinceLast(log, today);
  const due = forecast[0];
  const inRotation = items.length - pipe.new;

  return `
    <div class="card">
      ${hero(
        due.count,
        due.count ? 'items due today' : 'nothing due today',
        [due.fresh ? `${due.fresh} never seen` : null,
         due.overdue ? `${due.overdue} overdue reviews` : null,
         `${inRotation} in rotation`].filter(Boolean).join(' · '),
        due.count ? null : 'good',
      )}
    </div>

    ${statGrid([
      { value: str.current, label: 'day streak' },
      { value: sum.attempts, label: 'attempts' },
      { value: pct(sum.accuracy), label: 'got it',
        tone: accuracyStatus(sum.accuracy).s === 'good' ? 'good'
            : accuracyStatus(sum.accuracy).s === 'warn' ? 'warn' : 'bad' },
      { value: `${Math.round(sum.medianSeconds)}s`, label: 'median' },
      { value: pipe.new, label: 'unseen' },
      { value: pipe.mature, label: 'mature' },
    ])}
    ${stale !== null && stale > 3
      ? `<div class="banner banner-warn">Last attempt was ${plural(stale, 'day')} ago.</div>` : ''}

    <div class="section-title">Coming due</div>
    <div class="card card-tight">
      ${/* Today is deliberately not in this chart. With a backlog it dwarfs every scheduled day,
            leaving one tall column and fourteen empty ones — a one-bar bar chart that says nothing
            the hero above hasn't already said. This answers the different question: what's ahead. */
        columns(
          forecast.slice(1).map((f) => ({ total: f.count, title: `${f.date}: ${f.count}` })),
          ['tomorrow', '+7', '+14'],
        )}
      <p class="meta" style="margin:.7rem 0 0">The next 14 days, not counting
        ${due.count ? `today's ${due.count}` : 'today'}.
        ${forecast.slice(1).some((f) => f.count)
          ? `Heaviest day ahead: ${Math.max(...forecast.slice(1).map((f) => f.count))} items.`
          : 'Nothing scheduled yet — intervals grow as you review.'}</p>
    </div>

    <div class="section-title">Calibration — did the confidence match?</div>
    <div class="card card-tight">
      <p class="meta" style="margin-bottom:.9rem">Bar = how often you were actually right.
        The line = how sure you felt. Bar well short of the line is the fluency illusion:
        material that felt known and wasn't.</p>
      ${meters(cal.filter((b) => b.n).map((b) => {
        const acc = b.accuracy ?? 0;
        return {
          name: `Felt ${b.lo}–${b.hi}% sure`,
          value: pct(acc),
          pct: acc * 100,
          marker: (b.lo + b.hi) / 2,
          status: calibrationStatus(b.gap ?? 0),
          note: `${plural(b.n, 'attempt')} · ${b.correct} right`,
        };
      }))}
      <p class="meta" style="margin:.9rem 0 0">Brier score ${brier === null ? '—' : brier.toFixed(3)}
        — lower is better; 0.25 is what pure guessing scores.</p>
    </div>

    <div class="section-title">Accuracy by Bloom level</div>
    <div class="card card-tight">
      ${statusLegend()}
      ${/* The line is your own overall accuracy. The status colour answers "how am I doing" in
            absolute terms, but real accuracy tends to cluster inside one band — the marker is what
            separates the levels from each other, without recolouring anything by rank. */
        meters(blooms.map((b) => ({
          name: b.bloom,
          value: pct(b.accuracy),
          pct: b.accuracy * 100,
          marker: sum.accuracy * 100,
          status: accuracyStatus(b.accuracy),
          note: `${plural(b.n, 'attempt')} · ${b.correct} right`,
        })))}
      <p class="meta" style="margin:.9rem 0 0">The line is your ${pct(sum.accuracy)} overall average.
        Apply and analyze sitting below remember is the normal pattern — definitions are the
        easy 30%.</p>
    </div>

    ${weak.length ? `
      <div class="section-title">Weakest clusters</div>
      <div class="card card-tight">
        ${meters(weak.map((c) => ({
          name: c.cluster.replace(/-/g, ' '),
          value: pct(c.accuracy),
          pct: c.accuracy * 100,
          marker: sum.accuracy * 100,
          status: accuracyStatus(c.accuracy),
          note: `${plural(c.n, 'attempt')} · ${c.correct} right`,
        })))}
        <p class="meta" style="margin:.9rem 0 0">Confusable groups you're still not separating${
          weak.every((c) => c.accuracy < sum.accuracy) ? `, all below your ${pct(sum.accuracy)} average` : ''
        }. Interleaving them is the fix, not more repetitions of each alone.</p>
      </div>` : ''}

    <div class="section-title">Last 30 days</div>
    <div class="card card-tight">
      ${columns(
        act.map((a) => ({ total: a.count, title: `${a.date}: ${a.count}` })),
        ['30 days ago', 'today'],
      )}
      <p class="meta" style="margin:.7rem 0 0">${plural(str.activeDays, 'active day')} in the log ·
        current streak ${plural(str.current, 'day')}.</p>
    </div>`;
}

// ---------------------------------------------------------------- you / settings

function viewYou() {
  const user = api.currentUser();
  const s = store.status;
  const standalone = window.matchMedia('(display-mode: standalone)').matches
    || window.navigator.standalone === true;

  const syncCard = !api.configured
    ? `<div class="card">
         <b>Local only</b>
         <p class="meta" style="margin-top:.4rem">Progress is saved in this browser, but not synced.
           To share one queue with the laptop, fill in <code>docs/config.js</code> with your Supabase
           URL and anon key — the steps are in <code>docs/README.md</code>.</p>
       </div>`
    : user
      ? `<div class="card">
           <b>Signed in</b>
           <p class="meta" style="margin:.3rem 0 .8rem">${esc(user.email || '')}<br>
             Last sync ${esc(relTime(s.lastSync))}${s.queued ? ` · ${plural(s.queued, 'attempt')} waiting to upload` : ''}</p>
           ${s.error ? `<div class="banner banner-bad">${esc(s.error)}</div>` : ''}
           <div class="btn-row">
             <button class="btn btn-ghost" data-action="signout">Sign out</button>
             <button class="btn btn-primary" data-action="sync" ${s.syncing ? 'disabled' : ''}>
               ${s.syncing ? 'Syncing…' : 'Sync now'}</button>
           </div>
         </div>`
      : `<div class="card">
           <b>Sign in to sync</b>
           <p class="meta" style="margin:.3rem 0 .8rem">Same account as the laptop, so both share one
             queue and one history.</p>
           <label class="field"><span>Email</span>
             <input type="email" id="email" autocomplete="username" autocapitalize="none"
                    inputmode="email" enterkeyhint="next"></label>
           <label class="field"><span>Password</span>
             <input type="password" id="password" autocomplete="current-password"
                    enterkeyhint="go"></label>
           <div id="signinError"></div>
           <button class="btn btn-primary" data-action="signin">Sign in</button>
         </div>`;

  return `
    ${syncCard}

    <div class="section-title">Version</div>
    <div class="card card-tight">
      <p class="meta" style="margin:0">Build <code>${esc(localStorage.getItem(BUILD_KEY) || '—')}</code> ·
        content <code>${esc(store.content.version || '—')}</code><br>
        ${store.content.items.length} items ·
        ${store.content.readingsLoaded ? `${store.content.pages.length} readings` : 'readings not loaded'}</p>
      <div class="btn-row" style="margin-top:.7rem">
        <button class="btn btn-ghost btn-sm" data-action="checkcontent">Check for updates</button>
        <button class="btn btn-ghost btn-sm" data-action="forceupdate">Force refresh</button>
      </div>
      <p class="meta" style="margin:.7rem 0 0">Updates are picked up automatically on the next open.
        <b>Force refresh</b> is the escape hatch — it throws away every cache and the service worker
        and reloads from the network.</p>
    </div>

    ${!standalone ? `
      <div class="section-title">Add to home screen</div>
      <div class="card card-tight">
        <p class="meta" style="margin:0">In Safari: Share → <b>Add to Home Screen</b>. It then opens
          full-screen and keeps working with no signal.</p>
      </div>` : ''}

    <div class="section-title">Reset</div>
    <div class="card card-tight">
      <p class="meta" style="margin:0 0 .7rem">Clears this device's cached progress and session.
        ${api.configured ? 'Anything already synced comes back on the next sync.' :
          '<b>Nothing is synced, so this cannot be undone.</b>'}</p>
      <button class="btn btn-ghost btn-sm" data-action="reset">Clear local data</button>
    </div>`;
}

// ---------------------------------------------------------------- sync chip

function updateChip() {
  const s = store.status;
  let state = 'local';
  let text = 'local';
  if (!api.configured) { state = 'local'; text = 'local'; }
  else if (!api.signedIn()) { state = 'local'; text = 'sign in'; }
  else if (s.syncing) { state = 'syncing'; text = 'syncing'; }
  else if (s.error) { state = 'error'; text = 'error'; }
  else if (s.queued) { state = 'queued'; text = `${s.queued} queued`; }
  else if (!s.online) { state = 'queued'; text = 'offline'; }
  else { state = 'synced'; text = 'synced'; }
  syncChip.dataset.state = state;
  syncChip.textContent = text;
}

// ---------------------------------------------------------------- events

view.addEventListener('click', async (ev) => {
  const cite = ev.target.closest('.cite');
  if (cite) {
    const host = cite.closest('[data-slug]');
    openCite(host?.dataset.slug, cite.dataset.cite);
    return;
  }

  const el = ev.target.closest('[data-action]');
  if (!el) return;
  const { action, value, kind } = el.dataset;

  // --- study setup
  if (action === 'mode') { prefs.cram = value === 'cram'; render(); }
  else if (action === 'length') { prefs.length = Number(value); render(); }
  else if (action === 'filter') {
    const list = prefs.filters[kind];
    const at = list.indexOf(value);
    if (at >= 0) list.splice(at, 1); else list.push(value);
    render();
  } else if (action === 'clearfilters') { prefs.filters = { units: [], blooms: [], types: [] }; render(); }
  else if (action === 'start') { startSession(); }
  else if (action === 'resume') { location.hash = '#/study/run'; render(); }
  else if (action === 'discard') { store.clearSession(); render(); }
  else if (action === 'again') { store.clearSession(); location.hash = '#/study'; render(); }
  else if (action === 'donesession') { store.clearSession(); location.hash = '#/stats'; render(); }

  // --- the loop
  else if (action === 'conf') {
    const s = store.loadSession();
    s.draft.confidence = Number(value);
    s.draft.response = readResponse(s);
    store.saveSession(s);
    render();
  } else if (action === 'pick') {
    const s = store.loadSession();
    s.draft.response = value;
    store.saveSession(s);
    render();
  } else if (action === 'reveal') {
    const s = store.loadSession();
    s.draft.response = readResponse(s);
    s.stage = 'reveal';
    store.saveSession(s);
    render();
  } else if (action === 'grade') {
    submitGrade(el.dataset.g);
  } else if (action === 'quizpage') {
    const ids = store.content.items
      .filter((it) => String(it.source_page).replace(/^.*\//, '').replace(/\.md$/, '') === el.dataset.slug)
      .map((it) => it.id);
    startSession(ids);
  }

  // --- reader
  else if (action === 'toggleunit') {
    openUnit = openUnit === value ? null : value;
    render();
    if (openUnit) scrollUnitIntoView(openUnit);
  }

  // --- account
  else if (action === 'signin') {
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const errBox = document.getElementById('signinError');
    el.disabled = true;
    el.textContent = 'Signing in…';
    try {
      await api.signIn(email, password);
      await store.afterSignIn();
      render();
    } catch (err) {
      errBox.innerHTML = `<div class="banner banner-bad">${esc(err.message)}</div>`;
      el.disabled = false;
      el.textContent = 'Sign in';
    }
  } else if (action === 'signout') {
    await api.signOut();
    store.afterSignOut();
    render();
  } else if (action === 'sync') {
    await store.sync();
    render();
  } else if (action === 'checkcontent') {
    el.textContent = 'Checking…';
    const build = await fetchBuild();
    if (!build) { el.textContent = "Couldn't check — offline?"; return; }
    if (build === localStorage.getItem(BUILD_KEY)) { el.textContent = 'Already up to date'; return; }
    el.textContent = 'Updating…';
    localStorage.setItem(BUILD_KEY, build);
    // A plain reload would be served the old files out of the service worker cache, so clear the
    // caches first and let the worker repopulate them from the network.
    await purgeCaches();
    location.reload();
  } else if (action === 'forceupdate') {
    // The escape hatch: throw away every cache and the worker itself, then reload from the network.
    el.textContent = 'Clearing…';
    await purgeCaches();
    if ('serviceWorker' in navigator) {
      for (const reg of await navigator.serviceWorker.getRegistrations()) await reg.unregister();
    }
    localStorage.removeItem(BUILD_KEY);
    location.reload();
  } else if (action === 'reset') {
    if (confirm('Clear this device\'s cached progress, session, and sign-in?')) {
      await purgeCaches();
      if ('serviceWorker' in navigator) {
        for (const reg of await navigator.serviceWorker.getRegistrations()) await reg.unregister();
      }
      localStorage.clear();
      location.reload();
    }
  }
});

/** Read the free-text answer out of the DOM before a re-render throws it away. */
function readResponse(s) {
  const input = document.getElementById('responseInput');
  return input ? input.value : s.draft.response;
}

// Keyboard shortcuts, for studying at the laptop: 1–5 confidence, Enter to reveal, 1/2/3 to grade.
document.addEventListener('keydown', (ev) => {
  if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
  const { parts } = parseHash();
  if (parts[0] !== 'study' || parts[1] !== 'run') return;
  const s = store.loadSession();
  if (!s || s.stage === 'summary') return;
  const typing = ['INPUT', 'TEXTAREA'].includes(document.activeElement?.tagName);

  if (s.stage === 'prompt') {
    if (/^[1-5]$/.test(ev.key) && !typing) {
      s.draft.confidence = CONFIDENCE[Number(ev.key) - 1].v;
      store.saveSession(s);
      render();
      ev.preventDefault();
    } else if (ev.key === 'Enter' && s.draft.confidence !== null && (!typing || ev.shiftKey)) {
      s.draft.response = readResponse(s);
      s.stage = 'reveal';
      store.saveSession(s);
      render();
      ev.preventDefault();
    }
  } else if (/^[1-3]$/.test(ev.key) && !typing) {
    submitGrade(GRADES[Number(ev.key) - 1].g);
    ev.preventDefault();
  }
});

view.addEventListener('input', (ev) => {
  if (ev.target.id === 'searchInput') {
    searchQuery = ev.target.value;
    clearTimeout(view._searchTimer);
    view._searchTimer = setTimeout(() => {
      const at = document.activeElement === ev.target;
      render();
      if (at) {
        const next = document.getElementById('searchInput');
        next?.focus();
        next?.setSelectionRange(next.value.length, next.value.length);
      }
    }, 180);
  }
});

// The tab bar's two rules (see tabMemory): same tab pops to its home, a different tab resumes where
// it was left. The anchors keep their hrefs so they still read as links and open in a new tab on a
// modifier-click; this only takes over the plain tap.
tabbar.addEventListener('click', (ev) => {
  if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return;
  const link = ev.target.closest('.tab');
  if (!link) return;
  ev.preventDefault();

  const tab = link.dataset.tab;
  const { parts } = parseHash();
  const here = parts[0] || 'study';
  const target = tab === here ? `#/${tab}` : (tabMemory.get(tab) || `#/${tab}`);

  if (target === currentPath(parts)) {
    // Already at that tab's home: the second tap is "take me back to the top".
    window.scrollTo(0, 0);
    return;
  }
  // Returning to a tab restores its scroll position, the same as a back-navigation would.
  if (tab !== here) restoreScrollNext = true;
  location.hash = target;
});

// --- swipe back --------------------------------------------------------------
// A rightward swipe on a reading goes back, the way it does in a native app — the ‹ button is a
// small target at the top of a page you're usually scrolled well down.
//
// Deliberately narrow, because a false positive hijacks the page:
//   * only where the back button is showing, so it can never fire on a tab's home;
//   * only for a gesture that is clearly horizontal, so it doesn't trip while scrolling;
//   * never one that starts inside something that scrolls sideways itself (a wide table in a
//     reading) — there the swipe belongs to that element;
//   * never from the left edge strip, which is where iOS runs its own back gesture. Leaving it
//     alone is what stops one swipe popping two entries.
const SWIPE = { minX: 64, maxY: 48, maxMs: 700, edge: 24 };
let swipeStart = null;

/** True if the touch landed in something that scrolls sideways on its own and actually overflows. */
function inSideScroller(target) {
  const box = target?.closest ? target.closest('.table-wrap, pre') : null;
  return !!box && box.scrollWidth > box.clientWidth + 1;
}

view.addEventListener('touchstart', (ev) => {
  // Reset first: a second finger arriving (a pinch) cancels whatever was in progress.
  const t = ev.touches.length === 1 ? ev.touches[0] : null;
  swipeStart = !backBtn.hidden && t && t.clientX >= SWIPE.edge && !inSideScroller(ev.target)
    ? { x: t.clientX, y: t.clientY, at: Date.now() }
    : null;
}, { passive: true });

view.addEventListener('touchend', (ev) => {
  const start = swipeStart;
  swipeStart = null;
  if (!start || ev.changedTouches.length !== 1) return;
  const dx = ev.changedTouches[0].clientX - start.x;
  const dy = Math.abs(ev.changedTouches[0].clientY - start.y);
  if (dx >= SWIPE.minX && dy <= SWIPE.maxY && dx > dy * 2 && Date.now() - start.at <= SWIPE.maxMs) {
    goBack();
  }
}, { passive: true });

backBtn.addEventListener('click', goBack);
syncChip.addEventListener('click', () => { location.hash = '#/you'; });
document.getElementById('citeClose').addEventListener('click', () => { citeSheet.hidden = true; });
citeSheet.addEventListener('click', (ev) => { if (ev.target === citeSheet) citeSheet.hidden = true; });

window.addEventListener('hashchange', () => { citeSheet.hidden = true; render(); });

// Going back should land you where you left, not at the top — leaving a reading to follow a
// wikilink and returning to the top of it is the same annoyance in reverse. popstate only fires on
// an actual history traversal, never on the programmatic `location.hash = …` navigations, which is
// exactly the distinction needed. Both popstate and hashchange fire here and the spec's ordering
// between them isn't worth depending on, so handle either: flag it for a render still to come, and
// apply it directly if render already ran.
window.addEventListener('popstate', () => {
  restoreScrollNext = true;
  const { parts, params } = parseHash();
  const key = viewKey(parts);
  if (key === lastViewKey) {
    if (!params.get('h') && scrollMemory.has(key)) window.scrollTo(0, scrollMemory.get(key));
    restoreScrollNext = false;
  }
});

store.subscribe((what) => {
  updateChip();
  // Only re-render for events that change what's on screen, and never during the prompt stage — a
  // re-render there would drop whatever is half-typed in the textarea.
  const { parts } = parseHash();
  if (what === 'readings' && parts[0] === 'read') render();
  if (what === 'sync' && parts[0] === 'you') render();
  // The reveal stage shows the source reading. If the readings finished downloading while the first
  // item was on screen, fill it in — safe here because the answer is already captured in the draft.
  if (what === 'readings' && parts[0] === 'study' && parts[1] === 'run'
      && store.loadSession()?.stage === 'reveal') render();
});

// ---------------------------------------------------------------- boot

const BUILD_KEY = 'psych.build.v1';

/** The deployed build id, or null if the network couldn't answer.
 *
 *  Deliberately compared against a *stored* id rather than anything baked into this file: the whole
 *  problem is that running code can't tell it's old. `build` in version.json covers the shell as
 *  well as the content (see build_hash in apps/build_web.py), so a restyled chart bumps it just as a
 *  new unit does. The earlier check only compared the *content* hash, which meant a code-only deploy
 *  reported "already current" forever. */
async function fetchBuild(timeoutMs = 4000) {
  const abort = new AbortController();
  const timer = setTimeout(() => abort.abort(), timeoutMs);
  try {
    const res = await fetch(new URL('content/version.json', import.meta.url).href,
                            { cache: 'no-store', signal: abort.signal });
    if (!res.ok) return null;
    return (await res.json()).build || null;
  } catch {
    return null;                        // offline, or slow — carry on with what's cached
  } finally {
    clearTimeout(timer);
  }
}

async function purgeCaches() {
  if (!('caches' in window)) return;
  for (const name of await caches.keys()) await caches.delete(name);
}

/** Adopt a newly deployed build: drop the caches and reload, once. Returns true if a reload is
 *  under way, so the caller can stop rather than render a page that's about to be replaced. */
async function adoptNewBuild() {
  const build = await fetchBuild();
  if (!build) return false;
  const seen = localStorage.getItem(BUILD_KEY);
  if (seen === build) return false;
  // Record before reloading. If the reload somehow still lands on stale code, this is what stops it
  // becoming a reload loop — the app stays stale until the next deploy instead of thrashing.
  localStorage.setItem(BUILD_KEY, build);
  if (seen === null) return false;      // first run on this device; nothing to replace
  await purgeCaches();
  location.reload();
  return true;
}

async function boot() {
  updateChip();
  // Before anything renders: if a newer build is deployed, drop the caches and reload into it.
  // Bounded by a timeout inside fetchBuild, so a slow connection delays the app by seconds at worst
  // and an absent one not at all.
  if (await adoptNewBuild()) return;
  try {
    await store.loadItems();
  } catch (err) {
    view.innerHTML = `<div class="banner banner-bad">Couldn't load the item bank: ${esc(err.message)}.
      Run <code>python apps/build_items.py &amp;&amp; python apps/build_web.py</code> and redeploy.</div>`;
    return;
  }
  render();

  // Readings in the background so the Read tab is instant once you get there.
  store.loadReadings();

  if (api.configured && api.signedIn()) {
    store.sync().then(() => { if (parseHash().parts[0] !== 'study') render(); });
  }

  if ('serviceWorker' in navigator) {
    try {
      // updateViaCache: 'none' keeps the worker script itself out of the HTTP cache, so a deploy is
      // noticed on the next visit rather than up to ten minutes later.
      await navigator.serviceWorker.register(new URL('sw.js', import.meta.url).href,
                                             { updateViaCache: 'none' });
    } catch { /* offline support is a bonus, never a requirement */ }
  }
}

boot();
