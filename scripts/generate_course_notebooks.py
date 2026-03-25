#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "course.json"
SELF_CHECKS_PATH = ROOT / "content" / "self_checks.json"
OUTPUT_ROOT = ROOT / "notebooks"


def repo_root_snippet() -> str:
    return """import os
import subprocess
import sys
from pathlib import Path

REPO_URL = "https://github.com/Jonny-English/circuits-zoom-in-fresh-20260325.git"
REPO_DIR = "circuits-zoom-in-fresh-20260325"

if "google.colab" in sys.modules:
    candidate = Path("/content") / REPO_DIR
    if not candidate.exists():
        subprocess.run(["git", "clone", "--depth", "1", REPO_URL, str(candidate)], check=True)
    os.chdir(candidate)

root = Path.cwd().resolve()
while not (root / "content" / "course.json").exists():
    if root.parent == root:
        raise RuntimeError("Run this notebook from the repository root.")
    root = root.parent
"""


def markdown_cell(text: str) -> dict:
    text = text.strip("\n")
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.splitlines()],
    }


def code_cell(code: str) -> dict:
    code = code.strip("\n")
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in code.splitlines()],
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.9",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


WORKSHEETS = {
    "M00": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Name the three terms you want to leave with: feature, circuit, intervention.",
            "Pick one figure and predict what later papers will complicate or break.",
            "Open the paper-reading-note template before you run the notebook.",
        ],
        "before_zh": [
            "先写下你这篇要带走的 3 个词：feature、circuit、intervention。",
            "挑一张图，预测后续论文会在哪个地方把它复杂化或打破。",
            "运行前先打开 paper-reading-note 模板。",
        ],
        "after_en": [
            "Write one paragraph on what this visual picture explains well and what it cannot explain in language models.",
            "List the first ambiguity that appears when you try to generalize this intuition.",
        ],
        "after_zh": [
            "写一段话说明这套视觉图像擅长解释什么，又解释不了语言模型里的什么。",
            "列出当你把这套直觉推广出去时，最先出现的一个歧义点。",
        ],
        "ship_en": [
            "One reading note with a manager-summary paragraph.",
            "One glossary list of unclear terms.",
            "One next-question list for M01.",
        ],
        "ship_zh": [
            "1 份带 manager summary 的 reading note。",
            "1 份不懂术语清单。",
            "1 份通往 M01 的 next-question list。",
        ],
    },
    "M01": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Choose one variable family to change: hidden dimension, sparsity, or loss weight.",
            "Predict how the geometry should change before you run the sweep.",
            "Write the baseline settings into the experiment-log template.",
        ],
        "before_zh": [
            "先选一个变量家族：hidden dimension、sparsity 或 loss weight。",
            "在做 sweep 之前，先预测几何图像会怎么变。",
            "先把 baseline 设置写进 experiment-log 模板。",
        ],
        "after_en": [
            "State the geometric reason overlap appears in your run.",
            "Separate what the plot shows directly from the story you tell about neurons.",
        ],
        "after_zh": [
            "写清这次 run 里概念重叠出现的几何原因。",
            "把图直接展示的东西和你对 neuron 的解释分开写。",
        ],
        "ship_en": [
            "One experiment log with baseline and one sweep.",
            "One annotated plot of the hidden geometry.",
            "One 100-200 word memo on why neuron semantics break.",
        ],
        "ship_zh": [
            "1 份带 baseline 和 sweep 的 experiment log。",
            "1 张带注释的隐藏空间图。",
            "1 份 100-200 字的 memo，说明为什么 neuron semantics 会失效。",
        ],
    },
    "M02": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Choose one axis to sweep: sparsity coefficient, feature count, or noise level.",
            "Write down what 'better feature recovery' means before you look at the result.",
            "Decide which failure pattern would make you distrust the recovered features.",
        ],
        "before_zh": [
            "先选一个要扫的轴：稀疏系数、feature 数量或噪声水平。",
            "在看结果前，先定义“更好的 feature recovery”是什么意思。",
            "先写下哪种失败模式会让你不信任这些恢复出来的 feature。",
        ],
        "after_en": [
            "Compare the recovered directions to the planted dictionary and name one mismatch.",
            "Write down the boundary where monosemanticity starts to degrade in your setup.",
        ],
        "after_zh": [
            "把恢复出来的方向和真实字典对比，并指出一个不匹配点。",
            "写清在你的设定里，monosemanticity 从哪里开始变差。",
        ],
        "ship_en": [
            "One experiment log with a sweep.",
            "One short note on failure boundaries.",
            "One next experiment that would test whether the degradation is about capacity or regularization.",
        ],
        "ship_zh": [
            "1 份带 sweep 的 experiment log。",
            "1 份失败边界短说明。",
            "1 个下一步实验，用来区分问题更像是 capacity 还是 regularization。",
        ],
    },
    "M03": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Decide how you want to group the catalog: by domain, usefulness, or ambiguity.",
            "Pick one feature you expect to be easy to recover and one you expect to be missing.",
            "Open the paper-reading-note template and write the question in one sentence.",
        ],
        "before_zh": [
            "先决定你要怎么给 catalog 分组：按领域、用途还是歧义程度。",
            "提前选一个你觉得容易恢复的 feature，再选一个你觉得可能缺失的 feature。",
            "先打开 paper-reading-note 模板，用一句话写下这篇的核心问题。",
        ],
        "after_en": [
            "Write one paragraph on why a catalog changes the research style from anecdotes to cartography.",
            "Name one missing-feature question that would be worth chasing next.",
        ],
        "after_zh": [
            "写一段话说明为什么 catalog 会把研究风格从轶事变成制图。",
            "提出一个值得继续追的缺失 feature 问题。",
        ],
        "ship_en": [
            "One taxonomy note.",
            "One missing-feature question.",
            "One short memo explaining how you would prioritize the next cataloging pass.",
        ],
        "ship_zh": [
            "1 份 taxonomy note。",
            "1 个缺失 feature 问题。",
            "1 份短 memo，说明下一轮 cataloging 你会优先找什么。",
        ],
    },
    "M04": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Pick one baseline and one possible confounder before you fit the probe.",
            "Write down what high accuracy would and would not prove.",
            "Decide which feature weight you expect to dominate.",
        ],
        "before_zh": [
            "在训练 probe 之前，先定一个 baseline 和一个潜在 confounder。",
            "先写清高 accuracy 能证明什么、不能证明什么。",
            "提前判断哪个 feature 权重会占主导。",
        ],
        "after_en": [
            "Explain why the strongest probe weight might still be misleading.",
            "List three confounders or alternative explanations for the result.",
        ],
        "after_zh": [
            "解释为什么最大的 probe 权重仍然可能误导你。",
            "列出 3 个 confounders 或替代解释。",
        ],
        "ship_en": [
            "One probe memo with baseline and confounders.",
            "One figure of feature weights.",
            "One proposed follow-up label or task.",
        ],
        "ship_zh": [
            "1 份包含 baseline 和 confounders 的 probe memo。",
            "1 张 feature 权重图。",
            "1 个后续标签或任务建议。",
        ],
    },
    "M05": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Define the target metric and one off-target metric before you run the sweep.",
            "Predict roughly where the sweet spot should appear.",
            "Write the stop condition for a bad steering direction.",
        ],
        "before_zh": [
            "在跑 sweep 之前，先定义 target metric 和一个 off-target metric。",
            "提前预测 sweet spot 大概会落在哪一段。",
            "先写下一个坏 steering 方向的 stop condition。",
        ],
        "after_en": [
            "Identify where benefit and collateral cost stop moving together.",
            "State the smallest steering strength you would ship and why.",
        ],
        "after_zh": [
            "指出收益和副作用开始不再同步变化的位置。",
            "写下如果要上线，你会选择的最小 steering strength 以及理由。",
        ],
        "ship_en": [
            "One steering evaluation memo.",
            "One explicit off-target metric.",
            "One failure-analysis paragraph on where the sweep becomes untrustworthy.",
        ],
        "ship_zh": [
            "1 份 steering evaluation memo。",
            "1 个明确写出的 off-target metric。",
            "1 段 failure analysis，说明从哪里开始这个 sweep 不再可信。",
        ],
    },
    "M06": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Choose one path or subgraph you plan to explain in detail.",
            "Write down what a faithful slice of computation means in this context.",
            "Open the memo template and reserve a section called 'what the graph does not prove'.",
        ],
        "before_zh": [
            "先挑一条你准备详细解释的路径或子图。",
            "先写下在这个语境里，什么叫 faithful slice of computation。",
            "打开 memo 模板，预留一段“这张图还不能证明什么”。",
        ],
        "after_en": [
            "Explain three high-contribution edges in plain language.",
            "Mark one ambiguity that would require a follow-up experiment.",
        ],
        "after_zh": [
            "用自己的话解释 3 条高贡献边。",
            "标出一个必须靠后续实验才能消除的歧义。",
        ],
        "ship_en": [
            "One graph walkthrough.",
            "One ambiguity note.",
            "One next experiment that would reduce uncertainty about the graph.",
        ],
        "ship_zh": [
            "1 份 graph walkthrough。",
            "1 份 ambiguity note。",
            "1 个能降低这张图不确定性的下一步实验。",
        ],
    },
    "M07": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Write the workflow stages you expect before loading the artifact.",
            "Pick one point in the pipeline where cost or latency might dominate.",
            "Decide what output a research engineer would actually need from the tool.",
        ],
        "before_zh": [
            "在加载 artifact 之前，先写下你预期的 workflow 阶段。",
            "提前挑一个你觉得成本或延迟会占主导的位置。",
            "先想清楚研究工程师真正需要工具输出什么。",
        ],
        "after_en": [
            "Point to the bottleneck that most shapes what research can be asked.",
            "Write one concrete tooling improvement request.",
        ],
        "after_zh": [
            "指出最会改变研究问题形状的那个 bottleneck。",
            "写一个具体的工具改进请求。",
        ],
        "ship_en": [
            "One workflow diagram.",
            "One bottleneck analysis.",
            "One tooling-needs note that could be handed to an engineer.",
        ],
        "ship_zh": [
            "1 张 workflow 图。",
            "1 份 bottleneck analysis。",
            "1 份可以直接交给工程师的 tooling-needs note。",
        ],
    },
    "M08": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Pick one trait you care about before looking at the artifact.",
            "Predict whether vector similarity should line up with behavioral similarity.",
            "Write one risk of controlling character through a direction.",
        ],
        "before_zh": [
            "在看 artifact 前，先选一个你最关心的 trait。",
            "预测向量相似度是否应该和行为相似度对齐。",
            "先写一条通过方向控制 character 的风险。",
        ],
        "after_en": [
            "Compare before/after trait shifts and say which one looks most controllable.",
            "State one reason persona control might drift or destabilize.",
        ],
        "after_zh": [
            "比较前后 trait 变化，并说哪个 trait 看起来最可控。",
            "写出 persona control 可能漂移或失稳的一个原因。",
        ],
        "ship_en": [
            "One short memo on what persona vectors make legible.",
            "One risk paragraph.",
            "One follow-up question about stability.",
        ],
        "ship_zh": [
            "1 份短 memo，说明 persona vectors 让什么变得可读。",
            "1 段风险说明。",
            "1 个关于稳定性的后续问题。",
        ],
    },
    "M09": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Predict where self-report and behavior should diverge most strongly.",
            "Write one warning against over-interpreting introspection-like signals.",
            "Decide which mismatch would be most interesting if it appeared.",
        ],
        "before_zh": [
            "先预测 self-report 和 behavior 最可能在哪些地方明显分叉。",
            "先写一条不要过度解释 introspection-like signals 的提醒。",
            "提前决定哪一种 mismatch 最值得研究。",
        ],
        "after_en": [
            "Rank the mismatch cases and explain why the top case matters.",
            "Write what evidence would be needed before making a stronger introspection claim.",
        ],
        "after_zh": [
            "给 mismatch 案例排个序，并解释为什么排第一的最重要。",
            "写出如果要提出更强的 introspection claim，还需要哪些证据。",
        ],
        "ship_en": [
            "One critique separating self-report from internal-state claims.",
            "One follow-up experiment idea.",
            "One short memo on the strongest mismatch.",
        ],
        "ship_zh": [
            "1 份 critique，把 self-report 和内部状态 claim 分开。",
            "1 个 follow-up experiment 想法。",
            "1 份关于最强 mismatch 的短 memo。",
        ],
    },
    "M10": {
        "title_en": "Research worksheet",
        "title_zh": "研究工作单",
        "before_en": [
            "Predict how axis position should relate to helpfulness, safety, and warmth.",
            "Choose one failure mode of trying to stabilize assistant character.",
            "Write down one reason a single axis might be too simple.",
        ],
        "before_zh": [
            "先预测轴位置和 helpfulness、safety、warmth 之间会是什么关系。",
            "先挑一个稳定 assistant character 时可能出现的 failure mode。",
            "先写下一条“单一轴可能太简单”的理由。",
        ],
        "after_en": [
            "Explain what moves smoothly along the axis and what does not.",
            "State one reason character control may require a manifold rather than a single direction.",
        ],
        "after_zh": [
            "解释哪些属性会沿着这条轴平滑变化，哪些不会。",
            "写出为什么 character control 可能需要一个流形，而不是单一方向。",
        ],
        "ship_en": [
            "One short memo on what the axis captures.",
            "One failure-mode note.",
            "One two-week proposal idea for character stabilization.",
        ],
        "ship_zh": [
            "1 份短 memo，说明这条轴到底捕捉了什么。",
            "1 份 failure-mode note。",
            "1 个关于 character stabilization 的两周提案想法。",
        ],
    },
}

