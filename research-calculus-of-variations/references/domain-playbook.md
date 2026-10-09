# Variations, existence and sufficiency

## Choose a branch
- First variation: specify an admissible vector space or affine space and differentiability of the functional along permitted perturbations. Fixed endpoint perturbations vanish at the endpoints; free endpoints create natural boundary terms. Stationarity is only a necessary condition for an interior minimum.
- Direct method: use a nonempty admissible set, a finite infimum, a bounded minimizing sequence from coercivity, compactness in a named topology, closure of the constraints and lower semicontinuity in that topology. For reflexive spaces, bounded sequences have weakly convergent subsequences, but weak closure and weak lower semicontinuity remain separate obligations.
- Global comparison: convexity on a convex admissible set makes a stationary point globally minimizing when the first-order inequality is valid. Strict convexity yields at most one minimizer. Positive second variation supplies local conclusions only under an appropriate norm and quantitative control.

## Worked minimization
On absolutely continuous u:[0,1]→R with u' in L², u(0)=0 and u(1)=1, minimize J(u)=integral (u')². Write u=x+v with v endpoints zero. Then J(u)=1+2 integral v'+integral (v')²=1+integral (v')² because integral v'=v(1)-v(0)=0. Hence u=x attains the global minimum 1, uniquely since equality forces v'=0 almost everywhere and zero endpoint forces v=0. This comparison discharges sufficiency without relying only on Euler–Lagrange stationarity.

## Tempting inference and counterexample
For the same endpoints, K(u)=-integral (u')² has stationary curve u=x: its first variation against v is -2 integral v'=0. But K(x+a sin(pi x))=-1-a²pi²/2 decreases without bound as |a| grows. Stationarity does not even imply a local minimum here.

## Stop or hand off
If differentiation under the integral lacks domination, preserve the directional derivative obligation. If a minimizing sequence oscillates or concentrates, send the exact functional and topology to relaxation or compactness analysis. Deliver admissibility, boundary terms, existence, stationarity and minimality as separately justified statements.
