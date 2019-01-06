#coding:utf-8


if __name__ == "__main__":
    S = raw_input()
    T = raw_input()
    q = int(raw_input())

    S_sum = [0] * (len(S) + 1)
    T_sum = [0] * (len(T) + 1)

    for i, char in enumerate(S):
        if char == "A":
            S_sum[i+1] = S_sum[i] + 1
        elif char == "B":
            S_sum[i+1] = S_sum[i] + 2

    for i, char in enumerate(T):
        if char == "A":
            T_sum[i+1] = T_sum[i] + 1
        elif char == "B":
            T_sum[i+1] = T_sum[i] + 2

    for query in range(q):
        a, b, c, d = map(int, raw_input().split(" "))

        S_mod = (S_sum[b] - S_sum[a-1]) % 3
        T_mod = (T_sum[d] - T_sum[c-1]) % 3

        if S_mod == T_mod:
            print "YES"
        else:
            print "NO"

