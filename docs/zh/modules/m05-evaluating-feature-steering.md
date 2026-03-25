# M05 Evaluating Feature Steering

## 目标

研究沿着 feature 方向干预时，“有效改变”与“副作用”之间的权衡。

## 核心参考

- [Evaluating Feature Steering](https://www.anthropic.com/research/evaluating-feature-steering)

## 重点观察

- steering 强度不是越大越好。
- 通常会存在一个 sweet spot，让目标行为提升但副作用还没失控。
- 评估本身和干预同样重要。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m05_evaluating_feature_steering.ipynb`
- 共享 artifact：`artifacts/concept_graph.json`

## 验收题

- 你会怎么区分 target metric 和 off-target metric，它们为什么必须同时存在？
- 在你的 steering sweep 里，sweet spot 出现在哪一段，你认为为什么会在那里出现？
- 什么样的证据会让你决定放弃这条 steering 方向，而不是继续调强度？

## 模块结论

只有被认真评估的 steering，才值得当成 interpretability 结果来讨论。
