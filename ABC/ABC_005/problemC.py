#coding:utf-8

time_limit = int(raw_input())
tako_num = int(raw_input())
tako_list = map(int, raw_input().split(" "))
people_num = int(raw_input())
people_list = map(int, raw_input().split(" "))


result = ""
if tako_num < people_num:
	result = "no" 
else:
	bought_num = 0
	for people_time in people_list:
		for tako_time in tako_list:
			if tako_time <= people_time and people_time <= tako_time + time_limit:
				tako_list.remove(tako_time)
				bought_num += 1
				break
				
	if len(people_list) == bought_num:
		result = "yes"
	else:
		result = "no"

print result
