N = int(input())
b_list = list(map(int, input().split()))

total = b_list[0] + b_list[-1]
for i in range(1, N - 1):
    total += min(b_list[i - 1], b_list[i])

print(total)