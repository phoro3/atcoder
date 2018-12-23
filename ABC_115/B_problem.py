N = int(input())
p_list = [None] * N
for n in range(N):
    p_list[n] = int(input())

max_price = max(p_list)
p_list[p_list.index(max_price)] = max_price // 2
print(sum(p_list))