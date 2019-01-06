#coding:utf-8

def get_sign(operation):
    plus_num = 0
    minus_num = 0

    for i in range(len(operation)):
        if operation[i] == "+":
            plus_num += 1
        elif operation[i] == "-":
            minus_num += 1

    return (plus_num, minus_num)


def calc_score(operation):
    scores = []
    
    plus_num, minus_num = get_sign(operation)

    for s in operation:
        if s == "+":
            plus_num -= 1
        elif s == "-":
            minus_num -= 1
        elif s == "M":
            scores.append(plus_num - minus_num)
    
    if len(scores) > 0:
        scores.sort()
    
        first_half = sum(scores[:len(scores)/2])
        second_half = sum(scores[len(scores)/2:])
    
        return second_half - first_half
    else:
        return 0

if __name__ == "__main__":
    operation = list(raw_input())

    print calc_score(operation)
    
