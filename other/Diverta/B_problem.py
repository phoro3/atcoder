R, G, B, N = map(int, input().split())

for r in filter(lambda x: x % R == 0 and x <= N // R, range(R + 1)):
    for g filter(lambda x: x % G == 0 and x <= N // G, range(G + 1)):
        for b filter(lambda x: x % B == 0 and x <= N // B, range(B + 1)):
