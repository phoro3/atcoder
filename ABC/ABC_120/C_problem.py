S = list(input())
S_len = len(S)
one_num = len(list(filter(lambda x: x == '1', S)))
zero_num = S_len - one_num

print(min(one_num, zero_num) * 2)