#coding:utf-8

def get_index(rate):
    if 1 <= rate <= 399:
        return 0
    elif 400 <= rate <= 799:
        return 1
    elif 800 <= rate <= 1199:
        return 2
    elif 1200 <= rate <= 1599:
        return 3
    elif 1600 <= rate <= 1999:
        return 4
    elif 2000 <= rate <= 2399:
        return 5
    elif 2400 <= rate <= 2799:
        return 6
    elif 2800 <= rate <= 3199:
        return 7

if __name__ == "__main__":
    N = int(input())
    rates = list(map(int, input().split(" ")))
    color_list = [0] * 8

    free_num = 0
    for rate in rates:
        if rate >= 3200:
            free_num += 1
        else:
            color_list[get_index(rate)] += 1

    color_kind = len(list(filter(lambda x: x > 0, color_list)))
    if color_kind == 0:
        print(str(1) + " " + str(free_num))
    else:
        print(str(color_kind) + " " + str(color_kind + free_num))
