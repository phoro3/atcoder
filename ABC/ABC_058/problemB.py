#coding:utf-8

if __name__ == "__main__":
    o_str = raw_input()
    e_str = raw_input()

    password = ""
    for o, e in zip(o_str, e_str):
        password += o
        password += e

    if len(o_str) != len(e_str):
        password += o_str[-1]

    print password

