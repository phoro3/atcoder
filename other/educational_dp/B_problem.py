N, K = map(int, input().split())
h = [0] + list(map(int, input().split()))

dp = [-1] * (N + 1)
dp[N] = 0
dp[N - 1] = abs(h[N] - h[N - 1])

for i in reversed(range(1, N - 1)):
    candidates = [10 ** 5] * K
    for k in range(1, K + 1):
        if i + k > N:
            continue
        candidates[k - 1] = dp[i + k] + abs(h[i + k] - h[i])
    dp[i] = min(candidates)
print(dp[1])
