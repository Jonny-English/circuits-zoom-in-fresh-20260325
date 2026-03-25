# F01 Transformer 形状与注意力读图

## 目标

让你在进入 circuits 和 tracing 之前，先读懂最基础的 token、attention 和 residual update 形状。

## 为什么在文章主线前学

- 如果你只会说“模型在看这里”，后面的 attention 解释会一直停留在口语层面。
- 如果 Q、K、V 和 residual update 的形状感不稳，tracing 会变成背术语。
- 后面的 feature、path 和 graph 讨论，本质上都依赖这层形状直觉。

## 你会练什么

- 解释 token、embedding、attention score 和 context vector 的关系。
- 手动读一张 attention heatmap，而不是只说“模型在看这里”。
- 把 residual stream 看成逐步累加的计算缓存。

## Notebook 与交付

- Notebook：`notebooks/foundations/zh/f01_transformer_shapes_attention.ipynb`
- 交付物：1 张标注过的 attention heatmap、1 段 residual update 说明、1 份张量形状注释。

## 验收题

- attention 权重高，并不自动等于“因果贡献大”，为什么？
- residual stream 为什么比“某个单一神经元”更适合作为后续 tracing 的语言？
- 如果你看不懂 Q、K、V 的形状，后面的 circuit 解释会卡在哪里？

## Lab 结论

在 interpretability 里，“看懂一张图”往往先是形状问题，然后才是意义问题。
