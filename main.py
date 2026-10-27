"""Incident timeline builder: sorted timeline from CSV events with gaps."""
import argparse
import csv
import datetime
import sys


def build(csv_path):
    events = []
    with open(csv_path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            ts = datetime.datetime.fromisoformat(row["timestamp"])
            events.append({"timestamp": ts, "description": row.get("description", ""),
                           "actor": row.get("actor", "")})
    events.sort(key=lambda e: e["timestamp"])
    timeline = []
    prev = None
    for e in events:
        gap = None if prev is None else round((e["timestamp"] - prev).total_seconds() / 60, 1)
        timeline.append({**e, "gap_minutes": gap})
        prev = e["timestamp"]
    return timeline


def render(timeline):
    lines = []
    for e in timeline:
        gap = "start" if e["gap_minutes"] is None else f"+{e['gap_minutes']} min"
        lines.append(f"{e['timestamp'].isoformat()}  [{gap}]  {e['actor']}: {e['description']}")
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(description="Build a sorted incident timeline.")
    p.add_argument("--csv", required=True)
    args = p.parse_args(argv)
    print(render(build(args.csv)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
