# F00 Environment, Plots, and Baseline Discipline

## Goal

Move from "I can run a notebook once" to "I can leave behind the first reproducible experiment record."

## Why learn this before the article core

- If the environment is unstable, you cannot tell whether a change came from the experiment or the runtime.
- If the baseline is underspecified, later sweeps, ablations, and failure analysis become distorted.
- Many beginners do not fail on paper reading first. They fail on turning a run into something reviewable.

## What you will practice

- Run notebooks reliably both locally and in Colab.
- Separate a baseline from a variant instead of treating every run as one blur.
- Read basic loss, metric, and seed-variance plots.

## Notebook and deliverables

- Notebook: `notebooks/foundations/en/f00_environment_plots_baselines.ipynb`
- Deliverables: one experiment log, one baseline-versus-variant plot, and one judgment call.

## Self-check

- Why is an experiment that merely runs still not a usable research input?
- If the baseline is underspecified, where do later sweeps and ablations become distorted?
- What minimum log fields would let you revisit this run two days later without guessing?

## Lab conclusion

The first step in research is not a more complex model. It is making the baseline, variant, and boundary on the claim explicit.
