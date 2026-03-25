# F03 Sweeps, Ablations, and Failure Analysis

## Goal

Move from "I can run one experiment" to "I can design the smallest useful experiment and know when to stop."

## Why learn this before the article core

- Once you enter a real research environment, the common task is not "understand this" but "change one variable family and give me a judgment."
- If you cannot design sweeps and ablations, it is hard to turn observation into judgment.
- If you cannot write failure analysis, you will over-interpret many notebook results.

## What you will practice

- Design the smallest useful sweep around one variable family.
- Use ablations to rule out explanations instead of merely deleting a component.
- Write down a stop condition, a failure mode, and the next step.

## Notebook and deliverables

- Notebook: `notebooks/foundations/en/f03_sweeps_ablations_failure_analysis.ipynb`
- Deliverables: one sweep table, one ablation comparison plot, and one failure-analysis memo.

## Self-check

- What kind of sweep is merely "running a few more times" rather than actual experiment design?
- When an ablation does not change the result, how do you tell a negative result from a bad experiment?
- If the signal is weak, how do you decide to stop instead of appending more trials forever?

## Lab conclusion

The density of your experiment design often matters more for research mode than the beauty of one single run.
