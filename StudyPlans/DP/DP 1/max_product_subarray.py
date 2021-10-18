from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        max_so_far = max_here = min_here = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            candidate_x = max_here * num
            candidate_y = min_here * num

            max_here = max(candidate_x, candidate_y, num)
            min_here = min(candidate_x, candidate_y, num)

            max_so_far = max(max_so_far, max_here)

        return max_so_far


if __name__ == "__main__":
    solver = Solution()
    print(solver.maxProduct([2, 3, -2, 4]))
