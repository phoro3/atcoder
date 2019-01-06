#coding:utf-8


def judge(relation, present, node):
	for i in present:
		if [node, i] not in relation:
			return False

	return True		

def count_relation(relation, present, rest):
	max_size = 0
	for node in rest:
		if judge(relation, present, node): 
			present_copy = list(present)
			present_copy.append(node)
			rest_copy = list(rest)
			rest_copy.remove(node)
			size = count_relation(relation, present_copy, rest_copy)
			if size > max_size:
				max_size = size

	if max_size == 0:
		return len(present)
	else:
		return max_size

first_input = map(int, raw_input().split(" "))
people_num = first_input[0]
input_num = first_input[1]

relation = []
for i in range(input_num):
	relation.append(map(int, raw_input().split(" ")))

max_size = 0
for i in range(1, people_num + 1):
	node_list = range(1, people_num+1)
	node_list.remove(i)
	size = count_relation(relation, [i], node_list)

	if size > max_size:
		max_size = size

print max_size		
