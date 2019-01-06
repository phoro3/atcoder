import sys

C_MAX = 1000 + 1

if __name__ == "__main__":
    N, T = map(int, input().split())

    input_list = []
    for n in range(N):
        c, t = map(int, input().split())
        input_list.append((c, t))

    min_cost = C_MAX 

    for c, t in input_list:
        if t <= T and c < min_cost:
            min_cost = c

    if min_cost == C_MAX:
        print("TLE")
    else:
        print(min_cost)
            
