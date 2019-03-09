class UnionFind():
    def __init__(self, num):
        self.parents = [i for i in range(num + 1)]
        self.sizes = [1] * (num + 1)

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            return self.find(self.parents[x])

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.sizes[root_x] < self.sizes[root_y]:
            root_x, root_y = root_y, root_x

        # xがyの親となるように連結する
        self.parents[root_y] = root_x
        self.sizes[root_x] += self.sizes[root_y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def sizeof(self, x):
        return self.sizes[self.find(x)]

if __name__ == "__main__":
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]

    unionfind = UnionFind(N)
    inconvenience = [0] * M
    inconvenience[M - 1] = N * (N - 1) // 2

    for i, t in enumerate(reversed(bridges), start = 1):
        a, b = t
        if i == M:
            break

        prev = inconvenience[M - i]
        if unionfind.is_same(a, b):
            inconvenience[M - i - 1] = prev
            continue
        n1 = unionfind.sizeof(a)
        n2 = unionfind.sizeof(b)
        inconvenience[M - i - 1] = max(0, prev - n1 * n2)
        unionfind.unite(a, b)

    [print(i) for i in inconvenience]
