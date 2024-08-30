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
    return parent, level

if __name__ == '__main__':
    
    graph = dict()
    graph['a'] = ['b', 'd']
    graph['b'] = ['a', 'c']
    graph['c'] = ['b', 'd']
    graph['d'] = ['a', 'c']
    print(bfs(graph,'a'))