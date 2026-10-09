# Kinematics, balances and admissible constitutive laws

## Method branches
1. For finite deformation, define a deformation χ from reference to current configuration and F=∇χ. Require det F>0 for a locally orientation-preserving nonsingular deformation; this local condition alone does not prove global injectivity.
2. For material laws, distinguish reference stresses from spatial stresses. Under a superposed proper rotation Q, F transforms to QF and C=FᵀF remains unchanged. Verify objectivity by the actual transformation rule, rather than by a familiar-looking scalar formula.
3. For balance laws, derive the weak or strong form with density convention, body force and boundary tractions. Use a transport theorem only with sufficient regularity and distinguish mass balance from constitutive closure.
4. For linearization, state the small-displacement-gradient regime and reference state. Infinitesimal strain sym ∇u is appropriate to linearized kinematics; it is not an exact finite-rotation measure.

## Worked calculation
In a homogeneous deformation χ(X)=(2X₁,X₂,X₃), F=diag(2,1,1) and J=det F=2. Conservation of mass gives current density ρ=ρ₀/J=ρ₀/2. The right Cauchy-Green tensor is C=diag(4,1,1). After a proper rigid rotation Q, (QF)ᵀ(QF)=FᵀF since QᵀQ=I, so a stored energy depending only on C is unchanged by this observer transformation.

## Tempting inference and counterexample
Small-strain formulas cannot evaluate large rigid rotations as exact deformation measures. In two dimensions choose Q=-I, a rotation by π, and u(X)=QX-X. Then sym ∇u=-2I although the motion is rigid and FᵀF=I. The nonzero linearized strain reflects using an approximation outside its regime.

## Stop and handoff
Stop before assigning a physical stress response if the constitutive law, units or boundary conditions are absent. Pass configuration, F/J conventions, stress measure, balance equations, constitutive assumptions and admissibility checks to PDE or numerical work. Separate material stability hypotheses from numerical solver stability and mathematical well-posedness; none of these follows merely from successful simulation.
