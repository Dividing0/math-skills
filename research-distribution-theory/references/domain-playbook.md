# Pairings and legal operations on distributions

## Method branches
1. For distributions on an open Ω, use test functions C∞c(Ω) and define ∂ⱼT by ⟨∂ⱼT,φ⟩=-⟨T,∂ⱼφ⟩. Higher derivatives alternate signs. Check support and boundary conventions before extending an integration-by-parts argument.
2. For multiplication, a smooth function a defines aT through ⟨aT,φ⟩=⟨T,aφ⟩. Multiplying arbitrary distributions is not a general operation. For less regular multipliers state the narrower function-space result that licenses it.
3. For convolution on Rⁿ, compact support of one factor supplies a standard sufficient condition for convolution of two distributions. For two general noncompact factors check an applicable support or decay condition rather than assuming the integral converges.
4. For weak solutions, prove the identity against every test function, and separate local integrability from stronger classical regularity. Recovering a pointwise equation requires additional regularity of the representative.

## Worked calculation
Let H be the locally integrable step function, equal to zero for x<0 and one for x>0. Then ⟨H′,φ⟩=-∫₀∞φ′(x)dx=φ(0), since φ has compact support. Therefore H′=δ₀ as distributions. The choice of H(0) is irrelevant to the regular distribution because changing a function at one point changes no Lebesgue integral.

## Tempting inference and counterexample
Distributional derivative zero does not force a specified representative to be pointwise constant. The function f equal to 0 except f(0)=1 represents the zero distribution and has distributional derivative zero, while its displayed pointwise values are not constant. A conclusion about equivalence classes almost everywhere differs from a conclusion about every selected representative.

## Stop and handoff
Stop an undefined product or pullback rather than guessing a regularization. Pass test-function space, support, pairing conventions, legal operations and weak identities to PDE analysis. If a regularized limit is used, state the regularization and prove independence where claimed. A numerical spike approximation is not a distribution identity until convergence against the declared test class is established.
