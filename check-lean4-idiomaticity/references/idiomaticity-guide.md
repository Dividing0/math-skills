# Idiomaticity guide

## Apply the right convention

Under [Mathlib naming conventions](https://leanprover-community.github.io/contribute/naming.html), proofs of propositions (including theorem names) typically use `snake_case`; predicates and types use `UpperCamelCase`; other data and computational definitions typically use `lowerCamelCase`. Functions follow the convention for their result: a predicate returning `Prop` differs from a proof returning a term of a particular proposition. Namespaces and established API families also affect the choice. Inspect nearby declarations before recommending a public rename.

The [Mathlib style guide](https://leanprover-community.github.io/contribute/style.html) favors explicit declaration types, readable proof layout and scoped structure. Follow the pinned project's rules for layout, headers and imports. Current online examples can use module syntax unavailable or inappropriate in an older project; never introduce it solely to match the latest webpage.

## Review decisions

| Observation | Useful action | Avoid |
|---|---|---|
| Proof only repackages a known fact | Test `exact` or a direct term | Replacing an explanatory argument solely to minimize lines |
| Search tactic left in a final proof | Try its checked suggested proof when useful | Banning all automation |
| Global `[simp]` addition | Check orientation, normal form and affected uses | Marking every new equality as a simplification rule |
| Broad import | Try a sufficient narrower import and check consumers | Claiming redundancy from text search alone |
| Large namespace or instance scope | Limit it if unintended influence is demonstrated | Cosmetic scope churn with no readability benefit |
| Different naming style | Identify the applicable project convention | Classifying all differences as correctness errors |

[Idioms.lean](../assets/Idioms.lean) demonstrates an indirect conjunction proof and a direct constructor term. Both prove the same proposition and both compile. The direct version avoids a redundant intermediate fact in this example; it is not a rule against named intermediate facts in substantial proofs.

## Verification and acceptance cases

Read configured linter commands and inspect their actual output. Compiler warnings, Mathlib linters and project-specific style checks have different coverage. If no linter is available, provide a manual review and disclose that coverage; do not invent a successful linter run.

- Mathlib-style theorem named `addZero`: suggest the existing API's naming convention, while checking whether a public rename would break callers.
- Executable helper named `parseInput`: do not force a theorem-style name onto a computational definition.
- Predicate named `IsReady : State → Prop` and theorem named `isReady_initial : IsReady initial`: recognize the distinction between defining a proposition and proving one.
- A clear domain-appropriate `simp` proof passes checks: accept it unless there is a concrete reason to control its dependencies.
- A local style convention differs from Mathlib: follow local requirements and label Mathlib advice as optional.
- Replacing explicit error handling with a default would be shorter: preserve the behavior and reject the change as mere style cleanup.
- Review-only request: deliver findings; cleanup request: edit and verify only the relevant code.
