def euclid(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

N = int(input())
a_list = list(map(int, input().split()))

min_g = 10 ** 9 + 1
for n in range(N-1):
    g = euclid(a_list[n], a_list[n+1])
    min_g = min(min_g, g)

print(min_g)
