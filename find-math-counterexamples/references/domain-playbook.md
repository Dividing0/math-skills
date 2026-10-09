# Domain playbook

## Select the method

1. Negate the exact quantifiers first. To refute for all x there exists y R(x,y), find one x for which every admissible y fails; a single failed pair does not suffice.
2. For finite algebraic claims, enumerate small structures or matrices and verify axioms exactly. Preserve stated dimension, field and invertibility; do not use floating tolerances to certify a failed identity.
3. For analytic universal claims, test endpoints, disconnected domains, concentrated sequences and noncompact spaces. Verify each premise, compute the failed conclusion, and distinguish a theorem counterexample from a witness against one proof step.

## Worked check

The claim that products of symmetric real matrices are symmetric fails for A=diag(1,2) and B=[[0,1],[1,0]]. Both transpose to themselves. AB=[[0,1],[2,0]], whose transpose differs. The witness also isolates the repair: commuting symmetric matrices have (AB)^T=BA=AB.

## Invalid inference and witness

A failed hypothesis cannot refute an implication. To challenge “every continuous map on a compact interval is bounded,” the function 1/x on (0,1] is tempting but the domain is not compact. It diagnoses the importance of compactness, not a counterexample to the original theorem.

## Completion and handoff

Return a fully specified witness and a premise-by-premise verification. For computational discovery, record the search range, arithmetic and exact final check; lack of a witness is inconclusive. Hand theorem repair the minimum changed assumptions plus verification of the repaired statement; do not infer the repaired theorem merely because the old witness is excluded.

Before reporting success, recheck the selected branch against the exact requested conclusion. Record which premises came from the user and which were derived. A missing premise must remain an explicit obligation, with a concrete description of the additional input or proof needed to continue.
