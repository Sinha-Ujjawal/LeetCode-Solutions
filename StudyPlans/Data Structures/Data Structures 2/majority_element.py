from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) >> 1]


if __name__ == "__main__":
    solver = Solution()
    print(solver.majorityElement([3, 2, 3]))
    print(solver.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(solver.majorityElement([1]))