SELF_CHECKS = {
    entry["module_id"]: entry
    for entry in json.loads(SELF_CHECKS_PATH.read_text())
}


def bullet_block(heading: str, items: list[str]) -> str:
    return "\n".join([heading, "", *[f"- {item}" for item in items]])


def research_cells(module_id: str, language: str) -> list[dict]:
    worksheet = WORKSHEETS[module_id]
    title = worksheet["title_en"] if language == "en" else worksheet["title_zh"]
    before = worksheet["before_en"] if language == "en" else worksheet["before_zh"]
    after = worksheet["after_en"] if language == "en" else worksheet["after_zh"]
    ship = worksheet["ship_en"] if language == "en" else worksheet["ship_zh"]
    headings = {
        "en": ("## Turn this notebook into research output", "### Before you run", "### After you run", "### Ship these artifacts"),
        "zh": ("## 把这本 notebook 变成研究产出", "### 运行前", "### 运行后", "### 最后交付这些产物"),
    }
    intro_heading, before_heading, after_heading, ship_heading = headings[language]
    intro = (
        f"{intro_heading}\n\n"
        f"{title} means this notebook is not complete when the cells finish. "
        f"{'Use the templates in /templates and leave behind written outputs.' if language == 'en' else '请配合 /templates 里的模板，把结果写成可复查的输出。'}"
    )
    return [
        markdown_cell(intro),
        markdown_cell(bullet_block(before_heading, before)),
        markdown_cell(bullet_block(after_heading, after)),
        markdown_cell(bullet_block(ship_heading, ship)),
    ]


