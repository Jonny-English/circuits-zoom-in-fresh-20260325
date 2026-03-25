# 参考两周提案

## 研究问题

在 `M08 Persona Vectors` 的教学设定里，persona control 的 sweet spot 是否会随着任务分布变化而漂移？

## 假设

如果 persona direction 真的在表示空间里抓住了相对稳定的 trait，那么不同任务分布下的最佳强度不应该完全漂移；如果漂移很大，说明当前 direction 更像局部 prompt hack。

## Baseline

- baseline assistant：不加 steering。
- baseline 评估：helpful、cautious、concise 三个 trait score，加一个 off-target stability 指标。

## 实验设计

- 分布 A：短回答总结任务。
- 分布 B：需要解释不确定性的问答任务。
- 分布 C：多轮对话任务。
- 对同一个 persona direction 扫强度 `0.0 → 1.4`，记录每个分布下的 sweet spot。

## 预算

- 第 1-2 天：整理 prompts 和评分脚本。
- 第 3-6 天：跑三组 sweep，记录异常案例。
- 第 7-9 天：做 off-target 分析和 stability 对比。
- 第 10-12 天：写 memo、结论和下一步建议。

## 风险与 Stop Condition

- 如果三组分布都没有清晰 sweet spot，而只有随机抖动，就停止，不继续堆更多 prompt。
- 如果评分脚本本身不稳定，先修评分，不扩实验面。
- 如果 off-target 指标持续恶化，说明当前方向不值得继续推进到更大设定。
