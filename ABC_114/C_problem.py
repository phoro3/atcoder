def solve(s):
    if int(s) > N:
        return 0

    ret = 0
    if all(s.count(c) >= 1 for c in '753'):
        ret = 1
    for c in '753':
        ret += solve(s + c)
    return ret

if __name__ == "__main__":
    N = int(input())
    print(solve('0'))