from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            elif s == target:
                return [i + 1, j + 1]
            else:
                i += 1


if __name__ == "__main__":
    solver = Solution()
    print(solver.twoSum([2, 7, 11, 15], 9))
    print(solver.twoSum([2, 3, 4], 6))
    print(solver.twoSum([-1, 0], -1))
