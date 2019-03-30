N, Q = map(int, input().split())
S = input()

flags = [0] * len(S)
for i in range(len(S) - 1):
    flags[i + 1] = flags[i] + (1 if S[i:i + 2] == "AC" else 0)

for _ in range(Q):
    l, r = map(lambda x: x - 1, map(int, input().split()))
    print(flags[r] - flags[l])
