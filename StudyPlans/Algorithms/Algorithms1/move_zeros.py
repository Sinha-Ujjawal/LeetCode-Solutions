from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero_index = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if first_zero_index is None:
                    first_zero_index = i
            elif first_zero_index is not None:
                nums[i], nums[first_zero_index] = nums[first_zero_index], nums[i]
                first_zero_index += 1


if __name__ == "__main__":
    solver = Solution()
    nums = [0, 1, 0, 3, 12]
    solver.moveZeroes(nums)
    print(nums)
