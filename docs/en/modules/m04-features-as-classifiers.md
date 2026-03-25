# M04 Using Dictionary Learning Features as Classifiers

## Goal

Show that learned features are not only descriptive; they can also support concrete readout tasks.

## Core reference

- [Using Dictionary Learning Features as Classifiers](https://www.anthropic.com/research/features-as-classifiers)

## What to look for

- Feature activations can feed a classifier directly.
- Readout quality depends on the feature basis you have recovered.
- This is the first clear step from “understanding” to “using” features.

## Notebook and artifacts

- Notebook: `notebooks/en/m04_features_as_classifiers.ipynb`
- Shared artifact: `artifacts/concept_graph.json`

## Self-check questions

- If features can feed a classifier directly, what does that show, and what does it still not show?
- If the probe accuracy looks strong, which confounders would you check before trusting the result?
- Besides accuracy, which baseline or comparison would you use to judge whether the features really have readout value?

## Takeaway

If features can classify, they become operational tools rather than only interpretive stories.
