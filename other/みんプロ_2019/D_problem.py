# 参考
# https://atcoder.jp/contests/yahoo-procon2019-qual/submissions/4223019

L = int(input())
a_list = [int(input()) for _ in range(L)]

dp = [[0] * 5 for _ in range(L+1)]

for i in range(L):
    a = a_list[i]

    if a > 0:
        even = a % 2
    else:
        even = 2
    odd = (a + 1) % 2

    #0
    dp[i+1][0] = dp[i][0] + a
    #偶数（0であれば0の項目に含まれるはずなので、0より大きい偶数）
    dp[i+1][1] = min(dp[i][:2]) + even
    #奇数（スタートとゴールの間の区間）
    dp[i+1][2] = min(dp[i][:3]) + odd
    #偶数（0であれば0の項目に含まれるはずなので、0より大きい偶数）
    dp[i+1][3] = min(dp[i][:4]) + even
    #0
    dp[i+1][4] = min(dp[i][:5]) + a
print(min(dp[L]))