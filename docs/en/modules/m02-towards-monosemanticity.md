# M02 Towards Monosemanticity

## Goal

Introduce dictionary learning and sparse autoencoders as a way to recover cleaner units than raw neurons.

## Core reference

- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)

## What to look for

- Sparse reconstruction is a modeling choice that can surface reusable directions.
- Learned features can be more interpretable than the original basis.
- “Monosemanticity” is an aspiration, not a guarantee.

## Notebook and artifacts

- Notebook: `notebooks/en/m02_towards_monosemanticity.ipynb`
- Shared artifact: `artifacts/concept_graph.json`

## Self-check questions

- What interpretability advantage do recovered features give you over looking at raw neurons directly?
- Where did monosemanticity start to degrade in your sweep, and did it look more like a capacity, regularization, or noise problem?
- If the recovered features still feel unstable, which variable family would you change next, and why?

## Takeaway

This paper turns interpretability from neuron inspection into feature discovery.
