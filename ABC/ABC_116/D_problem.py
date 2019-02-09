# 参考
# https://dalekspritner.hatenablog.com/entry/2019/01/20/233645

from collections import defaultdict

N, K = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(N)]

sushi = sorted(sushi, key = lambda x: x[1], reverse = True)
types = set()
max_vals = [0]
other_vals = [0]

for typ, val in sushi:
    if typ not in types:
        max_vals.append(max_vals[-1] + val)
        types.add(typ)
    else:
        other_vals.append(other_vals[-1] + val)

max_score = 0
for k in range(1, K + 1):
    if K - k < len(other_vals) and k < len(max_vals):
        score = max_vals[k] + other_vals[K - k] + k ** 2
        max_score = max(max_score, score)

print(max_score)
