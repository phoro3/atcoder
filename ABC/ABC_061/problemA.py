#coding:utf-8

if __name__ == "__main__":
    a, b, c = map(int, input().split(" "))

    if a <= c <= b:
        print ("Yes")
    else:
        print ("No")
