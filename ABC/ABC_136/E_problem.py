N, K = map(int, input().split())
a_list = list(map(int, input().split()))

total_a = sum(a_list)
#約数の列挙
candidates = set()
for i in range(1, total_a):
    if i * i > total_a:
        break
    if total_a % i == 0:
        candidates.add(i)
        candidates.add(total_a // i)

ans = 1
for x in candidates:
    remainders = sorted(map(lambda a: a % x, a_list))
    total_r = sum(remainders)
    border = total_r // x
    need = sum(remainders[:(N - border)])
    if need <= K:
        ans = max(ans, x)
print(ans)
