N = int(input())
w_list = list(map(int, input().split()))

min_diff = 100 * 4
for i in range(N):
    former = sum(w_list[:i])
    latter = sum(w_list[i:])
    min_diff = min(min_diff, abs(former - latter))

print(min_diff)
