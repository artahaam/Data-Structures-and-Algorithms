# Introduction to Algorithms: 6.006
# Instructors: Erik Demaine, Jason Ku, and Justin Solomon
# Recitation 9 


def bfs(adj, s):                            # Adj: adjacency list, s: starting vertex
    parent = [None for v in adj]            # O(V) 
    parent[s] = s                           # O(1) root
    level = [[s]]                           # O(1) initialize levels
    while 0 < len(level[-1]):               # O(?) last level contains vertices
        level.append([])                    # O(1) amortized, make new level
        for u in level[-2]:                 # O(?) loop over last full level
            for v in adj[u]:                # O(Adj[u]) loop over neighbors
                if parent[v] is None:       # O(1) parent not yet assigned
                    parent[v] = u           # O(1) assign parent from level[-2]
                    level[-1].append(v)     # O(1) amortized, add to border
    level.pop()                             # O(1) removing the empty level 
    return parent, level                    # returning parent and level lists


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
    
    print(bfs(adj, 0)[1])

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
    
    print(bfs(adj)[1])
