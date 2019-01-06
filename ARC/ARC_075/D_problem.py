#coding:utf-8

import math

def enough(A, B, h_list, T):
    h_list = filter(lambda x: (x - B * T) > 0, h_list)
    h_list = map(lambda x : x - B * T, h_list)

    exp_num = 0
    for val in h_list:
        exp_num += math.ceil(val / (A - B))

    if exp_num <= T:
        return True
    else:
        return False

def binary_search(A, B, h_list, T_min, T_max):
    if T_min == T_max:
        return T_min
    else:
        T_mid = T_min + (T_max - T_min) // 2
        if enough(A, B, h_list, T_mid):
            return binary_search(A, B, h_list, T_min, T_mid)
        else:
            return binary_search(A, B, h_list, T_mid + 1, T_max)

if __name__ == "__main__":
    N, A, B = map(int, input().split(" "))

    h_list = []
    for i in range(N):
        h_list.append(int(input()))

    T_max = math.ceil(sum(h_list) / B)
    print(binary_search(A, B, h_list, 0, T_max))
