#coding:utf-8

if __name__ == "__main__":
    X, Y = map(int, raw_input().split(" "))

    if X + Y <= 1:
        print "Brown"
    elif abs(X - Y) > 1:
        print "Alice"
    else:
        print "Brown"
