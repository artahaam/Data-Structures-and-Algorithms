def transpose(graph):
    t_graph = dict()
    for key in graph.keys():
        for value in graph[key]:
            if value in t_graph:
                if t_graph[value]:
                    t_graph[value].append(key)
            else:
                t_graph[value] = [key]
    return t_graph


if __name__ == '__main__':
    graph = dict()
    graph[0] = [1, 2]
    graph[1] = [0, 3]
    graph[2] = [3]
    graph[3] = [4]
    graph[4] = [2]

    print(graph)
    print(transpose(graph))
