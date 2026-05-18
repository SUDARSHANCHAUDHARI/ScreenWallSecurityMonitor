# ScreenWall Security Monitor

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-product%20polish-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Security auditing MVP for signage URLs, kiosk configurations, public playlists, CSP, and browser risks.

- **Portfolio group:** Product-style SaaS project
- **Status:** Product polish implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/ScreenWallSecurityMonitor
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/ScreenWallSecurityMonitor`

## MVP Snapshot

This repository includes a working MVP with safe signage scan fixtures, deterministic risk checks, JSON outputs, Markdown security report, triage checklist, tests, and Docker demo support.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- exposed dashboard detection
- public playlist check
- weak kiosk config checklist
- outdated browser warning
- CSP/embed check
- report export
- risk level and severity breakdown
- remediation checklist

## Suggested Stack

FastAPI, React, Docker.

## Status

Working CLI MVP.

## Quick Start

Analyze the included signage scan fixture:

```bash
python3 -m apps.api.app.cli --fixture data/samples/signage-scan.json --out-dir data/reports
```

Run tests:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Generated outputs:

- `data/reports/scan.json`
- `data/reports/findings.json`
- `data/reports/summary.json`
- `data/reports/report.md`
- `data/reports/triage.md`

## Docker Demo

```bash
docker compose run --rm api
```

## Product Polish Capabilities

- Detects public signage dashboard, player, or playlist-style URLs.
- Checks weak kiosk configuration flags.
- Checks CSP and iframe/clickjacking protection.
- Warns on outdated Chrome kiosk browsers.
- Generates JSON scan data, JSON findings, JSON summary, and a Markdown report.
- Adds recommended actions and a remediation checklist for signage operators.

## Roadmap

- Add authenticated scan profiles for owned signage deployments
- Add browser/user-agent inventory comparison
- Add scheduled monitoring and drift alerts
- Add web dashboard for risk summaries
- Add export formats for customer-ready audits
