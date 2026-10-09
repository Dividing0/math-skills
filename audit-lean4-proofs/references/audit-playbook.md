# Audit playbook

## Three independent checks

A proof can pass the checker yet formalize the wrong statement, or depend on an admitted axiom. Review the exact declaration before interpreting the build result.

1. **Correspondence:** Compare the mathematical claim and the elaborated theorem, including all section variables used as parameters. For “every natural number is zero”, a theorem with hypothesis `n = 0` establishes a different, trivial implication. `WrongStatement.lean` illustrates this case and should compile while failing correspondence review.
2. **Checker:** Run direct file checks and the relevant build. Record whether all intended modules are covered. `Admitted.lean` may return exit code zero while warning that its declaration uses `sorry`; success is not completion.
3. **Dependencies:** Run `#print axioms TargetName` in a temporary module importing the target. The target must be named; anonymous examples are unsuitable for this dependency report. `Clean.lean` should have no axiom dependencies, whereas the admitted target should list `sorryAx`.

A scratch audit module has this shape, with the actual import and fully qualified target substituted:

```lean
import Project.Proofs
#check Project.target
#print Project.target
#print axioms Project.target
```

Run it in the project with `lake env lean Audit.lean`. Place it where project module resolution works, or use a temporary project with equivalent pins and imports. Keep diagnostic modules out of production roots unless requested.

## Trust and interpretation

`#print axioms` reports axioms reachable through the target's dependencies; a textual `sorry` search cannot replace it. An unrelated placeholder still matters for project-wide completion but need not contaminate a specific target. Report the audit scope precisely.

Standard Lean classical foundations and quotient soundness are not the same as a newly asserted mathematical claim. If the user requests constructive proofs, check for classical dependencies accordingly. Inspect custom axioms, admitted goals, imported unchecked assumptions, and evaluation mechanisms in context. Do not assume that a theorem is independent of all computation trust just because no literal `axiom` appears in its source. Consult the pinned toolchain's documentation for evaluator-related dependencies; do not universally label `native_decide` either untrusted or axiom-free.

## Acceptance cases

- Core conjunction proof: checker passes and target axiom list is empty.
- Admitted theorem: checker may pass; warning and `sorryAx` prevent a complete-proof verdict.
- Weak theorem with the desired name: compilation passes, correspondence fails.
- Target depends on a custom imported axiom: report it even when the local file contains no placeholder.
- Ordinary Mathlib proof uses classical axioms: report them without falsely treating them as unfinished obligations.
- No executable available: distinguish static review from actual verification.

## Sources

- [Lean axioms reference](https://lean-lang.org/doc/reference/latest/Axioms/): axioms and `#print axioms`.
- [Lean elaboration and compilation](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/): proof checking and compiled artifacts.
- [Lean source](https://github.com/leanprover/lean4): consult the pinned revision for implementation-dependent trust mechanisms.
