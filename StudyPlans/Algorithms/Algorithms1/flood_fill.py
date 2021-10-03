from typing import List
from copy import deepcopy

Image = List[List[int]]


class Solution:
    def floodFill(self, image: Image, sr: int, sc: int, newColor: int) -> Image:
        stack = [(sr, sc)]
        seen = {(sr, sc)}
        rows, cols = len(image), len(image[0])
        oldColor = image[sr][sc]
        newImage = deepcopy(image)
        neighbors = lambda r, c: [
            (y, x)
            for y, x in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
            if (0 <= y < rows) and (0 <= x < cols) and (image[y][x] == oldColor)
        ]
        while stack:
            (r, c) = stack.pop()
            newImage[r][c] = newColor
            for y, x in neighbors(r, c):
                if (y, x) not in seen:
                    seen.add((y, x))
                    stack.append((y, x))

        return newImage


if __name__ == "__main__":
    solver = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(solver.floodFill(image=image, sr=sr, sc=sc, newColor=newColor))
