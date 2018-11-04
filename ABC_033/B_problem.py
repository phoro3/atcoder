#coding:utf-8

city_num = int(raw_input())
people = {}
for i in range(city_num):
    inp = raw_input().split(" ")
    name = inp[0]
    num = int(inp[1])
    people[name] = num

name_list = people.keys()
num_list = people.values()
total = sum(num_list)

if max(num_list) > total / 2:
    index = num_list.index(max(num_list))
    print name_list[index]
else:
    print "atcoder"
