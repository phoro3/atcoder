A, B = map(int, input().split())

if abs(A - B) >= 2:
    max_num = max(A, B)
    print(max_num + max_num - 1)
else:
    print(A + B)
