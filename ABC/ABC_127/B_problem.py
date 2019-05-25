r, D, x = map(int, input().split())

num = 10
current = x
for i in range(num):
    current = r * current - D
    print(current)
