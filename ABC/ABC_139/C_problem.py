N = int(input())
h_list = list(map(int, input().split()))

max_count = 0
count = 1
for i in range(N - 1):
    if h_list[i] >= h_list[i + 1]:
        count += 1
    else:
        max_count = max(count, max_count)
        count = 1
max_count = max(count, max_count)
print(max_count- 1)