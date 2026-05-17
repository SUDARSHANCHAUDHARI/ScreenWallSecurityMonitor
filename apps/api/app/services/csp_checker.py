"""Check signage embed and CSP risks."""

from __future__ import annotations


def check_csp(headers: dict) -> list[dict]:
    """Return CSP/embed findings."""
    normalized = {str(k).lower(): str(v) for k, v in headers.items()}
    csp = normalized.get("content-security-policy", "").lower()
    findings: list[dict] = []
    if not csp:
        findings.append(
            {
                "kind": "headers.csp_missing",
                "severity": "high",
                "summary": "Content-Security-Policy header is missing.",
                "evidence": {},
            }
        )
    elif "frame-ancestors" not in csp:
        findings.append(
            {
                "kind": "headers.frame_ancestors_missing",
                "severity": "medium",
                "summary": "CSP does not define frame-ancestors for signage embedding control.",
                "evidence": {"csp": csp},
            }
        )
    if "x-frame-options" not in normalized and "frame-ancestors" not in csp:
        findings.append(
            {
                "kind": "headers.clickjacking_unprotected",
                "severity": "high",
                "summary": "No iframe/clickjacking protection is configured.",
                "evidence": {},
            }
        )
    return findings
