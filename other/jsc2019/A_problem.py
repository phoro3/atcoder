M, D = map(int, input().split())

count = 0
for d in range(22, D + 1):
    d1 = d // 10
    d2 = d % 10

    if d1 >= 2 and d2 >= 2 and d1 * d2 <= M:
        count += 1
print(count)