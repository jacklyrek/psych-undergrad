// Stats and calibration maths, over the synced attempt log.
//
// This is the "calibration dashboard" CLAUDE.md lists as the third app, and the reason it matters is
// in the learning-science doc: the fluency illusion means feeling sure and being right come apart,
// and the only way to see that is to record a confidence prediction *before* the answer and compare
// it to the outcome afterwards. Both apps already log predicted_confidence, so the data is there.
//
// Pure functions over plain arrays — no DOM, no storage — so they're testable under JavaScriptCore.

import { addDays, daysBetween, todayISO } from './sm2.js';

const CORRECT = 'correct';

/** The local calendar day an attempt happened on.
 *
 *  Not `ts.slice(0, 10)`: Supabase returns timestamptz in UTC, so a session at 9pm Pacific comes
 *  back dated tomorrow. Slicing the string would credit it to the wrong day and break the streak.
 *  Attempts loaded from the local optimistic log carry no offset, which the Date parser reads as
 *  local time — also what we want. */
export function localDay(ts) {
  const d = new Date(ts);
  return Number.isNaN(d.getTime()) ? String(ts).slice(0, 10) : todayISO(d);
}

/** Headline counts. `shaky` deliberately isn't folded into either side: it's a pass that needs
 *  requeueing, and averaging it away hides the shakiness. */
export function summarize(log) {
  const n = log.length;
  const by = { correct: 0, shaky: 0, missed: 0 };
  let seconds = 0;
  for (const a of log) {
    if (by[a.outcome] !== undefined) by[a.outcome] += 1;
    seconds += Number(a.time_taken_s) || 0;
  }
  return {
    attempts: n,
    ...by,
    accuracy: n ? by.correct / n : 0,
    seconds,
    medianSeconds: median(log.map((a) => Number(a.time_taken_s) || 0)),
  };
}

function median(xs) {
  const ys = xs.filter((x) => x > 0).sort((a, b) => a - b);
  if (!ys.length) return 0;
  const mid = Math.floor(ys.length / 2);
  return ys.length % 2 ? ys[mid] : (ys[mid - 1] + ys[mid]) / 2;
}

/** Bucket attempts by the confidence predicted before answering, against how often that band was
 *  actually right. A perfectly calibrated studier tracks the diagonal; the interesting rows are the
 *  high-confidence bands with accuracy well below them. */
export function calibration(log, bucketSize = 20) {
  const buckets = [];
  for (let lo = 0; lo < 100; lo += bucketSize) {
    buckets.push({ lo, hi: Math.min(100, lo + bucketSize), n: 0, correct: 0 });
  }
  for (const a of log) {
    const c = Number(a.predicted_confidence);
    if (!Number.isFinite(c)) continue;
    const idx = Math.min(buckets.length - 1, Math.floor(c / bucketSize));
    buckets[idx].n += 1;
    if (a.outcome === CORRECT) buckets[idx].correct += 1;
  }
  return buckets.map((b) => ({
    ...b,
    accuracy: b.n ? b.correct / b.n : null,
    // Positive = overconfident (felt surer than you were). The midpoint stands in for the band.
    gap: b.n ? ((b.lo + b.hi) / 2) / 100 - b.correct / b.n : null,
  }));
}

/** One number for "how well do you know what you know": mean |predicted − outcome|.
 *  Lower is better; ~0.5 means the prediction carried no information. */
export function brierScore(log) {
  let sum = 0;
  let n = 0;
  for (const a of log) {
    const c = Number(a.predicted_confidence);
    if (!Number.isFinite(c)) continue;
    const actual = a.outcome === CORRECT ? 1 : 0;
    sum += (c / 100 - actual) ** 2;
    n += 1;
  }
  return n ? sum / n : null;
}

/** Attempts you were sure about and still got wrong. The fluency illusion, itemised — these are
 *  worth re-reading rather than just re-drilling. */
export function overconfidentMisses(log, threshold = 70) {
  return log.filter((a) => a.outcome !== CORRECT && Number(a.predicted_confidence) >= threshold);
}

/** Accuracy split by Bloom level. Apply/analyze sitting well below remember is the normal and
 *  informative pattern: definitions are the easy 30%. */
