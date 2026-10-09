# Weakness review guide

## Review by consequence

| Area | Question to resolve | Evidence to collect |
|---|---|---|
| Specification | Does the type/statement encode the requested behavior? | Elaborated declaration and a counterexample or missing requirement |
| Boundary handling | Are empty input, failed lookup and invalid data distinguishable where needed? | Small executable input or checked equality |
| API stability | Do clients depend on binder shape, unfolding or instances? | A concrete downstream declaration |
| Proof robustness | What plausible local change causes the proof to fail? | A scratch reproduction; label hypothetical risks |
| Performance | Is the cost in elaboration, compilation or execution? | Same command, pins, input sizes and comparable timings |
| Trust | Are theorem dependencies or runtime implementations different from expectations? | Named axiom output and inspected implementation path |

Prioritize wrong required behavior or a broken public contract above maintenance risks. Treat purely presentational suggestions as optional. Avoid arbitrary numeric quality scores and findings based solely on text patterns.

## Compiling code with a conditional weakness

[BoundaryCases.lean](../assets/BoundaryCases.lean) defines `firstOrZero`. Both `[]` and `[0]` yield zero. This is a confirmed information loss but only a defect if the caller must distinguish missing input from a present zero. The two `rfl` examples establish the boundary behavior without implying a specification that the user never supplied.

The alternative `first?` returns `Option Nat`. Adopting it changes the public type and requires callers to handle `none`; propose it when the specification requires the distinction. Do not silently change the API during an analysis-only request.

## Logical and executable boundaries

An `unsafe` implementation may be appropriate in low-level or metaprogramming code. Trace its use rather than reporting a keyword as a proof hole. A `partial` declaration does not supply a termination guarantee; a `noncomputable` definition is not a substitute for executable code when runtime output is required. A logical proof about a function with a substituted runtime implementation does not by itself check that replacement. See the [Lean reference on partial and unsafe definitions](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/#partial-and-unsafe-definitions), and confirm the mechanism against local source for the pinned version.

For axioms and admitted proofs, inspect actual target dependencies; reuse the existing proof-audit workflow. Keep mathematical correspondence, kernel checking and runtime correctness as separate conclusions.

## Acceptance cases

- Default-valued lookup is intentional and documented: do not invent a bug; note the tradeoff only if useful to the review.
- A theorem compiles after an extra premise is introduced: identify the contract mismatch even if tests pass.
- A harmless `unsafe` declaration is never in a reviewed runtime path: do not claim it invalidates unrelated theorems.
- Suspected quadratic work has no measured or analyzed workload: report a hypothesis with a concrete next check.
- A build succeeds but excludes the reviewed file: run the file checker and relevant target before claiming coverage.
- Existing code has no supported findings: report the reviewed scope and residual uncertainty, without manufacturing weaknesses.
