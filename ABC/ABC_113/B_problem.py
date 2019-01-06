if __name__ == "__main__":
    C = 0.006
    N = int(input())
    T, A = map(int, input().split())
    H_list = map(int, input().split())

    t_list = map(lambda x: T - C * x, H_list)
    abs_list = list(map(lambda x: abs(x - A), t_list))
    print(abs_list.index(min(abs_list)) + 1)
