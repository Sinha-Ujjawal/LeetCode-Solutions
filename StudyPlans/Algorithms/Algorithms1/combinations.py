from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = [([], 1)]
        while stack:
            xs, i = stack.pop()
            if len(xs) == k:
                yield xs
            else:
                for j in range(i, n + 1):
                    stack.append((xs + [j], j + 1))


if __name__ == "__main__":
    solver = Solution()
    print(list(solver.combine(4, 2)))
