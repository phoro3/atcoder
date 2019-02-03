N = int(input())
H = int(input())
W = int(input())

count = 0
for i in range(N):
    for j in range(N):
        if i + W <= N and j + H <= N:
            count += 1

print(count)