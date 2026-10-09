# Domain playbook: research-nonlinear-analysis

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For a contraction on a nonempty complete metric space mapping the space to itself, use Banach's theorem for existence, uniqueness and an iterative error bound. For a continuous self-map on a nonempty compact convex subset of finite-dimensional Euclidean space, Brouwer gives existence but no uniqueness. For F(x,p) that is C¹ on an open neighborhood of a known zero (x₀,p₀), the implicit-function theorem requires the square derivative D_xF(x₀,p₀) to be invertible and gives only a local branch x(p). For a C¹ map Rⁿ→Rⁿ with invertible derivative, distinguish the local inverse-function conclusion. For monotone operator arguments, specify domain, Hilbert/Banach setting and the coercivity or maximality conditions of the chosen theorem; monotonicity alone is not surjectivity.

## Worked valid example

On X=[0,1], T(x)=(1+x)/3 maps X into [1/3,2/3]⊂X and has Lipschitz constant 1/3. X is complete, so there is exactly one fixed point. Solving x=(1+x)/3 gives x*=1/2. Starting x₀=0 yields x₁=1/3; the a-posteriori estimate for the new iterate is |x₁-x*|≤q/(1-q)|x₁-x₀|=(1/2)(1/3)=1/6, which here equals the exact error.

## Tempting invalid inference

A continuous self-map can have several fixed points even on a compact convex set: T(x)=x on [0,1] fixes every point. A Brouwer existence argument therefore cannot establish uniqueness. Conversely local invertibility says nothing about all distant solutions.

## Stop and handoff

Return the precise space, invariant set, constants and whether results are local or global. If a self-map or completeness check fails, identify that obstruction before iterating. Transfer PDE-specific compactness and boundary conditions to functional analysis or PDE research.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
