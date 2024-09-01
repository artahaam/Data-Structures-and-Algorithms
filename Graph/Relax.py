# Introduction to Algorithms: 6.006
# Massachusetts Institute of Technology
# Instructors: Erik Demaine, Jason Ku, and Justin Solomon 
# Recitation 11

W2 = {
    0 : {1 : 1, 3 : 2, 4 : -1}, #0
    1 : {0 : 1},                #1
    2 : {3 : 0},                #2
    3 : {0 : 2, 2 : 0},         #3  
    4 : {0 : -1},               #4
    } 

def try_to_relax(adj, w, d, parent, u, v):
    # extract weights
    def w(u,v):
        return W2[u][v]
    
    if d[v] > d[u] + w(u, v): # better path through vertex u
        d[v] = d[u] + w(u, v) # relax edge with shorter path found
        parent[v] = u