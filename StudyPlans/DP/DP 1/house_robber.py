from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ri = riplus1 = 0
        for num in reversed(nums):
            ri, riplus1 = max(num + riplus1, ri), ri
        return ri
