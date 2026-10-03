"""Smoke test for cross-platform documentation animation generation."""

import subprocess
import sys
from pathlib import Path


def test_generate_termynal(tmp_path):
    script = Path(__file__).parents[1] / "docs/scripts/generate-termynal.py"
    result = subprocess.run(
        [sys.executable, "-X", "utf8", str(script)],
        cwd=tmp_path,
        capture_output=True,
        encoding="utf-8",
        timeout=90,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert '<div id="termynal"' in result.stdout
    assert 'data-ty="input"' in result.stdout
