# Domain playbook: build-mathematical-models

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- Use a balance model when a conserved quantity and boundary fluxes are known. Define stocks and flux units before constitutive laws; a well-mixed approximation requires mixing faster than the resolved dynamics.
- Use an agent or compartment model when populations are heterogeneous and exchange rules matter. Specify nonnegative rates, admissible state space, and observation aggregation rather than treating a fitted coefficient as a physical law.
- Use a spatial PDE when transport or gradients determine the target. Supply initial and boundary data and identify whether parameters can be inferred from available sensors; a solvable equation can still be a poor model.

## Worked valid example

A constant-volume tank V has inflow and outflow q, inlet concentration c_in, and perfectly mixed concentration c. Solute balance gives Vc'=q c_in-q c. With k=q/V>0 and constant c_in, c(t)=c_in+(c₀-c_in)e^(-kt). For nonnegative c₀ and c_in it stays nonnegative. The observed sensor may instead report y=c+b+ε; offset b belongs to the measurement model, not the solute balance.

## Tempting inference and counterexample

A perfect fit does not identify a mechanism. If observations follow y(t)=ab e^(-t), then (a,b)=(1,6) and (2,3) produce identical records at every time. More timestamps cannot separate a and b without another observable or an external constraint.

## Stop conditions and handoff

Stop calibration if the target, state meaning, units or measurement map is undefined. Hand off equations, parameter ambiguities, estimated regimes and independent validation conditions to identifiability and numerical implementation skills.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
