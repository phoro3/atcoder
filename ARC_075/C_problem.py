#coding:utf-8

if __name__ == "__main__":
    N = int(input())

    points = []
    for i in range(N):
        points.append(int(input()))

    points.sort()

    total_point = sum(points)
    if total_point % 10 != 0:
        print(total_point)
    elif sum(map(lambda x: x % 10, points)) == 0:
        print(0)
    else:
        for point in points:
            if point % 10 != 0:
                print(total_point - point)
                break
