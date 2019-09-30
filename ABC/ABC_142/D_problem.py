def prime_facorize(N):
    res = {1}
    for i in range(2, int(N ** 0.5) + 1):
        while N % i == 0:
            res.add(i)
            N /= i

        if N <= 1:
            break
    if N > 1:
        res.add(N)
    return res


A, B = map(int, input().split())
commons = prime_facorize(A) & prime_facorize(B)
print(len(commons))