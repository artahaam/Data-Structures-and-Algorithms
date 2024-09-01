from Relax import try_to_relax
from Initialization import initialize


def bellman_ford(adj, w, s): # Adj: adjacency list, w: weights, s: start
    # initialization
    d, parent = initialize(adj, s)
    # construct shortest paths in rounds
    V = len(adj)                                # number of vertices
    for k in range(V - 1):                      # relax all edges in (V - 1) rounds
        for u in adj.keys():                    # loop over all edges (u, v)
            for v in adj[u]:                    # relax edge from u to v
                try_to_relax(w, d, parent, u, v)
                
    # check for negative weight cycles accessible from s
    for u in adj.keys():                        # Loop over all edges (u, v)
        for v in adj[u]:
            if d[v] > d[u] + w[u][v]:            # If edge relax-able, report cycle
                d, parent = None, None
                return d, parent
    return d, parent



if __name__ == '__main__':
    # weighted graph
    #---------------------EX.1----------------------------------------------------
    print('\n' + ' '*10 + 'example 1 \n')
    
    # weighted graph
    W1 = {
        0: {1: -1, 2: 4},           #0
        1: {2: 3, 3: 2, 4: 2},      #1
        2: {},                      #2
        3: {1: 1, 2: 3},            #3  
        4: {3: -3},                 #4
        } 
    
    adj = dict()
    for v in W1.keys():
        adj[v] = {u for u in W1[v].keys()}
    
    # printing the result
    print(f'adjacency dictionary -> {adj} ')
    d, parent = bellman_ford(adj, W1, 0)
    print(f'distance list -> {d}')
    print(f'parent list -> {parent}')
    
    
    
    #---------------------EX.2----------------------------------------------------
    print('\n' + ' '*10 + 'example 2 \n')
    
    W2 = {
    0 : {1 : 1, 3 : 2, 4 : -1}, #0
    1 : {0 : 1},                #1
    2 : {3 : 0},                #2
    3 : {0 : 2, 2 : 0},         #3  
    4 : {0 : -1},               #4
    } 
    
    # adjacency dictionary 
    adj = dict()
    for v in W2.keys():
        adj[v] = {u for u in W2[v].keys()}
        
    # printing the result
    print(f'adjacency dictionary -> {adj} ')
    d, parent = bellman_ford(adj, W2, 0)
    print(f'distance list -> {d}')
    print(f'parent list -> {parent}')