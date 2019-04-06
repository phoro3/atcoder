import math

N = int(input())
people = [int(input()) for _ in range(5)]
max_turn = max(map(lambda x: math.ceil(N / x), people))
print(max_turn + 4)
