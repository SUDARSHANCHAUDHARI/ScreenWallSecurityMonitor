# Architecture

ScreenWall Security Monitor is a defensive scanner for signage and kiosk exposure risks.

## Flow

1. `signage_url_scanner.py` loads a safe scan fixture and checks public signage paths.
2. `kiosk_config_checker.py` checks weak kiosk flags such as default passwords and remote debugging.
3. `csp_checker.py` checks embed and clickjacking controls.
4. `browser_version_checker.py` checks kiosk browser age.
5. `report_generator.py` writes JSON, Markdown report, and triage checklist outputs.

## Outputs

- scan fixture JSON
- enriched findings JSON
- summary JSON
- Markdown risk report
- Markdown remediation checklist

The current MVP is fixture-based and does not scan live URLs.
