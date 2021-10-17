from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums)
        max_sum = -float("inf")
        s = 0
        for num in nums:
            s = max(s + num, num)
            max_sum = max(max_sum, s)
        return max_sum
