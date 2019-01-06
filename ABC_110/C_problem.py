from collections import defaultdict

S = input()
T = input()

s_dic = defaultdict(lambda: -1)
t_dic = defaultdict(lambda: -1)

can_replace = True
for i in range(len(S)):
    s_char = S[i]
    t_char = T[i]

    if s_dic[s_char] != -1 or t_dic[t_char] != -1:
        if s_dic[s_char] != t_char and t_dic[t_char] != s_char:
            can_replace = False
            break
    else:
        s_dic[s_char] = t_char
        t_dic[t_char] = s_char

if can_replace:
    print("Yes")
else:
    print("No")