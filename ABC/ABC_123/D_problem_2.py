# TLE
X, Y, Z, K = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

a_list.sort(reverse = True)
b_list.sort(reverse = True)
c_list.sort(reverse = True)

max_k_list = [0] * (K ** 2)
i = 0
for a_i in range(X):
    for b_i in range(Y):
        for c_i in range(Z):
            if (a_i + 1) * (b_i + 1) * (c_i + 1) <= K:
                max_k_list[i] = a_list[a_i] + b_list[b_i] + c_list[c_i]
                i += 1

max_k_list.sort(reverse = True)
[print(k) for k in max_k_list[:K]]
