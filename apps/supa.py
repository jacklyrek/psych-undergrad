#!/usr/bin/env python3
"""Supabase client for the local Python side. Stdlib only (urllib) — no `pip install supabase`.

The web app and this module talk to the same two tables (supabase/schema.sql), which is what makes
the phone and the laptop share one queue: grade an item on the train, and the Streamlit runner at
home already knows it isn't due.

Credentials come from a `.env` at the repo root (gitignored) or from real environment variables,
which win:

    SUPABASE_URL=https://<project>.supabase.co
    SUPABASE_ANON_KEY=eyJ...          # the public anon key, same one docs/config.js uses
    SUPABASE_EMAIL=you@example.com
    SUPABASE_PASSWORD=...

Deliberately *not* the service_role key. Signing in as the ordinary user means row-level security
applies here exactly as it does on the phone, so a bug in this file cannot reach anything the phone
couldn't, and there's no key on disk that bypasses the policies.

Offline is normal, not an error: attempts that can't be sent are appended to .supabase-outbox.jsonl
and go out on the next successful call.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
OUTBOX = ROOT / ".supabase-outbox.jsonl"

TIMEOUT = 25


class OfflineError(RuntimeError):
    """The request never reached Supabase — queue and retry rather than fail."""


class SupabaseError(RuntimeError):
    """Supabase answered, and said no."""


# ---------------------------------------------------------------- config

def load_env() -> dict[str, str]:
    """Parse .env, then let real environment variables override it."""
    values: dict[str, str] = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            values[key.strip()] = val.strip().strip("'\"")
    for key in ("SUPABASE_URL", "SUPABASE_ANON_KEY", "SUPABASE_EMAIL", "SUPABASE_PASSWORD"):
        if os.environ.get(key):
            values[key] = os.environ[key]
    return values


REQUIRED = ("SUPABASE_URL", "SUPABASE_ANON_KEY", "SUPABASE_EMAIL", "SUPABASE_PASSWORD")


def configured() -> bool:
    env = load_env()
    return all(env.get(k) for k in REQUIRED)


def missing_keys() -> list[str]:
    env = load_env()
    return [k for k in REQUIRED if not env.get(k)]


# ---------------------------------------------------------------- client

class Client:
    """One signed-in session. Construct it once per script run; the token lasts an hour."""

    def __init__(self, env: dict[str, str] | None = None):
        env = env or load_env()
        missing = [k for k in REQUIRED if not env.get(k)]
        if missing:
            raise SupabaseError(
                f"Supabase is not configured — missing {', '.join(missing)}. "
                f"Add them to {ENV_FILE.name} (see supabase/schema.sql and docs/README.md).")
        self.url = env["SUPABASE_URL"].rstrip("/")
        self.anon_key = env["SUPABASE_ANON_KEY"]
        self.email = env["SUPABASE_EMAIL"]
        self._password = env["SUPABASE_PASSWORD"]
        self.access_token: str | None = None
        self.user_id: str | None = None

    # ---- plumbing

    def _request(self, url: str, method: str = "GET", body=None,
                 headers: dict[str, str] | None = None):
        data = json.dumps(body).encode("utf-8") if body is not None else None
        hdrs = {"apikey": self.anon_key, "Content-Type": "application/json"}
        if self.access_token:
            hdrs["Authorization"] = f"Bearer {self.access_token}"
        hdrs.update(headers or {})
        req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as res:
                raw = res.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as err:
            detail = err.read().decode("utf-8", "replace")[:400]
            raise SupabaseError(f"{method} {url.split('/rest/v1')[-1] or url} → "
                                f"{err.code} {detail}") from err
        except urllib.error.URLError as err:
            raise OfflineError(str(err.reason)) from err
        except TimeoutError as err:
            raise OfflineError("timed out") from err

    def sign_in(self) -> str:
        data = self._request(f"{self.url}/auth/v1/token?grant_type=password", "POST",
                             {"email": self.email, "password": self._password})
        self.access_token = data["access_token"]
        self.user_id = data.get("user", {}).get("id")
        return self.user_id

    def _rest(self, path: str, method: str = "GET", body=None, prefer: str | None = None):
        headers = {"Prefer": prefer} if prefer else None
        return self._request(f"{self.url}/rest/v1{path}", method, body, headers)

    # ---- state

    STATE_COLUMNS = "item_id,ease,interval_days,reps,due_date,last_reviewed,updated_at"

    def pull_state(self) -> dict[str, dict]:
        """Remote state, keyed by item id, in review_state.json's local shape."""
        rows = self._rest(f"/review_state?select={self.STATE_COLUMNS}") or []
        return {r["item_id"]: {"ease": r["ease"], "interval": r["interval_days"],
                               "reps": r["reps"], "due": r["due_date"],
                               "last": r["last_reviewed"], "_updated": r["updated_at"]}
                for r in rows}

    def push_state(self, state: dict[str, dict], chunk: int = 500) -> int:
        """Upsert local state. Chunked because a single 712-row body is needlessly large and a
        partial failure is easier to reason about in batches."""
        rows = [{"item_id": item_id, "ease": st["ease"], "interval_days": st["interval"],
                 "reps": st["reps"], "due_date": st["due"], "last_reviewed": st.get("last")}
                for item_id, st in state.items()]
        sent = 0
        for i in range(0, len(rows), chunk):
            batch = rows[i:i + chunk]
            self._rest("/review_state", "POST", batch,
                       prefer="resolution=merge-duplicates,return=minimal")
            sent += len(batch)
        return sent

    # ---- log

    LOG_COLUMNS = ("ts,item_id,type,bloom_level,cluster,predicted_confidence,outcome,"
                   "interval_before,interval_after,ease,reps,time_taken_s,client")

    def pull_log(self, limit: int = 100000) -> list[dict]:
        return self._rest(f"/review_log?select={self.LOG_COLUMNS}&order=ts.asc&limit={limit}") or []

    def push_log(self, rows: list[dict], chunk: int = 500) -> int:
        """Insert attempts, ignoring ones already present. Idempotent thanks to the
        (user_id, item_id, ts) unique constraint, so re-running a seed is safe."""
        sent = 0
        for i in range(0, len(rows), chunk):
            batch = rows[i:i + chunk]
            self._rest("/review_log?on_conflict=user_id,item_id,ts", "POST", batch,
                       prefer="resolution=ignore-duplicates,return=minimal")
            sent += len(batch)
        return sent

    # ---- one attempt

    def record_attempt(self, attempt: dict) -> None:
        """Advance state and append the attempt atomically — see record_attempt in schema.sql."""
        self._rest("/rpc/record_attempt", "POST", {
            "p_item_id": attempt["item_id"],
            "p_outcome": attempt["outcome"],
            "p_ease": attempt["ease"],
            "p_interval_days": attempt["interval_after"],
            "p_reps": attempt["reps"],
            "p_due_date": attempt["due"],
            "p_last_reviewed": attempt.get("last"),
            "p_ts": attempt["ts"],
            "p_type": attempt.get("type"),
            "p_bloom_level": attempt.get("bloom_level"),
            "p_cluster": attempt.get("cluster") or None,
            "p_predicted_confidence": attempt.get("predicted_confidence"),
            "p_interval_before": attempt.get("interval_before"),
            "p_time_taken_s": attempt.get("time_taken_s"),
            "p_client": attempt.get("client", "streamlit"),
        }, prefer="return=minimal")


