#coding:utf-8

num = map(int, raw_input().split(" "))

sums = []

for i in range(len(num)):
    for j in range(i+1, len(num)):
        for k in range(j+1, len(num)):
            sums.append(num[i] + num[j] + num[k])

sums.sort()
sums.reverse()
print sums[2]
