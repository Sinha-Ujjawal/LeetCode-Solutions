from typing import List

IntGrid = List[List[int]]


class Solution:
    def maxAreaOfIsland(self, grid: IntGrid) -> int:
        visited = set()
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        neighbors = lambda r, c: [
            (y, x)
            for y, x in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ]
            if (0 <= y < rows) and (0 <= x < cols) and grid[y][x] == 1
        ]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    stack = [(r, c)]
                    area = 0
                    start = r, c
                    while stack:
                        r, c = stack.pop()
                        if (r, c) not in visited:
                            area += 1
                            visited.add((r, c))
                            for pos in neighbors(r, c):
                                if pos not in visited:
                                    stack.append(pos)
                    max_area = max(max_area, area)

        return max_area


if __name__ == "__main__":
    solver = Solution()
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]
    print(solver.maxAreaOfIsland(grid=grid))
