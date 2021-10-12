from typing import List, Optional


class Solution:
    NEG_INF = -float("inf")

    def findPeakElement(self, nums: List[int]) -> Optional[int]:
        lb, ub = 0, len(nums) - 1
        value_at = lambda i: nums[i] if 0 <= i < len(nums) else self.NEG_INF
        is_peak = lambda i: (
            value_at(i - 1) < value_at(i) and value_at(i) > value_at(i + 1)
        )
        while lb <= ub:
            m = (lb + ub) >> 1
            if is_peak(m):
                return m
            elif value_at(m - 1) < value_at(m):
                lb = m + 1
            else:
                ub = m - 1


if __name__ == "__main__":
    solver = Solution()
    print(solver.findPeakElement([2, 1]))
