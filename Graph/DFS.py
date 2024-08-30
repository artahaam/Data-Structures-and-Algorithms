# Introduction to Algorithms: 6.006
# Massachusetts Institute of Technology
# Instructors: Erik Demaine, Jason Ku, and Justin Solomon
# Recitation 10

def dfs(adj, s, parent = None, order = None):           # adj: adjacency list, s: start 
    if parent is None:                                  # O(1) initialize parent list 
        parent = [None for v in adj]                    # O(V) (use hash if unlabeled) 
        parent[s] = s                                   # O(1) root 
        order = []                                      # O(1) initialize order array 
    for v in adj[s]:                                    # O(adj[s]) loop over neighbors 
        if parent[v] is None:                           # O(1) parent not yet assigned 
            parent[v] = s                               # O(1) assign parent 
            dfs(adj, v, parent, order)                  # Recursive call
    order.append(s)                                     # O(1) amortized
    return parent, order


def full_dfs(adj):                                      # adj: adjacency list 
    parent = [None for v in adj]                        # O(V) (use hash if unlabeled) 
    order = []                                          # O(1) initialize order list 
    for v in range(len(adj)):                           # O(V) loop over vertices 
        if parent[v] is None:                           # O(1) parent not yet assigned 
            parent[v] = v                               # O(1) assign self as parent (a root) 
            dfs(adj, v, parent, order)                  # DFS from v (BFS can also be used) 
    return parent, order


if __name__ == '__main__':
    
    #---------------------EX.1----------------------------------------------------
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['E','C', 'A']
    graph['C'] = ['A', 'B', 'E','F']
    graph['E'] = ['B', 'C']
    graph['F'] = ['C']


    adj = dict()
    equivalent = dict()
    for key in enumerate(graph.keys()):
        equivalent[key[1]] = key[0]
    for key in graph.keys():
        adj[equivalent[key]] = {equivalent[x] for x in graph[key]}
    
    print(full_dfs(adj)[1])
    
    #---------------------EX.2----------------------------------------------------
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['E','C', 'A']
    graph['C'] = ['A', 'B', 'E','F']
    graph['E'] = ['B', 'C']
    graph['F'] = ['G', 'H']
    graph['G'] = ['F', 'H']
    graph['H'] = ['G', 'G']

    adj = dict()
    equivalent = dict()
    for key in enumerate(graph.keys()):
        equivalent[key[1]] = key[0]
    for key in graph.keys():
        adj[equivalent[key]] = {equivalent[x] for x in graph[key]}
    
    print(full_dfs(adj)[1])
