from typing import List

IntMatrix = List[List[int]]


class Solution:
    def updateMatrix(self, mat: IntMatrix) -> IntMatrix:
        rows, cols = len(mat), len(mat[0])
        dummy_dist = max(rows, cols) + 1
        ans = [
            [dummy_dist if mat[i][j] else 0 for j in range(cols)] for i in range(rows)
        ]
        ans_lookup = (
            lambda i, j: ans[i][j]
            if (0 <= i < rows) and (0 <= j < cols)
            else dummy_dist
        )

        # (i - 1, j) and (i, j - 1) case
        for i in range(rows):
            for j in range(cols):
                ans[i][j] = min(
                    (1 + min(ans_lookup(i - 1, j), ans_lookup(i, j - 1)))
                    if mat[i][j]
                    else 0,
                    ans[i][j],
                )

        # (i + 1, j) and (i, j + 1) case
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                ans[i][j] = min(
                    (1 + min(ans_lookup(i + 1, j), ans_lookup(i, j + 1)))
                    if mat[i][j]
                    else 0,
                    ans[i][j],
                )

        return ans


if __name__ == "__main__":
    solver = Solution()
    mat = [
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
    ]
    print(solver.updateMatrix(mat))
