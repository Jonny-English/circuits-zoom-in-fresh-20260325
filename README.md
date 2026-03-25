# From Circuits to Claude

[**中文版 README**](README_zh.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Next.js Static Export](https://img.shields.io/badge/web-next.js-black.svg)](web/)

`From Circuits to Claude` is a bilingual interpretability course for readers who know basic Python and PyTorch, but are new to mechanistic interpretability. The repository is now article-first: every core paper in the path has one mirrored note and one Colab notebook.

The repository has three synced layers:

- `content/course.json` is the single source of truth for order, prerequisites, links, and artifacts.
- `docs/en` and `docs/zh` mirror each other exactly.
- `notebooks/en` and `notebooks/zh` mirror each other exactly, while `web/` turns the same metadata into a static course explorer.

It also now has a second layer for serious learners: a research-ready path with a 12-week bootcamp, memo templates, a rubric, and simulated company-style research tasks.

That second layer exists to stop the most common self-study failure mode: finishing the reading without building research habits.

## Who This Project Is For

- It is beginner-friendly for readers with basic Python and PyTorch but little or no mechanistic-interpretability background.
- It is for readers who want to move from "I can follow a few papers" to "I can take on clearly scoped research tasks inside a company."
- It is not designed as passive popularization. You are expected to write reading notes, experiment logs, and short memos.

The target output of this repository is not "a person who has seen many papers." The target output is someone approaching the capability density of an Alibaba-style `P6` large-model research engineer.

To reduce ambiguity, the ladder below is rewritten to match the public, commonly used understanding of Alibaba-style `P4-P12` technical levels:

| Level | Capability |
|---|---|
| `P4` | Entry-level engineer: can work under explicit guidance, run notebooks, reproduce setup steps, and explain basic concepts, but still lacks strong independent research judgment. |
| `P5` | Engineer: can independently reproduce a scoped result, keep experiment logs, compare baseline versus variant, and write basic conclusions. |
| `**P6**` | Senior engineer / strong IC starting point: can take a clearly scoped research task inside a company, read papers, reproduce results, critique evidence, and propose the next experiment. |
| `P7` | Expert: can define a small direction, design a two-week research plan, and close the loop across experiments, tools, and reporting. |
| `P8` | Senior expert: can own a research sub-area or tooling line and create sustained technical leverage across multiple collaborators. |
| `P9` | Principal / senior expert: can define a medium-term research thread and influence methods, judgment, and collaboration across teams. |
| `P10` | Fellow / organization-level expert: can set organization-level research direction, choose key methodological bets, and influence product and safety strategy. |
| `P11` | Company-level top technical leader: can define long-term agenda, standards, and talent systems. |
| `P12` | Industry-shaping figure: can significantly change how the field frames the technology and its control problems. |

On that scale, no single teaching project should claim "finish this and become `P10`." In Alibaba-style language, `P10` is already a very high organization-level expert bar.

The credible target of this repository is narrower: move a true beginner from below an Alibaba-style `P4` state toward `P5`, with strong completers beginning to touch the lower edge of `P6`. It is the start of a research path, not the end-state.

## Why Learn This

After the spinning jenny appeared, the center of value in textile work stopped being "who has the most refined hand-spinning technique." It shifted toward:

- who understood the machine
- who could use the machine well
- who could modify the machine
- who could reorganize production around the machine

The large-model era creates the same shift.

When models can already perform a large amount of local cognitive work, the scarce skill is no longer only "manually weaving every sentence, reasoning step, or code block by hand." The scarce skill becomes:

- understanding what the model is representing internally
- understanding why it succeeds and why it fails
- understanding which directions can be read out, intervened on, and controlled safely
- understanding how to turn those judgments into research, tooling, and product decisions

So learning interpretability is not just learning a set of paper summaries. It is learning how to understand and steer machine intelligence once the machine itself becomes the central productive object.

Put more precisely: AI is also just another layer of abstraction over lower-level computation.

- Assembly is a layer of abstraction over machine code.
- High-level languages are another layer over assembly.
- Large models and AI systems are one more layer of abstraction built on top of those computational stacks.

So the right focus is no longer only the fine-grained craft of manually executing the old workflow. The focus shifts toward:

- what capability this abstraction layer exposes
- what mechanism this abstraction layer hides
- how we understand, use, debug, and control this abstraction layer

That is also why this repository is not only about paper summaries. It is also about experiments, artifacts, steering, tracing, and research communication.

## One Article, One Colab

Each row below corresponds to exactly one paper and one notebook. Every paired note and Colab notebook now also includes self-check questions so readers can test whether they actually absorbed the material.

<!-- COURSE_TABLE:START -->
| ID | Paper | Date | Notebook | Colab | Runnable tier | What you will do |
|---|---|---|---|---|---|---|
| `M00` | Zoom In: An Introduction to Circuits | `2020-03-10` | [Open](notebooks/en/m00_zoom_in_circuits.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m00_zoom_in_circuits.ipynb) | `warmup` | Build first-pass intuition for features, circuits, and interventions in a visual model. |
| `M01` | Toy Models of Superposition | `2022-09-14` | [Open](notebooks/en/m01_toy_models_superposition.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m01_toy_models_superposition.ipynb) | `cpu-colab` | Use a minimal toy model to see why neurons can mix multiple semantics. |
| `M02` | Towards Monosemanticity | `2023-10-05` | [Open](notebooks/en/m02_towards_monosemanticity.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m02_towards_monosemanticity.ipynb) | `cpu-colab` | Use a teaching-scale sparse autoencoder to see why a feature view can be cleaner than a neuron view. |
| `M03` | Mapping the Mind of a Large Language Model | `2024-05-21` | [Open](notebooks/en/m03_mapping_the_mind.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m03_mapping_the_mind.ipynb) | `artifact-guided` | Browse a teaching-scale feature catalog to understand what it means to discover many reusable features. |
| `M04` | Using Dictionary Learning Features as Classifiers | `2024-10-16` | [Open](notebooks/en/m04_features_as_classifiers.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m04_features_as_classifiers.ipynb) | `cpu-colab` | Treat features as classifier inputs and study where readout ability comes from. |
| `M05` | Evaluating Feature Steering | `2024-10-25` | [Open](notebooks/en/m05_evaluating_feature_steering.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m05_evaluating_feature_steering.ipynb) | `cpu-colab` | Sweep steering strength to inspect target gain, sweet spots, and off-target costs. |
| `M06` | Tracing the Thoughts of a Large Language Model | `2025-03-27` | [Open](notebooks/en/m06_tracing_thoughts.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m06_tracing_thoughts.ipynb) | `artifact-guided` | Use a precomputed attribution graph to read a local computation path. |
| `M07` | Open-sourcing Circuit Tracing Tools | `2025-05-29` | [Open](notebooks/en/m07_circuit_tracing_tools.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m07_circuit_tracing_tools.ipynb) | `artifact-guided` | Inspect tracing artifacts and workflow stages to understand the tooling layer behind the analysis. |
| `M08` | Persona Vectors | `2025-08-01` | [Open](notebooks/en/m08_persona_vectors.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m08_persona_vectors.ipynb) | `artifact-guided` | Use before/after persona-vector comparisons to study character traits as directions. |
| `M09` | Signs of Introspection in Large Language Models | `2025-10-29` | [Open](notebooks/en/m09_signs_of_introspection.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m09_signs_of_introspection.ipynb) | `artifact-guided` | Compare self-report and behavior signals in teaching data to discuss what 'signs of introspection' actually mean. |
| `M10` | The Assistant Axis | `2026-01-19` | [Open](notebooks/en/m10_assistant_axis.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/en/m10_assistant_axis.ipynb) | `artifact-guided` | Project multiple assistant styles onto one axis and inspect the problem of stabilizing character. |
<!-- COURSE_TABLE:END -->

## Suggested Paths

- `Foundations`: `M00 → M01 → M02`
- `Feature discovery and use`: `M03 → M04 → M05`
- `Tracing and character`: `M06 → M07 → M08 → M09 → M10`

If you want the shortest useful path, start with `M00`, `M01`, `M02`, `M05`, and `M06`.

## Research-Ready Path

If your goal is not just understanding but becoming useful in a company research setting, use these files alongside the article notebooks:

- [Research-ready overview](docs/en/program/research-ready.md)
- [12-week bootcamp](docs/en/program/week-by-week.md)
- [Research playbook](docs/en/program/research-playbook.md)
- [Evaluation rubric](docs/en/program/evaluation-rubric.md)
- [Company onramp simulation](docs/en/program/company-onramp.md)

Templates:

- [Paper reading note](templates/paper_reading_note_en.md)
- [Experiment log](templates/experiment_log_en.md)
- [Research memo](templates/research_memo_en.md)

Use the research-ready track as an operating system, not as extra reading:

- Every article should leave behind a reading note, an experiment log, a short memo, and a next-question list.
- The weekly path assumes `8-12` focused hours per week.
- You should finish with a real portfolio: notes, logs, memos, an artifact critique, and a two-week capstone proposal.
- The bar is not "I followed the notebooks." The bar is "I can read, reproduce, critique, and propose the next experiment."

## Quick Start

```bash
pip install -r requirements.txt

# Refresh derived assets after editing course metadata
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py

# Validate metadata, docs, notebook parity, and links
python3 scripts/validate_course.py
python3 scripts/check_links.py

# Execute all generated notebooks as a smoke test
python3 scripts/smoke_notebooks.py
```

To build the static site:

```bash
cd web
npm install
npm run build
```

If you prefer a browser-first workflow, open the Colab links in the table above directly.

## Repo Structure

```text
.
├── content/               # Course metadata and glossary
├── docs/                  # Mirrored zh/en article notes
├── notebooks/             # Legacy notebook + mirrored article notebooks
├── artifacts/             # Shared JSON artifacts for notebooks and web
├── web/                   # Static Next.js explorer
├── scripts/               # Notebook generation and validation
├── figures/               # Legacy visual circuit figures reused by M00
└── utils/                 # Shared plotting helpers from the original tutorial
```

## What Stays From the Original Project

The original notebooks remain in place:

- `notebooks/circuits_zoom_in_en.ipynb`
- `notebooks/circuits_zoom_in_zh.ipynb`

They now act as the long-form background material behind `M00`.

## References

The core reading path is anchored in official Anthropic research pages as of `2026-03-25`, with the interpretability team page as the index:

- [Anthropic Interpretability team page](https://www.anthropic.com/research/team/interpretability)
- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)
- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## License

[MIT](LICENSE)
