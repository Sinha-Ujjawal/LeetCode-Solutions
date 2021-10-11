from typing import List

IntMatrix = List[List[int]]


class Solution:
    def searchMatrix(self, matrix: IntMatrix, target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lb, ub = 0, (rows * cols) - 1
        to_coords = lambda x: (x // cols, x % cols)
        while lb <= ub:
            m = (lb + ub) >> 1
            i, j = to_coords(m)
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                ub = m - 1
            else:
                lb = m + 1
        return False
