#coding:utf-8

from collections import defaultdict

if __name__ == "__main__":
    N, K = map(int, input().split(" "))

    num = defaultdict(int)
    for i in range(N):
        a, b = map(int, input().split(" "))
        num[a] += b

    count = 0
    for key in sorted(num.keys()):
        count += num[key]

        if count >= K:
            print (key)
            break
