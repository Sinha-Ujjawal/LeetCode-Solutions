from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter()
        for e, char in enumerate(s2):
            if e >= len(s1):
                c2[char] += 1
                x = s2[e - len(s1)]
                if c2[x] == 1:
                    c2.pop(x)
                else:
                    c2[x] -= 1
            else:
                c2[char] += 1
            if c1 == c2:
                return True
        return False


if __name__ == "__main__":
    solver = Solution()
    print(solver.checkInclusion(s1="ab", s2="eidbaooo"))