def self_check_cells(module_id: str, language: str) -> list[dict]:
    payload = SELF_CHECKS[module_id]
    questions = payload["questions_en"] if language == "en" else payload["questions_zh"]
    title = "## Self-check questions" if language == "en" else "## 验收题"
    pass_line = (
        "If you cannot answer at least two of these without rereading the note, revisit the article and your written outputs."
        if language == "en"
        else "如果你不能在不重看讲义的情况下独立答出其中至少 2 题，就回去重看文章和你的书面输出。"
    )
    return [markdown_cell(bullet_block(title, questions + [pass_line]))]


def m00(language: str) -> list[dict]:
    intro = """
# M00 Zoom In: An Introduction to Circuits

Start with the cleanest picture in the course: visible neurons, visible motifs, visible circuits.
""" if language == "en" else """
# M00 Zoom In：电路入门

先从整门课里最干净的图像开始：可见的神经元、可见的模式、可见的局部电路。
"""
    context = """
## What this notebook does

- Revisits the four key figures from the original tutorial.
- Uses them to define feature, circuit, and universality.
- Establishes the intuition that later papers will complicate.
""" if language == "en" else """
## 本 notebook 会做什么

- 重看原始教程最关键的 4 张图。
- 用它们定义 feature、circuit 和 universality。
- 先建立一个后续论文会不断打破和修正的直觉。
"""
    code = repo_root_snippet() + """
import matplotlib.pyplot as plt
from PIL import Image

figure_specs = [
    ("feature_viz_grid.png", "Feature visualization"),
    ("polar_tuning.png", "Orientation tuning"),
    ("circuit_diagram.png", "Circuit composition"),
    ("universality_comparison.png", "Universality"),
]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, (filename, title) in zip(axes.flatten(), figure_specs):
    image = Image.open(root / "figures" / filename)
    ax.imshow(image)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
"""
    takeaway = """
## Takeaway

Visual circuits are a warm-up, not the final destination. Keep this picture in mind when the next notebook shows why neurons stop behaving so cleanly.
""" if language == "en" else """
## 小结

视觉电路只是热身，不是终点。后面一旦开始谈 superposition，这幅干净图像就会被重新解释。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m01(language: str) -> list[dict]:
    intro = """
