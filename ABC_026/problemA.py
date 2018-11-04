#coding:utf-8

A = int(raw_input())

x_list = range(0, A / 2 + 1)
x_list.reverse()
y_list = range(0, A - A / 2 + 1)
y_list.reverse()

m_num = 0

for i in x_list:
    for j in y_list:
        if i * j > m_num:
            m_num = i * j

print m_num
