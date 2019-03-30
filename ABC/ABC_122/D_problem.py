N = int(input())
mod = 10 ** 9 + 7
memo = [{} for _ in range(N + 1)]

def is_agc(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]
        if ''.join(t).count('AGC') >= 1:
            return True
    return False

def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1
    ret = 0

    for char in 'ATGC':
        if not is_agc(last3 + char):
            ret = (ret + dfs(cur + 1, last3[1:] + char)) % mod
        memo[cur][last3] = ret
    return ret

print(dfs(0, 'TTT'))