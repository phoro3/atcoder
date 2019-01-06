#coding:utf-8

total_num = int(raw_input())

time_list = []

for i in range(total_num):
	time_list.append(int(raw_input()))

print min(time_list)	
