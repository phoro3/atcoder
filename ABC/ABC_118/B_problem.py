from collections import defaultdict
N, M = map(int, input().split())

a_dic = defaultdict(int)
for _ in range(N):
    a_list = list(map(int, input().split()))[1:]

    for a in a_list:
        a_dic[a] += 1

ans = 0
for val in a_dic.values():
    if val == N:
        ans += 1

print(ans)