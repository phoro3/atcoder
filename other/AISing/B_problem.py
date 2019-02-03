N = int(input())
A, B = map(int, input().split())
p_list = list(map(int, input().split()))

first_list = list(filter(lambda x: x <= A, p_list))
second_list = list(filter(lambda x: A + 1 <= x <= B, p_list))
third_list = list(filter(lambda x: x >= B + 1, p_list))

print(min(map(len, [first_list, second_list, third_list])))