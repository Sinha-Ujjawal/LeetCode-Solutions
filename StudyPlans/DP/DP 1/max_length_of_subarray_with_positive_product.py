from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        neg = pos = 0
        if nums[0] > 0:
            pos = 1
        elif nums[0] < 0:
            neg = 1
        ans = pos

        for i in range(1, len(nums)):
            num = nums[i]

            if num > 0:
                pos += 1
                neg = 1 + neg if neg > 0 else 0
            elif num < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
            else:
                pos = neg = 0

            ans = max(pos, ans)

        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.getMaxLen(nums=[1, -2, -3, 4]))
    print(solver.getMaxLen(nums=[0, 1, -2, -3, -4]))
