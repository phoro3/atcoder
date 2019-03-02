N, A, B, C = map(int, input().split())
l_list = [int(input()) for _ in range(N)]

INF = 10 ** 5

def dfs(current, a, b, c):
    if current == N:
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return INF

    ret0 = dfs(current + 1, a, b, c)
    ret1 = dfs(current + 1, a + l_list[current], b, c) + 10
    ret2 = dfs(current + 1, a, b + l_list[current], c) + 10
    ret3 = dfs(current + 1, a, b, c + l_list[current]) + 10
    return min(ret0, ret1, ret2, ret3)

print(dfs(0, 0, 0, 0))