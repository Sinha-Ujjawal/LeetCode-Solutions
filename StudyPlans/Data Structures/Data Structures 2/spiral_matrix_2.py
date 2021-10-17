from typing import List, Tuple
from enum import IntEnum, auto


class Dir(IntEnum):
    UP: int = auto()
    RIGHT: int = auto()
    DOWN: int = auto()
    LEFT: int = auto()


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[None] * n for _ in range(n)]

        def next_coords(i: int, j: int, dir: int) -> Tuple[int, int, int]:
            if dir == Dir.RIGHT:
                return (
                    i,
                    j + 1,
                    dir if j < n - 2 and ans[i][j + 2] is None else Dir.DOWN,
                )
            elif dir == Dir.DOWN:
                return (
                    i + 1,
                    j,
                    dir if i < n - 2 and ans[i + 2][j] is None else Dir.LEFT,
                )
            elif dir == Dir.LEFT:
                return (i, j - 1, dir if j > 0 and ans[i][j - 2] is None else Dir.UP)
            else:  # dir == UP
                return (i - 1, j, dir if i > 0 and ans[i - 2][j] is None else Dir.RIGHT)

        i = j = 0
        dir = Dir.RIGHT
        for val in range(1, (n * n) + 1):
            ans[i][j] = val
            i, j, dir = next_coords(i, j, dir)

        return ans


if __name__ == "__main__":
    solver = Solution()
    for row in solver.generateMatrix(4):
        print(row)
