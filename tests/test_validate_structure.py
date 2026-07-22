from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


EXTENSION_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCRIPT = EXTENSION_ROOT / "scripts" / "validate_structure.py"


def copy_valid_project(tmp_path: Path) -> Path:
    target = tmp_path / "project"
    shutil.copytree(FIXTURES / "valid_project", target)
    return target


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), "--strict"],
        text=True,
        capture_output=True,
        check=False,
    )


def test_valid_project_passes_structure(tmp_path: Path) -> None:
    project = copy_valid_project(tmp_path)

    result = run_validator(project)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Estructura SDD/Scrum minima encontrada" in result.stdout


def test_project_without_specs_fails_structure(tmp_path: Path) -> None:
    project = copy_valid_project(tmp_path)
    shutil.rmtree(project / "specs")

    result = run_validator(project)

    assert result.returncode == 1
    output = result.stdout + result.stderr
    assert "specs" in output
    assert "Falta" in output
