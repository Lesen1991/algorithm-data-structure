INFINITE = 10000


def kruskal(graph, nodenum, edgenum):
    res = []
    if nodenum <= 0 or edgenum < nodenum - 1:
        return res
    edge_list = []
    for i in range(nodenum):
        for j in range(i, nodenum):
            # if i == j:
            #     continue
            if graph[i][j] < INFINITE:
                edge_list.append([i, j, graph[i][j]])  # 按[begin, end, weight]形式加入
    edge_list.sort(key=lambda a: a[2])  # 已经排好序的边集合
    group = [[i] for i in range(nodenum)]
    for edge in edge_list:
        for i in range(len(group)):
            if edge[0] in group[i]:
                m = i
            if edge[1] in group[i]:
                n = i
        if m != n:
            res.append(edge)
            group[m] = group[m] + group[n]
            group[n] = []
    return res


def prim(graph, nodenum, edgenum):
    res = []
    if nodenum <= 0 or edgenum < nodenum - 1:
        return res
    res = []
    seleted_node = [0]
    candidate_node = [i for i in range(1, nodenum)]

    while len(candidate_node) > 0:
        begin, end, minweight = 0, 0, INFINITE
        for i in seleted_node:
            for j in candidate_node:
                if graph[i][j] < minweight:
                    minweight = graph[i][j]
                    begin = i
                    end = j
        res.append([begin, end, minweight])
        seleted_node.append(end)
        candidate_node.remove(end)
    return res


adjMat = [[INFINITE] * 6 for i in range(6)]


def adj_matrix(matrix):
    matrix[0][1] = 4
    matrix[0][2] = 4
    matrix[1][0] = 4
    matrix[1][2] = 2
    matrix[2][0] = 4
    matrix[2][1] = 2
    matrix[2][3] = 3
    matrix[2][4] = 2
    matrix[2][5] = 4
    matrix[3][2] = 3
    matrix[3][5] = 3
    matrix[4][2] = 2
    matrix[4][5] = 3
    matrix[5][3] = 3
    matrix[5][2] = 4
    matrix[5][4] = 3


adj_matrix(adjMat)
print(kruskal(adjMat, 6, 16))
print(prim(adjMat, 6, 16))
