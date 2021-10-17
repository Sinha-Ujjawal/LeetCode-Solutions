from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = cur_end = cur_farthest = 0
        for i, num in enumerate(nums):
            if i > cur_farthest:
                return float("inf")
            cur_farthest = max(cur_farthest, num + i)
            if i < len(nums) - 1 and i == cur_end:
                jumps += 1
                cur_end = cur_farthest
        return jumps


if __name__ == "__main__":
    solver = Solution()
    print(solver.jump([2, 0, 1, 1, 4]))
    print(solver.jump([2, 3, 0, 1, 4]))
    print(solver.jump([3, 2, 1, 0, 4]))
    print(solver.jump([0]))
    print(solver.jump([1]))
    print(solver.jump([2, 0]))
