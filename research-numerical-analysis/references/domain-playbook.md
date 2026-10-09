# Domain playbook: research-numerical-analysis

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. Before choosing an algorithm separate the mathematical problem's conditioning from the method's stability. For square invertible A and Ax=b in a declared norm, relate error to residual using x−x̂=A^(−1)(b−Ax̂); normalize by ||b||>0 when discussing relative residuals. For singular or rectangular A, check compatibility and nullspaces first; any pseudoinverse bound must specify the selected solution and control its nullspace component. A zero residual does not identify a unique solution.
2. For discretization analyze consistency and stability in the relevant norm and time horizon. A refinement table suggests a rate only after the asymptotic regime and reference accuracy are checked; compare multiple h values and separate solver error from mesh error.
3. For certification use exact arithmetic, directed-rounding intervals or a proved residual-to-error inequality with all constants. Floating-point residual evaluation itself can suffer cancellation. A convergence stopping rule needs an error bound for the returned iterate, not merely a small change or exhausted iterations.

## Worked derivation

Let A=diag(1,10^(−8)), b=(1,10^(−8))ᵀ, so x=(1,1)ᵀ. The approximation x̂=(1,0) has residual r=b−Ax̂=(0,10^(−8))ᵀ but forward error ||x−x̂||₂=1. Here ||A^(−1)||₂=10⁸ and the bound ||x−x̂||₂≤||A^(−1)||₂||r||₂ is attained. A tiny absolute residual alone therefore supplies no tiny absolute forward error.

## Invalid inference and witness

For iteration x_(k+1)=x_k+10^(−12) aimed at solving x=1, consecutive differences are tiny even starting at zero, while the solution error remains nearly one for many iterations. Small updates without a contraction or residual bound are not a solution certificate.

## Stop and handoff

Return arithmetic, norm, conditioning, error decomposition and which constants were verified. Hand off a rigor claim if rounding or inverse bounds remain unproved. Report an empirical rate as observed, never as a theorem from a finite table.
