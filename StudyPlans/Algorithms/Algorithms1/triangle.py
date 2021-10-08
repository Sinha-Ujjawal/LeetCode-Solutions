from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle:
            min_path = triangle[-1].copy()

            for i in range(len(triangle) - 2, -1, -1):
                for j in range(len(triangle[i])):
                    min_path[j] = triangle[i][j] + min(min_path[j], min_path[j + 1])

            return min_path[0]
        else:
            return -1


if __name__ == "__main__":
    solver = Solution()
    print(solver.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(solver.minimumTotal(triangle=[[-10]]))
