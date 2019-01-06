#coding:utf-8

#input
distance = int(raw_input())

#calc VV
VV = -1
if distance < 100:
	VV = 0

elif distance >= 100 and distance <= 5000:
	VV = int((float(distance) / 1000) * 10)

elif distance >= 6000 and distance <= 30000:
	VV = int(float(distance) / 1000 + 50)

elif distance >= 35000 and distance <= 70000:
	VV = int((float(distance) / 1000 - 30) / 5 + 80)

elif distance >= 70000:
	VV = 89


if VV / 10 == 0:
	print "0" + str(VV)
else:
	print VV
