from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums) - 1
        while lb <= ub:
            mid = (lb + ub) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lb = mid + 1
            else:
                ub = mid - 1
        return lb


if __name__ == "__main__":
    solver = Solution()
    print(solver.searchInsert(nums=[1, 3, 5, 6], target=2))
