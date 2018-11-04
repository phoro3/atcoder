#coding:utf-8

if __name__ == "__main__":
    s = raw_input()
    char_list = ["y", "a", "h", "o", "o"]

    for c in s:
        if c in char_list:
            char_list.remove(c)

    if len(char_list) == 0:
        print "YES"
    else:
        print "NO"
