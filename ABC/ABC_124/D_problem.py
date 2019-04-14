# ref. https://atcoder.jp/contests/abc124/submissions/4963013
N, K = map(int, input().split())
S = map(int, list(input()))

num_list = []
now = 1
count = 0

for char in S:
    if char == (0 + now):
        count += 1
    else:
        num_list.append(count)
        now = 1 - now
        count = 1
if count > 0:
    num_list.append(count)
# 1-0-1-0になっていたら、最後に1つ0を足す
if len(num_list) % 2 == 0:
    num_list.append(0)

#累積和を作る
cumulative = [0] * (len(num_list) + 1)
for i in range(len(num_list)):
    cumulative[i + 1] = cumulative[i] + num_list[i]

ans = 0
add = 2 * K + 1

for i in range(len(cumulative)):
    if i % 2 == 0:
        add_i = min(i + add, len(cumulative) - 1)
        ans = max(ans, cumulative[add_i] - cumulative[i])
print(ans)
