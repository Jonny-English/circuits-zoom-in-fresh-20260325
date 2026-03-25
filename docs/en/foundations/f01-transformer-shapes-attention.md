# F01 Transformer Shapes and Attention Reading

## Goal

Before you enter circuits and tracing, learn to read the basic shapes behind tokens, attention, and residual updates.

## Why learn this before the article core

- If all you can say is "the model looks here," later attention explanations stay stuck at the slogan level.
- If the shapes of Q, K, V, and residual updates are unstable in your head, tracing turns into vocabulary recital.
- Later discussions of features, paths, and graphs all depend on this shape intuition.

## What you will practice

- Explain the relationship between tokens, embeddings, attention scores, and context vectors.
- Read an attention heatmap directly instead of saying only "the model looks here."
- Treat the residual stream as an accumulating computation cache.

## Notebook and deliverables

- Notebook: `notebooks/foundations/en/f01_transformer_shapes_attention.ipynb`
- Deliverables: one annotated attention heatmap, one residual-update explanation, and one tensor-shape annotation.

## Self-check

- Why does high attention weight not automatically mean high causal contribution?
- Why is the residual stream a better language for later tracing than "one single neuron"?
- If you do not understand the shapes of Q, K, and V, where do later circuit explanations break down?

## Lab conclusion

In interpretability, "reading a figure" is often a shape problem before it becomes a meaning problem.
