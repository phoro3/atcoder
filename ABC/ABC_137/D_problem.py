import heapq
N, M = map(int, input().split())

rewards = [[] for _ in range(M + 1)]
for i in range(N):
    a, b = map(int, input().split())
    if a <= M:
        rewards[a].append(b)

heap = []
total = 0
for day in range(1, M + 1):
    for reward in rewards[day]:
        heapq.heappush(heap, -reward)

    if len(heap) > 0:
        max_reward = heapq.heappop(heap)
        total += -max_reward

print(total)
