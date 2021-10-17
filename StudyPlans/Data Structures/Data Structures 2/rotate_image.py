from typing import List

Image = List[List[int]]


class Solution:
    def rotate(self, matrix: Image) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


if __name__ == "__main__":
    solver = Solution()
    img = [
        [5, 1, 9, 11, 12],
        [2, 4, 8, 10, 100],
        [13, 3, 6, 7, 200],
        [15, 14, 12, 16, 300],
        [1, 2, 3, 4, 5],
    ]
    solver.rotate(img)
    for row in img:
        print(row)
