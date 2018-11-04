#coding:utf-8

string = input()

res = ""
for i, char in enumerate(string):
    if i % 2 == 0:
        res += char
print (res)
