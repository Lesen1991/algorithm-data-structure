import copy

INFINITE = 10000
graph = {
    'a': {'a': 0, 'b': -1, 'c': 4, 'd': INFINITE, 'e': INFINITE},
    'b': {'a': INFINITE, 'b': INFINITE, 'c': 3, 'd': 2, 'e': 2},
    'c': {'a': INFINITE, 'b': INFINITE, 'c': INFINITE, 'd': INFINITE, 'e': INFINITE},
    'd': {'a': INFINITE, 'b': 1, 'c': 5, 'd': INFINITE, 'e': INFINITE},
    'e': {'a': INFINITE, 'b': INFINITE, 'c': INFINITE, 'd': -3, 'e': INFINITE}
    # 'a': {'a': 0, 'b': 5, 'c': 4, 'd': INFINITE, 'e': INFINITE},
    # 'b': {'a': INFINITE, 'b': INFINITE, 'c': 3, 'd': 2, 'e': 3},
    # 'c': {'a': INFINITE, 'b': INFINITE, 'c': INFINITE, 'd': INFINITE, 'e': INFINITE},
    # 'd': {'a': INFINITE, 'b': 1, 'c': 5, 'd': INFINITE, 'e': INFINITE},
    # 'e': {'a': INFINITE, 'b': INFINITE, 'c': INFINITE, 'd': 2, 'e': INFINITE}
}


def shortest_path_djs(graph, start):
    short_path = {start: 0}
    graph[start][start] = INFINITE
    while len(short_path) < len(graph):
        for i in graph[start]:
            if i == start:
                continue
            # 获取最小值
            min_key = min(graph[start], key=graph[start].get)
            # 最小值加入结果集
            short_path[min_key] = graph[start][min_key]
            # 判断其他点经过最小值点时是否有更小值，如果有，则更新最小值
            for j in graph[start]:
                if j == min_key or j == start:
                    continue
                if j not in short_path and graph[start][j] > graph[start][min_key] + graph[min_key][j]:
                    graph[start][j] = graph[start][min_key] + graph[min_key][j]
            # 将最小值标记为跳过
            graph[start][min_key] = INFINITE
    print({i: short_path[i] for i in sorted(short_path.keys())})


def bellman_ford(graph, start):
    s = {}
    for v in graph:
        s[v] = INFINITE
    s[start] = 0
    for i in graph:
        for j in graph[i]:
            if graph[j][i] != INFINITE and s[i] > s[j] + graph[j][i]:
                s[i] = s[j] + graph[j][i]
                for k in graph:
                    if s[k] > graph[i][k] + s[i]:
                        s[k] = graph[i][k] + s[i]
    print(s)


def floyd(graph, start):
    k_max = len(graph[start])
    for k in range(k_max):
        for i in range(k_max):
            for j in range(k_max):
                if i == k or j == k or i == j:
                    continue
                if graph[k][i] > graph[k][j] + graph[j][i]:
                    graph[k][i] = graph[k][j] + graph[j][i]
    print(graph)


# shortest_path_djs(copy.deepcopy(graph), 'a')
# floyd(copy.deepcopy(adjMat), 0)
bellman_ford(copy.deepcopy(graph), 'a')
# ({0: 0, 1: -1, 2: 2, 3: 1}, {0: None, 1: 0, 2: 1, 3: 1})
