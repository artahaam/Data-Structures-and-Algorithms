# Adjacency lists
graph = dict()
graph['a'] = ['b', 'd']
graph['b'] = ['a', 'c']
graph['c'] = ['b', 'd']
graph['d'] = ['a', 'c']

# Adjacency matrix
elements = sorted(graph.keys())
rows = cols = len(elements)
adj_matrix = [[0 for x in range(rows)] for i in range(cols)]

# Edge list
edges = []
for key in elements:
    for neighbor in graph[key]:
        edges.append((key, neighbor))


for edge in edges:
    x = elements.index(edge[0])
    y = elements.index(edge[1])
    adj_matrix[x][y] = 1

# Represent Graph with numbers instead of Letters
adj = dict()
equivalent = dict()

for key in enumerate(graph.keys()):
    equivalent[key[1]] = key[0]
for key in graph.keys():
    adj[equivalent[key]] = {equivalent[x] for x in graph[key]}

print(graph)
print(adj)