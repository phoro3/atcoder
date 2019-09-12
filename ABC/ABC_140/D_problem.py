N, K = map(int, input().split())
S = input()

total = 0
for i in range(1, N):
    if S[i - 1] == S[i]:
        total += 1

print(min(total + 2 * K, N - 1))