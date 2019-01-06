#coding:utf-8

def validate(N, points, c_x, c_y):
    #estimate height
    for n in range(N):
        h = points[n][2]
        if h != 0:
            x = points[n][0]
            y = points[n][1]
            estimated_height = h + abs(c_x - x) + abs(c_y - y)

    #validate height
    for n in range(N):
        x = points[n][0]
        y = points[n][1]
        h = points[n][2]
        height = max(estimated_height - abs(c_x - x) - abs(c_y - y), 0)

        if h != height:
            return -1
    return estimated_height

if __name__ == "__main__":
    N = int(input())
    points = [None] * N
    for n in range(N):
        x, y, h = map(int, input().split())
        points[n] = [x, y, h]

    candidates = [i for i in range(101)]
    for c_x in candidates:
        for c_y in candidates:
            height = validate(N, points, c_x, c_y)
            if height != -1:
                print(c_x, c_y, height)
                break
