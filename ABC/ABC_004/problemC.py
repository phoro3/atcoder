#coding:utf-8

input_num = int(raw_input())

loop_num = input_num % 30

card = [1, 2, 3, 4, 5, 6]
tmp = 0
for i in range(loop_num):
	tmp = card[i % 5] 
	card[i % 5] = card[i % 5 + 1]
	card[i % 5 + 1] = tmp

card_str = map(str, card)
print "".join(card_str)	
