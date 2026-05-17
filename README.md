# ScreenWall Security Monitor

**Goal:** Security auditing platform for signage/video wall setups.

**MVP:** Scan public signage URLs and device configs for risks.

## Core Features

- exposed dashboard detection
- public playlist check
- weak kiosk config checklist
- outdated browser warning
- CSP/embed check
- report export

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

## MVP Capabilities

- Detects public signage dashboard, player, or playlist-style URLs.
- Checks weak kiosk configuration flags.
- Checks CSP and iframe/clickjacking protection.
- Warns on outdated Chrome kiosk browsers.
- Generates JSON scan data, JSON findings, JSON summary, and a Markdown report.

## Repository Status

This repository contains the production-ready foundation for the ScreenWall Security Monitor MVP. The current codebase is scaffolded and ready for focused implementation work.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
