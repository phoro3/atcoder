from heapq import nsmallest
l, r = map(int, input().split())

ans = 10 ** 9
if r - l > 2019:
    ans = 0
else:
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            prod = (i * j) % 2019

            if prod < ans:
                ans = prod
print(ans)