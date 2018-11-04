#coding:utf-8

inst = raw_input().split(" ")

for i in range(len(inst)):
    if inst[i] == "Left":
        inst[i] = "<"
    elif inst[i] == "Right":
        inst[i] = ">"
    elif inst[i] == "AtCoder":
        inst[i] = "A"

s = " ".join(inst)
print s
