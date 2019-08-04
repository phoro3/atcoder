N = int(input())
h_list = list(map(int, input().split()))

result = True
for i in reversed(range(1, N)):
    if h_list[i] < h_list[i - 1]:
        if h_list[i - 1] - h_list[i] >= 2:
            result = False
            break
        else:
            h_list[i - 1] -= 1
if result:
    print("Yes")
else:
    print("No")
