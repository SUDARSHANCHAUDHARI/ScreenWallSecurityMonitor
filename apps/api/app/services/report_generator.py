"""Build ScreenWall reports."""

from __future__ import annotations

from collections import Counter
import json


POINTS = {"critical": 45, "high": 30, "medium": 15, "low": 5}


RECOMMENDED_ACTIONS = {
    "signage.public_sensitive_path": "Restrict public access to dashboard, player, and playlist paths with authentication and network controls.",
    "signage.public_playlist": "Move playlist manifests behind authenticated delivery or signed URLs.",
    "kiosk.remote_debugging": "Disable remote debugging outside controlled maintenance windows.",
    "kiosk.default_password": "Rotate default credentials and enforce unique device passwords.",
    "kiosk.usb_enabled": "Disable or physically control USB access on unattended signage devices.",
    "kiosk.auto_update_disabled": "Enable managed browser and OS updates or document a patch window.",
    "headers.csp_missing": "Add a Content-Security-Policy header with frame and source restrictions.",
    "headers.clickjacking_unprotected": "Configure frame-ancestors or X-Frame-Options for embed control.",
    "browser.outdated": "Upgrade the kiosk browser to a supported version.",
}


def risk_level(score: int) -> str:
    if score >= 80:
        return "high"
    if score >= 45:
        return "medium"
    return "low"


def summarize(findings: list[dict]) -> dict:
    """Return scan summary."""
    score = min(100, sum(POINTS.get(str(f["severity"]), 0) for f in findings))
    by_category = Counter(str(f["kind"]).split(".", 1)[0] for f in findings)
    return {
        "findings": len(findings),
        "risk_score": score,
        "risk_level": risk_level(score),
        "by_severity": dict(Counter(str(f["severity"]) for f in findings)),
        "by_category": dict(by_category),
        "top_priority": findings[0] if findings else None,
    }


def enrich_findings(findings: list[dict]) -> list[dict]:
    """Add analyst-facing response guidance."""
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    enriched = []
    for finding in findings:
        item = dict(finding)
        item["recommended_action"] = RECOMMENDED_ACTIONS.get(
            item["kind"],
            "Review the finding and document the remediation decision.",
        )
        enriched.append(item)
    return sorted(enriched, key=lambda item: (severity_order.get(str(item["severity"]), 9), item["kind"]))


def build_report(scan: dict, findings: list[dict]) -> str:
    """Return Markdown report."""
    findings = enrich_findings(findings)
    summary = summarize(findings)
    lines = [
        "# ScreenWall Security Monitor Report",
        "",
        f"- URL: {scan.get('url')}",
        f"- Findings: {summary['findings']}",
        f"- Risk score: {summary['risk_score']}/100",
        f"- Risk level: {summary['risk_level']}",
        "",
        "## Priority Queue",
        "",
    ]
    if not findings:
        lines.append("No signage security findings.")
    for index, finding in enumerate(findings, start=1):
        lines.append(f"{index}. `{finding['kind']}` - {finding['severity']} - {finding['summary']}")
    lines.extend(
        [
            "",
            "## Findings",
            "",
        ]
    )
    if not findings:
        lines.append("No signage security findings.")
    for finding in findings:
        lines.extend(
            [
                f"### {finding['summary']}",
                "",
                f"- Severity: `{finding['severity']}`",
                f"- Type: `{finding['kind']}`",
                f"- Evidence: `{json.dumps(finding.get('evidence', {}), sort_keys=True)}`",
                f"- Recommended action: {finding['recommended_action']}",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_triage_report(scan: dict, findings: list[dict]) -> str:
    findings = enrich_findings(findings)
    summary = summarize(findings)
    lines = [
        "# ScreenWall Security Triage",
        "",
        f"- URL: {scan.get('url')}",
        f"- Risk level: {summary['risk_level']}",
        f"- Risk score: {summary['risk_score']}/100",
        "",
        "## Remediation Checklist",
        "",
    ]
    if not findings:
        lines.append("No remediation items were generated.")
    for finding in findings:
        lines.append(f"- [ ] {finding['recommended_action']} (`{finding['kind']}`)")
    return "\n".join(lines).rstrip() + "\n"
