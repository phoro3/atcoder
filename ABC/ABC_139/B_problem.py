A, B = map(int, input().split())

if B == 1:
    print(0)
else:
    total = 1
    B -= A

    while B > 0:
        B -= A - 1
        total += 1
    print(total)