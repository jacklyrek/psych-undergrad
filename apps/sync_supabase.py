#!/usr/bin/env python3
"""Move scheduler state and attempt history between the local files and Supabase.

Day to day you never need this: the Streamlit runner syncs on launch (scheduler.sync_down) and pushes
each grade as you make it, and the phone does the same. This is for the three moments outside that
loop — seeding Supabase with the history that predates it, pulling a fresh snapshot back into git,
and looking at why sync isn't doing what you expect.

    python apps/sync_supabase.py status         what's here, what's there, what's stuck
    python apps/sync_supabase.py push           seed Supabase from the local files (idempotent)
    python apps/sync_supabase.py pull           overwrite the local files from Supabase
    python apps/sync_supabase.py flush          send attempts queued while offline

`push` is safe to re-run: review_log rows are deduplicated on (user_id, item_id, ts) by the unique
constraint in schema.sql, and review_state is upserted per item. `pull` overwrites review_state.json
and review_log.csv, which git tracks — so it asks first unless you pass --yes.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scheduler as sch  # noqa: E402
import supa  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# review_log.csv columns that are numbers, and how to read them back off a CSV row.
NUMERIC = {"predicted_confidence": int, "interval_before": int, "interval_after": int,
           "ease": float, "reps": int, "time_taken_s": float}


def connect() -> supa.Client:
    if not supa.configured():
        sys.exit(f"Supabase isn't configured — missing {', '.join(supa.missing_keys())}.\n"
                 f"Add them to {supa.ENV_FILE.name} at the repo root; see docs/README.md.")
    client = supa.Client()
    try:
        client.sign_in()
    except supa.OfflineError as err:
        sys.exit(f"Offline — can't reach {client.url} ({err}).")
    except supa.SupabaseError as err:
        sys.exit(f"Sign-in failed: {err}\n"
                 f"Check SUPABASE_EMAIL / SUPABASE_PASSWORD, and that the user exists in the "
                 f"Supabase dashboard under Authentication → Users.")
    return client


def read_local_log() -> list[dict]:
    """review_log.csv -> Supabase row dicts, with the timestamps given an explicit zone."""
    path = sch.REVIEW_LOG
    if not path.exists():
        return []
    rows: list[dict] = []
    with path.open(encoding="utf-8") as f:
        for raw in csv.DictReader(f):
            row = {"ts": supa.to_utc_iso(raw["timestamp"]),
                   "item_id": raw["item_id"],
                   "type": raw.get("type") or None,
                   "bloom_level": raw.get("bloom_level") or None,
                   "cluster": raw.get("cluster") or None,
                   "outcome": raw["outcome"],
                   "client": "streamlit"}
            for key, cast in NUMERIC.items():
                value = raw.get(key)
                try:
                    row[key] = cast(value) if value not in (None, "") else None
                except ValueError:
                    row[key] = None
            rows.append(row)
    return rows


# ---------------------------------------------------------------- commands

def cmd_status(args) -> None:
    local_state = sch.load_state()
    local_log = read_local_log()
    queued = supa.outbox_read()

    print("Local")
    print(f"  review_state.json   {len(local_state)} items")
    print(f"  review_log.csv      {len(local_log)} attempts")
    print(f"  outbox              {len(queued)} attempt(s) waiting to upload")

    if not supa.configured():
        print(f"\nSupabase: not configured — missing {', '.join(supa.missing_keys())}")
        print("  Everything still works locally; the phone just won't share this queue.")
        return

    client = connect()
    remote_state = client.pull_state()
    remote_log = client.pull_log()
    print(f"\nSupabase ({client.url})")
    print(f"  user                {client.email}")
    print(f"  review_state        {len(remote_state)} items")
    print(f"  review_log          {len(remote_log)} attempts")

    only_local = set(local_state) - set(remote_state)
    only_remote = set(remote_state) - set(local_state)
    differing = [k for k in set(local_state) & set(remote_state)
                 if {f: local_state[k].get(f) for f in ("ease", "interval", "reps", "due")}
                 != {f: remote_state[k].get(f) for f in ("ease", "interval", "reps", "due")}]
    print("\nDifference")
    print(f"  only local          {len(only_local)}")
    print(f"  only remote         {len(only_remote)}")
    print(f"  differing           {len(differing)}")
    if len(remote_log) < len(local_log):
        print(f"\n  {len(local_log) - len(remote_log)} local attempts aren't in Supabase yet — "
              f"run `python apps/sync_supabase.py push`.")
    elif differing or only_local:
        print("\n  Run `push` to send local progress, or `pull` to take Supabase's version.")
    else:
        print("\n  In step.")


def cmd_push(args) -> None:
    client = connect()
    state = sch.load_state()
    log = read_local_log()
    if not state and not log:
        sys.exit("Nothing local to push.")

    print(f"Pushing {len(state)} state rows and {len(log)} attempts to {client.url} …")
    sent_state = client.push_state(state)
    sent_log = client.push_log(log)
    remote_log = client.pull_log()
    print(f"  review_state  {sent_state} rows upserted")
    print(f"  review_log    {sent_log} rows offered, {len(remote_log)} now stored "
          f"(duplicates ignored)")
    print("Done — the phone will pick this up on its next sync.")


def cmd_pull(args) -> None:
    client = connect()
    remote_state = client.pull_state()
    remote_log = client.pull_log()
    if not remote_state and not remote_log:
        sys.exit("Supabase has no rows yet — did you mean `push`?")

    if not args.yes:
        print(f"This overwrites review_state.json ({len(sch.load_state())} items) and "
              f"review_log.csv with Supabase's {len(remote_state)} items / {len(remote_log)} "
              f"attempts.\nBoth files are tracked by git, so `git checkout` undoes it.")
        if input("Continue? [y/N] ").strip().lower() not in ("y", "yes"):
            sys.exit("Cancelled.")

    state = {item_id: {k: st[k] for k in ("ease", "interval", "reps", "due", "last")}
             for item_id, st in remote_state.items()}
    sch.save_state(state)

    with sch.REVIEW_LOG.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=sch.LOG_FIELDS)
        writer.writeheader()
        for row in remote_log:
            writer.writerow({
                "timestamp": supa.to_local_naive(row["ts"]),
                "item_id": row["item_id"],
                "type": row.get("type") or "",
                "bloom_level": row.get("bloom_level") or "",
                "cluster": row.get("cluster") or "",
                "predicted_confidence": row.get("predicted_confidence") if row.get("predicted_confidence") is not None else "",
                "outcome": row["outcome"],
                "interval_before": row.get("interval_before") if row.get("interval_before") is not None else "",
                "interval_after": row.get("interval_after") if row.get("interval_after") is not None else "",
                "ease": row.get("ease") if row.get("ease") is not None else "",
                "reps": row.get("reps") if row.get("reps") is not None else "",
                "time_taken_s": row.get("time_taken_s") if row.get("time_taken_s") is not None else "",
            })

    print(f"Wrote {len(state)} items to review_state.json and {len(remote_log)} attempts to "
          f"review_log.csv.")


def cmd_flush(args) -> None:
    queued = supa.outbox_read()
    if not queued:
        print("Outbox is empty — nothing was queued offline.")
        return
    client = connect()
    sent, remaining = supa.flush_outbox(client)
    print(f"Sent {sent} of {len(queued)} queued attempt(s).")
    if remaining:
        print(f"  {remaining} still queued — run again when the connection is better.")


# ---------------------------------------------------------------- main

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Run with no command for `status`.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="compare local files with Supabase")
    sub.add_parser("push", help="seed Supabase from the local files (idempotent)")
    pull = sub.add_parser("pull", help="overwrite the local files from Supabase")
    pull.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    sub.add_parser("flush", help="send attempts queued while offline")

    args = parser.parse_args()
    {"status": cmd_status, "push": cmd_push, "pull": cmd_pull,
     "flush": cmd_flush}[args.command or "status"](args)


if __name__ == "__main__":
    main()
