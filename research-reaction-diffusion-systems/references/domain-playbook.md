# Domain playbook: research-reaction-diffusion-systems

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For positivity, verify that each reaction component points inward when its concentration is zero and other concentrations are nonnegative. Combine this with compatible diffusion and boundary conditions and the required existence regularity.
- For homogeneous stability, compute the reaction Jacobian J. For a two-component real system, trace J<0 and det J>0 give strictly stable ODE linearization, but do not decide spatial stability.
- For spatial modes with scalar species diffusion matrix D, use Laplacian eigenvalues μ≥0 and analyze J-μD. A Turing instability requires an allowed mode with positive growth, not merely a continuum wavenumber outside the domain spectrum.

## Worked valid example

For u_t=dΔu-ku with d,k>0 and homogeneous Neumann conditions, expand in Laplacian modes -Δφ_j=μ_jφ_j. Each coefficient obeys a_j'=-(dμ_j+k)a_j, hence a_j(t)=a_j(0)e^(-(dμ_j+k)t). Since μ_j≥0, every mode decays; the constant mode decays at rate k. This is an exact linear modal conclusion and does not by itself establish properties of a nonlinear coupled reaction system.

## Tempting inference and counterexample

Stable ODE dynamics can be destabilized by unequal diffusion. Take J=[[1,2],[-2,-3]] with trace -2 and determinant 1, and D=diag(1,10). For an allowed mode μ=0.2, J-μD=[[0.8,2],[-2,-5]] has determinant 0 and is neutral; at μ=0.3 its determinant is 0.7(-6)+4=-0.2, so one eigenvalue is positive. A domain must actually admit that mode.

## Stop conditions and handoff

Stop pattern claims based solely on a linear unstable eigenvalue; saturation, positivity and nonlinear existence need further analysis. Hand off J, diffusion constants, boundary spectrum and the precise linear-versus-nonlinear status. Source: https://www.mcb111.org/w13/w13-lecture.html, two-component Turing stability derivation.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
