from collections import defaultdict
roads = [list(map(int, input().split())) for _ in range(3)]

degree = defaultdict(int)

for r in roads:
    degree[r[0]] += 1
    degree[r[1]] += 1

odd_num = 0
for val in degree.values():
    if val % 2 != 0:
        odd_num += 1

if odd_num == 0 or odd_num == 2:
    print("YES")
else:
    print("NO")
