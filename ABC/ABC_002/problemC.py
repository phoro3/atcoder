#coding:utf-8

input_list = map(int, raw_input().split(" "))

p_list = []
p_list.append([input_list[0], input_list[1]])
p_list.append([input_list[2], input_list[3]])
p_list.append([input_list[4], input_list[5]])


deg_x = input_list[0]
deg_y = input_list[1]

for point in p_list:
	point[0] -= deg_x
	point[1] -= deg_y

#–ÊÏ‚ÌŒvZ
a = p_list[1][0]
b = p_list[1][1]
c = p_list[2][0]
d = p_list[2][1]
area = float(abs(a*d - b*c)) / 2

print area
