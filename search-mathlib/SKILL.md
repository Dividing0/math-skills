---
name: search-mathlib
description: "Find and reuse Lean 4 Mathlib definitions and theorems using local source search, signatures, goal-directed search and documentation. Use when identifying a library result or its imports is the main task."
---

# Search Mathlib

## Workflow

1. Record the exact goal, local hypotheses, types and relevant structures. Read the pinned Mathlib revision and current imports. Distinguish theorem discovery from proving a genuinely absent result.
2. Search project files first, then `.lake/packages/mathlib/Mathlib` using `rg` with name fragments, namespaces and mathematical synonyms. Search by statement shape when the mathematical name is absent or ambiguous.
3. Use `#check Namespace.candidate` and, when necessary, `#print Namespace.candidate` in the project to inspect explicit and implicit binders, typeclasses, coercions and hypotheses. A familiar name or online signature is not sufficient evidence of compatibility.
4. Use available goal-directed tools such as `exact?` or `apply?` in a scratch example, and Loogle for type-pattern discovery. Check the pinned version's imports and help instead of assuming a search tactic exists. External search results are candidates until locally checked.
5. Inspect the declaring module and choose an import sufficient for the candidate. A broad `import Mathlib` can aid exploration but is not evidence that a narrower final import works. Avoid editing dependency sources or adding a redundant dependency to find a theorem.
6. Construct and check a minimal application with the actual goal and assumptions. Use explicit arguments or `simpa using` only when the normalization preserves meaning. Report the qualified name, signature, defining module, tested import and checker outcome; explain any missing hypotheses or near match.

## Resources

Read [search playbook](references/search-playbook.md) for search patterns and boundary cases. [Reuse.lean](assets/Reuse.lean) demonstrates signature inspection and reuse with a focused import. Use `prove-with-lean4` once a new mathematical argument is needed; use `debug-lean4-proofs` when a discovered theorem fails to elaborate.

## Runnable helper

Use [search_local.py](scripts/search_local.py) to search local Lean source for a literal query and return bounded file/line matches. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