# M01 Toy Models of Superposition
""" if language == "en" else """
# M01 Toy Models of Superposition
"""
    context = """
## Toy setup

Compress four sparse concepts into a two-dimensional hidden space and inspect how overlap appears.
""" if language == "en" else """
## Toy 设定

把 4 个稀疏概念压进 2 维隐藏空间，观察概念重叠是怎么出现的。
"""
    code = """
import torch
import matplotlib.pyplot as plt

torch.manual_seed(7)

num_features = 4
hidden_dim = 2
encoder = torch.nn.Linear(num_features, hidden_dim, bias=False)
decoder = torch.nn.Linear(hidden_dim, num_features, bias=False)
optimizer = torch.optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=0.05)

for step in range(500):
    active = (torch.rand(512, num_features) < 0.22).float()
    strengths = torch.rand(512, num_features)
    batch = active * strengths
    hidden = encoder(batch)
    recon = decoder(hidden)
    loss = torch.nn.functional.mse_loss(recon, batch) + 0.002 * hidden.abs().mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

samples = torch.eye(num_features)
hidden_samples = encoder(samples).detach()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].scatter(hidden_samples[:, 0], hidden_samples[:, 1], s=130, c=range(num_features), cmap="tab10")
for index, point in enumerate(hidden_samples):
    axes[0].annotate(f"f{index}", (point[0].item(), point[1].item()))
axes[0].set_title("Feature positions in 2D hidden space")
axes[0].axhline(0, color="0.8", linewidth=1)
axes[0].axvline(0, color="0.8", linewidth=1)

