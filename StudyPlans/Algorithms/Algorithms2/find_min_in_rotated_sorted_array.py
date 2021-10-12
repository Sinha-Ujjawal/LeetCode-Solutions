from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb, ub = 0, len(nums) - 1
        while lb <= ub:
            m = (lb + ub) >> 1
            if nums[0] <= nums[m]:
                lb = m + 1
            else:
                ub = m - 1
        return nums[lb] if 0 <= lb < len(nums) else nums[0]


if __name__ == "__main__":
    solver = Solution()
    print(solver.findMin([3, 4, 5, 1, 2]))
    print(solver.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(solver.findMin([11, 13, 15, 17]))
    print(solver.findMin([2, 1]))
