# Domain playbook: research-mathematical-logic

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For propositional validity, exhaustive truth tables are complete for a finite set of variables, provided every valuation is covered. For first-order semantic claims, specify structures and assignments; a countermodel disproves validity without deciding provability from additional axioms. For proof-theoretic claims, name the inference system and use its soundness/completeness result only within its logic. For substitution under quantifiers, perform capture-avoiding renaming. For incompleteness or undecidability, verify consistency, effective axiomatization and expressive strength instead of attributing the phenomenon to every formal theory.

## Worked valid example

To show (P→Q) and P entail Q in classical propositional logic, consider a valuation satisfying both premises. P is true; if Q were false, the material implication P→Q would be false. Therefore Q is true. Syntactically the same conclusion follows by modus ponens, so semantic entailment and derivability are separately exhibited. This example uses the declared classical truth-functional interpretation, not an unspecified notion of implication.

## Tempting invalid inference

Existential witnesses cannot be promoted to universal claims: a structure with domain {0,1} and P true only at 0 satisfies ∃x P(x) but not ∀x P(x). Similarly, replacing a free variable by a bound one can change meaning; rename bound variables before substitution.

## Stop and handoff

Return language, axioms, logic and whether the conclusion is semantic, syntactic or metatheoretic. A failed proof search is inconclusive. Transfer machine-checked derivations to formalization and independence claims to genuine model or relative-consistency arguments with explicit assumptions.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
