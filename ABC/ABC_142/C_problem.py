N = int(input())
a_list = list(map(int, input().split()))

result = [None] * N
for i in range(1, N + 1):
    index = a_list[i - 1]
    result[index - 1] = i
print(" ".join(map(str, result)))