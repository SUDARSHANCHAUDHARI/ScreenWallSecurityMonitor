"""Build ScreenWall reports."""

from __future__ import annotations

from collections import Counter


POINTS = {"critical": 45, "high": 30, "medium": 15, "low": 5}


def summarize(findings: list[dict]) -> dict:
    """Return scan summary."""
    return {
        "findings": len(findings),
        "risk_score": min(100, sum(POINTS.get(str(f["severity"]), 0) for f in findings)),
        "by_severity": dict(Counter(str(f["severity"]) for f in findings)),
    }


def build_report(scan: dict, findings: list[dict]) -> str:
    """Return Markdown report."""
    summary = summarize(findings)
    lines = [
        "# ScreenWall Security Monitor Report",
        "",
        f"- URL: {scan.get('url')}",
        f"- Findings: {summary['findings']}",
        f"- Risk score: {summary['risk_score']}/100",
        "",
        "## Findings",
        "",
    ]
    if not findings:
        lines.append("No signage security findings.")
    for finding in findings:
        lines.extend(
            [
                f"### {finding['summary']}",
                "",
                f"- Severity: `{finding['severity']}`",
                f"- Type: `{finding['kind']}`",
                f"- Evidence: `{finding.get('evidence', {})}`",
                "",
            ]
        )
    return "\n".join(lines) + "\n"
