# M05 Evaluating Feature Steering

## Goal

Study the tradeoff between useful intervention and collateral damage when you steer along a feature direction.

## Core reference

- [Evaluating Feature Steering](https://www.anthropic.com/research/evaluating-feature-steering)

## What to look for

- Stronger steering is not always better.
- There is often a sweet spot where target behavior improves before off-target effects dominate.
- Evaluation matters as much as the intervention itself.

## Notebook and artifacts

- Notebook: `notebooks/en/m05_evaluating_feature_steering.ipynb`
- Shared artifact: `artifacts/concept_graph.json`

## Self-check questions

- How do you distinguish the target metric from the off-target metric, and why do you need both?
- Where is the sweet spot in your sweep, and why do you think it appears there?
- What evidence would make you give up on this steering direction instead of just tuning the strength further?

## Takeaway

Feature steering is only interesting if it is measured carefully.
