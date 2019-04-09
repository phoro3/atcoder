# TLE
X, Y, Z, K = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))


ab_sum = [0] * (X * Y)
i = 0
for a in a_list:
    for b in b_list:
        ab_sum[i] = a + b
        i += 1
ab_sum.sorta(reverse = True)

answer_sums = [0] * (K * Z)
i = 0
for e in ab_sum[:K]:
    for c in c_list:
        answer_sums[i] = e + c
        i += 1
answer_sums.sort(reverse = True)
[print(num) for num in answer_sums[:K]]




