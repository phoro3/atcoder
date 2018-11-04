#coding:utf-8

if __name__ == "__main__":
    N, K = map(int, raw_input().split(" "))
    A_list = map(int, raw_input().split(" "))

    A_list.sort()
    print sum(A_list[:K]) + sum(range(1, K))
