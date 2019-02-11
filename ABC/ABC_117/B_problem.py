N = int(input())
l_list = list(map(int, input().split()))

max_len = max(l_list)
other_total = sum(l_list) - max_len

if max_len < other_total:
    print("Yes")
else:
    print("No")
