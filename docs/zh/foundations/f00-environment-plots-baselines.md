# F00 环境、图表与基线纪律

## 目标

把“能跑一下 notebook”推进到“能留下第一次可复查的实验记录”。

## 为什么在文章主线前学

- 如果 environment 不稳定，你后面很难区分结果变化是来自实验，还是来自运行环境。
- 如果 baseline 写不清楚，后面的 sweep、ablation 和失败分析都会变形。
- 很多初学者不是不会看论文，而是不会把 run 写成可以复盘的输入。

## 你会练什么

- 在本地和 Colab 两种环境里稳定运行 notebook。
- 区分 baseline 与 variant，而不是把一次改动写成一团。
- 看懂最基本的 loss、metric 和 seed 波动。

## Notebook 与交付

- Notebook：`notebooks/foundations/zh/f00_environment_plots_baselines.ipynb`
- 交付物：1 份 experiment log、1 张 baseline 与 variant 对比图、1 段 judgment call。

## 验收题

- 为什么一个只会“跑通”的实验，还不能叫研究输入？
- 如果 baseline 没写清楚，后面的 sweep 和 ablation 会在哪些地方失真？
- 你会用什么最小日志字段，保证两天后还能复盘这次 run？

## Lab 结论

研究的第一步不是更复杂的模型，而是把 baseline、variant 和结论边界写清楚。
