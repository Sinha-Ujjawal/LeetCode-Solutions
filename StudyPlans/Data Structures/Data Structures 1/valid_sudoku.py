from typing import List
from collections import Counter

Board = List[List[str]]

VALID_CHARS = ".123456789"


class Solution:
    def isValidSudoku(self, board: Board) -> bool:
        def validate(xs: List[str]) -> bool:
            seen = set()
            for x in xs:
                if x not in VALID_CHARS or (x != "." and x in seen):
                    return False
                seen.add(x)
            return True

        return (
            all(validate(board[i][j] for j in range(9)) for i in range(9))
            and all(validate(board[i][j] for i in range(9)) for j in range(9))
            and all(
                validate(
                    board[i + offseti][j + offsetj] for i in range(3) for j in range(3)
                )
                for offseti in range(0, 9, 3)
                for offsetj in range(0, 9, 3)
            )
        )


if __name__ == "__main__":
    solver = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(solver.isValidSudoku(board))
