# Repo Map

Use this page if you want to understand how the repository is organized without reading the whole README first.

## Reader Paths

- If you are new and not stable on setup, start with [foundations/index.md](foundations/index.md).
- If you can already run notebooks, start with [index.md](index.md) and the live core.
- If you want the full long-horizon path, go to [program/research-ready.md](program/research-ready.md).

## Top-Level Layout

```text
.
├── content/      # Source-of-truth metadata for the course, program, references, and glossary
├── docs/         # Mirrored English and Chinese notes, indices, and program docs
├── notebooks/    # Runnable notebooks: core, foundations, extensions, plus legacy long-form notebooks
├── examples/     # Reference outputs used to calibrate memo/log/proposal quality
├── templates/    # Blank note, log, and memo templates
├── artifacts/    # Reading-only data and public artifacts that live notebooks may not depend on
├── scripts/      # README rendering, notebook generation, validation, and policy checks
├── figures/      # Legacy visual-circuit figures reused by M00
├── utils/        # Shared plotting helpers kept from the original tutorial
└── launch/       # Release notes and launch-post drafts; not part of the learning path
```

## What Is Source Of Truth

- [content/course.json](../../content/course.json): article order, status, prerequisites, and paper metadata
- [content/foundations.json](../../content/foundations.json): foundation labs
- [content/program.json](../../content/program.json): research-ready path, weeks, and graduation rules
- [content/extensions.json](../../content/extensions.json): extension-track papers
- [content/reference_outputs.json](../../content/reference_outputs.json): calibrated example outputs

If you want to change the curriculum, start there, not in the generated tables.

## What Is Generated Or Derived

- [README.md](../../README.md) and [README_zh.md](../../README_zh.md) contain rendered tables
- runnable notebooks under `notebooks/en`, `notebooks/zh`, `notebooks/foundations`, and `notebooks/extensions` are generated

When metadata changes, refresh these derived surfaces instead of editing them by hand.

## Maintenance Commands

```bash
pip install -r requirements.txt
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```

## Non-Core Material

- [notebooks/circuits_zoom_in_en.ipynb](../../notebooks/circuits_zoom_in_en.ipynb)
- [notebooks/circuits_zoom_in_zh.ipynb](../../notebooks/circuits_zoom_in_zh.ipynb)

These are the original long-form background notebooks behind `M00`. They stay in the repo, but they are not the main navigation surface anymore.

## Reference Pages

- [program/research-ready.md](program/research-ready.md)
- [program/p6-graduation-checklist.md](program/p6-graduation-checklist.md)
- [extensions/index.md](extensions/index.md)
- [foundations/index.md](foundations/index.md)

If the repository still feels cluttered, use those four pages plus [index.md](index.md) and ignore the rest until you need it.
