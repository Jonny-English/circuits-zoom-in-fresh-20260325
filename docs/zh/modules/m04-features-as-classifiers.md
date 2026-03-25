# M04 Features as Classifiers

## 目标

展示 learned feature 不只是描述单位，它们还可以支撑具体的读出任务。

## 核心参考

- [Using Dictionary Learning Features as Classifiers](https://www.anthropic.com/research/features-as-classifiers)

## 重点观察

- feature activation 可以直接作为分类器输入。
- 读出效果会依赖你恢复出的 feature 基底。
- 这是从“理解 feature”走向“使用 feature”的第一步。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m04_features_as_classifiers.ipynb`
- 共享 artifact：`artifacts/concept_graph.json`

## 验收题

- 当 feature 能直接喂给 classifier 时，这说明了什么，又还没有说明什么？
- 如果 probe 准确率很高，你会先检查哪几个 confounders，再决定是否相信这个结果？
- 除了 accuracy，你还会用什么 baseline 或对照来判断这些 feature 真的有读出价值？

## 模块结论

当 feature 可以拿来分类时，它们就从解释故事变成了操作工具。
