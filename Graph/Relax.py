# Introduction to Algorithms: 6.006
# Massachusetts Institute of Technology
# Instructors: Erik Demaine, Jason Ku, and Justin Solomon 
# Recitation 11

from Initialization import initialize


def try_to_relax(w, d, parent, u, v):
    if d[v] > d[u] + w[u][v]:       # better path through vertex u
        d[v] = d[u] + w[u][v]       # relax edge with shorter path found
        parent[v] = u

        
if __name__ == '__main__':
    
    #---------------------EX.1----------------------------------------------------
    print('\n' + ' '*10 + 'example 1 \n')
    
    # weighted graph
    W = {
        0 : {1 : 1, 3 : 2, 4 : -1}, #0
        1 : {0 : 1},                #1
        2 : {3 : 0},                #2
        3 : {0 : 2, 2 : 0},         #3  
        4 : {0 : -1},               #4
        } 
    
    # adjacency dictionary 
    adj = dict()
    for v in W.keys():
        adj[v] = {u for u in W[v].keys()}
    print('the adjacency dictionary: ')
    print(adj)
    print('-'*40 + '\n')

    # initializing distance and parent lists
    d, parent = initialize(adj, 0)
    print(f'initialized distance -> {d} \ninitialized parent -> {parent}')
    print('-'*40 + '\n') 

    # relaxing all edges
    for u in adj.keys():
        for v in adj[u]:
            try_to_relax(W, d, parent, u, v)
    
    print(f'relaxed distance -> {d}')
    print('-'*80 + '\n')
    
    #---------------------EX.2----------------------------------------------------
    print(' '*10 +'example 2 \n')
    
    # weighted graph
    W = {
        0: {1: -1, 2: 4},           #0
        1: {2: 3, 3: 2, 4: 2},      #1
        2: {},                      #2
        3: {1: 1, 2: 3},            #3  
        4: {3: -3},                 #4
        } 
    
    # adjacency dictionary 
    adj = dict()
    for v in W.keys():
        adj[v] = {u for u in W[v].keys()}
    print(f'adjacency dictionary -> {adj} ')
    print('-'*40 + '\n')

    # initializing distance and parent lists
    d, parent = initialize(adj, 0)
    print(f'initialized distance -> {d} \ninitialized parent -> {parent}')
    print('-'*40 + '\n') 

    # relaxing all edges
    for u in adj.keys():
        for v in adj[u]:
            try_to_relax(W, d, parent, u, v)
    
    print(f'relaxed distance -> {d}')
    print('-'*40)