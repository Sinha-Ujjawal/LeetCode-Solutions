from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = False
        min_posn_that_can_reach = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            max_step = nums[i] + i
            if min_posn_that_can_reach <= max_step:
                ans = True
                min_posn_that_can_reach = i
            else:
                ans = False
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.canJump([2, 3, 1, 1, 4]))
    print(solver.canJump([3, 2, 1, 0, 4]))
    print(solver.canJump([0]))
    print(solver.canJump([1]))
    print(solver.canJump([2, 0]))
