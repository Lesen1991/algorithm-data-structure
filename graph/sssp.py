import copy

INFINITE = 10000
adjMat = [[INFINITE] * 6 for i in range(6)]


def adj_matrix(matrix):
    matrix[0][1] = 50
    matrix[0][2] = 10
    matrix[0][4] = 45
    matrix[1][2] = 15
    matrix[1][4] = 10
    matrix[2][0] = 20
    matrix[2][3] = 15
    matrix[3][1] = 20
    matrix[3][4] = 35
    matrix[3][5] = 3
    matrix[4][3] = 30


def shortest_path_djs(graph, start):
    s = graph[start]
    short_path = {}
    has_visit = []
    pass_node = {}
    # 取出第一个最小值
    cache = []
    while len(short_path) < len(s) - 1:
        for i in range(len(s)):
            if i == start:
                continue
            if s[i] != INFINITE and i not in short_path.keys():
                cache.append(s[i])
        now_index = s.index(min(cache))
        node = '-' + str(now_index) if now_index not in pass_node else pass_node[now_index] + '-' + str(now_index)
        short_path[now_index] = {'node': node, 'len': min(cache)}
        has_visit.append(now_index)
        s[now_index] = INFINITE
        # 刷新 s
        for i in range(len(graph[start])):
            if i != start and i not in has_visit and short_path[now_index]['len'] + graph[now_index][i] < s[i]:
                s[i] = short_path[now_index]['len'] + graph[now_index][i]
                pass_node[i] = '-' + str(now_index) if now_index not in pass_node else pass_node[now_index] + '-' + str(
                    now_index)
        cache = []

    print({k: short_path[k] for k in sorted(short_path)})


def floyd(graph, start):
    k_max = len(graph[start])
    for k in range(k_max):
        for i in range(k_max):
            for j in range(k_max):
                if i == k or j == k or i == j:
                    continue
                if graph[k][j] + graph[i][k] < graph[i][j]:
                    graph[i][j] = graph[k][j] + graph[i][k]
    print(graph)


adj_matrix(adjMat)
shortest_path_djs(copy.deepcopy(adjMat), 1)
floyd(copy.deepcopy(adjMat), 1)
