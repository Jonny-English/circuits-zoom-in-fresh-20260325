# M01 Toy Models of Superposition

## Goal

Show why neurons are often poor semantic units by compressing several sparse concepts into a smaller space.

## Core reference

- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)

## What to look for

- Reconstruction can stay good even when concepts overlap internally.
- A model can use geometry to pack more concepts than clean neuron semantics would suggest.
- The paper is the conceptual bridge from circuits intuition to feature-based interpretability.

## Notebook and artifacts

- Notebook: `notebooks/en/m01_toy_models_superposition.ipynb`
- Shared artifact: `artifacts/concept_graph.json`

## Self-check questions

- Why is superposition better understood as geometry rather than just a training bug?
- In your sweep, which variable most clearly changed concept overlap, and what did that teach you?
- If someone insists that one neuron should represent one clean concept, which evidence from this article would you use to push back?

## Takeaway

Superposition explains why “one neuron, one meaning” is an unsafe default.
