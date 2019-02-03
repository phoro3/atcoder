N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = 0
diff_list = []
smaller_num = 0
for n in range(N):
    if A[n] < B[n]:
        total += B[n] - A[n]
        smaller_num += 1
    else:
        diff_list.append(A[n] - B[n])

diff_list = sorted(diff_list, reverse = True)
diff_total = 0
diff_count = 0
for i, diff in enumerate(diff_list):
    diff_total += diff
    if diff_total >= total:
        diff_count = i + 1
        break

if smaller_num == 0:
    print(0)
elif diff_total < total:
    print(-1)
else:
    print(smaller_num + diff_count)