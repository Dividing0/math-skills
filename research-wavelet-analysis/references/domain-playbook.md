# Normalization, reconstruction and approximation

## Choose a branch
- Finite orthonormal transform: specify signal length, scaling and boundary convention. Verify the analysis matrix is orthogonal (or unitary) and write its inverse; this is a finite algebraic assertion, distinct from a continuous basis theorem.
- Continuous system: name the function space, translation/dilation lattice and normalization. Orthonormality requires pairwise inner products and completeness; a frame requires both positive lower and finite upper frame bounds before stable reconstruction is asserted.
- Thresholding or compression: in an orthonormal basis, squared L² error equals the sum of squares of discarded coefficients. A sparsity or decay rate requires assumptions about the function class and the wavelet's regularity and vanishing moments; thresholding is not automatically lossless.

## Worked Haar pair
For samples (a,b), define approximation c=(a+b)/sqrt(2) and detail d=(a-b)/sqrt(2). The analysis matrix (1/sqrt(2))*[[1,1],[1,-1]] satisfies A^T A=I. Therefore reconstruction gives a=(c+d)/sqrt(2), b=(c-d)/sqrt(2), and c²+d²=a²+b². For (3,1), c=2sqrt(2), d=sqrt(2). Discarding d reconstructs (2,2), with squared error 1²+(-1)²=2=d². This demonstrates exact reconstruction before thresholding and precisely quantified loss afterward.

## Tempting inference and counterexample
Zero mean of a candidate wavelet does not guarantee orthogonality of integer translates. Let psi=1_[0,2]-1_[2,4]. Its integral is zero, but the inner product of psi(t) with psi(t-1) is 1-1+1=1, obtained on the overlap intervals [1,2],[2,3],[3,4]. Their supports overlap and the translate pair is not orthogonal. A vanishing moment alone cannot certify a wavelet basis.

## Stop or hand off
For finite filtering, pass downsampling phase, extension at edges and reconstruction identities to implementation. If completeness or frame bounds are absent, return the verified orthogonality facts only. Keep quantization error, threshold error and boundary artifacts distinct. Do not export an infinite-domain L² theorem to short padded data without checking the finite transform convention and inverse.
