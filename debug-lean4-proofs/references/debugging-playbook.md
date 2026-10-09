# Debugging playbook

## Expected failures

`MissingHypothesis.lean` attempts `exact h` in a theorem asserting an arbitrary proposition `P`, with no `h`. Expect an unknown-identifier diagnostic and nonzero checker exit. The unrestricted claim is unprovable: adding `h : P` is a different theorem, so explain the missing assumption rather than presenting the revised declaration as a proof of the original.

`CoercionFailure.lean` supplies a proof of equality in `Nat` to a goal about its casts in `Int`. Equality proofs are not automatically transported between types. Expect a type-mismatch diagnostic. In `Fixed.lean`, `cases h` substitutes equal naturals before `rfl` checks the integer equality, preserving the original statement.

From a temporary project, check the failure files separately with `lake env lean File.lean`, retain their expected nonzero exits, and check `Fixed.lean` for success. Do not erase the failing lines or add `sorry` merely to make a demonstration build green.

## Diagnostic branches

| Diagnostic | Inspect | Typical next action |
|---|---|---|
| Unknown module or missing `.olean` | Pins, imports, resolved packages | Restore compatible environment or build artifact |
| Unknown constant | Namespace, spelling, version, declaring module | Check local signature and sufficient import |
| Type mismatch | Expected/inferred type and hidden casts | Annotate terms or prove cast transport |
| Failed typeclass synthesis | Required structure and local instances | Supply legitimate structure; avoid arbitrary instances |
| Rewrite found no occurrence | Expression after elaboration, orientation | Normalize or target the actual subterm |
| Unsolved goals | Remaining hypotheses and side conditions | Prove missing lemma or identify false claim |
| Maximum heartbeats | Expensive search/simplification step | Narrow the proof first, then tune locally if justified |

Keep debug options scoped to the scratch declaration. `set_option pp.all true` reveals details but can overwhelm output; start with the relevant expression. Distinguish a tactic that made progress from a tactic that closed all goals.

## Acceptance cases

- Expected `Int` equality, supplied `Nat` equality: transport the equality without changing domains.
- `exact h` references an absent assumption: expose the missing premise; do not silently change the theorem.
- Failed division cancellation: identify and prove the nonzero condition or show the counterexample.
- Cache incompatibility produces many import errors: repair the environment before rewriting proofs.
- `simp` leaves a goal: inspect the residual goal rather than declaring success from partial progress.

## Sources

- [Lean elaboration and compilation](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/): elaboration, checking and diagnostics.
- [Lean type classes](https://lean-lang.org/doc/reference/latest/Type-Classes/): instance synthesis.
- [Lean coercions](https://lean-lang.org/doc/reference/latest/Coercions/): coercion insertion and limitations.
