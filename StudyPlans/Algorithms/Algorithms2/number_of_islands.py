from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_of_island = 0
        rows, cols = len(grid), len(grid[0])
        valid_index = lambda i, j: 0 <= i < rows and 0 <= j < cols
        right_down_neighbors = lambda i, j: [
            pos
            for pos in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            if valid_index(*pos)
        ]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num_of_island += 1
                    q = deque([(i, j)])
                    while q:
                        (x, y) = q.popleft()
                        if (x, y) not in visited and grid[x][y] == "1":
                            visited.add((x, y))
                            for neighbor in right_down_neighbors(x, y):
                                q.append(neighbor)

        return num_of_island


if __name__ == "__main__":
    solver = Solution()
    print(
        solver.numIslands(
            grid=[
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
    )
    print(
        solver.numIslands(
            grid=[
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )
    print(
        solver.numIslands(
            [
                ["1", "1", "1"],
                ["0", "1", "0"],
                ["1", "1", "1"],
            ]
        )
    )
    print(
        solver.numIslands(
            [
                ["0", "1", "0"],
                ["1", "0", "1"],
                ["0", "1", "0"],
            ]
        )
    )

    # [[10011101100000000000]
    #  [10011001000101010010]
    #  [00011110101100001010]
    #  [00011001000111001001]
    #  [00000001110000000000]
    #  [10000101011000000101]
    #  [00010001010101010101]
    #  [00010100110101101110]
    #  [00001001100001000101]
    #  [00100100000100100010]
    #  [10010000000100101010]
    #  [01000101011011101100]
    #  [11010000100000010001]
    #  [01001110001111101000]
    #  [00111000110001010000]
    #  [10010100001000101011]
    #  [10100000010001010000]
    #  [01100011101010111100]
    #  [01000011001010010011]
    #  [00000011110100011000]]
