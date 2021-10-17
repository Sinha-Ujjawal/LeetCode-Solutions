from typing import List


class Solution:
    def simple_rob(self, nums: List[int]) -> int:
        ri = riplus1 = 0
        for num in reversed(nums):
            ri, riplus1 = max(num + riplus1, ri), ri
        return ri

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(self.simple_rob(nums[:-1]), self.simple_rob(nums[1:]))
