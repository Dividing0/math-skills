# Algebraic methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| Explicit construction or small example | The structure is finite or has a tractable presentation | Verify all axioms and relations; one example does not classify the class | Use it to falsify a proposed statement before a classification argument |
| Homomorphisms, kernels and quotients | A relation suggests a structure-preserving map | Verify preservation, normality or ideal conditions and representative independence | Keep the set quotient separate if operations are not well-defined |
| Normal forms or decomposition | A structure theorem may simplify the object | Check characteristic, finiteness and semisimplicity assumptions | Retain indecomposable or nonsemisimple structure if the theorem does not apply |
| Exact symbolic computation | Polynomial identities or finite algebraic data dominate | Fix coefficient domain and verify exact identities or certificates | Treat numerical reconstruction as a conjecture until verified |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
