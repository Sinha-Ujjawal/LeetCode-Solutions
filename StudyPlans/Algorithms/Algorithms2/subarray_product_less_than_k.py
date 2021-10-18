from typing import List, Union
from math import log2
from itertools import accumulate, chain
from bisect import bisect

# Intuition-
# For each right, call opt(right) the smallest left so that the product of the subarray
# nums[left] * nums[left + 1] * ... * nums[right] is less than k.
# opt is a monotone increasing function, so we can use a sliding window.
# proof- for every right' >= right
# a1 a2 a3 ... a100 ...  a101 ...,      a200, an
#    opt(right)          right          right'
# opt(right') has to be something bigger than opt(right)
# because a[opt[right]] * a[opt[right] + 1] * ... * a[right] < k
# and, right' is already introducing more elements, hence opt(right') should be somewhere in the right
# of opt(right)


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = left = 0
        prod = 1
        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


class Solution2:
    def prefix_sum(self, nums: List[Union[int, float]]) -> Union[int, float]:
        return list(accumulate(chain([0], nums)))

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        k = log2(k)
        prefix_sum = self.prefix_sum(map(log2, nums))
        ans = 0
        for i, prefix_i in enumerate(prefix_sum):
            j = bisect(prefix_sum, prefix_i + k - 1e-9, i + 1)
            ans += j - i - 1
        return ans


if __name__ == "__main__":
    solver = Solution2()
    print(solver.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
