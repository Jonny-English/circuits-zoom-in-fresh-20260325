# M06 Tracing the Thoughts

## 目标

先在本地构造一条 toy tracing 路径，再学习如何阅读一张局部 attribution graph，并解释一条从输入走到答案的计算路径。

## 核心参考

- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## 重点观察

- 输入、中间特征和输出可以通过带权路径连起来。
- 好的 trace 是有选择地暴露局部，而不是一次性摊开整个模型。
- “解释答案是什么”与“解释答案是怎么算出来的”是两件不同的事。

## Notebook 与 artifact

- Notebook：`notebooks/zh/m06_tracing_thoughts.ipynb`
- 共享 artifact：`artifacts/m06_attribution_graph.json`
- notebook 现在先跑一个本地 toy trace，再把结果和共享图对照。

## 验收题

- 不用照抄图上的标签，解释这张 attribution graph 里最重要的 3 条贡献路径在做什么。
- 这张图支持什么结论，又明确不支持什么结论？
- 如果你只能再做一个后续实验来降低这张图的歧义，你会选什么？

## 模块结论

这篇论文把焦点从孤立 feature 推进到局部计算图，而 notebook 则把“自己先算一条路径”放到了阅读共享图之前。
