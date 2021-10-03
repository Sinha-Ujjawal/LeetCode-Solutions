from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any(nums[i] == nums[i - 1] for i in range(1, len(nums)))


if __name__ == "__main__":
    solver = Solution()
    solver2 = Solution()
    nums = [1, 2, 3, 1]
    print(solver.containsDuplicate(nums=nums))
    print(solver2.containsDuplicate(nums=nums))
