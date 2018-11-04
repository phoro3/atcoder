#coding:utf-8

import sys
from collections import defaultdict

if __name__ == "__main__":
    N, M = map(int, input().split(" "))

    V = set()
    E = []
    for i in range(M):
        a, b, c = map(int, input().split(" "))
        V.add(a)
        V.add(b)
        E.append((a, b, -c))

    dist = defaultdict(lambda :10**20 + 1)
    pre = {}
    dist[1] = 0


    for i in range(1, len(V)):
        for edge in E:
            u = edge[0]
            v = edge[1]

            if dist[v] > dist[u] + edge[2]:
                dist[v] = dist[u] + edge[2]
                pre[v] = u

    is_cycle = False
    cycle_node = []
    for edge in E:
        u = edge[0]
        v = edge[1]
        if dist[u] + edge[2] < dist[v]:
            is_cycle = True
            cycle_node.append(u)

    is_inf = False
    if is_cycle:
        route_node = N
        while route_node != 1:
            route_node = pre[route_node]
            if route_node in cycle_node:
                is_inf = True
                break


    if is_inf:
        print ("inf")
    else:
        print (-dist[N])
