N = int(input())
rewards = [None] * N
for i in range(N):
    a, b, c = map(int, input().split())
    rewards[i] = (a, b, c)

dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = max(dp[i - 1][1] + rewards[i - 1][0], dp[i - 1][2] + rewards[i - 1][0])
    dp[i][1] = max(dp[i - 1][0] + rewards[i - 1][1], dp[i - 1][2] + rewards[i - 1][1])
    dp[i][2] = max(dp[i - 1][0] + rewards[i - 1][2], dp[i - 1][1] + rewards[i - 1][2])
print(max(dp[N]))
