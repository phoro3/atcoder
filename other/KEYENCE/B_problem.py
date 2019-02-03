S = input()

keyence = "keyence"

isKey = False
for i in range(len(S) + 1):
    for j in range(i, len(S) + 1):
        rest_str = S[:i] + S[j:]
        if rest_str == keyence:
            isKey = True
            break
    if isKey:
        break

if isKey:
    print("YES")
else:
    print("NO")

