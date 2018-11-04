#coding:utf-8

#c‚ª@‚Å’uŠ·‰Â”\‚©‚Ç‚¤‚©
def is_replace_at(c):
	at_list = ["a", "t", "c", "o", "d", "e", "r"]

	if c in at_list:
		return True
	else:
		return False

def judge_win(str_s, str_t):
	for i in range(len(str_s)):
		if str_s[i] != str_t[i]:
			if str_s[i] == "@":
				if not is_replace_at(str_t[i]):
					return False
			elif str_t[i] == "@":
				if not is_replace_at(str_s[i]):
					return False
			else:
				return False
	return True			


str_s = raw_input()
str_t = raw_input()

win_flag = judge_win(str_s, str_t)

if win_flag:
	print "You can win"
else:
	print "You will lose"	

					 
		
