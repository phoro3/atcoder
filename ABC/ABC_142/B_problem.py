N, K = map(int, input().split())
h_list = list(map(int, input().split()))

print(len([h for h in h_list if h >= K]))