N, M = map(int, input().split())
a_set = set()
for i in range(M):
    a_set.add(int(input()))
mod = 1000000007

ways = [0] * (N + 1)
if N not in a_set:
    ways[N] = 1
if N - 1 not in a_set:
    ways[N - 1] = 1

for n in reversed(range(N - 1)):
    if n in a_set:
        continue
    ways[n] = (ways[n + 1] + ways[n + 2]) % mod
print(ways[0])
