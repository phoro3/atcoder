#coding:utf-8

def calc_common_prefix_len(s1, s2):
    n = min(len(s1), len(s2))
    for i in range(n):
        if s1[i] != s2[i]:
            return i
    return n

if __name__ == "__main__":
    N, K = map(int, raw_input().split(" "))
    show_num_list = map(lambda x: int(x) - 1, raw_input().split(" "))
    show_num_set = set(show_num_list)
    site_list = []
    for n in range(N):
        site_list.append(raw_input())


    base_str = site_list[show_num_list[0]]

    show_min = min([calc_common_prefix_len(base_str, site_list[i]) for i in show_num_list])
    not_show_common_list = [calc_common_prefix_len(base_str, site_list[j]) for j in range(N) if j not in show_num_set]

    not_show_max = -1
    if len(not_show_common_list) > 0:
        not_show_max = max(not_show_common_list)

    if not_show_max < show_min:
        print base_str[:not_show_max + 1]
    else:
        print "-1"
