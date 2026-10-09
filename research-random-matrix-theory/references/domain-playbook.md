# Ensemble normalization and spectral conclusions

## Choose a branch
- Global Wigner law: for a real symmetric or Hermitian ensemble, verify independent upper-triangular entries, centered off-diagonal variables of the specified variance and appropriate diagonal control. The 1/sqrt(n) normalization is decisive. Use a theorem with its exact moment and coupling assumptions for the stated convergence mode.
- Trace moments: compute (1/n)tr(H^k) through index walks and independence. Zero mean kills many unmatched factors; dependence can change which terms survive. An expected moment identity does not alone establish concentration or almost-sure convergence.
- Edge or eigenvector analysis: bulk empirical-measure convergence does not control a vanishing number of outliers or individual eigenvectors. Apply an edge/local law only after checking its extra moments, regularity and probability scale.

## Worked second moment
Let H be n by n real symmetric with H_ij=X_ij/sqrt(n) for i<j, independent mean-zero variance-one X_ij, and diagonal zero. Then tr(H²)=sum_(i,j) H_ij²=2 sum_(i<j)X_ij²/n. Consequently E[(1/n)tr(H²)]=2[n(n-1)/2]/n²=(n-1)/n→1. This calculation checks the scale without needing fourth moments, since it uses only second moments. It does not prove a full limiting distribution or an edge bound.

## Tempting inference and counterexample
Weak convergence of empirical spectral measures does not bound operator norms. The deterministic diagonal matrix diag(n,0,...,0) has measure (1-1/n)delta_0+(1/n)delta_n, which converges weakly to delta_0 because the escaping atom has mass 1/n. Yet its operator norm is n. Thus a bulk limit can ignore a diverging outlier; isolate extreme eigenvalues before making an edge claim.

## Stop or hand off
If entries are correlated, preserve their joint law rather than relabeling them iid. Pass ensemble, normalization, aspect ratio, moment assumptions and convergence mode to probability analysis. Keep simulation histograms as finite-n observations. Primary source: Terence Tao, 254A Notes 4, Theorem 1 and the separate Bai–Yin discussion, https://terrytao.wordpress.com/2010/02/02/254a-notes-4-the-semi-circular-law/, checked 2026-10-08. Read the theorem's ensemble definition before applying its statement.
