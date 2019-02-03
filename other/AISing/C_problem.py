from collections import deque

BLACK = '#'
WHITE = '.'
vec_x = [1, 0, -1, 0]
vec_y = [0, 1, 0, -1]
vec_num = len(vec_x)

def solve():
    count = 0
    for i in range(H):
        for j in range(W):
            if used[i][j]:
                continue
            b = 0
            w = 0
            que = deque([(i, j)])
            used[i][j] = True

            while que:
                next_i, next_j = que.popleft()

                #黒か白かをカウント
                if(S[next_i][next_j] == BLACK):
                    b += 1
                else:
                    w += 1

                #隣接するマスの色が現在のマスと違うならキューに追加
                for d in range(vec_num):
                    d_i = next_i + vec_y[d]
                    d_j = next_j + vec_x[d]
                    if not check(next_i, next_j, d_i, d_j) or used[d_i][d_j]:
                        continue
                    que.append((d_i, d_j))
                    used[d_i][d_j] = True
            count += b * w
    return count

def check(i, j, d_i, d_j):
    if not (0 <= d_i < H and 0 <= d_j < W):
        return False
    if S[i][j] == S[d_i][d_j]:
        return False
    return True



if __name__ == "__main__":
    H, W = map(int, input().split())
    S = [[]] * H
    used = [[]] * H
    for h in range(H):
        S[h] = list(input())
        used[h] = [False] * W
    print(solve())
