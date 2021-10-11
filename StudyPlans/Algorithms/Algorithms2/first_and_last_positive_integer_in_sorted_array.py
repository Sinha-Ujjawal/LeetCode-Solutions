from typing import List, Tuple
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> Tuple[int, int]:
        i = bisect_left(nums, target)
        j = bisect_right(nums, target)
        if i < len(nums) and nums[i] == target:
            return i, j - 1
        else:
            return -1, -1


if __name__ == "__main__":
    solver = Solution()
    print(solver.searchRange([5, 7, 7, 8, 8, 10], 8))
