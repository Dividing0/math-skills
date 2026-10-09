# Discrete and algorithmic methods

Use this family-level guide together with the domain-specific workflow and boundary case. It supplies candidate strategies, not a theorem whose hypotheses may be skipped.

| Method | Choose when | Obligations | If obligations fail |
|---|---|---|---|
| Bijection, recurrence or invariant | Counting or finite structural task | Verify both directions, initial values and exclusions | Check small cases to expose overcounting |
| Extremal construction | Need a best constant or obstruction | Prove the universal bound and a matching witness separately | Label a unmatched bound as possibly nonsharp |
| Reduction or relaxation | Need complexity transfer or algorithm design | Check reduction direction, encoding, cost and feasibility after rounding | A relaxation value alone is not a feasible solution |
| Enumeration or certificate | Finite witness or exhaustive claim | Verify generator completeness and an independent checker | A heuristic search failure is inconclusive |

## Task-specific anchor

Read [acceptance-cases.md](acceptance-cases.md). State which strategy above handles that case, what exact assumption is missing, and what can be concluded after repairing it. Do not assume the repair automatically proves the desired result.
