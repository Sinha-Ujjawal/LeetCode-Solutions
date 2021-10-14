from typing import Iterable, List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> Iterable[List[int]]:
        m = defaultdict(lambda: -1)
        for e, num in enumerate(nums):
            m[num] = e
        seen = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = m[-nums[i] - nums[j]]
                if k > j:
                    ky = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if ky not in seen:
                        yield ky
                        seen.add(ky)


if __name__ == "__main__":
    solver = Solution()
    print(list(solver.threeSum([-1, 0, 1, 2, -1, -4])))
