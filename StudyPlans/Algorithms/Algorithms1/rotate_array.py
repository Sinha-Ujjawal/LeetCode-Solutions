from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if nums:
            where_go = lambda i: (i + k) % len(nums)
            i = been_here = 0
            val = nums[i]
            for _ in range(len(nums)):
                j = where_go(i)
                i, val, nums[j] = j, nums[j], val
                if i == been_here:  # cycle detected, just increment
                    i = (i + 1) % len(nums)
                    been_here = i
                    val = nums[i]


if __name__ == "__main__":
    solver = Solution()
    arr = [-1, -100, 3, 99]
    k = 2
    solver.rotate(arr, k)
    print(arr)

