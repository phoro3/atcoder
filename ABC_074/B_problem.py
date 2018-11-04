#coding:utf-8

N = int(input())
K = int(input())
x_list = map(int, input().split(" "))

dist = 0
for x in x_list:
    dist += 2 * min(x, K - x)
print(dist)
