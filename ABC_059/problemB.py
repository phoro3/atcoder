#coding:utf-8
import math

if __name__ == "__main__":
    a = raw_input()
    b = raw_input()

    if len(a) > len(b):
        print "GREATER"
    elif len(a) < len(b):
        print "LESS"
    elif len(a) == len(b):
        for i in range(len(a)):
            if a[i] > b[i]:
                print "GREATER"
                break
            elif a[i] < b[i]:
                print "LESS"
                break
            elif a[i] == b[i] and i == len(a) - 1:
                print "EQUAL"