axes[1].imshow(decoder.weight.detach().T, cmap="coolwarm", aspect="auto")
axes[1].set_title("Decoder weights")
axes[1].set_xlabel("Hidden dimension")
axes[1].set_ylabel("Original feature")
plt.tight_layout()

print("Final loss:", float(loss.detach()))
print("Hidden representations:\\n", hidden_samples)
"""
    takeaway = """
## Takeaway

Once the hidden space is smaller than the concept set, overlap stops being a bug and becomes the expected geometry.
""" if language == "en" else """
## 小结

一旦隐藏空间小于概念集合，重叠就不再是 bug，而会变成预期中的几何结构。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m02(language: str) -> list[dict]:
    intro = """
# M02 Towards Monosemanticity
""" if language == "en" else """
# M02 Towards Monosemanticity
"""
    context = """
## Sparse autoencoder toy lab

Generate activations from a hidden dictionary, then train a tiny sparse autoencoder to recover reusable directions.
""" if language == "en" else """
## Sparse autoencoder 教学实验

先用一个隐藏字典生成激活，再训练一个小型 sparse autoencoder 去恢复可复用方向。
"""
    code = """
import torch
import matplotlib.pyplot as plt

torch.manual_seed(11)

activation_dim = 6
true_features = 4
sae_features = 8

true_dictionary = torch.tensor(
    [
        [1.0, 0.0, 0.0, 0.5],
        [0.8, 0.1, 0.2, 0.0],
        [0.0, 0.9, 0.1, 0.4],
        [0.0, 0.8, 0.4, 0.1],
        [0.3, 0.0, 0.9, 0.2],
        [0.1, 0.2, 0.8, 1.0],
    ],
    dtype=torch.float32,
)

encoder = torch.nn.Linear(activation_dim, sae_features)
decoder = torch.nn.Linear(sae_features, activation_dim, bias=False)
optimizer = torch.optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=0.03)

for step in range(700):
    sparse_codes = (torch.rand(256, true_features) < 0.28).float() * torch.rand(256, true_features)
    activations = sparse_codes @ true_dictionary.T + 0.02 * torch.randn(256, activation_dim)
    hidden = torch.relu(encoder(activations))
    recon = decoder(hidden)
    loss = torch.nn.functional.mse_loss(recon, activations) + 0.01 * hidden.mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

decoder_weights = decoder.weight.detach().T
norms = decoder_weights.norm(dim=1)
top_indices = torch.topk(norms, k=4).indices

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].imshow(true_dictionary, cmap="viridis", aspect="auto")
axes[0].set_title("Ground-truth dictionary")
axes[0].set_xlabel("Feature")
axes[0].set_ylabel("Activation dimension")

axes[1].imshow(decoder_weights[top_indices], cmap="viridis", aspect="auto")
axes[1].set_title("Recovered decoder directions (top 4)")
axes[1].set_xlabel("Activation dimension")
axes[1].set_ylabel("Recovered feature")
plt.tight_layout()

print("Top recovered feature indices:", top_indices.tolist())
print("Final loss:", float(loss.detach()))
"""
    takeaway = """
## Takeaway

The recovered directions are not perfect copies of the planted dictionary, but they are much easier to reuse and reason about than the raw basis.
""" if language == "en" else """
## 小结

恢复出来的方向不会完美等于埋进去的字典，但它们比原始基底更容易复用，也更容易讲清楚。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m03(language: str) -> list[dict]:
    intro = """
# M03 Mapping the Mind of a Large Language Model
""" if language == "en" else """
# M03 Mapping the Mind
"""
    context = """
## Browse a teaching-scale feature catalog

This notebook loads a tiny catalog of features and groups them by domain so you can see the shift from isolated examples to feature maps.
""" if language == "en" else """
## 浏览教学版 feature catalog

这本 notebook 读取一个小型 feature 目录，并按领域分组，展示 interpretability 如何从零散例子走向 feature 地图。
"""
    code = repo_root_snippet() + """
import json
from collections import Counter
import matplotlib.pyplot as plt

payload = json.loads((root / "artifacts" / "m03_feature_catalog.json").read_text())
features = payload["features"]
domain_counts = Counter(feature["domain_en"] for feature in features)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(domain_counts.keys(), domain_counts.values(), color="#1f5f8b")
axes[0].set_title("Features per domain")
axes[0].tick_params(axis="x", rotation=20)

top_features = sorted(features, key=lambda item: item["max_activation"], reverse=True)
axes[1].bar(
    [feature["label_en"] for feature in top_features],
    [feature["max_activation"] for feature in top_features],
    color="#c96a28",
)
axes[1].set_title("Maximum activation by feature")
axes[1].tick_params(axis="x", rotation=35)
plt.tight_layout()

print("Top feature cards:")
for feature in top_features:
    print("-", feature["label_en"], "|", feature["domain_en"], "|", feature["max_activation"])
    for example in feature["examples_en"]:
        print("   ", example)
