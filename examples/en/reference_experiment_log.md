# Reference Experiment Log

## Experiment question

In the `M06` toy trace, what happens to the compose score if I weaken the readout from the right-number token?

## Baseline

- Setup: keep the default attention distribution in the toy trace.
- Metrics: compose score and left-versus-right contribution share.
- Expectation: the right-number path should contribute slightly more because its value is larger.

## Variant

- Single change: reduce the readout weight on the right-number token from `1.0` to `0.65`.
- Everything else stays fixed: token embeddings, QK scores, and path structure.

## Result

- The compose score drops from `2.144` to `1.755`.
- The left/right contribution ratio moves from `0.43 / 0.57` to `0.52 / 0.48`.
- The graph still looks present, but the quantitative dominance has already flipped.

## Judgment Call

This shows that in tracing, "the graph still exists" does not mean "the mechanism strength stayed stable." If you only inspect structure rather than edge weights and ablation drops, you can overestimate how stable a path really is.

## Failure Analysis

- This is still a toy trace and does not claim the same cleanliness in a real model.
- The readout is hand-set, so this is only local-mechanism intuition rather than paper-scale reproduction.
- The next step should mirror the intervention on the left readout and test whether the conclusion stays stable.
