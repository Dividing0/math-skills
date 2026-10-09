# Domain playbook: research-galois-theory

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For a polynomial over a field, compute irreducibility and separability separately; characteristic-zero irreducibles are separable, but positive characteristic requires checking the derivative and repeated-root behavior. For finite extensions, subgroup-field correspondence requires normality and separability, equivalently the extension is Galois. For automorphism counting, compare the number of base-fixing embeddings with the degree only under appropriate separability and target-field containment assumptions. For infinite Galois extensions, use the Krull topology and closed subgroups; finite correspondence cannot simply be reused for arbitrary subgroups.

## Worked valid example

Let L=Q(sqrt(5)). The polynomial X²-5 is irreducible over Q because 5 is not a rational square. Its two distinct roots ±sqrt(5) both belong to L, so L is its separable splitting field. The Q-automorphisms are the identity and the map sqrt(5)↦-sqrt(5). Their group has order two, matching [L:Q]=2. Its two subgroups correspond to L and Q respectively; an element a+b sqrt(5) is fixed by both precisely when b=0.

## Tempting invalid inference

Degree alone does not determine automorphism count: Q(real cuberoot(2))/Q has degree three, but its other two conjugates are nonreal and outside this real field. Every Q-automorphism fixes the real root, so the automorphism group is trivial; the extension is not normal.

## Stop and handoff

Return base field, characteristic, defining polynomial and normality/separability proofs. If irreducibility is only experimentally suspected, stop the correspondence argument. Transfer computational factorization to computational algebra with exact coefficients and finite/infinite scope.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