"""
    takeaway = """
## Takeaway

Once features can be grouped, ranked, and browsed, interpretability starts looking like cartography instead of isolated case studies.
""" if language == "en" else """
## 小结

一旦 feature 可以被分组、排序和浏览，interpretability 看起来就更像制图，而不再只是孤立案例。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m04(language: str) -> list[dict]:
    intro = """
# M04 Using Dictionary Learning Features as Classifiers
""" if language == "en" else """
# M04 Features as Classifiers
"""
    context = """
## Probe on top of features

Train a tiny classifier on synthetic feature activations and inspect which recovered directions matter most.
""" if language == "en" else """
## 在 feature 上做 probe

在 synthetic feature activation 上训练一个小分类器，看看哪些恢复出的方向最重要。
"""
    code = """
import torch
import matplotlib.pyplot as plt

torch.manual_seed(31)

feature_names = ["calendar", "citation", "refusal", "tool"]
features = torch.randn(400, 4)
target = 1.4 * features[:, 2] + 0.8 * features[:, 3] - 0.9 * features[:, 1]
labels = (torch.sigmoid(target) > 0.5).float().unsqueeze(1)

probe = torch.nn.Linear(4, 1)
optimizer = torch.optim.Adam(probe.parameters(), lr=0.05)

for step in range(500):
    logits = probe(features)
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    probs = torch.sigmoid(probe(features))
    accuracy = ((probs > 0.5).float() == labels).float().mean().item()
    weights = probe.weight.flatten()

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(feature_names, weights.tolist(), color=["#4c78a8", "#9ecae9", "#f58518", "#54a24b"])
ax.axhline(0, color="0.75", linewidth=1)
ax.set_title("Probe weights over recovered features")
plt.tight_layout()

print("Final BCE loss:", float(loss.detach()))
print("Accuracy:", round(accuracy, 3))
print("Weights:", dict(zip(feature_names, [round(value, 3) for value in weights.tolist()])))
"""
    takeaway = """
## Takeaway

Feature quality becomes measurable once features can support a readout task.
""" if language == "en" else """
## 小结

一旦 feature 可以支撑读出任务，feature 的质量就开始变得可衡量。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m05(language: str) -> list[dict]:
    intro = """
# M05 Evaluating Feature Steering
""" if language == "en" else """
# M05 Evaluating Feature Steering
"""
    context = """
## Sweep steering strength

Simulate how target improvement and off-target cost change as you move farther along a steering direction.
""" if language == "en" else """
## 扫描 steering 强度

模拟沿着 steering 方向越走越远时，目标增益和副作用成本如何一起变化。
"""
    code = """
import torch
import matplotlib.pyplot as plt

strengths = torch.linspace(-1.2, 1.6, 28)
target_gain = torch.sigmoid(2.9 * (strengths - 0.05))
off_target = 0.06 + 0.24 * torch.relu(strengths - 0.25) ** 2
utility = target_gain - off_target
best_index = int(torch.argmax(utility))

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(strengths.tolist(), target_gain.tolist(), label="target gain", color="#1f5f8b", linewidth=2.4)
ax.plot(strengths.tolist(), off_target.tolist(), label="off-target cost", color="#c96a28", linewidth=2.4)
ax.plot(strengths.tolist(), utility.tolist(), label="net utility", color="#2c7a4b", linewidth=2.4)
ax.axvline(float(strengths[best_index]), color="0.55", linestyle="--")
ax.set_title("Steering sweep")
ax.set_xlabel("steering strength")
ax.legend()
plt.tight_layout()

print("Best steering strength:", round(float(strengths[best_index]), 3))
print("Target gain there:", round(float(target_gain[best_index]), 3))
print("Off-target cost there:", round(float(off_target[best_index]), 3))
"""
    takeaway = """
## Takeaway

Steering becomes useful only when you can identify where benefit peaks before collateral effects dominate.
""" if language == "en" else """
## 小结

