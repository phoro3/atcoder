N, M = map(int, input().split())
a_list = list(map(int, input().split()))

written_nums = []
for i in range(M):
    b, c = map(int, input().split())
    written_nums.append((c, b))

written_nums.sort(reverse = True)
append_list = []
for c, b in written_nums:
    append_list += [c for _ in range(b)]

    if len(append_list) >= N:
        break

a_list += append_list
a_list.sort(reverse = True)

print(sum(a_list[:N]))
