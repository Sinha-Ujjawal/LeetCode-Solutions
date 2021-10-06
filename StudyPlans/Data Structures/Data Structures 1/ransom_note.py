class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        i = j = 0
        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] == magazine[j]:
                i += 1
            elif ransomNote[i] < magazine[j]:
                return False
            j += 1

        return i == len(ransomNote)


if __name__ == "__main__":
    solver = Solution()
    print(solver.canConstruct(ransomNote="a", magazine="b"))
    print(solver.canConstruct(ransomNote="aa", magazine="ab"))
    print(solver.canConstruct(ransomNote="aa", magazine="aab"))
