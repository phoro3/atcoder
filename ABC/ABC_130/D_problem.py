import numpy as np
N, K = map(int, input().split())
a_list = list(map(int, input().split()))

total = 0
count = 0
right = 0
for left in range(N):
    while right < N and total < K:
        total += a_list[right]
        right += 1

    if total < K:
        break
    count += N - right + 1
    if right == left:
        right += 1
    else:
        total -= a_list[left]
print(count)
