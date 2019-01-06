#coding:utf-8

def count(seq, is_positive):
    operation = 0
    sum = 0
    for i in range(n):
        sum += seq[i]
        if sum == 0:
            operation += 1
            if is_positive:
                sum -= 1
            else:
                sum += 1
        elif sum > 0 and is_positive:
            operation += abs(sum) + 1
            sum = -1
        elif sum < 0 and not is_positive:
            operation += abs(sum) + 1
            sum = 1

        if sum > 0:
            is_positive = True
        else:
            is_positive = False

    return operation


if __name__ == "__main__":
    n = int(raw_input())
    seq = map(int, raw_input().split(" "))

    print min(count(seq, False), count(seq, True))
