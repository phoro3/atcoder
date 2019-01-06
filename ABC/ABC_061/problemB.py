#coding:utf-8

from collections import defaultdict

if __name__ == "__main__":
    N, M = map(int, input().split(" "))

    roads = defaultdict(int)
    for i in range(M):
        a, b = map(int, input().split(" "))
        roads[a] += 1
        roads[b] += 1

    for j in range(1, N + 1):
        print (roads[j])
