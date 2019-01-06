#coding:utf-8

inp = raw_input().split("+")

count = 0
for multi in inp:
    if "0" not in multi:
        count += 1

print count
