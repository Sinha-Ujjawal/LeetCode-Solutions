from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        m = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in m:
                return [m[x], i]
            m[num] = i


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i][1] + nums[j][1]
            if s == target:
                return [nums[i][0], nums[j][0]]
            elif s < target:
                i += 1
            else:
                j -= 1


if __name__ == "__main__":
    solver = Solution()
    solver2 = Solution2()
    nums = [2, 7, 11, 15]
    print(solver.twoSum(nums=nums, target=9))
    print(solver2.twoSum(nums=nums, target=9))
