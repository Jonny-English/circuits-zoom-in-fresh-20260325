# M01 Toy Models of Superposition

## 目标

通过把多个稀疏概念压进更小空间，解释为什么神经元通常不是好语义单位。

## 核心参考

- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)

## 重点观察

- 即使内部发生重叠，模型依然可以重建输入。
- 几何结构会让模型装下比“干净神经元语义”更多的概念。
- 这篇论文是从视觉电路直觉走向 feature 视角的桥。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m01_toy_models_superposition.ipynb`
- 共享 artifact：`artifacts/concept_graph.json`

## 验收题

- 为什么 superposition 更像一个几何结果，而不只是训练中的 bug？
- 在你的 sweep 里，哪一个变量最明显地改变了概念重叠，这告诉了你什么？
- 如果有人坚持把单个 neuron 当成稳定语义单位，你会用这篇文章里的哪条证据来反驳？

## 模块结论

superposition 解释了为什么“一个神经元只代表一个意思”通常靠不住。
