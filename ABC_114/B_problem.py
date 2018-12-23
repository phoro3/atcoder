N = input()
X = 753
min_diff = int(N)
for s in range(len(N) - 2):
    num = int(N[s] + N[s+1] + N[s+2])
    diff = abs(X - num)
    if diff < min_diff:
        min_diff = diff
print(min_diff)