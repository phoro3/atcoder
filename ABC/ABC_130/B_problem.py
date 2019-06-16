N, X = map(int, input().split())
l_list = list(map(int, input().split()))

bounce_list = [0] * (N + 1)
for i in range(1, N + 1):
    bounce_list[i] = bounce_list[i - 1] + l_list[i - 1]

print(len([i for i in bounce_list if i <= X]))
