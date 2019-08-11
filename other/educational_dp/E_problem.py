N, W = map(int, input().split())
items = [None] * N
for n in range(N):
    w, v = map(int, input().split())
    items[n] = (w, v)
V = 10 ** 5 + 1

dp = [[10 ** 9 + 1] * V for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(V):
        w, v = items[i]
        if j >= v:
            dp[i + 1][j] = min(dp[i][j - v] + w, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]

ans = 0
for v in range(V):
    if dp[N][v] <= W:
        ans = v
print(ans)
