N, M = map(int, input().split())

l_list = [None] * M
r_list = [None] * M

allows = [0] * (N + 1)
for i in range(M):
    l, r = map(int, input().split())

    allows[l - 1] += 1
    allows[r] -= 1

total = 0
count = 0
for n in allows:
    total += n
    if total == M:
        count += 1
print(count)
