# Closedness, nondegeneracy and Hamiltonian signs

## Method branches
1. For a proposed symplectic form ω, check smoothness, dω=0 and nondegeneracy pointwise. A closed form can be degenerate, and a nondegenerate two-form in dimensions above two need not be closed.
2. For Hamiltonian dynamics, fix the sign convention. With ι_Xω=dH and ω=dq∧dp, obtain X_H=(∂H/∂p)∂q-(∂H/∂q)∂p. Derive this once so downstream Poisson-bracket conventions remain consistent.
3. For a symplectic vector field, use Cartan's formula L_Xω=d(ι_Xω) because dω=0. Hamiltonianity requires exactness of the contracted one-form, not just closedness. On a contractible coordinate neighborhood closed one-forms are exact; global periods can obstruct this.
4. For normal forms, apply Darboux locally and distinguish coordinates from global symplectomorphisms. For global flows, check completeness rather than assuming every smooth vector field on a noncompact manifold integrates for all time.

## Worked calculation
On R² with ω=dq∧dp and H=(q²+p²)/2, contraction of a∂q+b∂p gives a dp-b dq. Equating to dH=q dq+p dp yields a=p,b=-q. Along the flow dH/dt=q p+p(-q)=0, so energy is conserved. The trajectories solve q″=-q and are globally defined periodic circles, including the stationary origin.

## Tempting inference and counterexample
Hamiltonian vector fields need not be complete on noncompact spaces. For H=q²p, Hamilton's equations give q′=q²,p′=-2qp. Starting at q(0)=1,p(0)=0 yields q(t)=1/(1-t),p(t)=0, which blows up at t=1. Smoothness of H on all R² alone does not ensure a global flow.

## Stop and handoff
Stop global claims if periods, topology or completeness have not been checked. Pass the manifold, form, contraction convention, Hamiltonian, coordinate domains and maximal-flow interval to dynamics. Conservation of a function does not establish integrability or compactness of its level sets; state those extra obligations explicitly before using a recurrence or global-existence theorem.
