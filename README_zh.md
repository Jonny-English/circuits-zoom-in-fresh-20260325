# From Circuits to Claude

[**English README**](README.md) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Next.js Static Export](https://img.shields.io/badge/web-next.js-black.svg)](web/)

`From Circuits to Claude` 是一个面向初学者的双语 interpretability 教程。仓库现在改成了“文章优先”结构：核心路径里的每一篇论文，都有一份同步讲义和一份独立 Colab notebook。

仓库由三层同步组成：

- `content/course.json`：顺序、先修关系、论文链接和 artifact 引用的唯一真相源。
- `docs/zh` 与 `docs/en`：结构完全镜像的文章讲义。
- `notebooks/zh` 与 `notebooks/en`：结构完全镜像的文章 notebook，`web/` 则把同一份元数据渲染成静态课程站。

现在仓库还多了一层面向严肃学习者的内容：research-ready path，包括 12 周训练营、memo 模板、rubric 和公司研究模拟任务。

这一层的目的，是避免自学里最常见的失败模式：内容看完了，但研究习惯没有建立起来。

## 这个项目适合谁

- 适合有基础 Python / PyTorch，但几乎没有 mechanistic interpretability 背景的小白。
- 适合想从“能看懂一点论文”升级到“能在公司里承担明确研究任务”的读者。
- 不适合把它当成纯浏览型科普。它要求你写 reading note、experiment log 和 memo。

这个项目的目标产出不是“看过很多论文的人”，而是一个更接近阿里技术序列里 `P6` 能力密度的大模型研究型工程师起步者。

这里直接改成更接近阿里巴巴技术岗常见理解的 `P4-P12` 说法：

| 等级 | 对应能力 |
|---|---|
| `P4` | 校招生 / 初级工程师水平：能在明确指导下完成环境搭建、跑通 notebook、复述概念，但独立研究判断还很弱。 |
| `P5` | 工程师水平：能独立完成小范围复现、记录实验、比较 baseline 与 variant，并写出基本结论。 |
| `**P6**` | 高级工程师 / 资深 IC 起步水平：能在给定方向下承担明确研究任务，完成读论文、复现、批判、提出下一步实验。 |
| `P7` | 专家水平：能独立定义一个小方向、设计两周级研究计划，并把实验、工具和汇报串成闭环。 |
| `P8` | 高级专家水平：能负责一个研究子方向或工具线，对多名研究工程师形成稳定技术带动。 |
| `P9` | 资深专家 / Principal 水平：能定义中期研究主题，影响多个团队的判断、方法和协作方式。 |
| `P10` | 研究 Fellow / 组织级专家水平：能主导组织级研究方向，决定关键方法路线，并影响产品与安全策略。 |
| `P11` | 公司级顶层技术负责人水平：能定义长期 agenda、技术标准和人才体系。 |
| `P12` | 行业级顶尖人物水平：能显著改变整个行业对技术路线和问题框架的理解。 |

如果按这个尺度说，任何单个教学项目都不应该声称“学完就到 `P10`”。`P10` 在阿里语境里已经是非常高的组织级专家。

这门课更可信的目标是：把一个“还没进入阿里式 `P4` 状态”的小白，推进到接近 `P5`，高质量完成者可以开始摸到 `P6` 的门槛。它是研究职业路径的起点，不是终点。

## 为什么要学这个

珍妮纺纱机出现之后，行业竞争的重点就不再是“谁的手工纺纱动作更熟练”，而转向了：

- 谁更理解机器原理
- 谁更会使用机器
- 谁更会改造机器
- 谁更会围绕机器组织新的生产流程

大模型时代也一样。

当模型已经能自动完成大量局部认知工作时，最稀缺的能力不再只是“手工把每一步文字、推理、代码一点点织出来”，而是：

- 理解模型内部到底在表示什么
- 理解它为什么会成功、为什么会失败
- 理解哪些方向可以被安全地读出、干预、控制
- 理解怎样把这些判断变成研究、工具和产品决策

所以学 interpretability，不只是学一套论文话术；本质上是在学“机器智能出现之后，研究者应该如何理解机器原理并驾驭机器”。

更准确地说，AI 也只是对底层计算的又一层封装。

- 就像汇编语言是对机器语言的一层封装
- 就像高级语言又是对汇编语言的一层封装
- 大模型和 AI 系统，则是在这些计算抽象之上再包出来的一层更高抽象

正确的关注点因此不该停留在“手工完成旧流程的细碎技巧”上，而应该转向：

- 这一层封装到底暴露了什么能力
- 这一层封装隐藏了什么机制
- 我们怎样理解、使用、调试和控制这一层封装

这也是为什么这个项目既讲论文，也讲实验、artifact、steering、tracing 和研究写作。

## 一篇文章，一个 Colab

下面每一行都对应一篇文章和一份 notebook。现在每篇讲义和每本 Colab 也都带有验收题，用来帮助读者检查自己到底学到了什么。

<!-- COURSE_TABLE:START -->
| ID | 文章 | 日期 | Notebook | Colab | 运行层级 | 你会做什么 |
|---|---|---|---|---|---|---|
| `M00` | Zoom In：电路入门 | `2020-03-10` | [打开](notebooks/zh/m00_zoom_in_circuits.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m00_zoom_in_circuits.ipynb) | `warmup` | 用视觉模型建立 feature、circuit 与 intervention 的最初直觉。 |
| `M01` | Toy Models of Superposition | `2022-09-14` | [打开](notebooks/zh/m01_toy_models_superposition.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m01_toy_models_superposition.ipynb) | `cpu-colab` | 用最小 toy model 理解为什么神经元会混装多个语义。 |
| `M02` | Towards Monosemanticity | `2023-10-05` | [打开](notebooks/zh/m02_towards_monosemanticity.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m02_towards_monosemanticity.ipynb) | `cpu-colab` | 通过教学版 sparse autoencoder 理解为什么 feature 视角比 neuron 视角更稳。 |
| `M03` | Mapping the Mind | `2024-05-21` | [打开](notebooks/zh/m03_mapping_the_mind.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m03_mapping_the_mind.ipynb) | `artifact-guided` | 浏览教学版 feature catalog，理解“发现大量特征”到底意味着什么。 |
| `M04` | Features as Classifiers | `2024-10-16` | [打开](notebooks/zh/m04_features_as_classifiers.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m04_features_as_classifiers.ipynb) | `cpu-colab` | 把 feature 当成分类器输入，理解“读出”能力从哪里来。 |
| `M05` | Evaluating Feature Steering | `2024-10-25` | [打开](notebooks/zh/m05_evaluating_feature_steering.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m05_evaluating_feature_steering.ipynb) | `cpu-colab` | 扫描 steering 强度，观察 target gain、sweet spot 与 off-target cost 的平衡。 |
| `M06` | Tracing the Thoughts | `2025-03-27` | [打开](notebooks/zh/m06_tracing_thoughts.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m06_tracing_thoughts.ipynb) | `artifact-guided` | 用预计算 attribution graph 学会阅读一条局部计算路径。 |
| `M07` | Circuit Tracing Tools | `2025-05-29` | [打开](notebooks/zh/m07_circuit_tracing_tools.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m07_circuit_tracing_tools.ipynb) | `artifact-guided` | 查看 tracing artifact 与工作流拆解，理解工具层如何支撑分析。 |
| `M08` | Persona Vectors | `2025-08-01` | [打开](notebooks/zh/m08_persona_vectors.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m08_persona_vectors.ipynb) | `artifact-guided` | 通过 persona vector 的前后对比，理解 character trait 如何被表示成方向。 |
| `M09` | Signs of Introspection | `2025-10-29` | [打开](notebooks/zh/m09_signs_of_introspection.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m09_signs_of_introspection.ipynb) | `artifact-guided` | 用教学数据对比 self-report 与行为信号，讨论“内省迹象”到底意味着什么。 |
| `M10` | The Assistant Axis | `2026-01-19` | [打开](notebooks/zh/m10_assistant_axis.ipynb) | [Colab](https://colab.research.google.com/github/Jonny-English/circuits-zoom-in-fresh-20260325/blob/main/notebooks/zh/m10_assistant_axis.ipynb) | `artifact-guided` | 把不同 assistant 风格投到同一条轴上，观察 character 稳定化问题。 |
<!-- COURSE_TABLE:END -->

## 推荐路径

- `基础段`：`M00 → M01 → M02`
- `feature 段`：`M03 → M04 → M05`
- `tracing 与 character 段`：`M06 → M07 → M08 → M09 → M10`

如果你想先走最短有效路径，建议先看 `M00`、`M01`、`M02`、`M05`、`M06`。

## Research-Ready Path

如果你的目标不是“看懂”，而是“能在公司研究环境里开始做事”，请把下面这些文件和文章 notebook 一起用：

- [研究就绪总览](docs/zh/program/research-ready.md)
- [12 周训练营](docs/zh/program/week-by-week.md)
- [研究工作流](docs/zh/program/research-playbook.md)
- [评估 rubric](docs/zh/program/evaluation-rubric.md)
- [公司入职模拟](docs/zh/program/company-onramp.md)

模板：

- [Paper reading note](templates/paper_reading_note_zh.md)
- [Experiment log](templates/experiment_log_zh.md)
- [Research memo](templates/research_memo_zh.md)

把 research-ready path 当成一套工作系统，而不是额外阅读：

- 每篇文章都应该留下 reading note、experiment log、短 memo 和 next-question list。
- 这条路径默认你每周投入 `8-12` 小时的专注学习时间。
- 结营时应该拿得出真实作品集：notes、logs、memos、artifact critique 和两周 capstone proposal。
- 标准不是“我跟着 notebook 跑过了”，而是“我能读、能复现、能批判、也能提出下一步实验”。

## 快速开始

```bash
pip install -r requirements.txt

# 在修改课程元数据后，刷新派生内容
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py

# 校验 metadata、文档、notebook 镜像和外链
python3 scripts/validate_course.py
python3 scripts/check_links.py

# 执行所有生成的 notebook 烟雾测试
python3 scripts/smoke_notebooks.py
```

构建静态站：

```bash
cd web
npm install
npm run build
```

如果你更喜欢浏览器工作流，直接点上表里的 Colab 链接即可。

## 仓库结构

```text
.
├── content/               # 课程元数据与术语表
├── docs/                  # 中英文镜像文章讲义
├── notebooks/             # 旧版长 notebook + 新版文章 notebook
├── artifacts/             # 供 notebook / web 共享的 JSON artifact
├── web/                   # 静态 Next.js 课程站
├── scripts/               # notebook 生成与校验脚本
├── figures/               # M00 继续复用的视觉电路图片
└── utils/                 # 原教程留下的绘图辅助函数
```

## 原项目保留内容

原始 notebook 仍然保留在仓库中：

- `notebooks/circuits_zoom_in_zh.ipynb`
- `notebooks/circuits_zoom_in_en.ipynb`

它们现在是 `M00` 的长篇背景材料。

## 参考来源

核心阅读路径按 `2026-03-25` 的官方页面状态冻结，索引页是：

- [Anthropic Interpretability team page](https://www.anthropic.com/research/team/interpretability)
- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)
- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)

## 许可证

[MIT](LICENSE)
