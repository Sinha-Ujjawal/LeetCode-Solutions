from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def transform(s: str) -> List[str]:
            chars = []
            for char in s:
                if char == "#":
                    if chars:
                        chars.pop()
                else:
                    chars.append(char)
            return chars

        return transform(s) == transform(t)


if __name__ == "__main__":
    solver = Solution()
    print(solver.backspaceCompare("ab#c", "ad#c"))
    print(solver.backspaceCompare("a#c", "b"))
