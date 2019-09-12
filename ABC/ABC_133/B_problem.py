import math

def dist(p1, p2):
    total = 0
    for x, y in zip(p1, p2):
        total += (x - y) ** 2
    return total

N, D = map(int, input().split())
point_list = [None] * N

for i in range(N):
    point_list[i] = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i + 1, N):
        dis = math.sqrt(dist(point_list[i], point_list[j]))
        if dis == int(dis):
            count += 1
print(count)