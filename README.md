# ScreenWall Security Monitor

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Security auditing tool for digital signage and kiosk fleets. Audits signage URLs, kiosk configurations, public playlists, CSP, and browser-version risks across a fleet of unattended screens.

---

## Overview

ScreenWall Security Monitor is a defensive analysis tool built for operators of digital signage and kiosk fleets (the kind of devices unattended in lobbies, retail, and public spaces). It scans configured signage URLs and kiosk configs to flag insecure URLs, missing security headers, outdated browser versions, and exposed admin interfaces. Outputs include findings, risk-scored summary, Markdown report, and a triage handoff for fleet operators.

The current MVP is a Python CLI. A FastAPI + React fleet dashboard is scaffolded under `apps/` for future development.

## Features

- Audits signage URLs for HTTPS, certificate validity, and security headers
- Checks Content-Security-Policy on each URL
- Detects outdated browser versions on devices
- Flags exposed admin paths and debug endpoints
- Scores risk per URL and per device
- Outputs JSON findings, risk summary, Markdown report, and triage handoff

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container
- Network access for live URL audits (fixture mode works offline)

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/ScreenWallSecurityMonitor.git
cd ScreenWallSecurityMonitor
pip install .
```

This registers the `screenwall-monitor` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Audit the included fixture fleet:

```bash
python3 main.py --fixture data/samples/fleet-fixture.json --out-dir data/reports
```

Generated outputs in `data/reports/`:

- `findings.json` — per-URL / per-device findings
- `summary.json` — risk score and severity breakdown
- `report.md` — Markdown fleet audit report
- `triage.md` — operator triage checklist

## Project Structure

```
ScreenWallSecurityMonitor/
├── apps/
│   ├── api/        FastAPI app scaffold (planned)
│   └── web/        React/Next.js fleet dashboard scaffold (planned)
├── data/
│   ├── samples/    Safe sample fleet fixtures
│   └── reports/    Example generated output
├── docker/         Dockerfile + compose support
├── docs/           Architecture, security notes, demo
├── scripts/        Setup, seed, run helpers
├── tests/          Unit and integration tests
├── main.py         CLI entrypoint
├── pyproject.toml  Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm api
```

## Safe Use

This project is defensive and analysis-focused. Use only on signage URLs, kiosks, and fleets you own or have explicit written permission to audit.

## Status

Working Python CLI MVP. Web dashboard scaffold present but not yet implemented.

## Roadmap

- Live ingestion from common digital signage platforms
- Per-device browser version checks via remote agent
- Scheduled fleet-wide scans with diff alerts
- Web dashboard for fleet visualization
- GitHub release `v0.1.0-mvp`

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/ScreenWallSecurityMonitor/issues).
