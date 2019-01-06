#coding:utf-8

num = long(raw_input())

turn = 1
x = 1

n = num
depth = 0
while n > 0:
    depth += 1
    n /= 2

if depth % 2 == 0:
    while True:
        if turn == 1:
            x *= 2
        else:
            x = 2 * x + 1
        
        if x > num:
            break
        turn *= -1
else:
    while True:
        if turn == 1:
            x = 2 * x + 1
        else:
            x *= 2
        
        if x > num:
            break
        turn *= -1            

if turn == 1:
    print "Aoki"
else:
    print "Takahashi"
