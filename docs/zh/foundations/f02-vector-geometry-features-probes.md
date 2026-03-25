# F02 向量几何、特征与探针

## 目标

给 feature、probe 和 direction 这些词补上几何底座，避免它们只停留在抽象名词。

## 为什么在文章主线前学

- M02、M04、M08 都在用方向、投影、可分性这些几何语言。
- 如果你把 feature 只理解成“一个语义标签”，probe 很容易被看成黑箱。
- 很多“可读出”与“可控制”之间的混淆，本质上来自几何概念不清。

## 你会练什么

- 把 feature 理解成方向、投影和可分性，而不是模糊语义标签。
- 区分相似方向、混叠方向和 probe 可读出的方向。
- 用几何语言解释为什么 probe 能读出某个属性。

## Notebook 与交付

- Notebook：`notebooks/foundations/zh/f02_vector_geometry_features_probes.ipynb`
- 交付物：1 张方向与 decision boundary 图、1 段 probe 权重解释、1 份几何混叠 failure note。

## 验收题

- 如果两个特征方向高度相关，probe 的高分为什么仍然可能误导你？
- 什么时候 cosine 相似有用，什么时候它会把结构压扁？
- 把 feature 看成方向之后，你会如何重新解释 M02 里的 monosemanticity？

## Lab 结论

一旦 feature 语言落回向量几何，很多“看起来玄”的 interpretability 说法会变得更可检验。
