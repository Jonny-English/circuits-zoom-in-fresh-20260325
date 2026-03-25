#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
PROGRAM_PATH = ROOT / "content" / "program.json"
SELF_CHECKS_PATH = ROOT / "content" / "self_checks.json"
ARTIFACTS_PATH = ROOT / "artifacts" / "manifest.json"
DOCS_ROOT = ROOT / "docs"
NOTEBOOKS_ROOT = ROOT / "notebooks"
TEMPLATES_ROOT = ROOT / "templates"

REQUIRED_FIELDS = {
    "id",
    "order",
    "title_zh",
    "title_en",
    "summary_zh",
    "summary_en",
    "prereqs",
    "paper_refs",
    "artifact_refs",
    "runnable_tier",
    "web_slug",
}

PROGRAM_REQUIRED_FIELDS = {
    "goal_zh",
    "goal_en",
    "entry_requirements_zh",
    "entry_requirements_en",
    "study_contract_zh",
    "study_contract_en",
    "exit_portfolio_zh",
    "exit_portfolio_en",
    "phases",
    "weeks",
    "company_tasks",
    "capstones",
    "rubric",
}

EXPECTED_PROGRAM_DOCS = {
    "research-ready.md",
    "week-by-week.md",
    "research-playbook.md",
    "evaluation-rubric.md",
    "company-onramp.md",
}

EXPECTED_TEMPLATE_FILES = {
    "paper_reading_note_en.md",
    "paper_reading_note_zh.md",
    "experiment_log_en.md",
    "experiment_log_zh.md",
    "research_memo_en.md",
    "research_memo_zh.md",
}


def fail(message: str) -> None:
    raise SystemExit(message)


def assert_exists(path: Path, message: str) -> None:
    if not path.exists():
        fail(message)


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    program = json.loads(PROGRAM_PATH.read_text())
    self_checks = json.loads(SELF_CHECKS_PATH.read_text())
    artifacts = json.loads(ARTIFACTS_PATH.read_text())

    if not isinstance(course, list) or not course:
        fail("content/course.json must be a non-empty list")

    artifact_ids = [artifact["id"] for artifact in artifacts]
    if len(artifact_ids) != len(set(artifact_ids)):
        fail("artifact IDs must be unique")

    module_ids = [module["id"] for module in course]
    if len(module_ids) != len(set(module_ids)):
        fail("module IDs must be unique")

    orders = [module["order"] for module in course]
    if orders != sorted(orders):
        fail("module order must be sorted")

    artifact_lookup = {artifact["id"]: artifact for artifact in artifacts}
    expected_docs = {"en": set(), "zh": set()}
    expected_notebooks = {"en": set(), "zh": set()}

    for artifact in artifacts:
        if "path" in artifact:
            assert_exists(ROOT / artifact["path"], f"missing artifact file: {artifact['path']}")

    for module in course:
        missing = REQUIRED_FIELDS - set(module)
        if missing:
            fail(f"module {module.get('id', '<missing>')} is missing fields: {sorted(missing)}")
        if len(module["paper_refs"]) != 1:
            fail(f"module {module['id']} must reference exactly one paper")
        for prereq in module["prereqs"]:
            if prereq not in module_ids:
                fail(f"module {module['id']} references unknown prerequisite {prereq}")
        for paper in module["paper_refs"]:
            for field in ("title", "url", "date"):
                if field not in paper:
                    fail(f"module {module['id']} paper ref missing {field}")
        for artifact_id in module["artifact_refs"]:
            if artifact_id not in artifact_lookup:
                fail(f"module {module['id']} references missing artifact {artifact_id}")

        doc_name = f"{module['id'].lower()}-{module['web_slug']}.md"
        notebook_name = f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb"
        expected_docs["en"].add(doc_name)
        expected_docs["zh"].add(doc_name)
        expected_notebooks["en"].add(notebook_name)
        expected_notebooks["zh"].add(notebook_name)

    missing_program = PROGRAM_REQUIRED_FIELDS - set(program)
    if missing_program:
        fail(f"content/program.json is missing fields: {sorted(missing_program)}")
    if not program["phases"] or not program["weeks"] or not program["company_tasks"] or not program["rubric"]:
        fail("content/program.json must define non-empty phases, weeks, company_tasks, and rubric")

    phase_ids = [phase["id"] for phase in program["phases"]]
    if len(phase_ids) != len(set(phase_ids)):
        fail("program phase IDs must be unique")

    week_ids = [week["id"] for week in program["weeks"]]
    if len(week_ids) != len(set(week_ids)):
        fail("program week IDs must be unique")

    for week in program["weeks"]:
        for module_id in week["module_ids"]:
            if module_id not in module_ids:
                fail(f"program week {week['id']} references unknown module {module_id}")

    if not isinstance(self_checks, list) or not self_checks:
        fail("content/self_checks.json must be a non-empty list")
    self_check_ids = [entry["module_id"] for entry in self_checks]
    if len(self_check_ids) != len(set(self_check_ids)):
        fail("self-check module IDs must be unique")
    if set(self_check_ids) != set(module_ids):
        fail(
            f"self-check module set mismatch. expected={sorted(module_ids)}, actual={sorted(self_check_ids)}"
        )
    for entry in self_checks:
        for field in ("module_id", "questions_zh", "questions_en"):
            if field not in entry:
                fail(f"self-check entry missing field: {field}")
        if len(entry["questions_zh"]) < 2 or len(entry["questions_en"]) < 2:
            fail(f"self-check entry {entry['module_id']} must contain at least two questions per language")

    program_doc_sets = {}
    for language in ("zh", "en"):
        program_dir = DOCS_ROOT / language / "program"
        assert_exists(program_dir, f"missing program docs directory for {language}")
        actual_program_docs = {path.name for path in program_dir.glob("*.md")}
        program_doc_sets[language] = actual_program_docs
        if actual_program_docs != EXPECTED_PROGRAM_DOCS:
            fail(
                f"{language} program docs mismatch. expected={sorted(EXPECTED_PROGRAM_DOCS)}, actual={sorted(actual_program_docs)}"
            )

    template_files = {path.name for path in TEMPLATES_ROOT.glob("*.md")}
    if template_files != EXPECTED_TEMPLATE_FILES:
        fail(
            f"template set mismatch. expected={sorted(EXPECTED_TEMPLATE_FILES)}, actual={sorted(template_files)}"
        )

    for language in ("zh", "en"):
        index_path = DOCS_ROOT / language / "index.md"
        assert_exists(index_path, f"missing docs index for {language}")

        docs_dir = DOCS_ROOT / language / "modules"
        actual_docs = {path.name for path in docs_dir.glob("*.md")}
        if actual_docs != expected_docs[language]:
            fail(
                f"{language} docs set mismatch. expected={sorted(expected_docs[language])}, actual={sorted(actual_docs)}"
            )

        notebooks_dir = NOTEBOOKS_ROOT / language
        actual_notebooks = {path.name for path in notebooks_dir.glob("m*.ipynb")}
        if actual_notebooks != expected_notebooks[language]:
            fail(
                f"{language} notebook set mismatch. expected={sorted(expected_notebooks[language])}, actual={sorted(actual_notebooks)}"
            )

    print(
        f"validated {len(course)} article notebooks, {len(artifacts)} artifacts, "
        f"and {len(program['weeks'])} research-ready weeks"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        if exc.code not in (None, 0):
            print(exc, file=sys.stderr)
        raise
