from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums) - 1
        while lb <= ub:
            mid = (lb + ub) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lb = mid + 1
            else:
                ub = mid - 1
        return -1


if __name__ == "__main__":
    solver = Solution()
    print(solver.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
