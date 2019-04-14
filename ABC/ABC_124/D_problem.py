# しゃくとり
# ref. https://atcoder.jp/contests/abc124/submissions/4962905
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

ans = 0
add = 2 * K + 1

left = 0
right = 0
tmp = 0 # [left, right)のsum
for i in range(0, len(num_list), 2):
    next_left = i
    next_right = min(i + add, len(num_list))

    while left < next_left:
        tmp -= num_list[left]
        left += 1
    while right < next_right:
        tmp += num_list[right]
        right += 1
    ans = max(ans, tmp)
print(ans)
