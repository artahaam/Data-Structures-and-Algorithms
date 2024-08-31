# Introduction to Algorithms: 6.006
# Massachusetts Institute of Technology
# Instructors: Erik Demaine, Jason Ku, and Justin Solomon
# Recitation 9


from BFS import bfs

def unweighted_shortest_path(adj, s, t):
    parent = bfs(adj, s)[0]                 # O(V + E) BFS tree from s 
    if parent[t] is None:                   # O(1) t reachable from s? 
        return None                         # O(1) no path 
    i = t                                   # O(1) label of current vertex 
    path = [t]                              # O(1) initialize path 
    while i != s:                           # O(V) walk back to s 
        i = parent[i]                       # O(1) move to parent 
        path.append(i)                      # O(1) amortized add to path
    return path[::-1]                       # O(V) return reversed path



if __name__ == '__main__':
    
    #---------------------EX.1----------------------------------------------------
    graph = dict()
    graph[0] = [1, 2]
    graph[1] = [0, 3]
    graph[2] = [3]
    graph[3] = [4]
    graph[4] = [2]
    adj = graph
    
    print(unweighted_shortest_path(adj, 0, 4))
    print(unweighted_shortest_path(adj, 1, 3))

    #---------------------EX.2----------------------------------------------------
    graph = dict()
    graph[0] = [2]
    graph[1] = [0]
    graph[2] = []
    graph[3] = [1, 2]
    graph[4] = []
    adj = graph
    
    print(unweighted_shortest_path(adj, 0, 4))
    print(unweighted_shortest_path(adj, 1, 3))

    
    
    
    
    
    
    
    
    

    
    
    
    
    
    