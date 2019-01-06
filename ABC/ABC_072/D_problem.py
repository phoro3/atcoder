#coding:utf-8

def add_count(zero_count):
    if zero_count >= 2:
        return zero_count - 1
    else:
        return zero_count

N = int(input())
p_list = list(map(int, input().split(" ")))

count = 0
for i in range(N):
    if p_list[i] == i + 1:
        if i == N - 1:
            p_list[i] ,p_list[i - 1] = p_list[i - 1] ,p_list[i]
        else:
            p_list[i], p_list[i + 1] = p_list[i + 1], p_list[i]
        count += 1

print (count)
