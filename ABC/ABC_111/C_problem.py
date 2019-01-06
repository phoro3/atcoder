import collections


if __name__ == "__main__":
    N = int(input())
    v_list = list(map(int, input().split()))
    even_list = [v_list[i] for i in range(N) if i % 2 == 0]
    odd_list = [v_list[i] for i in range(N) if i % 2 != 0]

    even_counter = collections.Counter(even_list)
    odd_counter = collections.Counter(odd_list)

    even_common = even_counter.most_common()
    odd_common = odd_counter.most_common()

    even_max = even_common[0][0]
    odd_max = odd_common[0][0]

    if even_max != odd_max:
        print((N - even_common[0][1] - odd_common[0][1]))
    else:
        if len(even_common) > 1:
            even_second_replace = N - even_common[1][1] - odd_common[0][1]
        else:
            even_second_replace = N - odd_common[0][1]

        if len(odd_common) > 1:
            odd_second_replace = N - even_common[0][1] - odd_common[1][1]
        else:
            odd_second_replace = N - even_common[0][1]
        print(min(even_second_replace, odd_second_replace))