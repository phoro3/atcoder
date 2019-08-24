N, K = map(int, input().split())
a_list = list(map(int, input().split()))
MOD = 10 ** 9 + 7

inversion = 0
for i in range(len(a_list)):
    for j in range(i + 1, len(a_list)):
        if a_list[i] > a_list[j]:
            inversion += 1

total_lower = 0
for i in range(len(a_list)):
    total_lower += len([x for x in a_list if x < a_list[i]])


total_k = (K * (K - 1)) // 2
total = (total_lower * total_k+ inversion * K) % MOD
print(total)