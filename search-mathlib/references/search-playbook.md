# Search playbook

## Search and confirm

Given a natural-number equality involving commutativity, search likely namespaces and the statement structure, rather than guessing an English theorem title:

```sh
rg -n 'add_comm|theorem.*comm' .lake/packages/mathlib/Mathlib/Data/Nat
rg -n 'candidate_name' .lake/packages/mathlib/Mathlib
```

Declarations may originate in Lean or Batteries and be re-exported by Mathlib. A missing match in Mathlib's source does not imply that a constant is absent. Search dependency sources or use `#check` to distinguish declaration origin from a sufficient import.

The asset imports `Mathlib.Data.Nat.Basic`, checks `Nat.add_comm`, and proves the reversed-sum equality by direct application. Its dependency originated in core Lean; the example demonstrates reuse in a Mathlib environment without asserting that Mathlib defines the constant.

For a less familiar goal, place its exact binders and hypotheses in a scratch example and try `exact?` or `apply?` if available. Read suggestions and replace exploration with a checked application where that improves maintainability. These tools differ by version and imports; an unknown tactic is a discovery/environment issue, not evidence that no lemma exists.

## Signature discipline

Compare universes, ambient types, ordered/algebraic structures, implicit parameters and side conditions. A result over a field need not apply over a ring. A theorem requiring continuity cannot establish the same conclusion for an arbitrary function. For coercions or implicit arguments, use `set_option pp.all true in #check candidate` locally to expose details, then remove diagnostic output from production files.

For each selected theorem, hand off its qualified name, a sufficient import, the specialization to the goal, remaining obligations, pinned revision and actual check command. If no match is found, describe the search coverage and candidate gaps; do not claim exhaustive absence.

## Acceptance cases

- Online documentation has a renamed theorem: search local source and check the project version before changing dependencies.
- Name matches but a nonzero or continuity hypothesis is missing: report a near match and the obligation.
- Candidate works under `import Mathlib`: retest with the proposed final imports.
- Source search misses a core theorem: use `#check` and dependency source inspection.

## Sources

- [Mathematics in Lean, library search](https://leanprover-community.github.io/mathematics_in_lean/C02_Basics.html): source browsing and goal-directed discovery.
- [Loogle](https://loogle.lean-lang.org/): type-pattern search; online results can differ from project pins.
- [Mathlib 4 documentation](https://leanprover-community.github.io/mathlib4_docs/): signatures and source links. Do not use Mathlib 3 documentation for Lean 4 syntax.
