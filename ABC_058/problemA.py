#coding:utf-8

if __name__ == "__main__":
    a, b, c = map(int, raw_input().split(" "))

    if b - a == c - b:
        print "YES"
    else:
        print "NO"

