#coding:utf-8

inn = map(int, raw_input().split(" "))

print max(inn[4] + inn[3] + inn[0], inn[4] + inn[2] + inn[1])
