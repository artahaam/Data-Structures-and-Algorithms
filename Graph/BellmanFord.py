from Relax import try_to_relax
from Initialization import initialize

# weighted Graphs

W2 = {
    0: {1: 1, 3: 2, 4: -1},   #0
    1: {0: 1},                #1
    2: {3: 0},                #2
    3: {0: 2, 2: 0},          #3  
    4: {0: -1},               #4
    }
 

adj = dict()
for v in W2.keys():
    adj[v] = {u for u in W2[v].keys()}

def bellman_ford(adj, w, s): # Adj: adjacency list, w: weights, s: start
    # initialization
    d, parent = initialize(adj, s)
    # construct shortest paths in rounds
    V = len(adj) # number of vertices
    for k in range(V - 1): # relax all edges in (V - 1) rounds
        for u in range(V): # loop over all edges (u, v)
            for v in adj[u]: # relax edge from u to v
                try_to_relax(adj, w, d, parent, u, v)
                
    # check for negative weight cycles accessible from s
    for u in range(V): # Loop over all edges (u, v)
        for v in adj[u]:
            if d[v] > d[u] + w(u,v): # If edge relax-able, report cycle
                raise Exception('There is a negative weight cycle!')
    return d, parent


