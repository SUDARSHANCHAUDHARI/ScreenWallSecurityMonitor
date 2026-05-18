"""CLI for ScreenWall Security Monitor MVP."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from apps.api.app.services.browser_version_checker import check_browser_version
from apps.api.app.services.csp_checker import check_csp
from apps.api.app.services.kiosk_config_checker import check_kiosk_config
from apps.api.app.services.report_generator import build_report, build_triage_report, enrich_findings, summarize
from apps.api.app.services.signage_url_scanner import load_fixture, scan_signage_url


def analyze(scan: dict) -> tuple[list[dict], dict]:
    """Analyze one signage scan fixture."""
    findings = [
        *scan_signage_url(scan),
        *check_kiosk_config(scan.get("kiosk_config", {})),
        *check_csp(scan.get("headers", {})),
        *check_browser_version(str(scan.get("user_agent", ""))),
    ]
    return findings, summarize(findings)


def main() -> None:
    parser = argparse.ArgumentParser(description="ScreenWall signage security scanner")
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("data/reports"))
    args = parser.parse_args()

    scan = load_fixture(args.fixture)
    findings, summary = analyze(scan)
    enriched_findings = enrich_findings(findings)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "scan.json").write_text(json.dumps(scan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "findings.json").write_text(json.dumps(enriched_findings, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "report.md").write_text(build_report(scan, findings), encoding="utf-8")
    (args.out_dir / "triage.md").write_text(build_triage_report(scan, findings), encoding="utf-8")
    print(f"Generated {summary['findings']} finding(s)")
    print(f"Risk score: {summary['risk_score']}/100")


if __name__ == "__main__":
    main()
