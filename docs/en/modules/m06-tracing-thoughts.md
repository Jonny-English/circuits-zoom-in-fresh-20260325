# M06 Tracing the Thoughts of a Large Language Model

## Goal

Start with one local toy tracing path, then teach readers how to read an attribution graph and explain one computation path from input to answer.

## Core reference

- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## What to look for

- Inputs, intermediate features, and outputs can be linked by weighted paths.
- A useful trace is selective; it does not need the whole model at once.
- Explaining a route through the model is different from paraphrasing the final answer.

## Notebook and artifacts

- Notebook: `notebooks/en/m06_tracing_thoughts.ipynb`
- Shared artifact: `artifacts/m06_attribution_graph.json`
- The notebook now runs a local toy trace first and then compares it to the shared graph.

## Self-check questions

- Explain the three most important contribution paths in the graph without just reading the labels back.
- What conclusion does this graph support, and what conclusion does it clearly not support?
- If you could run one follow-up experiment to reduce the graph's ambiguity, what would it be?

## Takeaway

This paper shifts the focus from isolated features to local computation graphs, and the notebook now makes that shift concrete by asking the reader to compute one path before reading the shared graph.
