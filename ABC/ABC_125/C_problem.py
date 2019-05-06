def euclid(a, b):
    if a < b:
        b, a = a, b
    if b == 0:
        return a

    return euclid(b, a % b)

if __name__ == "__main__":
    N = int(input())
    a_list = list(map(int, input().split()))

    l_list = [0] * (N + 1)
    r_list = [0] * (N + 1)

    for i in range(N):
        l_list[i + 1] = euclid(l_list[i], a_list[i])
    for i in reversed(range(N)):
        r_list[i] = euclid(r_list[i + 1], a_list[i])

    max_m = 0
    for i in range(N):
        m = euclid(l_list[i], r_list[i + 1])
        max_m = max(m, max_m)
    print(max_m)
