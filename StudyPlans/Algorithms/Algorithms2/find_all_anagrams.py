from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sp = Counter(p)
        sc = Counter()
        ans = []
        for e, char in enumerate(s):
            if e >= len(p):
                char_to_remove = s[e - len(p)]
                cnt = sc[char_to_remove]
                if cnt == 1:
                    sc.pop(char_to_remove)
                else:
                    sc[char_to_remove] = cnt - 1
            sc[char] += 1
            if sc == sp:
                ans.append(e - len(p) + 1)
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.findAnagrams(s="cbaebabacd", p="abc"))
    print(solver.findAnagrams(s="abab", p="ab"))
