#coding:utf-8

from decimal import *
deg, dis = map(int, raw_input().split(" "))



speed = Decimal(dis) / Decimal(60)
speed = Decimal(speed).quantize(Decimal(".1"), rounding=ROUND_HALF_UP)
speed = float(speed)

if speed >= 0.0 and speed <= 0.2:
	power = 0
elif speed >= 0.3 and speed <= 1.5:
	power = 1
elif speed >= 1.6 and speed <= 3.3:
	power = 2 
elif speed >= 3.4 and speed <= 5.4:
	power = 3
elif speed >= 5.5 and speed <= 7.9:
	power = 4
elif speed >= 8.0 and speed <= 10.7:
	power = 5
elif speed >= 10.8 and speed <= 13.8:
	power = 6
elif speed >= 13.9 and speed <= 17.1:
	power = 7
elif speed >= 17.2 and speed <= 20.7:
	power = 8
elif speed >= 20.8 and speed <= 24.4:
	power = 9
elif speed >= 24.5 and speed <= 28.4:
	power = 10
elif speed >= 28.5 and speed <= 32.6:
	power = 11
elif speed >= 32.7:
	power = 12


dir_list = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]
if power == 0:
	direct = "C"
else:	
	for i in range(16):
		if i == 15:
			direct = dir_list[i]
			break
		if deg >= 225 * i + 113 and deg < 225 * (i + 1) + 113:
			direct = dir_list[i]
			break

print direct + " " + str(power)	
