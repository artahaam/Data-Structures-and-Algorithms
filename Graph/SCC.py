# The algorithm to find the Strongly Connected Components
# 1. dfs on graph 
# 2. find the transpose graph
# 3. dfs on the transposed graph but in reversed order

from Transpose import transpose

# modifing the dfs and full_dfs function to retrieve strongly connected components 
def dfs(adj, s, parent = None, order = None, scc = None):
    if parent is None:
        parent = [None for v in adj]
        parent[s] = s
        order = []
    for v in adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(adj, v, parent, order, scc)
    scc.append(s)
    order.append(s)
    return parent, order, scc


def full_dfs(adj):                                   
    parent = [None for v in adj]                      
    order = []
    full_scc = []
    for v in adj.keys():
        scc = []
        if parent[v] is None:                                              
            parent[v] = v
            full_scc.append(dfs(adj, v, parent, order, scc)[2])
    return parent, order, full_scc


if __name__ == '__main__':
    
    #---------------------EX.1----------------------------------------------------
    graph = dict()
    graph[0] = [1, 2]
    graph[1] = [0, 3]
    graph[2] = [3]
    graph[3] = [4]
    graph[4] = [2]
    adj = graph

    # finding the transpose graph
    t_graph = transpose(graph)
    
    # retrieve SCCs
    strongly_connected_components = full_dfs(t_graph)[2] 
    print(strongly_connected_components)
    
    
    
    #---------------------EX.2----------------------------------------------------
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

    # finding the transpose graph
    t_graph = transpose(adj)
    
    # retrieve SCCs
    strongly_connected_components = full_dfs(t_graph)[2] 
    print(strongly_connected_components)