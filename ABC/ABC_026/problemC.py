#coding;utf-8

#calc salary for member whose number is member_num
def calc_salary(rel_list, member_num, sal_list):
    index = member_num - 1
    if len(rel_list[index]) == 0:
        return 1
    else:
        tmp_list = []
        for i in rel_list[index]:
            if sal_list[index] != -1:
                tmp_list.append(sal_list[index])
            else:
                tmp_list.append(calc_salary(rel_list, i, sal_list))
        sal_list[index] = max(tmp_list) + min(tmp_list) + 1
        return sal_list[index]



if __name__ == "__main__":
    N = int(raw_input())

    #relationship list
    rel_list = []

    #salary for each person
    sal_list = []
    for i in range(N):
        rel_list.append([])
        sal_list.append(-1)

    for i in range(N - 1):
        boss = int(raw_input())

        rel_list[boss - 1].append(i + 2)

    print calc_salary(rel_list, 1, sal_list)
