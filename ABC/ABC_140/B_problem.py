N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

points = b_list[a_list[0] - 1]
for i in range(1, N):
    points += b_list[a_list[i] - 1]
    if a_list[i] == a_list[i - 1] + 1:
        points += c_list[a_list[i - 1] - 1]
print(points)