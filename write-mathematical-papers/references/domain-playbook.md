# Domain playbook: write-mathematical-papers

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For a theorem-centered manuscript, normalize statements and list proof dependencies before arranging exposition; every quantified conclusion needs a completed argument or explicit conjectural label. For an experimental manuscript, define inputs, metrics, baselines and reproducibility artifacts, and bound claims to measured regimes. For a survey or comparison, read decisive primary sources and compare assumptions and conclusions rather than titles; novelty cannot be inferred from an unsuccessful search. For a technical note, include a worked example and counterexample showing why its hypotheses matter while keeping notation consistent.

## Worked valid example

A short note can state: for real a,b, (a+b)²≤2(a²+b²), with equality exactly when a=b. The proof computes 2(a²+b²)-(a+b)²=(a-b)²≥0; equality is equivalent to a-b=0. The statement, proof and equality case are complete and dependency-light. An example a=1,b=3 gives 16≤20, while a=b=2 gives equality. The manuscript must still avoid claiming this elementary established inequality as a novel discovery without a justified prior-work assessment.

## Tempting invalid inference

A proof of a lemma does not validate a broader headline: proving convergence for fixed dimension does not establish a dimension-uniform rate if constants depend on dimension. For example a bound n·ε becomes arbitrarily large with n despite being finite for every fixed n. Quantifier order and parameter dependence belong in the statement.

## Stop and handoff

Return proof, citation and compilation status separately, naming unresolved items. Missing sources should remain citation obligations; missing checker or compiler execution should remain unchecked status. Transfer novelty assessment to literature survey and faulty theorem steps to proof review before polishing prose.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
