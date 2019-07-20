N = int(input())
a_list = list(map(int, input().split()))

ball_list = [0] * (N + 1)
for n in reversed(range(1, N + 1)):
    mod = 0
    for i in range(n, N + 1, n):
        mod ^= ball_list[i]
    if mod != a_list[n - 1]:
        ball_list[n] = 1

num = sum(ball_list)
print(num)

if num > 0:
    for i, b in enumerate(ball_list):
        if b == 1:
            print(i)
