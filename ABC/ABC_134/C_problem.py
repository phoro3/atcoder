N = int(input())
a_list = [None] * N
for i in range(N):
    a_list[i] = int(input())

#remove duplicate
sorted_a = sorted(a_list, reverse = True)
max_a = sorted_a[0]

result = []
for a in a_list:
    if a == max_a:
        print(sorted_a[1])
    else:
        print(max_a)
