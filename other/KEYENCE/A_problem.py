inputs = map(int, input().split())

target = [1, 9, 7, 4]

for n in inputs:
    if n in target:
        target.remove(n)

if len(target) == 0:
    print("YES")
else:
    print("NO")
