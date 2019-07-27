N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

total = 0
for i in range(N):
    b = b_list[i]

    defeated = min(a_list[i], b)
    a_list[i] -= defeated
    b -= defeated
    total += defeated

    defeated = min(a_list[i + 1], b)
    a_list[i + 1] -= defeated
    total += defeated
print(total)
