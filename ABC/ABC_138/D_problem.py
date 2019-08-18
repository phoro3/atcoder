from collections import defaultdict

N, Q = map(int, input().split())

parent = defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    parent[b] = a

values = [0] * (N + 1)
for i in range(Q):
    p, x = map(int, input().split())
    values[p] += x


for i in range(2, N + 1):
    values[i] += values[parent[i]]
values = map(str, values[1:])
print(" ".join(values))