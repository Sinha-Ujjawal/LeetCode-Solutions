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


if __name__ == "__main__":
    solver = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(solver.searchMatrix(matrix=matrix, target=target))
