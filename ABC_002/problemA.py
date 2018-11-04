#coding:utf-8

input_num = raw_input().split(" ")
num1 = long(input_num[0])
num2 = long(input_num[1])

if num1 > num2:
	print num1
elif num2 > num1:
	print num2

