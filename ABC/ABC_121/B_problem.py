def dot(a_list, b_list):
    prod = 0
    for a, b in zip(a_list, b_list):
        prod += a * b
    return prod

N, M, C = map(int, input().split())
b_list = list(map(int, input().split()))
a_lists = [list(map(int, input().split())) for _ in range(N)]

count = 0
for a_list in a_lists:
    prod = dot(a_list, b_list)
    if prod + C > 0:
        count += 1

print(count)