export function byBloom(log, order) {
  const rows = new Map();
  for (const a of log) {
    const key = a.bloom_level || '—';
    const row = rows.get(key) || { bloom: key, n: 0, correct: 0 };
    row.n += 1;
    if (a.outcome === CORRECT) row.correct += 1;
    rows.set(key, row);
  }
  const out = [...rows.values()].map((r) => ({ ...r, accuracy: r.n ? r.correct / r.n : 0 }));
  if (order) out.sort((a, b) => order.indexOf(a.bloom) - order.indexOf(b.bloom));
  return out;
}

/** Weakest clusters by accuracy — the confusable groups still not discriminated.
 *  `min` guards against a cluster looking terrible off two attempts. */
export function weakestClusters(log, { min = 4, limit = 6 } = {}) {
  const rows = new Map();
  for (const a of log) {
    if (!a.cluster) continue;
    const row = rows.get(a.cluster) || { cluster: a.cluster, n: 0, correct: 0 };
    row.n += 1;
    if (a.outcome === CORRECT) row.correct += 1;
    rows.set(a.cluster, row);
  }
  return [...rows.values()]
    .filter((r) => r.n >= min)
    .map((r) => ({ ...r, accuracy: r.correct / r.n }))
    .sort((a, b) => a.accuracy - b.accuracy)
    .slice(0, limit);
}

/** Items coming due over the next `days` days. Shows whether tomorrow is a wall or a trickle.
 *
 *  Today's row splits its count three ways, because "everything due" lumps together two very
 *  different things. `fresh` is items never reviewed — they carry a due date of the day they entered
 *  the bank, so a large backlog of them is just an unstarted bank, not a missed schedule. `overdue`
 *  is the one that should sting: items already in rotation whose review date has passed. Reporting
 *  the union as "overdue" turns an untouched bank into an alarming number. */
export function dueForecast(items, state, today, days = 14) {
  const out = [{ date: today, label: 'today', count: 0, overdue: 0, fresh: 0 }];
  for (let d = 1; d <= days; d++) {
    out.push({ date: addDays(today, d), label: `+${d}`, count: 0, overdue: 0, fresh: 0 });
  }
  const index = new Map(out.map((row, i) => [row.date, i]));

  for (const it of items) {
    const st = state[it.id];
    if (!st) continue;
    if (st.due <= today) {
      out[0].count += 1;
      if (st.reps === 0) out[0].fresh += 1;
      else if (st.due < today) out[0].overdue += 1;
    } else if (index.has(st.due)) {
      out[index.get(st.due)].count += 1;
    }
  }
  return out;
}

/** How the bank is distributed across the pipeline. `new` is the untouched backlog. */
export function pipeline(items, state) {
  const buckets = { new: 0, learning: 0, young: 0, mature: 0 };
  for (const it of items) {
    const st = state[it.id];
    if (!st || st.reps === 0) buckets.new += 1;
    else if (st.interval < 7) buckets.learning += 1;
    else if (st.interval < 30) buckets.young += 1;
    else buckets.mature += 1;
  }
  return buckets;
}

/** Consecutive days with at least one attempt, counting back from today. A day off resets it;
 *  studying earlier today or yesterday both keep it alive. */
export function streak(log, today) {
  const days = new Set(log.map((a) => localDay(a.ts)));
  if (!days.size) return { current: 0, activeDays: 0 };
  let cursor = days.has(today) ? today : addDays(today, -1);
  if (!days.has(cursor)) return { current: 0, activeDays: days.size };
  let current = 0;
  while (days.has(cursor)) {
    current += 1;
    cursor = addDays(cursor, -1);
  }
  return { current, activeDays: days.size };
}

/** Attempts per day over a trailing window, for the activity strip. */
export function activity(log, today, days = 30) {
  const counts = new Map();
  for (const a of log) {
    const d = localDay(a.ts);
    counts.set(d, (counts.get(d) || 0) + 1);
  }
  const out = [];
  for (let i = days - 1; i >= 0; i--) {
    const d = addDays(today, -i);
    out.push({ date: d, count: counts.get(d) || 0 });
  }
  return out;
}

/** Days since the newest attempt — used to caption a stale log honestly. */
export function daysSinceLast(log, today) {
  if (!log.length) return null;
  const newest = log.reduce((m, a) => (String(a.ts) > m ? String(a.ts) : m), '');
  return daysBetween(localDay(newest), today);
}
