# Reference Two-Week Proposal

## Research question

In the teaching setup of `M08 Persona Vectors`, does the sweet spot for persona control drift across task distributions?

## Hypothesis

If the persona direction really captures a relatively stable trait in representation space, the best intervention strength should not drift arbitrarily across task distributions. If it drifts heavily, the current direction is more like a local prompt hack than a stable control handle.

## Baseline

- Baseline assistant: no steering.
- Baseline evaluation: three trait scores for helpfulness, cautiousness, and concision, plus one off-target stability metric.

## Experiment design

- Distribution A: short summarization tasks.
- Distribution B: question answering tasks that require explicit uncertainty.
- Distribution C: multi-turn dialogue tasks.
- Sweep one persona direction from `0.0 → 1.4` and record the sweet spot under each distribution.

## Budget

- Days 1-2: finalize prompts and scoring scripts.
- Days 3-6: run the three sweeps and log abnormal cases.
- Days 7-9: compare off-target effects and stability.
- Days 10-12: write the memo, conclusion, and next-step recommendation.

## Risks and stop condition

- If none of the three distributions shows a clear sweet spot and the results only wobble randomly, stop instead of adding more prompts.
- If the scoring script itself is unstable, fix scoring before broadening the experiment.
- If off-target metrics keep worsening, the current direction is not worth pushing into a larger setup.
