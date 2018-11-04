#coding:utf-8

N, K = map(int, raw_input().split(" "))

less_k = K - 1
more_k = N - K
all_pat = N ** 3

pattern = 0
#all of three are same
pattern += 1

#two of three are same
pattern += 3 * (less_k + more_k)

#one of three is median
pattern += 6 * (less_k * more_k)

print float(pattern) / all_pat
