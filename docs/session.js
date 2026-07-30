// Session assembly — deciding which items a study session serves, and in what order.
//
// Pure functions, no DOM and no storage, so apps/test_web_logic.py can exercise them directly under
// JavaScriptCore. The rules mirror apps/quiz_runner.py: pull the due set, apply the optional
// focus filters, shuffle to interleave, then truncate to the requested length.

import { dueItems } from './sm2.js';

export const BLOOM_ORDER = ['remember', 'understand', 'apply', 'analyze', 'evaluate'];
export const NO_FILTERS = { units: [], blooms: [], types: [] };

/** Numeric syllabus units in numeric order, then elective modules alphabetically.
 *  Same ordering quiz_runner.py uses, so the two apps list units identically. */
export function unitSortKey(unit) {
  return /^\d+$/.test(unit) ? [0, Number(unit), ''] : [1, 0, unit];
}

export function compareUnits(a, b) {
  const ka = unitSortKey(a);
  const kb = unitSortKey(b);
  return ka[0] - kb[0] || ka[1] - kb[1] || ka[2].localeCompare(kb[2]);
}

/** "Unit 3" for spine units; elective module slugs are already self-describing. */
export function unitLabel(unit) {
  if (unit === undefined || unit === null || unit === '') return '—';
  return /^\d+$/.test(unit) ? `Unit ${unit}` : unit.replace(/^aux-/, '').replace(/-/g, ' ');
}

export function matchesFilters(item, filters) {
  if (filters.units?.length && !filters.units.includes(item.unit)) return false;
  if (filters.blooms?.length && !filters.blooms.includes(item.bloom_level)) return false;
  if (filters.types?.length && !filters.types.includes(item.type)) return false;
  return true;
}

function shuffled(list) {
  const xs = list.slice();
  for (let i = xs.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [xs[i], xs[j]] = [xs[j], xs[i]];
  }
  return xs;
}

/** Item ids for a new session.
 *  cram ignores due dates — useful before an exam, but it is massing, not spacing. */
export function buildQueue(items, state, { filters = NO_FILTERS, length = 15, cram = false,
                                           today, shuffle = true } = {}) {
  const pool = cram
    ? (shuffle ? shuffled(items) : items.slice())
    : dueItems(items, state, today, shuffle);
  return pool.filter((it) => matchesFilters(it, filters)).slice(0, length).map((it) => it.id);
}

/** How many items are due right now, and how many of those survive the current filters — the two
 *  numbers the setup screen shows so a filter that empties the queue is visible before starting. */
export function dueCounts(items, state, filters, today) {
  const due = dueItems(items, state, today, false);
  return { total: items.length, due: due.length,
           inFilter: due.filter((it) => matchesFilters(it, filters)).length };
}

/** Distinct facet values present in the bank, ordered for display. */
export function facets(items) {
  const units = [...new Set(items.map((it) => it.unit).filter(Boolean))].sort(compareUnits);
  const types = [...new Set(items.map((it) => it.type))].sort();
  const blooms = BLOOM_ORDER.filter((b) => items.some((it) => it.bloom_level === b));
  return { units, types, blooms };
}
