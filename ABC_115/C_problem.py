N, K = map(int, input().split())
h_list = [None] * N
for n in range(N):
    h_list[n] = int(input())

h_list = list(sorted(h_list))

print(min(h_list[K - 1 + i] - h_list[i] for i in range(N - K + 1)))