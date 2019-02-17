N, M= map(int, input().split())
a_list = sorted(map(int, input().split()), reverse = True)

# インデックスを分かりやすくするために先頭に0を追加
match_num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

inf = 10 ** 5
dp = [-inf] * (N + 1)
dp[0] = 0

# 桁数を調べる
for i in range(1, N+1):
    dp[i] = max([dp[i - match_num[a]] + 1 for a in a_list if i - match_num[a] >= 0] + [-inf])

# 各桁に使う数字を調べる
ans = [""] * dp[N]
rest_match = N
for i in range(dp[N]):
    for a in a_list:
        index = rest_match - match_num[a]
        if index >= 0 and dp[index] == dp[N] - i - 1:
            rest_match -= match_num[a]
            ans[i] = str(a)
            break
print("".join(ans))
