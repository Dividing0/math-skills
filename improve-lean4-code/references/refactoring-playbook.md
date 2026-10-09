# Refactoring playbook

## Preserve the contract that callers use

For a theorem, compare elaborated types with `#check` and `#print`: extra assumptions, changed universes or reordered implicit arguments can invalidate the intended API. For a definition, preserve output and effect semantics and inspect callers that unfold it. Changing recursion strategy, reducibility, a structure field or a global instance may break clients even if a new equality theorem checks.

The bundled [example](../assets/Refactor.lean) keeps `countItems` as a wrapper and proves equality for every list. This certifies returned values. It does not establish equal allocation cost, stack use or compatibility with every downstream reduction proof. Check those obligations separately when relevant.

| Requested improvement | Useful evidence | Insufficient evidence |
|---|---|---|
| Replace duplicate implementation | Checked equivalence plus relevant callers | Several matching outputs |
| Simplify a proof | Same elaborated statement and accepted replacement | Fewer lines after adding an assumption |
| Narrow imports | Direct file check and affected downstream build | Candidate theorem's source module alone |
| Speed up elaboration | Repeated comparable runs with the same pins/options | One cached `lake build` |
| Speed up executable code | Compiled workload, equivalent results, stated input sizes | A quicker `#eval` on a different input |

## Host verification

Use a scratch module within the target project for diagnostics, then remove it. Build imported modules before checking the scratch module. Choose actual Lake target names from the project configuration; a default build may omit the changed file.

```sh
lake env lean Path/To/File.lean
lake build ActualTarget
```

For pure code, an equality theorem is stronger than a finite output sample. For IO or stateful code, inspect failure handling, ordering and effects and run the project's relevant executable tests. Do not run external-effectful examples merely because they compile.

## Acceptance cases

- A long proof already has a matching library theorem: check the candidate signature and import, replace it, and check callers without changing the statement.
- A tail-recursive replacement returns the same values but breaks a consumer's `rfl`: retain a compatible definition or expose the API change; equality of results alone is not a complete refactor check.
- A faster branch returns a default on previously rejected input: identify the behavior change instead of claiming an equivalent optimization.
- No benchmark can run: report an unmeasured performance hypothesis, even if the code looks cheaper.
- A clean, short proof already follows local conventions: leave it intact rather than manufacturing a refactor.

## Source

The [Lean reference on recursive definitions](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/) explains the different reduction behavior of recursive definitions. Consult the documentation matching the project's pinned toolchain before changing recursion or reducibility.
