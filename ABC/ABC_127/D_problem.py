#TLE
N, M = map(int, input().split())
a_list = list(map(int, input().split()))
written_pairs = [None] * M

for i in range(M):
    b, c = map(int, input().split())
    a_list += [c] * b

a_list = sorted(a_list, reverse = True)

print(sum(a_list[:N]))
