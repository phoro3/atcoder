#coding:utf-8
import math

A, B, C, D, E, F = map(int, input().split(" "))

w_list = []
for i in range(math.ceil(F / (100 * A)) + 1):
    for j in range(math.ceil(F / (100 * B)) + 1):
        if i == 0 and j == 0:
            continue
        water = 100 * A * i + 100 * B * j
        if water <= F:
            w_list.append(water)

s_list = []
for i in range(math.ceil(F / C) + 1):
    for j in range(math.ceil(F / D) + 1):
        sugar = C * i + D * j
        if sugar <= F:
            s_list.append(sugar)

max_c = 0
max_w = 100 * A
max_s = 0
for w in set(w_list):
    for s in set(s_list):
        if w + s > F:
            continue
        if s > int(E * w / 100):
            continue
        c = 100 * s / (w + s)
        if c > max_c:
            max_c = c
            max_w = w
            max_s = s

print(max_w + max_s, max_s, end = " ")
