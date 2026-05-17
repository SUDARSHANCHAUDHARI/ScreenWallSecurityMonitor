"""Scan signage URL metadata."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse


PUBLIC_PATH_MARKERS = ("dashboard", "admin", "playlist", "player", "screen")


def load_fixture(path: Path) -> dict:
    """Load a signage scan fixture."""
    return json.loads(path.read_text(encoding="utf-8"))


def scan_signage_url(scan: dict) -> list[dict]:
    """Return signage URL exposure findings."""
    url = str(scan.get("url", ""))
    parsed = urlparse(url)
    path = parsed.path.lower()
    findings: list[dict] = []
    if any(marker in path for marker in PUBLIC_PATH_MARKERS) and scan.get("public", False):
        findings.append(
            {
                "kind": "signage.public_sensitive_path",
                "severity": "high",
                "summary": "Public signage URL exposes an admin, player, or playlist-style path.",
                "evidence": {"url": url},
            }
        )
    if scan.get("playlist_public"):
        findings.append(
            {
                "kind": "signage.public_playlist",
                "severity": "medium",
                "summary": "Playlist content appears publicly accessible.",
                "evidence": {"url": url},
            }
        )
    return findings
