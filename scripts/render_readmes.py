#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
REPO_SLUG = "Jonny-English/circuits-zoom-in-fresh-20260325"
README_PATHS = {
    "en": ROOT / "README.md",
    "zh": ROOT / "README_zh.md",
}


def notebook_path(module: dict, language: str) -> str:
    filename = f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb"
    return f"notebooks/{language}/{filename}"


def colab_url(module: dict, language: str) -> str:
    return (
        "https://colab.research.google.com/github/"
        f"{REPO_SLUG}/blob/main/{notebook_path(module, language)}"
    )


def build_table(course: list[dict], language: str) -> str:
    if language == "zh":
        header = "| 模块 | 主题 | Notebook | Colab | 运行层级 | 说明 |\n|---|---|---|---|---|---|"
        rows = [
            f"| `{module['id']}` | {module['title_zh']} | [打开]({notebook_path(module, 'zh')}) | [Colab]({colab_url(module, 'zh')}) | `{module['runnable_tier']}` | {module['summary_zh']} |"
            for module in course
        ]
    else:
        header = "| Module | Topic | Notebook | Colab | Runnable tier | Why it matters |\n|---|---|---|---|---|---|"
        rows = [
            f"| `{module['id']}` | {module['title_en']} | [Open]({notebook_path(module, 'en')}) | [Colab]({colab_url(module, 'en')}) | `{module['runnable_tier']}` | {module['summary_en']} |"
            for module in course
        ]
    return "\n".join([header, *rows])


def replace_block(text: str, rendered: str) -> str:
    start = "<!-- COURSE_TABLE:START -->"
    end = "<!-- COURSE_TABLE:END -->"
    before, remainder = text.split(start, maxsplit=1)
    _, after = remainder.split(end, maxsplit=1)
    return f"{before}{start}\n{rendered}\n{end}{after}"


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    for language, path in README_PATHS.items():
        rendered = build_table(course, language)
        updated = replace_block(path.read_text(), rendered)
        path.write_text(updated)
        print(f"updated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
