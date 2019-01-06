#coding:utf-8

import math

def pascal(n, k, pascal_tri):
	if k > n / 2:
		k = n - k
	
	if pascal_tri[n][k] != 0:
		return pascal_tri[n][k]
	else:
		pascal_tri[n][k] = (pascal(n-1, k-1, pascal_tri) + pascal(n-1, k, pascal_tri)) % 1000000007
		return pascal_tri[n][k]
			


all_raw, all_col = map(int, raw_input().split(" "))
sep_raw, sep_col = map(int, raw_input().split(" "))
desk_num, rack_num = map(int, raw_input().split(" "))


#‹æ‰æ“à‚ÌŠ÷‚Æƒ‰ƒbƒN‚Ì•À‚×•û
#pattern_num = math.factorial(desk_num + rack_num) / (math.factorial(desk_num) * math.factorial(rack_num))

pascal_tri = []
pascal_tri.append([])
for i in range(1, 900 + 1):
	pascal_tri.append([1] + [0] * (i/2))

pattern_num = pascal(desk_num + rack_num, desk_num, pascal_tri)	



#‹æ‰æ‚ÌŽæ‚è•û
raw_num = 1
for i in range(1, all_raw + 1):
	if sep_raw + i <= all_raw:
		raw_num += 1

col_num = 1
for i in range(1, all_col + 1):
	if sep_col + i <= all_col:
		col_num += 1

total_sep = raw_num * col_num		

div = long(1000000007)
print pattern_num * total_sep % div
