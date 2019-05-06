N = int(input())
v_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

diff = map(lambda x, y: x - y, v_list, c_list)
print(sum(filter(lambda x: x > 0, diff)))
