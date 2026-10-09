# Domain playbook: research-harmonic-analysis

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For periodic L² functions, Fourier coefficients and Parseval are Hilbert-space statements; equality is in L², not at every chosen representative value. For L¹ functions on R, the Fourier transform is defined by an absolutely convergent integral; pointwise inversion needs additional hypotheses, for example integrability of the transform with the standard continuous representative. For convolution in L¹, use Fubini justified by the product of L¹ norms. For sampled data, derive the sampling and window model before interpreting discrete coefficients as continuous-frequency information.

## Worked valid example

On [0,2π] with normalized measure dx/(2π), use coefficients c_k=∫f(x)e^-ikx dx/(2π). For f(x)=cos(2x), Euler's identity gives f=(e^2ix+e^-2ix)/2. Orthogonality of integer exponentials yields c₂=c₋₂=1/2 and all other coefficients zero. Thus Σ|c_k|²=1/2, equal to the normalized integral of cos²(2x). The normalization is essential: unnormalized integrals produce a factor 2π.

## Tempting invalid inference

Pointwise reconstruction cannot distinguish representatives that agree almost everywhere. The zero function and the function equal to one only at x=0 have identical L² Fourier coefficients, yet different values at zero. Coefficients determine an equivalence class, not arbitrary point values.

## Stop and handoff

State transform signs, constants, measure and convergence mode in the result. If a requested pointwise claim lacks regularity, supply an L² or almost-everywhere statement only when justified; pass sampling artifacts and implementation concerns to signal processing.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
