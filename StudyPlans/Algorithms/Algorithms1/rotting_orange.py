from typing import List

IntMatrix = List[List[int]]


class Solution:
    def orangesRotting(self, grid: IntMatrix) -> int:
        rows, cols = len(grid), len(grid[0])
        dummy_dist = rows * cols
        ans = [
            [dummy_dist if grid[i][j] != 0 else 0 for j in range(cols)]
            for i in range(rows)
        ]

        neighbors = lambda r, c: (
            (y, x)
            for y, x in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            if (0 <= y < rows) and (0 <= x < cols) and grid[y][x] == 1
        )

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    visited = {(i, j)}
                    frontier = [(i, j)]
                    dist = 0
                    while frontier:
                        new_frontier = []
                        for r, c in frontier:
                            visited.add((r, c))
                            ans[r][c] = min(ans[r][c], dist)
                            for pos in neighbors(r, c):
                                if pos not in visited:
                                    new_frontier.append(pos)

                        dist += 1
                        frontier = new_frontier

        max_dist = max(map(max, ans))

        return -1 if max_dist == dummy_dist else max_dist


if __name__ == "__main__":
    solver = Solution()
    grid = [
        [2, 1, 1],
        [1, 1, 1],
        [0, 1, 2],
    ]
    print(solver.orangesRotting(grid))
