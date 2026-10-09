# Domain playbook: research-operator-theory

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For bounded operators, distinguish invertibility from injectivity or dense range. Resolvent membership requires a bounded everywhere-defined inverse; use a lower bound and range argument when appropriate.
- For self-adjoint operators on Hilbert spaces, spectral claims require equality with the adjoint including its domain. Symmetry alone proves only an inner-product identity on the stated domain.
- For compact operators, eigenvalue-based structure is available under the relevant scalar field and hypotheses; for general bounded operators the spectrum need not consist of eigenvalues. Keep point, continuous and residual spectral distinctions explicit.

## Worked valid example

Let S on ℓ²(N) be the unilateral shift S(x₁,x₂,...)=(0,x₁,x₂,...). It is an isometry: ||Sx||=||x||. Its adjoint is S*(x₁,x₂,...)=(x₂,x₃,...). Therefore S*S=I but SS* projects away the first coordinate. S is injective yet not surjective, because e₁ is outside its range. Consequently 0 lies in its spectrum despite no nonzero vector satisfying Sx=0.

## Tempting inference and counterexample

A bounded operator need not be compact. For the identity on ℓ², the orthonormal vectors e_n lie in the unit ball and have pairwise distance √2, so their images have no norm-convergent subsequence. Matrix intuition cannot supply compactness in infinite dimension.

## Stop conditions and handoff

Stop products or adjoints when their domains are unspecified, and stop spectral decompositions without normality or another applicable theorem. Hand off the exact operator domain, topology, range information and unresolved spectral component.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
