# M02 Towards Monosemanticity

## 目标

引入字典学习和 sparse autoencoder，展示为什么它们能恢复出比原始神经元更干净的单位。

## 核心参考

- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)

## 重点观察

- 稀疏重建是一种建模选择，可以暴露出可复用方向。
- 学到的 feature 往往比原始基底更可解释。
- “单语义”更像目标，而不是保证。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m02_towards_monosemanticity.ipynb`
- 共享 artifact：`artifacts/concept_graph.json`

## 验收题

- 和直接看 neuron 相比，恢复出来的 feature 到底给了你什么可解释性优势？
- 在你的 sweep 里，monosemanticity 是从哪里开始变差的，主因更像是容量、正则化，还是噪声？
- 如果恢复出来的 feature 仍然不够稳定，你下一步会先改哪个变量家族，为什么？

## 模块结论

这篇论文把 interpretability 从“看神经元”推到了“发现 feature”。
