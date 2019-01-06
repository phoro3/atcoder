#coding:utf-8

from heapq import *

def score(input_list):
    s = sum(input_list[:N])
    score_list = [s]
    l = input_list[:N]
    heapify(l)

    for val in input_list[N:2 * N]:
        s -= heappushpop(l, val)
        s += val
        score_list.append(s)

    return score_list

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split(" ")))
    B = list(map(lambda x : -x, reversed(A)))

    max_score = 0
    left_score = score(A)
    right_score = reversed(score(B))
    score_list = map(lambda x,y : x + y, left_score, right_score)
    print (max(score_list))

