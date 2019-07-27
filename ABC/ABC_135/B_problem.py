N = int(input())
p_list = list(map(int, input().split()))

swap = 0
result = True
for i in range(1, N + 1):
    if p_list[i - 1] != i:
        swap += 1
    if swap > 2:
        result = False
        break

if result:
    print("YES")
else:
    print("NO")
