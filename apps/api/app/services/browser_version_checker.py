"""Check browser version age."""

from __future__ import annotations

import re


def check_browser_version(user_agent: str, minimum_chrome_major: int = 120) -> list[dict]:
    """Return outdated browser findings."""
    match = re.search(r"Chrome/(\d+)", user_agent)
    if not match:
        return [
            {
                "kind": "browser.unknown_version",
                "severity": "low",
                "summary": "Browser version could not be identified from user agent.",
                "evidence": {"user_agent": user_agent},
            }
        ]
    version = int(match.group(1))
    if version < minimum_chrome_major:
        return [
            {
                "kind": "browser.outdated",
                "severity": "high",
                "summary": "Kiosk browser version is below the configured minimum.",
                "evidence": {"chrome_major": version, "minimum": minimum_chrome_major},
            }
        ]
    return []
