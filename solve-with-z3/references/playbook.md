# Solve with Z3: playbook

## Worked encoding

For integer `x`, `(assert (> x 3))` together with `(assert (< x 6))` has a model, such as 4 or 5. Adding `(assert (= x 3))` makes those assertions inconsistent. To test a theorem, negate its conclusion; solving the conclusion directly asks a different question.

The helper accepts declarations and assertions in SMT-LIB2 and runs one solver query. Its tracking labels map an unsatisfiable core to zero-based assertion indices. The model can contain internal tracking symbols. Use assertion evaluations and the encoded source for interpretation; the helper does not verify a proof in Lean or another checker.

## Acceptance cases

- `sat`: return a witness and its interpretation, not a universal validity claim.
- `unsat` with contradictory premises: flag vacuity.
- `unknown`: retain `reason_unknown`; do not translate it to either Boolean outcome.
- Integer arithmetic was intended but a bit-vector was encoded: correct the model before trusting the result.
- An unsat core omits unrelated assertions: report it as a sufficient conflicting subset, without claiming minimality.

## Primary sources

[Programming Z3](https://z3prover.github.io/papers/programmingz3.html) by the solver authors; use the installed API/version for exact capabilities.
