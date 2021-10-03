from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    solver = Solution()
    strings = ["h", "e", "l", "l", "o"]
    solver.reverseString(strings)
    print(strings)
