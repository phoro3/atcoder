S = list(input())

even_zero_list = list('0' * len(S))
odd_zero_list = list('0' * len(S))
for i in range(len(S)):
    if i % 2 != 0:
        even_zero_list[i] = '1'
    else:
        odd_zero_list[i] = '1'

even_diff = 0
odd_diff = 0
for i in range(len(S)):
    if S[i] != even_zero_list[i]:
        even_diff += 1
    if S[i] != odd_zero_list[i]:
        odd_diff += 1
print(min(even_diff, odd_diff))
