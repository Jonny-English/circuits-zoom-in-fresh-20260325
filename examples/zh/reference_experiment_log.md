# 参考实验日志

## 实验问题

在 `M06` 的 toy trace 里，如果我削弱对右侧数字 token 的读取，compose score 会怎样变化？

## Baseline

- 配置：保持 toy trace 默认 attention 分布。
- 指标：compose score、左右路径贡献占比。
- 预期：右侧数字贡献略高于左侧，因为数值更大。

## Variant

- 唯一改动：把右侧数字的 readout weight 从 `1.0` 降到 `0.65`。
- 其余保持不变：token embedding、QK 打分、路径结构都不改。

## 结果

- compose score 从 `2.144` 降到 `1.755`。
- 左右贡献比从 `0.43 / 0.57` 变成 `0.52 / 0.48`。
- 图上看起来路径还在，但定量主导关系已经翻转。

## Judgment Call

这说明 tracing 里“图还在”不等于“机制强度没变”。如果只看结构，不看边权重和 ablation drop，很容易高估一条路径的稳定性。

## Failure Analysis

- 这是 toy trace，不代表真实模型里的路径强度分解同样干净。
- 当前 readout 是手工设定的，所以只能说明局部机制直觉，不是论文级复现。
- 下一步应该对左侧 readout 做对称改动，检查结论是否稳定。
