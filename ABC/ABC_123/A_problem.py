def solve(antennas, k):
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            if antennas[j] - antennas[i] > k:
                return False
    return True

antennas = [int(input()) for _ in range(5)]
k = int(input())

if solve(antennas, k):
    print("Yay!")
else:
    print(":(")
