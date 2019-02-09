s = int(input())

dict = {}
dict[s] = 1

last_a = s
f = 0
n = 2
ans = 0
while True:
    if last_a % 2 == 0:
        last_a = last_a // 2
    else:
        last_a = 3 * last_a + 1

    if last_a not in dict.keys():
        dict[last_a] = n
    else:
        ans = n
        break
    n += 1

print(ans)