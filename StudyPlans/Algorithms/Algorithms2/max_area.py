from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            max_area = max(area, max_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == "__main__":
    solver = Solution()
    print(solver.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
