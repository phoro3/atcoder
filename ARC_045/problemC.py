#coding:utf-8

import collections
import copy

N, X = map(int, raw_input().split(" "))

edge_list = collections.defaultdict(list)

weight = [list()]*N
for i in range(N):
    weight[i] = [0]*N

for i in range(N-1):
    j, k, w = map(int, raw_input().split(" "))

    #decrement index
    j -= 1
    k -= 1

    edge_list[j].append(k)
    edge_list[k].append(j)
    weight[j][k] = w
    weight[k][j] = w


path_list = []
is_checked = [False for x in range(N)]
S = []

for i in range(N):
    is_checked = [False] * N
    parent = [-1] * N
    cost = 0

    path = []
    S = [i]
    is_checked[i] = True
    last_node = i


    while len(S) != 0:
        node = S.pop()
        path.append(node)
        
        w = weight[last_node][node]
        cost = cost ^ w

        if cost == X:
            if path not in path_list:
                path_list.append(copy.deepcopy(path))


        is_neighbor = False
        for neighbor in edge_list[node]:
            if not is_checked[neighbor]:
                is_checked[neighbor] = True
                S.append(neighbor)
                parent[neighbor] = node
                is_neighbor = True
                break

        if not is_neighbor:
            if parent[node] != -1:
                S.append(parent[node])
                path.pop()
                path.pop()
            else:
                break
        last_node = node

result = []
for path in path_list:
    if path not in result and path.reverse() not in result:
        result.append(path)

print len(result)
