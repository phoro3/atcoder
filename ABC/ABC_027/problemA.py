#coding:utf-8

input_str = map(int,raw_input().split(" "))
a, b, c = input_str[0], input_str[1], input_str[2]

if a == b:
    print c
elif a == c:
    print b
elif b == c:
    print a
