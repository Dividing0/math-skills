#!/usr/bin/env python3
"""Small finite-graph calculation with independently enumerated routes."""

if not __debug__:
    raise RuntimeError('Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE.')

import argparse,json,sys,platform,math
p=argparse.ArgumentParser();p.add_argument('--self-test',action='store_true');args=p.parse_args()
try:
 import networkx as nx
except ImportError as exc:
 print(json.dumps({'status':'dependency_missing','dependency':'networkx','error':str(exc)}),file=sys.stderr);sys.exit(2)
g=nx.DiGraph();g.add_weighted_edges_from([('s','a',4),('a','t',3),('s','b',2),('b','t',8)])
for _,_,d in g.edges(data=True):
 if not math.isfinite(d['weight']) or d['weight']<0: raise ValueError('Dijkstra needs finite nonnegative weights')
cost,path=nx.single_source_dijkstra(g,'s','t',weight='weight')
def enumerate_costs(node,target,visited,total):
 if node==target: return [total]
 return [cost for child,data in g[node].items() if child not in visited for cost in enumerate_costs(child,target,visited|{child},total+data['weight'])]
assert cost==min(enumerate_costs('s','t',{'s'},0))==7
assert sum(g[u][v]['weight'] for u,v in zip(path,path[1:]))==cost
h=nx.DiGraph();h.add_weighted_edges_from([('s','a',3),('s','b',4),('a','b',-2),('b','t',2)])
negative_path=nx.bellman_ford_path(h,'s','t',weight='weight')
assert negative_path==['s','a','b','t']
checks=['exhaustive_simple_path_cost','edge_cost_recomputation','negative_edge_bellman_ford']
if args.self_test:
 h.add_edge('b','a',weight=1)
 try: nx.bellman_ford_path(h,'s','t',weight='weight')
 except nx.NetworkXUnbounded: checks.append('negative_cycle_rejected')
 else: raise AssertionError('negative cycle was not rejected')
 g.add_node('isolated')
 try: nx.single_source_dijkstra(g,'s','isolated')
 except nx.NetworkXNoPath: checks.append('disconnected_target_rejected')
 else: raise AssertionError('disconnected route returned')
print(json.dumps({'status':'passed','claim_status':'finite_graph_computation','python':platform.python_version(),'networkx':nx.__version__,'path':path,'cost':cost,'checks':checks}))
