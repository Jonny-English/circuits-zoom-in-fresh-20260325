# 仓库地图

如果你不想先把整个 README 看完，而是想先搞清楚这个仓库到底怎么组织，就看这页。

## 读者入口

- 如果你是小白、环境还不稳，先看 [foundations/index.md](foundations/index.md)。
- 如果你已经能跑 notebook，就先从 [index.md](index.md) 和 live 主线进入。
- 如果你要走完整长期路径，就去 [program/research-ready.md](program/research-ready.md)。

## 顶层结构

```text
.
├── content/      # 课程、训练营、参考输出、术语表的真相源 metadata
├── docs/         # 中英文镜像讲义、索引页、训练营文档
├── notebooks/    # 可运行 notebooks：主线、基础包、扩展轨道，以及旧版长 notebook
├── examples/     # 校准 memo / log / proposal 密度的参考输出
├── templates/    # 空白 reading note、experiment log、memo 模板
├── artifacts/    # 只读参考数据；严格 live notebook 不允许依赖这里
├── scripts/      # README 渲染、notebook 生成、校验与策略检查
├── figures/      # M00 继续复用的旧版视觉电路图片
├── utils/        # 从原始教程保留下来的绘图辅助函数
└── launch/       # release notes 和发布文案草稿；不属于学习主线
```

## 哪些文件是真相源

- [content/course.json](../../content/course.json)：文章顺序、状态、先修关系和论文信息
- [content/foundations.json](../../content/foundations.json)：基础包 labs
- [content/program.json](../../content/program.json)：research-ready 路径、周计划和毕业规则
- [content/extensions.json](../../content/extensions.json)：扩展论文轨道
- [content/reference_outputs.json](../../content/reference_outputs.json)：参考输出样例

如果你要改课程结构，先改这些文件，不要先改生成出来的表格。

## 哪些内容是派生出来的

- [README.md](../../README.md) 和 [README_zh.md](../../README_zh.md) 里的表格是渲染结果
- `notebooks/en`、`notebooks/zh`、`notebooks/foundations`、`notebooks/extensions` 里的 runnable notebooks 也是生成出来的

只要 metadata 改了，就应该刷新这些派生面，而不是手工改它们。

## 维护命令

```bash
pip install -r requirements.txt
python3 scripts/render_readmes.py
python3 scripts/generate_course_notebooks.py
python3 scripts/validate_course.py
python3 scripts/audit_realtime_policy.py
python3 scripts/check_links.py
python3 scripts/smoke_notebooks.py
```

## 非主线材料

- [notebooks/circuits_zoom_in_zh.ipynb](../../notebooks/circuits_zoom_in_zh.ipynb)
- [notebooks/circuits_zoom_in_en.ipynb](../../notebooks/circuits_zoom_in_en.ipynb)

这两个是旧版的长篇背景 notebook，现在主要作为 `M00` 的背景材料保留，不再是主导航入口。

## 关键导航页

- [program/research-ready.md](program/research-ready.md)
- [program/p6-graduation-checklist.md](program/p6-graduation-checklist.md)
- [extensions/index.md](extensions/index.md)
- [foundations/index.md](foundations/index.md)

如果你还是觉得仓库太乱，就先只看这四页，再加上 [index.md](index.md)，其他内容等需要时再进。
