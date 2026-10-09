# Domain playbook: research-mathematical-fluid-dynamics

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For smooth incompressible flows, derive energy estimates using div u=0 and boundary conditions that remove pressure and transport fluxes. State enough regularity to justify integration by parts.
- For weak solutions, use the available energy inequality instead of inserting an equality without proof. Distributional derivatives, initial trace and boundary conventions are part of the solution concept.
- For reduced regimes, compare nondimensional inertial, viscous and forcing scales. A low-Reynolds-number approximation is conditional on the stated scales and does not resolve arbitrary nonlinear flow or global regularity.

## Worked valid example

For smooth periodic incompressible Navier–Stokes, u_t+(u·∇)u=-∇p+νΔu with ν>0, take the L² inner product with u. The transport integral is ∫div(u|u|²/2)=0; the pressure term is ∫p div u=0. Periodic integration by parts gives d(||u||²₂/2)/dt=-ν||∇u||²₂. Thus kinetic energy decreases, but this estimate controls L² velocity rather than every higher derivative.

## Tempting inference and counterexample

An L² bound cannot alone bound pointwise amplitude. On a periodic interval, smooth bumps of width 1/n and height √n have bounded L² norm but diverging sup norm; normalization constants do not change this conclusion. Hence an energy bound is not a pointwise regularity proof.

## Stop conditions and handoff

Stop any regularity claim whose decisive higher-norm estimate is missing. Hand off dimension, viscosity, forcing, boundary fluxes, solution class and the exact norm controlled; keep numerical observations distinct from universal existence arguments.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
