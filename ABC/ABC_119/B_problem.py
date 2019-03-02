N = int(input())
x_list = [0] * N
u_list = [0] * N
rate = 380000.0

total = 0.0
for i in range(N):
    x, u = input().split()
    x = float(x)
    if u == "BTC":
        total += rate * x
    else:
        total += x

print(total)\
