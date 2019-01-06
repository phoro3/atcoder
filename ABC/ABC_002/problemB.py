#coding:utf-8

input_str = str(raw_input())

result = ""
for char in input_str:
	if char != "a" and char != "i" and char != "u" and char != "e" and char != "o":
		result += char

print result		
