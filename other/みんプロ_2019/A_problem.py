N, K = map(int, input().split())


lst = range(1, N + 1, 2)

if len(lst) >= K:
    print("YES")
else:
    print("NO")
