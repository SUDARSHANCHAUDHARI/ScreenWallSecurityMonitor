"""Tests for ScreenWall Security Monitor MVP."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from apps.api.app.cli import analyze
from apps.api.app.services.signage_url_scanner import load_fixture


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "data/samples/signage-scan.json"


class ScreenWallTests(unittest.TestCase):
    def test_detects_signage_risks(self) -> None:
        scan = load_fixture(FIXTURE)
        findings, summary = analyze(scan)
        kinds = {finding["kind"] for finding in findings}

        self.assertIn("signage.public_sensitive_path", kinds)
        self.assertIn("kiosk.default_password", kinds)
        self.assertIn("headers.csp_missing", kinds)
        self.assertIn("browser.outdated", kinds)
        self.assertGreater(summary["risk_score"], 80)

    def test_cli_writes_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, "-m", "apps.api.app.cli", "--fixture", str(FIXTURE), "--out-dir", tmp],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            summary = json.loads(Path(tmp, "summary.json").read_text(encoding="utf-8"))
            self.assertIn("Risk score", result.stdout)
            self.assertGreaterEqual(summary["findings"], 8)


if __name__ == "__main__":
    unittest.main()
