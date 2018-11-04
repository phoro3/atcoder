#coding:utf-8

def dist(p1, p2):
    sq_dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    return math.sqrt(sq_dist)

def judge_triangle(p1, p2, p3):
    sq_dist_list = []

    sq_dist_list.append((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    sq_dist_list.append((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
    sq_dist_list.append((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)

    max_dist = max(sq_dist_list)
    sq_dist_list.remove(max_dist)

    val = sq_dist_list[0] + sq_dist_list[1] - max_dist

    if val > 0:
        return "acute"
    elif val == 0:
        return "right"
    else:
        return "obtuse"

if __name__ == "__main__":
    N = int(raw_input())
    
    point_list = []
    for i in range(N):
        point = map(int, raw_input().split(" "))
        point_list.append(point)
    
    result = {}
    result["acute"] = 0
    result["right"] = 0
    result["obtuse"] = 0
    for i in range(len(point_list)):
        for j in range(i + 1, len(point_list)):
            for k in range(j + 1, len(point_list)):
                result[judge_triangle(point_list[i], point_list[j], point_list[k])] += 1


    print str(result["acute"]) + " " + str(result["right"]) + " " + str(result["obtuse"])
