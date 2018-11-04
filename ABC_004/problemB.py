#coding:utf-8

input_matrix = []
LEN = 4

for i in range(LEN):
	input_matrix.append(raw_input().split(" "))


output_matrix = []
for i in range(LEN):
	output_matrix.append([""] * LEN)

for i in range(LEN):
	for j in range(LEN):
		output_matrix[i][j] = input_matrix[LEN - 1 - i][LEN - 1 - j]

		
for i in range(LEN):
	output = ""
	for j in range(LEN):
		if j == LEN - 1:
			output += output_matrix[i][j]
		else:	
			output += output_matrix[i][j] + " "
	print output		
