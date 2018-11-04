#coding:utf-8

if __name__ == "__main__":
    H, W = map(int, input().split(" "))
    sub = 10 ** 10

    #horizontal division
    for h in range(1, H):
        s_a = h * W

        #divide remain area vertically
        s_b = (H - h) * (W // 2)
        s_c = (H - h) * (W - (W // 2))
        sub_v = max(s_a, s_b, s_c) - min(s_a, s_b, s_c)

        #divide remain area horizontally
        s_b = ((H - h) // 2) * W
        s_c = ((H - h) - (H - h) // 2) * W
        sub_h = max(s_a, s_b, s_c) - min(s_a, s_b, s_c)

        min_sub = min(sub_v, sub_h)
        if min_sub < sub:
            sub = min_sub

    #vertical division
    for w in range(1, W):
        s_a = H * w
        #divide remain area vertically
        s_b = H * ((W - w) // 2)
        s_c = H * ((W - w) - (W - w) // 2)
        sub_v = max(s_a, s_b, s_c) - min(s_a, s_b, s_c)

        #divide remain area horizontally
        s_b = (H // 2) * (W - w)
        s_c = (H - (H // 2)) * (W - w)
        sub_h = max(s_a, s_b, s_c) - min(s_a, s_b, s_c)

        min_sub = min(sub_v, sub_h)
        if min_sub < sub:
            sub = min_sub

    print (sub)
