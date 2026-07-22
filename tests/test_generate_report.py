from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


EXTENSION_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCRIPT = EXTENSION_ROOT / "scripts" / "generate_report.py"


def copy_valid_project(tmp_path: Path) -> Path:
    target = tmp_path / "project"
    shutil.copytree(FIXTURES / "valid_project", target)
    return target


def test_report_is_generated_with_pending_items_when_errors_exist(tmp_path: Path) -> None:
    project = copy_valid_project(tmp_path)
    shutil.rmtree(project / "specs")
    output = project / "docs" / "evidencias" / "sdd-compliance-report.md"

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(project), "--output", str(output), "--strict"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert output.is_file()
    report = output.read_text(encoding="utf-8")
    assert "## Pendientes" in report
    assert "PEND-001" in report
    assert "specs" in report
