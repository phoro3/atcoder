N, M, X, Y = map(int, input().split())
x_list = map(int, input().split())
y_list = map(int, input().split())

x_max = max(x_list)
y_min = min(y_list)

war_flag = True
for z in range(x_max + 1, y_min + 1):
    if X < z <= Y:
        war_flag = False
        break

if war_flag:
    print("War")
else:
    print("No War")