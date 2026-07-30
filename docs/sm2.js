// SM-2 spaced repetition — a faithful port of apps/scheduler.py.
//
// This file and scheduler.py must stay in lockstep: the phone and the laptop write to the same
// review_state rows, so if they disagree about what the next interval should be, an item's schedule
// depends on which device you happened to study it on. apps/test_sm2_parity.py enforces the
// agreement by replaying ~40k transitions through both implementations and diffing them — run it
// after touching either side.
//
// Grade -> SM-2 recall quality q, unchanged from the Python:
//     missed  -> q=2  (failed; relearn from interval 1, ease takes a real hit)
//     shaky   -> q=3  (a pass, but requeue soon and grow ease slowly)
//     correct -> q=5  (clean recall; interval expands by the easiness factor)

export const DEFAULT_EASE = 2.5;   // starting easiness factor
export const MIN_EASE = 1.3;       // floor; SM-2 never lets a card get easier-rated than this
export const FIRST_INTERVAL = 1;   // days, after the first successful recall
export const SECOND_INTERVAL = 6;  // days, after the second

export const QUALITY = { missed: 2, shaky: 3, correct: 5 };
export const OUTCOMES = ['missed', 'shaky', 'correct'];

// Legacy Leitner box -> interval in days. Kept only to migrate state written before the SM-2
// upgrade, exactly as scheduler.py does.
const LEGACY_BOX_DAYS = { 1: 1, 2: 3, 3: 7, 4: 16, 5: 35 };

// ---------------------------------------------------------------- rounding

// Python's round() breaks ties to even; JavaScript's Math.round() breaks them upward. That is not
// hypothetical here: a 'shaky' grade computes round(interval / 2), so an interval of 5 becomes 2 in
// Python and would become 3 under Math.round. Python owns the 555 attempts already logged, so the
// port matches Python rather than the other way round.
export function roundHalfEven(x) {
  const floor = Math.floor(x);
  const frac = x - floor;              // exact for doubles in this magnitude range
  if (frac > 0.5) return floor + 1;
  if (frac < 0.5) return floor;
  return floor % 2 === 0 ? floor : floor + 1;
}

// Ease is stored to 3 decimals. Reachable ease values are never exactly halfway at the 4th decimal,
// so plain scaling is safe here and the parity test covers the whole reachable set.
function round3(x) {
  return Math.round(x * 1000) / 1000;
}

// ---------------------------------------------------------------- dates

// Local calendar date, matching Python's date.today(). Deliberately not UTC: at 8pm Pacific, UTC is
// already tomorrow, which would make today's reviews look due tomorrow (or worse, skip a day).
export function todayISO(d = new Date()) {
  const p = (n) => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`;
}

// Integer arithmetic in UTC so adding days can never be perturbed by a DST transition.
export function addDays(iso, days) {
  const [y, m, d] = iso.split('-').map(Number);
  const t = Date.UTC(y, m - 1, d) + days * 86400000;
  const out = new Date(t);
  const p = (n) => String(n).padStart(2, '0');
  return `${out.getUTCFullYear()}-${p(out.getUTCMonth() + 1)}-${p(out.getUTCDate())}`;
}

export function daysBetween(fromISO, toISO) {
  const [y1, m1, d1] = fromISO.split('-').map(Number);
  const [y2, m2, d2] = toISO.split('-').map(Number);
  return Math.round((Date.UTC(y2, m2 - 1, d2) - Date.UTC(y1, m1 - 1, d1)) / 86400000);
}

// ---------------------------------------------------------------- state

export function newState(today) {
  return { ease: DEFAULT_EASE, interval: 0, reps: 0, due: today, last: null };
}

/** Initialise state for new items, migrate legacy box records, drop state for deleted items.
 *  Mirrors scheduler.ensure_state. Mutates and returns `state`. */
export function ensureState(items, state, today = todayISO()) {
  const known = new Set(items.map((it) => it.id));
  for (const it of items) {
    const st = state[it.id];
    if (!st) {
      state[it.id] = newState(today);
    } else if (st.ease === undefined) {
      // pre-upgrade Leitner record: the box's cadence becomes the interval, ease starts at default
      const box = st.box ?? 1;
      delete st.box;
      st.ease = DEFAULT_EASE;
      st.interval = LEGACY_BOX_DAYS[box] ?? FIRST_INTERVAL;
      st.reps ??= 0;
      st.due ??= today;
      st.last ??= null;
    }
  }
  for (const id of Object.keys(state)) {
    if (!known.has(id)) delete state[id];
  }
  return state;
}

/** Items due today or earlier. Shuffled by default — the learning-science doc calls for pulling the
 *  due set and interleaving it rather than serving topic by topic. */
export function dueItems(items, state, today = todayISO(), shuffle = true) {
  const due = items.filter((it) => {
    const st = state[it.id];
    return st && st.due <= today;   // ISO dates compare correctly as strings
  });
  if (shuffle) {
    for (let i = due.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [due[i], due[j]] = [due[j], due[i]];
    }
  }
  return due;
}

/** Apply one SM-2 transition in place. Returns { before, after } interval in days.
 *  Line-for-line equivalent of scheduler.update. */
export function update(state, itemId, outcome, today = todayISO()) {
  const st = state[itemId];
  const intervalBefore = st.interval ?? 0;
  let ease = st.ease ?? DEFAULT_EASE;
  let reps = st.reps ?? 0;
  const q = QUALITY[outcome];
  let interval;

  if (outcome === 'missed') {
    // q<3: failed; relearn from scratch
    reps = 0;
    interval = FIRST_INTERVAL;
  } else if (outcome === 'shaky') {
    // a pass, but requeue soon — don't advance the rep count
    interval = intervalBefore
      ? Math.max(FIRST_INTERVAL, roundHalfEven(intervalBefore * 0.5))
      : FIRST_INTERVAL;
  } else {
    if (reps === 0) interval = FIRST_INTERVAL;
    else if (reps === 1) interval = SECOND_INTERVAL;
    else interval = Math.max(FIRST_INTERVAL, roundHalfEven(intervalBefore * ease));
    reps += 1;
  }

  // SM-2 easiness update — applied on every review, including lapses.
  ease = Math.max(MIN_EASE, ease + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)));

  st.ease = round3(ease);
  st.reps = reps;
  st.interval = interval;
  st.due = addDays(today, interval);
  st.last = today;
  return { before: intervalBefore, after: interval };
}

// ---------------------------------------------------------------- auto-grading

// Python's string.punctuation, character for character. Not a Unicode property class: the items are
// full of typographic apostrophes and em dashes, which Python's ASCII-only set leaves in place, so
// stripping them here would make the two graders disagree on real answers.
const PY_PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~';
const PUNCT_SET = new Set(PY_PUNCTUATION);

export function normalize(text) {
  const lowered = String(text ?? '').toLowerCase().trim();
  let out = '';
  for (const ch of lowered) if (!PUNCT_SET.has(ch)) out += ch;
  return out.replace(/\s+/g, ' ');
}

/** true/false for auto-gradable types, or null when the item needs a self-grade. */
export function autograde(item, response) {
  if (item.type === 'cloze') return normalize(response) === normalize(item.answer);
  if (item.type === 'mcq') {
    // Grade against the exact correct option; `answer` may carry extra explanation that would
    // never match a chosen option. Fall back for legacy items predating the `correct` field.
    return normalize(response) === normalize(item.correct || item.answer);
  }
  return null;
}
