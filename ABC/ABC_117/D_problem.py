def f(x, a_list):
    return sum(map(lambda y: y ^ x, a_list))

N, K = map(int, input().split())
a_list = list(map(int, input().split()))

bit_num = len(bin(K)) - 2
dp = ["0" for _ in range(bit_num)]

for i in range(bit_num):
    bits = dp[:i]

    one = bits + ["1"] + ["0"] * (bit_num - i - 1)
    zero = bits + ["0"] + ["0"] * (bit_num - i - 1)

    if f(int("".join(one), 2), a_list) > f(int("".join(zero), 2), a_list) and int("".join(one), 2) <= K:
        dp[i] = "1"
    else:
        dp[i] = "0"
print(f(int("".join(dp), 2), a_list))

