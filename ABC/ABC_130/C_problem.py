W, H , x, y = map(int, input().split())

flag = 0
if x + x == W and y + y == H:
    flag = 1

print(W * H / 2, flag)
