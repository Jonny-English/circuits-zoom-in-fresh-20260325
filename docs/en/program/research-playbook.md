# Research Playbook

Use this playbook whenever an article or notebook starts feeling too open-ended. The goal is to force work into a repeatable research loop.

## The core loop

Every project in this repository should move through the same sequence:

1. State the question
2. State the hypothesis
3. State the baseline
4. Run the smallest useful experiment
5. Log what changed
6. Separate observation from interpretation
7. Decide the next experiment

If one of these steps is missing, the work will usually become vague very quickly.

## Paper-reading protocol

Read each paper in five passes:

1. Abstract and introduction: what problem is this paper actually trying to solve?
2. Figure pass: what is the strongest figure and what claim is it carrying?
3. Method pass: what intervention, representation, or training move is doing the work?
4. Evidence pass: what evidence would fail if the paper were wrong?
5. Limitation pass: what does the paper explicitly not show?

Your reading note should not look like a summary of every section. It should look like a decision aid.

## Reproduction protocol

When you reproduce a notebook:

- run the baseline first
- record seed, major hyperparameters, and environment
- change only one variable family at a time
- keep the smallest figure or table that lets you compare baseline versus variant
- write down failure before you normalize it away

The point of reproduction is not only to "get the same picture." It is to learn what changes matter.

## Ablation ladder

When you are unsure what to change next, move down this ladder:

1. Change scale: strength, sparsity, temperature, coefficient
2. Change capacity: number of features, hidden dimension, dataset size
3. Change noise or corruption
4. Change metric or evaluation target
5. Change the task itself

Beginners often jump to step 5 too early. Stay on the smallest useful rung.

## Evidence discipline

Every writeup should separate these three categories:

- Observation: what the run or artifact directly shows
- Inference: the most cautious interpretation of the observation
- Speculation: a wider story that still needs more evidence

This separation is one of the fastest ways to sound like a researcher instead of a fan.

## Failure-analysis prompts

When a result looks weak, ask:

- Is the baseline already weak?
- Did I change more than one variable family?
- Is the metric aligned with the claim?
- Is the effect real but too small?
- Is the artifact readable but underdetermined?
- What evidence would make me retract my current story?

Write the answers down. Failure analysis is a skill, not a mood.

## Weekly review ritual

At the end of every week, answer these four questions:

1. What was the strongest evidence I saw?
2. Where is the biggest ambiguity?
3. What failed or surprised me?
4. What is the smallest next action that would make me less confused?

Keep these answers short. The point is to preserve judgment, not to write a diary.

## Communication rules

- Use short memos, not long summaries.
- Lead with the decision or judgment call.
- Put evidence before interpretation when possible.
- Name the main risk explicitly.
- End with one next step, not five vague ideas.

Research communication gets better when it becomes concrete, not when it becomes longer.
