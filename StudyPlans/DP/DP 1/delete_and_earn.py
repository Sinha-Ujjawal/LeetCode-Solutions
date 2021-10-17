from typing import List
from collections import Counter


class Solution:
    def simple_rob(self, nums: List[int]) -> int:
        ri = riplus1 = 0
        for num in reversed(nums):
            ri, riplus1 = max(num + riplus1, ri), ri
        return ri

    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        points = [counts.get(k, 0) * k for k in range(min(counts), max(counts) + 1)]
        return self.simple_rob(points)


if __name__ == "__main__":
    solver = Solution()
    print(solver.deleteAndEarn([2, 2, 3, 3, 3, 4]))
