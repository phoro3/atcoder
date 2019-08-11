N = int(input())
h = [0] + list(map(int, input().split()))

dp = [-1] * (N + 1)
dp[N] = 0
dp[N - 1] = abs(h[N] - h[N - 1])

for i in reversed(range(1, N - 1)):
    dp[i] = min(dp[i + 1] + abs(h[i + 1] - h[i]), \
                dp[i + 2] + abs(h[i + 2] - h[i]))
print(dp[1])
