from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v, nums[k] = nums[k], 2
            if v < 2:
                nums[i] = 1
                i += 1
            if v == 0:
                nums[j] = 0
                j += 1


if __name__ == "__main__":
    solver = Solution()
    nums = [1, 0]
    solver.sortColors(nums)
    print(nums)
