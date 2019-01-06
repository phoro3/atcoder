#coding:utf-8

N, M = map(int, raw_input().split(" "))

area = []
class_num = [0]*N

for i in range(M):
    #decrement index
    area.append(map(int,raw_input().split(" ")))

X = [0]*(N+2)
for item in area:
    X[item[0]] += 1
    X[item[1]+1] -= 1


for i in range(1,len(X)):
    X[i] += X[i-1]

for i in range(len(X)):
    if X[i] != 1:
        X[i] = 0

for i in range(1,len(X)):
    X[i] += X[i-1]

result = []
for i in range(len(area)):
    if X[area[i][1]] - X[area[i][0]-1] == 0:
        result.append(i)

print len(result)
if len(result) > 0:
    print "\n".join(map(lambda x:str(x+1), result))
