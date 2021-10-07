from typing import List
from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = deque([(0, nums)])
        while queue:
            i, top_list = queue.popleft()
            if i == len(nums):
                yield top_list
            for j in range(i, len(top_list)):
                nums_copy = top_list.copy()
                nums_copy[i], nums_copy[j] = nums_copy[j], nums_copy[i]
                queue.append((i + 1, nums_copy))


if __name__ == "__main__":
    solver = Solution()
    print(list(solver.permute([1, 2, 3])))
