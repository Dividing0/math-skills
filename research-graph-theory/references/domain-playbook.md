# Domain playbook: research-graph-theory

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For connectivity or reachability, use BFS or DFS with specified directedness. Produce a spanning search tree for a positive result, or a partition with no admissible crossing edges for a negative result.
- For Euler trails in finite undirected graphs, check degree parity and connectivity of the non-isolated support. Connectivity of all vertices is unnecessarily strong when isolated vertices are allowed; directed variants require different balance conditions.
- For structural bounds, specify simple versus multi-graph hypotheses. Degree-sum arguments count loops twice, and parallel edges invalidate many simple-graph extremal bounds.

## Worked valid example

In a triangle with one pendant edge attached at vertex a, the degrees are 3 at a, 1 at the pendant vertex d and 2 at b,c. The edge support is connected and exactly two vertices have odd degree. A concrete Euler trail is d,a,b,c,a, traversing each of the four edges once. It cannot be an Euler circuit because entering and leaving every vertex would require all degrees even.

## Tempting inference and counterexample

Large minimum degree does not by itself ensure connectivity. The disjoint union of two copies of K₄ has minimum degree 3 but two connected components. Thresholds using the total vertex number must not be replaced by an absolute degree slogan.

## Stop conditions and handoff

Stop an absence claim when only heuristic failure is available. Hand off explicit vertex and edge sets, the graph convention and a verified witness or obstruction; route expensive exhaustive claims to certificate-based computational proof.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
