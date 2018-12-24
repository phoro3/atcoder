N = int(input())
MAX = 1000
for i in range(N, MAX):
    digit = str(i // 100)
    if all(x == digit for x in str(i)):
        print(i)
        break