只有在你能找到收益先达到峰值、而副作用还没占上风的位置时，steering 才真正有用。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m06(language: str) -> list[dict]:
    intro = """
# M06 Tracing the Thoughts of a Large Language Model
""" if language == "en" else """
# M06 Tracing the Thoughts
"""
    context = """
## Read a local attribution graph

Load a teaching artifact and inspect which paths contribute most strongly to the final answer.
""" if language == "en" else """
## 阅读一张局部 attribution graph

加载教学 artifact，检查哪些路径对最终答案的贡献最大。
"""
    code = repo_root_snippet() + """
import json
import matplotlib.pyplot as plt

graph = json.loads((root / "artifacts" / "m06_attribution_graph.json").read_text())
case = graph["cases"][0]

fig, ax = plt.subplots(figsize=(10, 4))
for edge in case["edges"]:
    source = next(node for node in case["nodes"] if node["id"] == edge["source"])
    target = next(node for node in case["nodes"] if node["id"] == edge["target"])
    ax.plot(
        [source["x"], target["x"]],
        [source["y"], target["y"]],
        linewidth=2 + 4 * edge["score"],
        color="#c96a28",
        alpha=0.65,
    )

for node in case["nodes"]:
    color = "#123b63" if node["kind"] == "feature" else "#b5893a"
    ax.scatter(node["x"], node["y"], s=700, color=color)
    ax.text(node["x"], node["y"], node["label_en"], ha="center", va="center", color="white", fontsize=9)

ax.set_title(case["title_en"])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
plt.tight_layout()

sorted_edges = sorted(case["edges"], key=lambda edge: edge["score"], reverse=True)
print("Top contributions:")
for edge in sorted_edges:
    print(f"  {edge['source']} -> {edge['target']}: {edge['score']:.2f}")
"""
    takeaway = """
## Takeaway

Tracing is about finding a faithful slice of computation, not about dumping the whole network.
""" if language == "en" else """
## 小结

tracing 的重点是找出一块忠实的计算切片，而不是把整个网络都摊出来。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m07(language: str) -> list[dict]:
    intro = """
# M07 Open-sourcing Circuit Tracing Tools
""" if language == "en" else """
# M07 Circuit Tracing Tools
"""
    context = """
## Inspect the workflow behind the graph

Load the tracing workflow and compare it to the edge-score distribution in the shared attribution artifact.
""" if language == "en" else """
## 看图背后的工作流

加载 tracing 工作流，并把它和共享 attribution artifact 里的边分数分布对照起来。
"""
    code = repo_root_snippet() + """
import json
import matplotlib.pyplot as plt

workflow = json.loads((root / "artifacts" / "m07_tracing_tool_workflow.json").read_text())
graph = json.loads((root / "artifacts" / "m06_attribution_graph.json").read_text())
edge_scores = [edge["score"] for case in graph["cases"] for edge in case["edges"]]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(
    [step["title_en"] for step in workflow["steps"]],
    [step["estimated_minutes"] for step in workflow["steps"]],
    color="#1f5f8b",
)
axes[0].set_title("Workflow stages")
axes[0].tick_params(axis="x", rotation=24)

axes[1].hist(edge_scores, bins=6, color="#c96a28", edgecolor="white")
axes[1].set_title("Edge score distribution")
axes[1].set_xlabel("score")
plt.tight_layout()

print("Workflow outputs:")
for step in workflow["steps"]:
    print("-", step["title_en"], "->", step["output"], f"({step['estimated_minutes']} min)")
"""
    takeaway = """
## Takeaway

Tooling decides what traces are available, how expensive they are to produce, and how readable they become.
""" if language == "en" else """
## 小结

工具层会决定你能得到什么 trace、它们有多贵，以及最后到底好不好读。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m08(language: str) -> list[dict]:
    intro = """
# M08 Persona Vectors
""" if language == "en" else """
# M08 Persona Vectors
"""
    context = """
## Compare trait shifts

Load a small persona-vector artifact and compare trait scores before and after a light intervention.
""" if language == "en" else """
## 比较 trait 的变化

加载一个小型 persona-vector artifact，比较轻量干预前后的 trait score。
"""
    code = repo_root_snippet() + """
import json
import math
import matplotlib.pyplot as plt

payload = json.loads((root / "artifacts" / "m08_persona_vectors.json").read_text())
traits = ["helpful", "cautious", "concise"]

fig, axes = plt.subplots(1, len(payload["personas"]), figsize=(12, 4), sharey=True)
for ax, persona in zip(axes, payload["personas"]):
    before = [persona["scores_before"][trait] for trait in traits]
    after = [persona["scores_after"][trait] for trait in traits]
    x = range(len(traits))
    ax.bar([index - 0.16 for index in x], before, width=0.32, label="before", color="#999999")
    ax.bar([index + 0.16 for index in x], after, width=0.32, label="after", color="#1f5f8b")
    ax.set_xticks(list(x))
    ax.set_xticklabels(traits, rotation=20)
    ax.set_ylim(0, 1)
    ax.set_title(persona["label_en"])

axes[0].legend()
plt.tight_layout()

def cosine(values_a, values_b):
    numerator = sum(a * b for a, b in zip(values_a, values_b))
    denom = math.sqrt(sum(a * a for a in values_a) * sum(b * b for b in values_b))
    return numerator / denom

reference = payload["personas"][0]
for persona in payload["personas"][1:]:
    score = cosine(reference["vector"], persona["vector"])
    print(f"cosine({reference['label_en']}, {persona['label_en']}) = {score:.3f}")
"""
    takeaway = """
## Takeaway

Persona vectors make character legible enough to compare, monitor, and lightly perturb.
""" if language == "en" else """
## 小结

persona vector 让 character 变得足够可读，从而可以比较、监控和轻量干预。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m09(language: str) -> list[dict]:
    intro = """
