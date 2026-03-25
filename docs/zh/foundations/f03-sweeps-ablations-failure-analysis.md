# F03 Sweep、Ablation 与 Failure Analysis

## 目标

把“会跑一次实验”推进到“会设计一个最小有用的实验并知道什么时候停”。

## 为什么在文章主线前学

- 真正进入研究环境后，最常见的任务不是“看懂”，而是“改一个变量家族并给判断”。
- 如果不会设计 sweep 和 ablation，你很难把 observation 变成 judgment。
- 如果不会写 failure analysis，很多 notebook 结果都会被你过度解释。

## 你会练什么

- 围绕一个变量家族设计最小 sweep。
- 把 ablation 当成排除解释的工具，而不是只是删掉一个组件。
- 写出 stop condition、failure mode 和 next step。

## Notebook 与交付

- Notebook：`notebooks/foundations/zh/f03_sweeps_ablations_failure_analysis.ipynb`
- 交付物：1 份 sweep 表格、1 张 ablation 对比图、1 份 failure-analysis memo。

## 验收题

- 什么样的 sweep 只是“多跑了几次”，还不能算实验设计？
- ablation 没有改变结果时，你会怎么判断这是负结果还是坏实验？
- 如果信号很弱，你该怎么决定停止，而不是一直追加试验？

## Lab 结论

实验设计的密度，往往比一次 run 的漂亮程度更能决定你能不能进入研究模式。
