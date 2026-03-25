# M09 Signs of Introspection in Large Language Models

## Goal

Use small teaching data to inspect the gap between what a model says about itself and what its behavior reveals.

## Core reference

- [Signs of introspection in large language models](https://www.anthropic.com/research/introspection)

## What to look for

- Self-report and observable behavior can align, but not perfectly.
- The interesting cases are the mismatches, not only the agreements.
- “Signs of introspection” should raise questions, not settle them.

## Notebook and artifacts

- Notebook: `notebooks/en/m09_signs_of_introspection.ipynb`
- Shared artifact: `artifacts/m09_introspection_signals.json`

## Self-check questions

- Why can self-report not be treated as direct evidence of internal state?
- Among the mismatch cases, which one is most worth following up, and what alternative explanations should you worry about?
- If you wanted to make the introspection claim stronger, which key class of evidence is still missing?

## Takeaway

This paper is best read as a frontier probe into self-modeling, not as proof of robust introspection.
