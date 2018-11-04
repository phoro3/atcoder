#coding:utf-8

def is_all_same(people):
    num = people[0]

    for i in range(1, len(people)):
        if people[i] != num:
            return False
    return True

def count_bridge(num, people):
    total = reduce(lambda x,y: x+y, people) 

    if is_all_same(people):
        return 0
    elif total % num != 0:
        return -1
    else:
        each_num = total / num
        bridge = 0

        for i in range(1, num):
            left_len = 0
            left_num = 0
            right_num = 0
            right_len = 0

            for j in range(i):
                left_num += people[j]
                left_len += 1
            for j in range(i, num):
                right_num += people[j]
                right_len += 1

            if left_num != left_len * each_num or right_num != right_len * each_num:
                bridge += 1

        return bridge


if __name__ == "__main__":
    num = int(raw_input())
    
    people = map(int, raw_input().split(" "))

    print count_bridge(num, people)

