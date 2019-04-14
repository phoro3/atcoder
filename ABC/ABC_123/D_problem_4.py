# TLE
def judge(P):
    count = 0
    for a in a_list:
        for b in b_list:
            for c in c_list:
                if a + b + c < P:
                    break
                count += 1
                if count >= K:
                    return True
    return False

def enum(P):
    result = []
    for a in a_list:
        for b in b_list:
            for c in c_list:
                if a + b + c >= P + 1:
                    result.append(a + b + c)
    return result


X, Y, Z, K = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

a_list.sort(reverse = True)
b_list.sort(reverse = True)
c_list.sort(reverse = True)

max_sum = a_list[0] + b_list[0] + c_list[0]
for p in reversed(range(max_sum + 1)):
    is_over = judge(p)

    if is_over:
        result = enum(p)

        if len(result) < K:
            result += [p] * (K - len(result))
        break

[print(val) for val in reversed(sorted(result[:K]))]