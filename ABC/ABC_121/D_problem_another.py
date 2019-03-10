# O(log(B))で求める場合

import math

# f(x) = 0からxまでのxor
def f(x):
    if x <= 0:
        return 0
    x += 1
    digit = math.ceil(math.log2(x)) + 1

    ret = 0
    for d in range(digit):
        loop = 1 << (d + 1)
        count = (x // loop) * (loop // 2)
        count += max(0, x % loop - loop // 2)

        if count % 2 == 1:
            ret += 1 << d
    return ret



A, B = map(int, input().split())
print(f(A - 1) ^ f(B))
