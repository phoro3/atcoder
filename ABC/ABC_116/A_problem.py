import heapq

inputs = list(map(int, input().split()))
a, b = heapq.nsmallest(2, inputs)

print(a * b // 2)
