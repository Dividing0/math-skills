# Domain playbook: research-abstract-algebra

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For a proposed homomorphism, first fix operation and identity conventions, prove preservation on arbitrary elements, then calculate kernel and image. For quotient rings, require a two-sided ideal in a possibly noncommutative ring; a one-sided ideal only gives the corresponding module quotient. For classification of finite groups, combine element orders, subgroup indices and homomorphisms under their exact finite hypotheses. For module decomposition, check the coefficient ring and finiteness conditions before importing a vector-space basis argument.

## Worked valid example

Define φ:Z→Z/6Z by φ(n)=[n]. Addition preservation follows from [a+b]=[a]+[b]; it is surjective because every class has an integer representative. Its kernel is 6Z. The induced map Z/6Z→image(φ) is well-defined because n-m∈6Z gives equal classes, injective by the same calculation, and surjective. This verifies the first-isomorphism mechanism rather than citing it without checking the map.

## Tempting invalid inference

A submodule of a free module need not be a vector subspace with a complement. In the Z-module Z, the submodule 2Z has no complementary submodule: a nonzero subgroup intersects 2Z nontrivially, and the zero subgroup cannot supply odd integers. Field-specific splitting cannot be copied to arbitrary rings.

## Stop and handoff

State the ambient category, identity preservation and left/right action conventions. Stop classification claims when only examples have been listed; transfer ideal computations or field extensions to the relevant specialized skill with the exact algebraic assumptions.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
