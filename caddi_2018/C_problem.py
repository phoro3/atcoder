#coding:utf-8
import math

def primeFact(P):
    s = math.floor(math.sqrt(P))
    result = {}

    for i in range(2, s + 1):
        if P % i == 0:
            r = 0
            while P % i == 0:
                r += 1
                P = P // i
            result[i] = r

    if P > s:
        result[P] = 1
    return result

def gcd(N, fact):
    gcd = 1
    for key in fact.keys():
        if fact[key] >= N:
            gcd *= key ** (fact[key] // N)
    return int(gcd)

if __name__ == "__main__":
    N, P = map(int, input().split())
    fact = primeFact(P)
    print(gcd(N, fact))