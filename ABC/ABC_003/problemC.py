#coding:utf-8

first_input = raw_input().split(" ")
num_class = int(first_input[0])
num_watch = int(first_input[1])

rate_list = map(int, raw_input().split(" "))
rate_list.sort()
rate_list.reverse()

#大きい方からレートを取る
use_rate_list = rate_list[0:num_watch]
#レートを小さい順に並び替え
use_rate_list.reverse()

t_rate = 0
for rate in use_rate_list:
	t_rate = (rate + t_rate) / 2.0

print t_rate
