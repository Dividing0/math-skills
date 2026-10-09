# Domain playbook: research-linear-algebra

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For exact linear systems use elimination, rank and null-space computations over the declared field. Ax=b is solvable exactly when b lies in the column space; if solvable, all solutions are a particular solution plus ker A.
2. For spectral questions check symmetry or normality before using an orthonormal eigenbasis. A repeated eigenvalue needs enough independent eigenvectors for diagonalization. Singular values describe norm amplification and numerical rank, not generally the eigenvalues.
3. For least squares or numerical solves use QR or SVD and expose tolerance and scaling. Exact rank differs from thresholded rank; a small residual supports small backward error only with the chosen normalization, while forward error depends on conditioning.

## Worked derivation

For A=[[1,1],[0,1]], the characteristic polynomial is (λ−1)². A−I=[[0,1],[0,0]] has kernel span(e₁), dimension one. Therefore A is not diagonalizable although its eigenvalue is repeated; its given matrix is already a Jordan block. Since A=I+N with N²=0, A^k=I+kN, so powers grow linearly even though all eigenvalues have modulus one.

## Invalid inference and witness

“AᵀA and A have the same eigenvalues” fails for A=[[0,2],[0,0]]: both eigenvalues of A are zero, while AᵀA=diag(0,4). Singular values are 0 and 2, exposing amplification invisible in the eigenvalues.

## Stop and handoff

Return field, basis, exact or numerical arithmetic and each decomposition's hypotheses. Stop before a numerical-rank conclusion when tolerances and data scale are missing. Hand off stability analysis with singular values, residual normalization and condition estimates.
