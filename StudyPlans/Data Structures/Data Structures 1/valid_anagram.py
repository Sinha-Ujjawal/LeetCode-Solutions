from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    solver = Solution()
    solver2 = Solution2()
    print(solver.isAnagram(s="anagram", t="nagaram"))
    print(solver2.isAnagram(s="anagram", t="nagaram"))
