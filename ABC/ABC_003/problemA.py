#coding:utf-8

task = int(raw_input())

sum = 0
for i in range(1, task+1):
	sum += i * 10000

average = float(sum) / task

print int(round(average, 0))
