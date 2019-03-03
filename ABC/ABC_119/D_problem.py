import bisect

A, B, Q = map(int, input().split())
INF = 10 ** 12
s_list = [-INF] + [int(input()) for _ in range(A)] + [INF]
t_list = [-INF] + [int(input()) for _ in range(B)] + [INF]

for _ in range(Q):
    x = int(input())
    s_right_index = bisect.bisect_right(s_list, x)
    s_right = s_list[s_right_index]
    s_left = s_list[s_right_index - 1]
    t_right_index = bisect.bisect_right(t_list, x)
    t_right = t_list[t_right_index]
    t_left = t_list[t_right_index - 1]

    dist = INF
    for s in [s_right, s_left]:
        for t in [t_right, t_left]:
            dist = min(dist, abs(s - t) + abs(s - x), abs(t - s) + abs(t - x))
    print(dist)

