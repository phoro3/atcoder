import math

# f(x) = 0からxまでのxor
def f(x):
    div = (x // 2) % 2
    if x % 2 == 0:
        return div ^ x
    else:
        return div ^ 1

A, B = map(int, input().split())
print(f(A - 1) ^ f(B))
