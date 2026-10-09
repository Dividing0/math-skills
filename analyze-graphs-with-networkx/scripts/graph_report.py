#!/usr/bin/env python3
"""Inspect finite simple graph structure, shortest paths and maximum flows."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from itertools import pairwise
from pathlib import Path

DEPENDENCIES = ("networkx",)
EVIDENCE = "finite-graph-computation; floating weights retain rounding error"
EXAMPLE = {
    "operation": "shortest-path",
    "directed": True,
    "nodes": ["s", "a", "t", "isolated"],
    "edges": [
        {"source": "s", "target": "a", "weight": 2},
        {"source": "a", "target": "t", "weight": 3},
    ],
    "source": "s",
    "target": "t",
}


def compute(data):
    import networkx as nx

    nodes = data["nodes"]
    if any(not isinstance(v, (str, int)) or isinstance(v, bool) for v in nodes) or len(
        set(nodes)
    ) != len(nodes):
        raise ValueError("nodes must be distinct strings or integers")
    if len(nodes) > 10000:
        raise ValueError("at most 10000 nodes")
    directed = data.get("directed", False)
    if type(directed) is not bool:
        raise TypeError("directed must be Boolean")
    graph = nx.DiGraph() if directed else nx.Graph()
    graph.add_nodes_from(nodes)
    for edge in data["edges"]:
        u, v = edge["source"], edge["target"]
        if u not in graph or v not in graph or u == v or graph.has_edge(u, v):
            raise ValueError(
                "unknown endpoint, loop or duplicate edge; this helper handles simple graphs"
            )
        weight = edge["weight"]
        if type(weight) not in (int, float) or not math.isfinite(weight):
            raise ValueError("every edge requires a finite numeric weight")
        graph.add_edge(u, v, weight=weight)
    components = (
        nx.weakly_connected_components(graph)
        if isinstance(graph, nx.DiGraph)
        else nx.connected_components(graph)
    )
    result = {
        "nodes": len(graph),
        "edges": graph.number_of_edges(),
        "components": [list(c) for c in components],
        "directed": directed,
    }
    op = data.get("operation", "summary")
    if op == "shortest-path":
        source, target = data["source"], data["target"]
        if source not in graph or target not in graph:
            raise ValueError("source and target must be nodes")
        try:
            if any(d["weight"] < 0 for _, _, d in graph.edges(data=True)):
                distance, path = nx.single_source_bellman_ford(
                    graph, source, target, weight="weight"
                )
            else:
                distance, path = nx.single_source_dijkstra(
                    graph, source, target, weight="weight"
                )
            recomputed = sum(graph[u][v]["weight"] for u, v in pairwise(path))
            result.update(
                path=path,
                distance=distance,
                recomputed_cost=recomputed,
                path_status="found",
            )
        except nx.NetworkXNoPath:
            result["path_status"] = "unreachable"
        except nx.NetworkXUnbounded:
            result["path_status"] = "source-reachable-negative-cycle"
            result["scope"] = (
                "Bellman-Ford rejects a reachable negative cycle; target-specific unboundedness is not established"
            )
    elif op == "max-flow":
        if not directed or any(d["weight"] < 0 for _, _, d in graph.edges(data=True)):
            raise ValueError(
                "flow requires a directed graph with nonnegative weights used as capacities"
            )
        source, target = data["source"], data["target"]
        if source == target or source not in graph or target not in graph:
            raise ValueError("flow requires distinct known source and target")
        value, flow = nx.maximum_flow(graph, source, target, capacity="weight")
        cut, (left, right) = nx.minimum_cut(graph, source, target, capacity="weight")
        violations = [
            abs(sum(flow[u].get(v, 0) for u in graph) - sum(flow[v].values()))
            for v in graph
            if v not in {source, target}
        ]
        result.update(
            flow_value=value,
            cut_capacity=cut,
            cut=[list(left), list(right)],
            flow=[
                {"source": u, "target": v, "value": amount}
                for u, edges in flow.items()
                for v, amount in edges.items()
            ],
            max_conservation_residual=max(violations, default=0),
            duality_gap=value - cut,
        )
    elif op == "summary":
        if isinstance(graph, nx.DiGraph):
            result["strong_components"] = [
                list(c) for c in nx.strongly_connected_components(graph)
            ]
        else:
            result["bipartite"] = nx.is_bipartite(graph)
    else:
        raise ValueError("operation must be summary, shortest-path or max-flow")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="-", help="JSON file, or - for stdin")
    parser.add_argument(
        "--example", action="store_true", help="Print an example input and exit"
    )
    args = parser.parse_args()
    if args.example:
        print(json.dumps(EXAMPLE, indent=2))
        return 0
    try:
        source = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
        data = json.loads(source, parse_constant=reject_constant)
        if not isinstance(data, dict):
            raise TypeError("input must be a JSON object")
        result = compute(data)
        payload = {
            "status": "completed",
            "evidence": EVIDENCE,
            "result": result,
            "input_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "versions": {
                "python": platform.python_version(),
                **{name: importlib.metadata.version(name) for name in DEPENDENCIES},
            },
        }
        print(json.dumps(payload, indent=2, allow_nan=False))
        return 0
    except ImportError as exc:
        print(json.dumps({"status": "dependency_missing", "error": str(exc)}))
        return 3
    except (
        ValueError,
        TypeError,
        KeyError,
        IndexError,
        ArithmeticError,
        OSError,
        SyntaxError,
        RuntimeError,
        NotImplementedError,
    ) as exc:
        print(
            json.dumps(
                {
                    "status": "failed",
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )
        )
        return 1


def reject_constant(value):
    raise ValueError(f"nonfinite JSON number: {value}")


if __name__ == "__main__":
    sys.exit(main())
