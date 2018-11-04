#coding:utf-8

#Can't answer in limited time

import math
from decimal import *

def f_t(A, B, C, t):
    return A * t + B * math.sin(C * t * math.pi)

def get_t(A, B, C):
    low = 0
    high = 400

    mid = 0
    while math.fabs(f_t(A, B, C, mid) - 100) > 1e-9:
        mid = (low + high) / 2.0

        if f_t(A, B, C, mid) < 100:
            low = mid
        else:
            high = mid

    return mid

if __name__ == "__main__":
    input_list = map(int, raw_input().split(" "))
    A = input_list[0]
    B = input_list[1]
    C = input_list[2]

    answer = get_t(A, B, C)
    print '{:.10f}'.format(answer) 
