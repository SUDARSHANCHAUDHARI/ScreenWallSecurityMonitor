# Demo

## Local CLI

```bash
python3 -m apps.api.app.cli --fixture data/samples/signage-scan.json --out-dir data/reports
```

Expected terminal output:

```text
Generated 9 finding(s)
Risk score: 100/100
```

## Review Outputs

```bash
cat data/reports/report.md
cat data/reports/triage.md
cat data/reports/summary.json
```

## Docker CLI

```bash
docker compose run --rm api
```
