N = int(input())
a_list = list(map(int, input().split()))

negative_num = len([a for a in a_list if a < 0])
zero_num = len([a for a in a_list if a == 0])
abs_a_list = list(map(abs, a_list))

if negative_num % 2 == 0 or zero_num >= 1:
    print(sum(abs_a_list))
else:
    print(sum(abs_a_list) - 2 * min(abs_a_list))
