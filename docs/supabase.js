// Supabase client — auth + the four calls this app makes. Hand-rolled over fetch.
//
// Why not supabase-js: it would have to be vendored in (there is no npm on the machine that builds
// this), it is ~40 KB over the wire for a phone, and this app needs exactly one auth flow and four
// endpoints. PostgREST and GoTrue are plain HTTP, so the whole client is below.
//
// Auth is email + password against a user created by hand in the Supabase dashboard
// (Authentication → Users → Add user). Magic links would mean bouncing to Mail on every expiry and
// they're rate-limited on the free tier; a password lands in the iOS keychain once and is done.

import { SUPABASE_URL, SUPABASE_ANON_KEY } from './config.js';

const SESSION_KEY = 'psych.session.v1';
const REFRESH_MARGIN_S = 120;   // refresh a token this long before it actually expires

export const configured = Boolean(SUPABASE_URL && SUPABASE_ANON_KEY);

/** Thrown when the request never reached Supabase, so the caller knows to queue instead of fail. */
export class OfflineError extends Error {}
/** Thrown when Supabase rejected the credentials — the caller should ask for a fresh sign-in. */
export class AuthError extends Error {}

let session = readSession();

function readSession() {
  try {
    return JSON.parse(localStorage.getItem(SESSION_KEY)) || null;
  } catch {
    return null;
  }
}

function writeSession(next) {
  session = next;
  if (next) localStorage.setItem(SESSION_KEY, JSON.stringify(next));
  else localStorage.removeItem(SESSION_KEY);
}

export function currentUser() {
  return session ? { id: session.user_id, email: session.email } : null;
}

export function signedIn() {
  return Boolean(session?.refresh_token);
}

function storeTokens(data) {
  writeSession({
    access_token: data.access_token,
    refresh_token: data.refresh_token,
    expires_at: Math.floor(Date.now() / 1000) + (data.expires_in ?? 3600),
    user_id: data.user?.id ?? session?.user_id,
    email: data.user?.email ?? session?.email,
  });
}

async function post(path, body, extraHeaders = {}) {
  let res;
  try {
    res = await fetch(`${SUPABASE_URL}${path}`, {
      method: 'POST',
      headers: { apikey: SUPABASE_ANON_KEY, 'Content-Type': 'application/json', ...extraHeaders },
      body: JSON.stringify(body),
    });
  } catch (err) {
    throw new OfflineError(err.message);
  }
  return res;
}

// ---------------------------------------------------------------- auth

export async function signIn(email, password) {
  if (!configured) throw new Error('Supabase is not configured — see docs/config.js.');
  const res = await post('/auth/v1/token?grant_type=password', { email, password });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new AuthError(data.error_description || data.msg || data.message || `sign-in failed (${res.status})`);
  }
  storeTokens(data);
  return currentUser();
}

export async function signOut() {
  // Best-effort server-side revoke; the local session goes regardless, including when offline.
  if (session?.access_token) {
    try {
      await post('/auth/v1/logout', {}, { Authorization: `Bearer ${session.access_token}` });
    } catch { /* offline: dropping the local session is still the right outcome */ }
  }
  writeSession(null);
}

async function refresh() {
  const res = await post('/auth/v1/token?grant_type=refresh_token',
                         { refresh_token: session.refresh_token });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    // A rejected refresh token is unrecoverable — the only fix is signing in again.
    writeSession(null);
    throw new AuthError(data.error_description || 'session expired — sign in again');
  }
  storeTokens(data);
}

async function accessToken() {
  if (!session) throw new AuthError('not signed in');
  if (session.expires_at - REFRESH_MARGIN_S <= Math.floor(Date.now() / 1000)) await refresh();
  return session.access_token;
}

// ---------------------------------------------------------------- data

async function rest(path, { method = 'GET', body, headers = {} } = {}) {
  const token = await accessToken();
  let res;
  try {
    res = await fetch(`${SUPABASE_URL}/rest/v1${path}`, {
      method,
      headers: {
        apikey: SUPABASE_ANON_KEY,
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
        ...headers,
      },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
  } catch (err) {
    throw new OfflineError(err.message);
  }
  if (res.status === 401 || res.status === 403) {
    throw new AuthError(`not authorised (${res.status})`);
  }
  if (!res.ok) {
    throw new Error(`${method} ${path} → ${res.status} ${(await res.text()).slice(0, 300)}`);
  }
  return res.status === 204 ? null : res.json();
}

const STATE_COLUMNS = 'item_id,ease,interval_days,reps,due_date,last_reviewed,updated_at';

/** Remote scheduler state, in the same shape the app keeps locally.
 *  `u` is the modification clock used to resolve which side is newer (see store.js). */
export async function pullState() {
  const rows = await rest(`/review_state?select=${STATE_COLUMNS}`);
  const out = {};
  for (const r of rows) {
    out[r.item_id] = {
      ease: r.ease,
      interval: r.interval_days,
      reps: r.reps,
      due: r.due_date,
      last: r.last_reviewed,
      u: Date.parse(r.updated_at) || 0,
    };
  }
  return out;
}

/** Recent attempts, newest first — the calibration history behind the Stats tab. */
export async function pullLog(limit = 4000) {
  return rest(`/review_log?select=ts,item_id,type,bloom_level,cluster,predicted_confidence,` +
              `outcome,interval_before,interval_after,ease,reps,time_taken_s,client` +
              `&order=ts.desc&limit=${limit}`);
}

/** Advance one item's state and append its attempt, atomically. See record_attempt in schema.sql. */
export async function recordAttempt(a) {
  return rest('/rpc/record_attempt', {
    method: 'POST',
    body: {
      p_item_id: a.item_id,
      p_outcome: a.outcome,
      p_ease: a.ease,
      p_interval_days: a.interval_after,
      p_reps: a.reps,
      p_due_date: a.due,
      p_last_reviewed: a.last,
      p_ts: a.ts,
      p_type: a.type ?? null,
      p_bloom_level: a.bloom_level ?? null,
      p_cluster: a.cluster || null,
      p_predicted_confidence: a.predicted_confidence ?? null,
      p_interval_before: a.interval_before ?? null,
      p_time_taken_s: a.time_taken_s ?? null,
      p_client: a.client ?? 'web',
    },
  });
}
