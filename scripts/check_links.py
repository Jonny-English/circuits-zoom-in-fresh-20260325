#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from repo_metadata import current_repo_url


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
EXTENSIONS_PATH = ROOT / "content" / "extensions.json"
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EXTRA_LINKS = [
    "https://github.com/shareAI-lab/learn-claude-code",
    "https://www.anthropic.com/research/team/interpretability",
]


def check_url(url: str) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "course-link-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return True, str(response.status)
    except urllib.error.HTTPError as error:
        if error.code in {403, 405}:
            follow_up = urllib.request.Request(url, method="GET", headers={"User-Agent": "course-link-check/1.0"})
            with urllib.request.urlopen(follow_up, timeout=15) as response:
                return True, f"GET:{response.status}"
        return False, f"HTTP {error.code}"
    except Exception as error:  # noqa: BLE001
        return False, str(error)


def markdown_files() -> list[Path]:
    files = list(ROOT.glob("*.md"))
    files.extend((ROOT / "docs").rglob("*.md"))
    files.extend((ROOT / "examples").rglob("*.md"))
    files.extend((ROOT / "templates").rglob("*.md"))
    files.extend((ROOT / "launch").rglob("*.md"))
    return sorted(set(files))


def check_markdown_links(path: Path) -> list[str]:
    problems: list[str] = []
    in_fence = False
    for line_number, raw_line in enumerate(path.read_text().splitlines(), start=1):
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in MARKDOWN_LINK_RE.finditer(raw_line):
            target = match.group(1).strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("/"):
                problems.append(f"{path.relative_to(ROOT)}:{line_number} uses absolute local link {target}")
                continue
            target_path = target.split("#", maxsplit=1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                problems.append(
                    f"{path.relative_to(ROOT)}:{line_number} points outside repo with link {target}"
                )
                continue
            if not resolved.exists():
                problems.append(
                    f"{path.relative_to(ROOT)}:{line_number} points to missing path {target}"
                )
    return problems


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    extensions = json.loads(EXTENSIONS_PATH.read_text())
    urls = []
    for module in course:
        for paper in module["paper_refs"]:
            urls.append(paper["url"])
    for item in extensions:
        urls.append(item["source_url"])
    urls.append(current_repo_url())
    urls.extend(EXTRA_LINKS)
    seen = []
    for url in urls:
        if url not in seen:
            seen.append(url)

    failures = []
    for url in seen:
        ok, detail = check_url(url)
        status = "ok" if ok else "fail"
        print(f"[{status}] {url} ({detail})")
        if not ok:
            failures.append((url, detail))
        time.sleep(0.05)

    if failures:
        details = ", ".join(f"{url} -> {detail}" for url, detail in failures)
        raise SystemExit(f"link check failed: {details}")

    markdown_failures: list[str] = []
    for path in markdown_files():
        markdown_failures.extend(check_markdown_links(path))

    if markdown_failures:
        raise SystemExit("markdown link check failed: " + "; ".join(markdown_failures))


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        if exc.code not in (None, 0):
            print(exc, file=sys.stderr)
        raise
