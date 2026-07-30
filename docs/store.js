// Content loading, local persistence, and sync orchestration.
//
// Offline-first by design, because the point of this app is studying on a phone with no signal.
// Everything is written to localStorage the instant you grade an item and the attempt goes onto a
// durable queue; the network is a background concern that drains the queue when it can. Supabase is
// the source of truth *across devices*, never a prerequisite for using the app.
//
// Conflict rule: last write wins per item, using a modification clock (`u`) on each local record
// against the server's updated_at — except that an item with an unflushed attempt in the queue is
// never overwritten by a pull. Two devices can only disagree if both studied the same item while
// offline, which for one person with one phone and one laptop is not a real scenario.

import * as sm2 from './sm2.js';
import * as api from './supabase.js';

const KEY = {
  state: 'psych.state.v1',
  queue: 'psych.queue.v1',
  log: 'psych.log.v1',
  session: 'psych.studysession.v1',
  contentVersion: 'psych.contentversion.v1',
  lastSync: 'psych.lastsync.v1',
};

const url = (rel) => new URL(rel, import.meta.url).href;

// ---------------------------------------------------------------- in-memory content

export const content = {
  items: [],
  itemsById: new Map(),
  pages: [],
  pagesBySlug: new Map(),
  version: null,
  readingsLoaded: false,
  readingsError: null,
};

export const status = {
  online: navigator.onLine,
  syncing: false,
  lastSync: readJSON(KEY.lastSync, null),
  queued: 0,
  error: null,
  needsSignIn: false,
};

let state = readJSON(KEY.state, {});
let queue = readJSON(KEY.queue, []);
let log = readJSON(KEY.log, []);
status.queued = queue.length;

// ---------------------------------------------------------------- tiny event bus

const listeners = new Set();
export function subscribe(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}
function emit(what = 'change') {
  for (const fn of listeners) fn(what);
}

function readJSON(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw === null ? fallback : JSON.parse(raw);
  } catch {
    return fallback;
  }
}

function writeJSON(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (err) {
    // Quota or Private Browsing. Progress still syncs; only the offline cache is lost.
    status.error = `couldn't save locally (${err.name}) — progress still syncs when online`;
  }
}

// ---------------------------------------------------------------- content

/** Items first: the study loop only needs these, so the app is usable before the 2 MB of readings
 *  has finished arriving. */
export async function loadItems() {
  const res = await fetch(url('content/items.json'));
  if (!res.ok) throw new Error(`items.json → ${res.status}`);
  const payload = await res.json();
  content.items = payload.items;
  content.version = payload.version;
  content.itemsById = new Map(payload.items.map((it) => [it.id, it]));

  sm2.ensureState(content.items, state, sm2.todayISO());
  persistState();

  const known = readJSON(KEY.contentVersion, null);
  if (known !== payload.version) writeJSON(KEY.contentVersion, payload.version);
  emit('items');
  return content.items;
}

/** Readings load in the background — 123 pages of pre-rendered HTML. */
export async function loadReadings() {
  if (content.readingsLoaded) return content.pages;
  try {
    const res = await fetch(url('content/readings.json'));
    if (!res.ok) throw new Error(`readings.json → ${res.status}`);
    const payload = await res.json();
    content.pages = payload.pages;
    content.pagesBySlug = new Map(payload.pages.map((p) => [p.slug, p]));
    content.readingsLoaded = true;
    content.readingsError = null;
  } catch (err) {
    content.readingsError = err.message;
  }
  emit('readings');
  return content.pages;
}

