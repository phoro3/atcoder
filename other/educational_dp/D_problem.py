N, W = map(int, input().split())
items = [None] * N
for n in range(N):
    w, v = map(int, input().split())
    items[n] = (w, v)

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        w, v = items[i]
        if j >= w:
            dp[i + 1][j] = max(dp[i][j - w] + v, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]
print(dp[N][W])
