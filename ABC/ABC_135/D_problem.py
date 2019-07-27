#PyPy
S = list(input())
MOD = 10 ** 9 + 7

length = len(S)
dp = [[0] * 13 for _ in range(length + 1)]
dp[0][0] = 1

for i in range(length):
    if S[i] == '?':
        s = -1
    else:
        s = int(S[i])

    for j in range(10):
        if s != -1 and s != j:
            continue
        for k in range(13):
            index = (k * 10 + j) % 13
            dp[i + 1][index] = (dp[i + 1][index] + dp[i][k]) % MOD

print(dp[length][5])