/** An item's source_page ("wiki/concept-empathy.md") as a bundled page. */
export function pageForItem(item) {
  const slug = String(item.source_page).replace(/^.*\//, '').replace(/\.md$/, '');
  return content.pagesBySlug.get(slug) || null;
}

// ---------------------------------------------------------------- state

export function getState() {
  return state;
}

function persistState() {
  writeJSON(KEY.state, state);
}

export function itemState(id) {
  return state[id];
}

/** Apply a grade: advance SM-2 locally, log it, queue it for Supabase, and try to flush now.
 *  Returns the scheduling result so the UI can say "back in 6 days". */
export function grade(item, outcome, { confidence, timeTaken, response } = {}) {
  const today = sm2.todayISO();
  if (!state[item.id]) state[item.id] = sm2.newState(today);

  const { before, after } = sm2.update(state, item.id, outcome, today);
  const st = state[item.id];
  st.u = Date.now();
  persistState();

  const attempt = {
    ts: new Date().toISOString(),
    item_id: item.id,
    type: item.type,
    bloom_level: item.bloom_level,
    cluster: item.cluster || '',
    predicted_confidence: confidence ?? null,
    outcome,
    interval_before: before,
    interval_after: after,
    ease: st.ease,
    reps: st.reps,
    time_taken_s: timeTaken ?? null,
    due: st.due,
    last: st.last,
    client: 'web',
  };

  // Optimistic: the local log powers Stats immediately, before any round trip.
  log.unshift(attempt);
  writeJSON(KEY.log, log.slice(0, 5000));

  queue.push(attempt);
  writeJSON(KEY.queue, queue);
  status.queued = queue.length;
  emit('graded');

  flush().catch(() => { /* queued; a later flush or the next app open will carry it */ });
  return { before, after, due: st.due, ease: st.ease, reps: st.reps, response };
}

// ---------------------------------------------------------------- sync

function mergeState(local, remote, protectedIds) {
  const out = {};
  for (const id of new Set([...Object.keys(local), ...Object.keys(remote)])) {
    const l = local[id];
    const r = remote[id];
    if (!r) { out[id] = l; continue; }
    if (!l) { out[id] = { ...r }; continue; }
    // An attempt still waiting to be pushed always wins: the server simply hasn't heard it yet.
    if (protectedIds.has(id)) { out[id] = l; continue; }
    out[id] = (l.u ?? 0) > (r.u ?? 0) ? l : { ...r };
  }
  return out;
}

/** Drain the queued attempts, oldest first. Stops at the first failure and keeps the rest queued —
 *  order matters, since two attempts on one item must land in sequence. */
export async function flush() {
  if (!api.configured || !api.signedIn() || !queue.length || status.syncing) return;
  status.syncing = true;
  emit('sync');
  try {
    while (queue.length) {
      await api.recordAttempt(queue[0]);
      queue.shift();
      writeJSON(KEY.queue, queue);
      status.queued = queue.length;
      emit('sync');
    }
    status.error = null;
  } catch (err) {
    handleSyncError(err);
  } finally {
    status.syncing = false;
    emit('sync');
  }
}

/** Full reconcile: push what's pending, pull the authoritative state and log, merge. Called on
 *  boot, on regaining connectivity, and from the You tab. */
export async function sync({ pullLog: withLog = true } = {}) {
  if (!api.configured || !api.signedIn()) return;
  status.syncing = true;
  status.error = null;
  emit('sync');
  try {
    if (queue.length) {
      while (queue.length) {
        await api.recordAttempt(queue[0]);
        queue.shift();
        writeJSON(KEY.queue, queue);
        status.queued = queue.length;
      }
    }

    const remote = await api.pullState();
    const pending = new Set(queue.map((a) => a.item_id));
    state = mergeState(state, remote, pending);
    if (content.items.length) sm2.ensureState(content.items, state, sm2.todayISO());
    persistState();

    if (withLog) {
      const rows = await api.pullLog();
      // The server's log is authoritative and already contains everything we pushed.
      log = rows;
      writeJSON(KEY.log, log.slice(0, 5000));
    }

    status.lastSync = new Date().toISOString();
    writeJSON(KEY.lastSync, status.lastSync);
    status.needsSignIn = false;
  } catch (err) {
    handleSyncError(err);
  } finally {
    status.syncing = false;
    emit('sync');
  }
}

function handleSyncError(err) {
  if (err instanceof api.OfflineError) {
    status.online = false;
    status.error = null;          // being offline is a normal state, not an error to report
  } else if (err instanceof api.AuthError) {
    status.needsSignIn = true;
    status.error = err.message;
  } else {
    status.error = err.message;
  }
}

export function getLog() {
  return log;
}

/** Called after signing in: adopt the server's state and history. */
export async function afterSignIn() {
  status.needsSignIn = false;
  await sync();
}

/** Called after signing out: keep studying locally, drop the borrowed history. */
export function afterSignOut() {
  log = [];
  writeJSON(KEY.log, log);
  status.lastSync = null;
  writeJSON(KEY.lastSync, null);
  emit('sync');
}

// ---------------------------------------------------------------- study session persistence

// iOS discards backgrounded tabs aggressively. Answering the phone mid-session shouldn't cost you
// the session, so it round-trips through localStorage.
export function saveSession(session) {
  writeJSON(KEY.session, session);
}
export function loadSession() {
  return readJSON(KEY.session, null);
}
export function clearSession() {
  try {
    localStorage.removeItem(KEY.session);
  } catch { /* nothing to clean up */ }
}

// ---------------------------------------------------------------- connectivity

window.addEventListener('online', () => {
  status.online = true;
  emit('sync');
  sync({ pullLog: false }).catch(() => {});
});
window.addEventListener('offline', () => {
  status.online = false;
  emit('sync');
});
