from typing import List, Optional


class DSet:
    def __init__(self, n: int) -> None:
        assert n > 0 and isinstance(n, int)
        self._parent = list(range(n))
        self._rank = [0] * n

    def sets(self) -> List[List[int]]:
        dsets = [[] for _ in range(len(self._parent))]
        for i in range(len(self._parent)):
            j = self.find(i)
            dsets[j].append(i)
        return [dset for dset in dsets if dset]

    __iter__ = sets

    def __str__(self):
        return f"DSet {self.sets()}"

    __repr__ = __str__

    def find(self, i: int) -> Optional[int]:
        if 0 <= i < len(self._parent):
            path = []
            while self._parent[i] != i:
                path.append(i)
                i = self._parent[i]
            for j in path:
                self._parent[j] = i
                self._rank[j] = 0
            return i

    def union(self, i: int, j: int) -> Optional[int]:
        if 0 <= i < len(self._parent) and 0 <= j < len(self._parent):
            x = self.find(i)
            y = self.find(j)
            if x != y:
                if self._rank[x] > self._rank[y]:
                    self._rank[x] += 1
                    self._parent[y] = x
                    self._rank[y] = 0
                    return x
                else:
                    self._rank[y] += 1
                    self._parent[x] = y
                    self._rank[x] = 0
                    return y
            else:
                return x


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dset = DSet(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    dset.union(i, j)
        return len(dset.sets())


if __name__ == "__main__":
    solver = Solution()
    print(
        solver.findCircleNum(
            isConnected=[
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 1],
            ]
        )
    )
    print(
        solver.findCircleNum(
            isConnected=[
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ]
        )
    )
