# Fixed-point hypotheses and conclusions

## Choose a branch
- Banach contraction: use a nonempty complete metric space X, a self-map T:X→X, and a global constant q<1 with d(Tx,Ty)<=q d(x,y). This gives a unique fixed point and convergence from every start in X; local derivative estimates need an invariant neighborhood first.
- Brouwer: a continuous self-map of a nonempty compact convex subset of finite-dimensional Euclidean space has a fixed point. It supplies existence; uniqueness and convergence of raw iteration require separate arguments.
- Schauder: for a nonempty closed bounded convex subset of a Banach space, a continuous self-map with relatively compact image has a fixed point. Boundedness alone does not replace relative compactness in infinite dimension.

## Worked contraction
On X=[0,1] with Euclidean distance, let T(x)=(x+1)/3. Its image is [1/3,2/3], and |T(x)-T(y)|=|x-y|/3. Completeness follows because X is closed in the real line. Solving x=(x+1)/3 gives x*=1/2. For consecutive exact iterates, |x_n-x*|<=q/(1-q)|x_n-x_(n-1)|=|x_n-x_(n-1)|/2 for n>=1, by summing the geometric tail of future increments. A computed rounded increment needs an additional arithmetic-error bound.

## Tempting inference and counterexample
Existence is not convergence. T(x)=1-x continuously maps [0,1] to itself and has the unique fixed point 1/2. Starting at 0 gives the alternating sequence 0,1,0,1,..., so Brouwer plus uniqueness still does not validate iteration. The map's Lipschitz constant is 1 rather than less than 1.

## Stop or hand off
When invariance or completeness is missing, state the failed hypothesis before extending the domain; check that any fixed point of the extension belongs to the original domain. For compactness arguments, preserve the topology and compactness proof. Hand numerical iteration its invariant set, contraction constant and exact a posteriori bound. If only existence is established, label uniqueness and algorithmic convergence unresolved rather than merging them into one assertion.
