# Domain playbook: formalize-math-proofs

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For a theorem already present in the project library, verify its elaborated statement and assumptions before using it; a matching informal name is insufficient. For a new elementary lemma, first encode the intended domain and quantifier order, then split the proof into small kernel-checkable steps. For computational decisions, use proof-producing reflection or a supported certified evaluator rather than an external Boolean assertion. For imported axioms or classical reasoning, inspect dependencies and report them separately from syntactic acceptance.

## Worked valid example

The informal claim “multiples of four are even” means: for every integer n, if there exists integer k with n=4k, there exists integer m with n=2m. Given the witness k, choose m=2k; then 2m=2(2k)=4k=n. This witness construction describes the proof obligation before any assistant syntax is written. Changing n to a natural number is a different encoded statement, even though a related proof also works. A project implementation must elaborate the actual integer statement and check the arithmetic identity.

## Tempting invalid inference

A successful checker run can verify the wrong theorem: “for every n, if n=0 then n is even” does not formalize “every integer is even.” An admitted axiom asserting the target can also make subsequent code compile without supplying its mathematical proof.

## Stop and handoff

Record the exact encoded statement, project revision, checker command, result and dependency audit. If the executable is absent, return a clearly unchecked draft; never fabricate output. Transfer unresolved mathematical lemmas to proof construction and version-specific syntax to the pinned assistant documentation.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
