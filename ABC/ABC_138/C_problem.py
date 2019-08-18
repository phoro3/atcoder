N = int(input())
v_list = map(int, input().split())

v_list = sorted(v_list)

total = v_list[0]
for i in range(1, N):
    total += v_list[i]
    total /= 2

print(total)