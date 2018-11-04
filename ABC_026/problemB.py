#coding:utf-8

def calc_area(input_list):
    PI = 3.1415926535
    r_list = []
    w_list = []

    for i in range(len(input_list)):
        if i % 2 == 0:
            r_list.append(input_list[i])
        elif i % 2 != 0:
            w_list.append(input_list[i])

    area = 0
    for i in r_list:
        area += i**2
    for i in w_list:
        area -= i**2
        
    area *= PI
    return area

if __name__ == "__main__":
    N = int(raw_input())

    input_list = []
    for i in range(N):
        input_list.append(int(raw_input()))

    input_list.sort()
    input_list.reverse()
    area = calc_area(input_list)
    print area
