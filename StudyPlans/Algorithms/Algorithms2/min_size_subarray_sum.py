from typing import List, Iterable, Union
from itertools import accumulate
from bisect import bisect_left

Num = Union[int, float]


def prefix_sum(nums: Iterable[Num]) -> Num:
    xs = list(accumulate(nums))
    xs.append(0)
    return xs


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p = prefix_sum(nums)
        # p[i] = p[0] + p[1] + ... + p[i]
        ans = None
        for i in range(len(nums)):
            s = target + p[i - 1]
            j = bisect_left(p, s, i, len(nums) - 1)
            if i <= j and p[j] >= s:
                ans = min(ans, (j - i + 1)) if ans != None else (j - i + 1)
        return ans or 0


# again, prefix_sum(i) is monotonically intreasing function
# hence, we can use two pointers approach
# O(n) solution, `left` can be incremented atmost n times
class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        ans = None
        left = 0
        for right, num in enumerate(nums):
            s += num
            while s >= target:
                ans = (right - left + 1) if ans is None else min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans or 0


if __name__ == "__main__":
    solver = Solution2()
    print(solver.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
    print(solver.minSubArrayLen(target=4, nums=[1, 4, 4]))
    print(solver.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
