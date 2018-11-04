#coding:utf-8

if __name__ == "__main__":
    N = int(input())
    num_list = list(map(int, input().split(" ")))

    print(max(num_list) - min(num_list))

