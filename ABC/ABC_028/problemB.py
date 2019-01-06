#coding:utf-8

string = raw_input()

count = [0] * 6
for c in string:
    if c == 'A':
        count[0] += 1
    elif c == 'B':
        count[1] += 1
    elif c == 'C':
        count[2] += 1
    elif c == 'D':
        count[3] += 1
    elif c == 'E':
        count[4] += 1
    elif c == 'F':
        count[5] += 1


for i in range(len(count)):
    if i == len(count) - 1:
        print count[i]
    else:
        print count[i],

