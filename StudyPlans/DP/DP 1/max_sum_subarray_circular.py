from typing import List
from itertools import islice


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        s = 0
        for num in nums:
            s = max(s + num, num)
            max_sum = max(max_sum, s)
        return max_sum

    def minSubArray(self, nums: List[int]) -> int:
        return -self.maxSubArray(map(lambda x: x * -1, nums))

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        assert len(nums)
        s = sum(nums)
        return max(
            s - self.minSubArray(islice(nums, 1, len(nums))),
            s - self.minSubArray(islice(nums, 0, len(nums) - 1)),
            self.maxSubArray(nums),
        )


if __name__ == "__main__":
    solver = Solution()
    print(solver.maxSubarraySumCircular([5, 5]))
    print(solver.maxSubarraySumCircular([-2, -3, -1]))
    print(solver.maxSubarraySumCircular([2, -2, 2, 7, 8, 0]))
    print(solver.maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]))
    print(solver.maxSubarraySumCircular([0, 5, 8, -9, 9, -7, 3, -2]))
