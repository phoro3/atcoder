import math

N, K = map(int, input().split())

total = 0
for d in range(1, N + 1):
    if d < K:
        ceil = math.ceil(math.log2(K) - math.log2(d))
        total += 1 / (2 ** ceil)
    else:
        total += 1

print(total / N)
