# incident-timeline-builder

Build a sorted incident timeline from CSV events
(`timestamp,description,actor`), showing the gap in minutes between events.

## How to run

```bash
python3 main.py --csv incident.csv
```

## Example output (sample from test fixture data)

```text
2026-10-26T10:00:00  [start]  bob: Outage reported
2026-10-26T10:15:00  [+15.0 min]  ali: Resolved
```

Standard library only. No network access.