# M09 Signs of Introspection in Large Language Models
""" if language == "en" else """
# M09 Signs of Introspection
"""
    context = """
## Compare self-report and behavior

Load teaching cases and inspect where the model's self-description matches or diverges from observed behavior.
""" if language == "en" else """
## 对比 self-report 和行为

加载教学案例，观察模型对自身的描述和可观察行为在哪些地方一致、在哪些地方分叉。
"""
    code = repo_root_snippet() + """
import json
import matplotlib.pyplot as plt

payload = json.loads((root / "artifacts" / "m09_introspection_signals.json").read_text())
cases = payload["cases"]

fig, ax = plt.subplots(figsize=(7, 5))
for case in cases:
    ax.scatter(case["self_report"], case["behavior_signal"], s=160, color="#1f5f8b")
    ax.annotate(case["id"], (case["self_report"], case["behavior_signal"]))

ax.plot([0, 1], [0, 1], linestyle="--", color="0.6")
ax.set_xlim(0.3, 0.95)
ax.set_ylim(0.3, 0.95)
ax.set_xlabel("self-report signal")
ax.set_ylabel("behavior signal")
ax.set_title("Where self-report and behavior align")
plt.tight_layout()

print("Largest mismatches:")
for case in sorted(cases, key=lambda item: abs(item["self_report"] - item["behavior_signal"]), reverse=True):
    gap = abs(case["self_report"] - case["behavior_signal"])
    print("-", case["id"], "gap=", round(gap, 3))
"""
    takeaway = """
## Takeaway

The most informative cases are often the mismatches between self-description and behavior.
""" if language == "en" else """
## 小结

最值得盯住的，往往不是自我描述和行为一致的地方，而是它们错开的地方。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


def m10(language: str) -> list[dict]:
    intro = """
# M10 The Assistant Axis
""" if language == "en" else """
# M10 The Assistant Axis
"""
    context = """
## Project assistant styles onto one shared axis

Use a small teaching artifact to compare assistant variants by axis position, helpfulness, and safety.
""" if language == "en" else """
## 把不同 assistant 风格投到同一条轴上

用一个小型教学 artifact 比较不同 assistant 变体在轴位置、helpfulness 和 safety 上的差异。
"""
    code = repo_root_snippet() + """
import json
import matplotlib.pyplot as plt

payload = json.loads((root / "artifacts" / "m10_assistant_axis.json").read_text())
assistants = payload["assistants"]

fig, ax = plt.subplots(figsize=(8, 5))
for assistant in assistants:
    ax.scatter(
        assistant["axis_position"],
        assistant["helpfulness"],
        s=200 + assistant["safety"] * 120,
        color="#c96a28",
        alpha=0.8,
    )
    ax.annotate(assistant["label_en"], (assistant["axis_position"], assistant["helpfulness"]))

ax.set_xlabel("assistant-axis position")
ax.set_ylabel("helpfulness")
ax.set_title("Assistant variants in a shared frame")
ax.axvline(0, color="0.75", linewidth=1)
plt.tight_layout()

print("Ordered by axis position:")
for assistant in sorted(assistants, key=lambda item: item["axis_position"]):
    print("-", assistant["label_en"], "| axis =", assistant["axis_position"], "| safety =", assistant["safety"])
"""
    takeaway = """
## Takeaway

Stabilizing character means controlling a whole style manifold, not only one local trait.
""" if language == "en" else """
## 小结

稳定 character 的问题，不是只调一个局部 trait，而是要面对整块风格流形。
"""
    return [markdown_cell(intro), markdown_cell(context), code_cell(code), markdown_cell(takeaway)]


NOTEBOOK_BUILDERS = {
    "M00": m00,
    "M01": m01,
    "M02": m02,
    "M03": m03,
    "M04": m04,
    "M05": m05,
    "M06": m06,
    "M07": m07,
    "M08": m08,
    "M09": m09,
    "M10": m10,
}


def write_notebook(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook(cells), ensure_ascii=False, indent=2))


def clean_generated_notebooks() -> None:
    for language in ("en", "zh"):
        language_root = OUTPUT_ROOT / language
        language_root.mkdir(parents=True, exist_ok=True)
        for path in language_root.glob("m*.ipynb"):
            path.unlink()


def main() -> None:
    course = json.loads(COURSE_PATH.read_text())
    clean_generated_notebooks()
    for module in course:
        builder = NOTEBOOK_BUILDERS[module["id"]]
        filename = f"{module['id'].lower()}_{module['web_slug'].replace('-', '_')}.ipynb"
        for language in ("en", "zh"):
            path = OUTPUT_ROOT / language / filename
            cells = builder(language) + research_cells(module["id"], language) + self_check_cells(module["id"], language)
            write_notebook(path, cells)
            print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