# ---------------------------------------------------------------- timestamps

def to_utc_iso(stamp: str) -> str:
    """Local naive timestamp (what review_log.csv holds) -> an explicit offset.

    review_log.csv rows were written by datetime.now(), i.e. local wall clock with no zone. Postgres
    would read a naive string as UTC, silently shifting every historical attempt by the local offset
    and moving some of them across a date boundary — which would corrupt the streak and activity
    views. So stamp the local zone on explicitly."""
    dt = datetime.fromisoformat(stamp)
    if dt.tzinfo is None:
        dt = dt.astimezone()
    return dt.isoformat()


def to_local_naive(stamp: str) -> str:
    """The inverse, for writing pulled rows back into review_log.csv in its original format."""
    text = stamp.replace("Z", "+00:00")
    # Postgres returns fractional seconds of varying width; datetime wants 3 or 6 digits.
    if "." in text:
        head, _, tail = text.partition(".")
        digits = "".join(c for c in tail if c.isdigit())
        rest = tail[len(digits):]
        text = f"{head}.{digits[:6].ljust(6, '0')}{rest}"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is not None:
        dt = dt.astimezone().replace(tzinfo=None)
    return dt.isoformat(timespec="seconds")


# ---------------------------------------------------------------- outbox

def outbox_append(attempt: dict) -> None:
    with OUTBOX.open("a", encoding="utf-8") as f:
        f.write(json.dumps(attempt, ensure_ascii=False) + "\n")


def outbox_read() -> list[dict]:
    if not OUTBOX.exists():
        return []
    out = []
    for line in OUTBOX.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def outbox_clear() -> None:
    OUTBOX.unlink(missing_ok=True)


def flush_outbox(client: Client) -> tuple[int, int]:
    """Send everything queued while offline. Returns (sent, still_queued). Stops at the first
    failure and keeps the remainder, because two attempts on one item must land in order."""
    pending = outbox_read()
    if not pending:
        return 0, 0
    sent = 0
    try:
        for attempt in pending:
            client.record_attempt(attempt)
            sent += 1
    except (OfflineError, SupabaseError):
        pass
    remaining = pending[sent:]
    if remaining:
        OUTBOX.write_text("".join(json.dumps(a, ensure_ascii=False) + "\n" for a in remaining),
                          encoding="utf-8")
    else:
        outbox_clear()
    return sent, len(remaining)


# ---------------------------------------------------------------- CLI smoke test

if __name__ == "__main__":
    import sys

    if not configured():
        sys.exit(f"Not configured — missing {', '.join(missing_keys())}. "
                 f"See the module docstring and docs/README.md.")
    c = Client()
    try:
        uid = c.sign_in()
    except SupabaseError as err:
        sys.exit(f"Sign-in failed: {err}")
    except OfflineError as err:
        sys.exit(f"Offline: {err}")
    state = c.pull_state()
    log = c.pull_log(limit=1)
    queued = len(outbox_read())
    print(f"Connected to {c.url}")
    print(f"  user       {c.email} ({uid})")
    print(f"  remote     {len(state)} state rows, log {'non-empty' if log else 'empty'}")
    print(f"  outbox     {queued} attempt(s) waiting locally")
