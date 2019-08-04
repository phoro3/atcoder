S = list(input())

count = 1
index = 0
cur = 'R'
ans = [0] * len(S)
r_count = 1
for i in range(1, len(S)):
    if cur == 'R' and S[i] == 'L':
        cur = 'L'
        index = i
    elif cur == 'L' and S[i] == 'R':
        if count % 2 == 0:
            ans[index - 1] = count // 2
            ans[index] = count // 2
        else:
            if r_count % 2 != 0:
                ans[index - 1] = count // 2 + 1
                ans[index] = count // 2
            else:
                ans[index - 1] = count // 2
                ans[index] = count // 2 + 1
        cur = 'R'
        r_count = 0
        count = 0
    count += 1
    if S[i] == 'R':
        r_count += 1

    if i == len(S) - 1:
        if count % 2 == 0:
            ans[index - 1] = count // 2
            ans[index] = count // 2
        else:
            if r_count % 2 != 0:
                ans[index - 1] = count // 2 + 1
                ans[index] = count // 2
            else:
                ans[index - 1] = count // 2
                ans[index] = count // 2 + 1
print(" ".join(map(str, ans)))
