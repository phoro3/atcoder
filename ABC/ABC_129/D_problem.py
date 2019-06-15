#ref. https://atcoder.jp/contests/abc129/submissions/5906191
import numpy as np
import sys


sin = sys.stdin.buffer
H, W = map(int, sin.readline().split())
grid = [[None] * W for _ in range(H)]
for h in range(H):
    grid[h] = list(input())
grid = (np.array(grid) == ".") * 1

L = np.empty((H, W), dtype="i4")
R = np.empty((H, W), dtype="i4")
T = np.empty((H, W), dtype="i4")
B = np.empty((H, W), dtype="i4")

T[0] = grid[0]
for i in range(1, H):
    T[i] = (T[i - 1] + 1) * grid[i]

B[-1] = grid[-1]
for i in range(H - 2, -1, -1):
    B[i] = (B[i + 1] + 1) * grid[i]

L[:, 0] = grid[:, 0]
for i in range(1, W):
    L[:, i] = (L[:, i - 1] + 1) * grid[:, i]

R[:, -1] = grid[:, -1]
for i in range(W - 2, -1, -1):
    R[:, i] = (R[:, i + 1] + 1) * grid[:, i]

ans = (T + B + L + R - 3).max()
print(ans)
