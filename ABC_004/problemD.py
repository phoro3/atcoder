#coding:utf-8

def op_num(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	else:
		return n - 1 + op_num(n - 1)
		

red_num, green_num, blue_num = map(int, raw_input().split(" "))


red_c = op_num((red_num + 1) / 2) + op_num((red_num + 1) - (red_num + 1) / 2)
green_c = op_num((green_num + 1) / 2) + op_num((green_num + 1) - (green_num + 1) / 2)
blue_c = op_num((blue_num + 1) / 2) + op_num((blue_num + 1) - (blue_num + 1) / 2)

print red_c + green_c + blue_c
