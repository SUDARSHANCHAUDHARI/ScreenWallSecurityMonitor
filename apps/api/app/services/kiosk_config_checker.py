"""Check kiosk configuration risks."""

from __future__ import annotations


def check_kiosk_config(config: dict) -> list[dict]:
    """Return kiosk configuration findings."""
    findings: list[dict] = []
    checks = [
        ("remote_debugging", "high", "Remote debugging is enabled."),
        ("default_password", "critical", "Kiosk configuration uses a default password."),
        ("usb_enabled", "medium", "USB access is enabled and should be verified."),
        ("auto_update_disabled", "medium", "Automatic browser or OS updates are disabled."),
    ]
    for key, severity, summary in checks:
        if config.get(key):
            findings.append(
                {
                    "kind": f"kiosk.{key}",
                    "severity": severity,
                    "summary": summary,
                    "evidence": {key: config.get(key)},
                }
            )
    return findings
