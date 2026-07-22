from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


EXTENSION_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCRIPT = EXTENSION_ROOT / "scripts" / "validate_traceability.py"


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


def replace_in_markdown(project: Path, old: str, new: str) -> None:
    for path in project.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace(old, new), encoding="utf-8")


def test_valid_project_passes_traceability(tmp_path: Path) -> None:
    project = copy_valid_project(tmp_path)

    result = run_validator(project)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Trazabilidad minima SDD/Scrum encontrada" in result.stdout


def test_requirement_without_acceptance_criterion_fails_traceability(tmp_path: Path) -> None:
    project = copy_valid_project(tmp_path)
    replace_in_markdown(project, "CA-001", "SIN-CA")

    result = run_validator(project)

    assert result.returncode == 1
    assert "RF-001 no tiene criterio de aceptacion vinculado" in result.stdout


def test_user_story_without_requirement_fails_traceability(tmp_path: Path) -> None:
    project = copy_valid_project(tmp_path)
    replace_in_markdown(project, "RF-001", "REQ-001")
    replace_in_markdown(project, "RNF-001", "REQNF-001")
    replace_in_markdown(project, "RN-001", "REGLA-001")

    result = run_validator(project)

    assert result.returncode == 1
    assert "HU-001 no tiene requisito vinculado" in result.stdout


def test_task_without_user_story_or_requirement_fails_traceability(tmp_path: Path) -> None:
    project = copy_valid_project(tmp_path)
    tasks = project / "specs" / "login" / "tasks.md"
    tasks.write_text(
        "\n".join(
            (
                "# Tareas",
                "",
                "| Tarea | RF/RNF/RN | CA | HU |",
                "| --- | --- | --- | --- |",
                "| TASK-002 | - | CA-001 | - |",
                "",
            )
        ),
        encoding="utf-8",
    )
    result = run_validator(project)

    assert result.returncode == 1
    assert "TASK-002 no tiene HU y requisito vinculados" in result.stdout
