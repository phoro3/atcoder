#coding:utf-8

from collections import defaultdict
import itertools

inf = 10 ** 9

N, M, R = map(int, input().split(" "))
r_list = map(int, input().split(" "))

cost = defaultdict(dict)
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if i == j:
            cost[i][j] = 0
        else:
            cost[i][j] = inf
for i in range(M):
    A, B, C = map(int, input().split(" "))
    cost[A][B] = cost[B][A] = C

#get shortest path for each node pair
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

min_dist = inf
for route in itertools.permutations(r_list):
    dist = 0
    for i in range(len(route) - 1):
        min_arg = min(route[i], route[i + 1])
        max_arg = max(route[i], route[i + 1])
        dist += cost[min_arg][max_arg]
    min_dist = min(dist, min_dist)
print(min_dist)

