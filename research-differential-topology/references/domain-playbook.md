# Domain playbook: research-differential-topology

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For a level set f⁻¹(c), apply the regular-value theorem only when f is smooth and Df has full target rank at every point in the preimage. The expected dimension is domain dimension minus target dimension.
- For intersections, use transversality of tangent spaces rather than visual crossing. If it fails, an intersection can still be smooth, but the transversal dimension formula is no longer justified.
- For degree arguments, specify orientations, equal dimensions and a proper map or an appropriate compact domain with boundary conditions. Local Jacobian signs must be summed over all preimages of a regular value.

## Worked valid example

For f:R²→R, f(x,y)=x²+y² and c=1, Df=(2x,2y) is nonzero at every point with f=1. The level set is therefore a smooth one-dimensional submanifold. At (1,0), the tangent vectors satisfy 2v_x=0, giving a vertical tangent line. The same argument does not cover c=0, where the only point has zero derivative.

## Tempting inference and counterexample

A critical value does not imply a singular underlying set. For f(x,y)=x² and c=0, every preimage has rank zero, but f⁻¹(0) is the smooth y-axis. The regular-value condition is sufficient, not necessary for an individual level set to be a manifold.

## Stop conditions and handoff

Stop global conclusions based solely on local differential rank. Hand off coordinate charts, critical loci, properness and orientation data to topology or geometry, with any global classification obligation explicit.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
