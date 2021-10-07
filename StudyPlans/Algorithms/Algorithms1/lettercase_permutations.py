from typing import List
from string import ascii_lowercase


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        stack = [""]
        s = s.lower()
        while stack:
            w = stack.pop()
            if len(w) == len(s):
                yield w
            else:
                if s[len(w)] in ascii_lowercase:
                    stack.append(w + s[len(w)])
                    stack.append(w + s[len(w)].upper())
                else:
                    stack.append(w + s[len(w)])


if __name__ == "__main__":
    solver = Solution()
    print(list(solver.letterCasePermutation("a1b1")))
