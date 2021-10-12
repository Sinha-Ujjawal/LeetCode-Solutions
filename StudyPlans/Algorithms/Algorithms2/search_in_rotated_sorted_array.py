from typing import Any, List, Optional


def binary_search(
    arr: List[Any],
    target: Any,
    lb: int = 0,
    ub: Optional[int] = None,
    default: Any = None,
) -> Optional[int]:
    ub = len(arr) - 1 if ub == None else ub
    while lb <= ub:
        m = (lb + ub) >> 1
        if target < arr[m]:
            ub = m - 1
        elif target > arr[m]:
            lb = m + 1
        else:
            return m
    return default


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums:
            lb, ub = 0, len(nums) - 1

            while lb <= ub:
                m = (lb + ub) >> 1
                if nums[0] <= nums[m]:
                    lb = m + 1
                else:
                    ub = m - 1

            if 0 < lb < len(nums):
                i = binary_search(nums, target, 0, lb - 1, default=-2)
                if i == -2:
                    i = binary_search(nums, target, lb, default=-2)
            else:
                i = binary_search(nums, target, 0, default=-2)
            return max(i, -1)


if __name__ == "__main__":
    solver = Solution()
    print(solver.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solver.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(solver.search([1], -1))
    print(solver.search([5, 1, 2], 5))
    print(solver.search([3, 1], 1))
    print(solver.search([3, 5, 1], 1))
    print(solver.search([4, 5, 1, 2, 3], 1))
    print(solver.search([3, 4, 5, 6, 1, 2], 2))
    print(solver.search([9, 1, 2, 3, 4, 5, 6, 7, 8], 9))
    print(solver.search([5, 6, 0, 2], 0))
