import heapq

X, Y, Z, K = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

a_list.sort(reverse = True)
b_list.sort(reverse = True)
c_list.sort(reverse = True)

heap = []
heapq.heappush(heap, (-(a_list[0] + b_list[0] + c_list[0]), 0, 0, 0))
searched = []
result = [0] * K

for k in range(K):
    elem = heapq.heappop(heap)
    result[k] = - elem[0]

    if elem[1] + 1 <= X - 1:
        a_next = (-(a_list[elem[1] + 1] + b_list[elem[2]] + c_list[elem[3]]), elem[1] + 1, elem[2], elem[3])
        if not a_next in searched:
            heapq.heappush(heap, a_next)
            searched.append(a_next)

    if elem[2] + 1 <= Y - 1:
        b_next = (-(a_list[elem[1]] + b_list[elem[2] + 1] + c_list[elem[3]]), elem[1], elem[2] + 1, elem[3])
        if not b_next in searched:
            heapq.heappush(heap, b_next)
            searched.append(b_next)

    if elem[3] + 1 <= Z - 1:
        c_next = (-(a_list[elem[1]] + b_list[elem[2]] + c_list[elem[3] + 1]), elem[1], elem[2], elem[3] + 1)
        if not c_next in searched:
            heapq.heappush(heap, c_next)
            searched.append(c_next)

[print(k) for k in result]