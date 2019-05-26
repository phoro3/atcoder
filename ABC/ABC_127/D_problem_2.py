N, M = map(int, input().split())
a_list = list(map(int, input().split()))
written_nums = []

for i in range(M):
    b, c = map(int, input().split())
    written_nums.append((c, b))

a_list = sorted(a_list)
written_nums = sorted(written_nums, reverse = True)

append_list = []
for c, b in written_nums:
    append_list += [c for _ in range(b)]

    if len(append_list) >= N:
        break
append_list.sort(reverse = True)


total = sum(a_list)
max_total = total
for i in range(min(N, len(append_list))):
    total -= a_list[i]
    total += append_list[i]
    max_total = max(max_total, total)

print(max_total)
