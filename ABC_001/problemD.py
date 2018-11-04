#coding:utf-8

#数値を文字列に変換
#1ケタだったら先頭にゼロを足す
def add_zero(num):
	if num / 10 == 0:
		return "0" + str(num)
	else:
		return str(num)

#input
#データの第1要素：降雨開始時刻
#データの第2要素：降雨終了時刻
size = int(raw_input())
data = []
for i in range(size):
	input_data = raw_input()
	data.append(input_data.split("-"))


#データの変換（0時から経過した分に変換）
#データの丸め
for i in range(size):
	s_time = int(data[i][0])
	e_time = int(data[i][1])

	s_hour = s_time / 100
	s_min = s_time % 100
	s_min -= s_min % 5
	s_time = 60 * s_hour + s_min

	e_hour = e_time / 100
	e_min = e_time % 100
	if e_min % 5 != 0:
		e_min += 5 - e_min % 5
	e_time = 60 * e_hour + e_min	

	data[i] = [s_time, e_time]
	

#開始時刻でソート	
data = sorted(data, key=lambda x:x[0])


#連続した時間の調査
time_list = [0] * 1440
for single_data in data:
	s_index = single_data[0]
	e_index = single_data[1]

	time_list[s_index:(e_index+1)] = [1] * (e_index+1-s_index)


i = 0
result = []
while True:
	if time_list[i] == 1:
		s_index = i
		while time_list[i] == 1:
			e_index = i
			i += 1

			if i == len(time_list):
				break
		result.append([s_index, e_index])	
	i += 1	

	if i >= len(time_list):
		break


for data in result:
	print add_zero(data[0] / 60) + add_zero(data[0] % 60) + "-" + add_zero(data[1] / 60) + add_zero(data[1] % 60) 
