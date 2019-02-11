N, M = map(int, input().split())
x_list = list(map(int, input().split()))

x_list = sorted(x_list, reverse = True)
diff_list = [0] * (M - 1)

ans = 0
if M > N:
    for i in range(M-1):
        diff_list[i] = x_list[i] - x_list[i+1]

    diff_list = sorted(diff_list, reverse = True)
    ans = sum(diff_list[N-1:])
print(ans)