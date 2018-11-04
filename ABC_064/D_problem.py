#coding:utf-8

if __name__ == "__main__":
    N = int(input())
    string = input()

    right = 0
    left = 0

    for char in string:
        if char == '(':
            right += 1
        else:
            right -= 1

        if right == -1:
            left += 1
            right = 0

    L = '(' * left
    R = ')' * right

    print(L + string + R)
