import itertools as it
from typing import List


IntMatrix = List[List[int]]


class Solution:
    def matrixReshape(self, mat: IntMatrix, r: int, c: int) -> IntMatrix:
        m, n = len(mat), len(mat[0])
        if m * n == r * c:
            values = it.chain.from_iterable(mat)
            new_mat = []
            for _ in range(r):
                rows = []
                for _ in range(c):
                    rows.append(next(values))
                new_mat.append(rows)
            return new_mat
        else:
            return mat


if __name__ == "__main__":
    solver = Solution()
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(solver.matrixReshape(mat, r, c))
