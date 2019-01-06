#coding:utf-8


N, H, W = map(int, input().split())
count = 0
for n in range(N):
    a, b = map(int, input().split())
    if a >= H and b >= W:
        count += 1
print(count)