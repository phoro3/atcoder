#coding:utf-8
#QlFhttps://beta.atcoder.jp/contests/abc113/submissions/3806710


if __name__ == "__main__":
    N, M = map(int, input().split())
    city_list = []
    for i in range(M):
        p, y = map(int, input().split())
        city_list.append([i, p, y])

    city_count = {}
    order_dic = {}
    for i, p, y in sorted(city_list, key = lambda x: x[2]):
        if not p in city_count:
            city_count[p] = 0
        city_count[p] += 1
        order_dic[i, p] = city_count[p]

    for i, p, y in city_list:
        print("{:06}{:06}".format(p, order_dic[i,p]))
