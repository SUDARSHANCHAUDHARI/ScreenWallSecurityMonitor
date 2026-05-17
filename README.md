# ScreenWall Security Monitor

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Security auditing MVP for signage URLs, kiosk configurations, public playlists, CSP, and browser risks.

- **Portfolio group:** Product-style SaaS project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/ScreenWallSecurityMonitor
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/ScreenWallSecurityMonitor`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

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

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
