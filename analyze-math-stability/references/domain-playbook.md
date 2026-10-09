# Domain playbook

## Select the method

1. For a C1 autonomous ODE near an equilibrium, a Jacobian whose eigenvalues have strictly negative real parts gives local exponential stability. Verify the equilibrium and remainder; zero real parts require nonlinear analysis.
2. For a nonlinear Lyapunov argument, require a C1 function V positive definite on the stated neighborhood and its derivative nonpositive along solutions. A strictly negative derivative away from equilibrium gives attraction under the applicable hypotheses; global conclusions additionally need control of escape and global existence, usually via proper sublevel sets.
3. For input robustness, derive an inequality such as Vdot <= -c V + d|w|² with c>0; integrate it to distinguish disturbance-dependent boundedness from convergence to the unforced equilibrium.

## Worked check

For xdot=-2x, V=x² has Vdot=2x(-2x)=-4V. Integration yields V(t)=exp(-4t)V(0), hence |x(t)|=exp(-2t)|x(0)|. Solutions exist for all nonnegative time, so this establishes global exponential stability, with an explicit rate and no hidden local restriction.

## Invalid inference and witness

A trajectory that decreases near zero need not imply global stability. For xdot=-x+x³, the Jacobian at zero is -1, but x(0)>1 gives positive derivative and moves away. The local theorem remains correct; a claim covering every initial state is false.

## Completion and handoff

Return the stability notion, norm, region of initial conditions, existence interval, decay constants, and allowed perturbations. Stop at marginal spectra unless higher-order terms or an invariant-set argument are checked. Hand numerical exploration a candidate region rather than a certified basin; hand proof review the complete derivative and boundary calculations.

Before reporting success, recheck the selected branch against the exact requested conclusion. Record which premises came from the user and which were derived. A missing premise must remain an explicit obligation, with a concrete description of the additional input or proof needed to continue.
