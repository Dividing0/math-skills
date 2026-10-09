# Domain playbook: analyze-math-symmetries

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For an ODE x'=F(x), test equivariance F(gx)=gF(x) for a specified linear group action and every admissible x. A symmetric potential only transfers to the gradient field when the action is orthogonal for the chosen metric.
- For a conserved quantity, differentiate it along trajectories. Rotation invariance of a first-order dissipative system does not imply conservation of angular momentum; a Noether argument requires a variational formulation and its hypotheses.
- For orbit reduction, use invariants that separate the relevant orbits and examine stabilizers. At fixed points the quotient can be singular; do not infer a globally smooth reduced coordinate chart.

## Worked valid example

Take F(x,y)=-(x²+y²)(x,y) on R². For an orthogonal rotation R, ||Rz||²=||z||², so F(Rz)=RF(z). With s=x²+y², differentiation gives s'=2z·F(z)=-2s². For s(0)=s₀≥0 this yields s(t)=s₀/(1+2s₀t), t≥0. The radius is reduced exactly, while the initial angular coordinate is required to reconstruct the trajectory; at z=0 the rotation stabilizer is the whole group.

## Tempting inference and counterexample

An invariant equation need not make every solution invariant. The rotation-equivariant equation z'=0 has the constant solution z(t)=(1,0), which changes under a quarter turn. Equivariance maps solutions to solutions; it does not identify them.

## Stop conditions and handoff

Stop a proposed quotient when invariants fail to separate orbits or a gauge condition excludes admissible states. Hand off the action, invariant equations, singular strata and reconstruction data to geometry or dynamics work.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
