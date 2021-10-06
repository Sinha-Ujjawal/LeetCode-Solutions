from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        ordered_map = OrderedDict()
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char not in seen:
                ordered_map[char] = i
            elif char in ordered_map:
                ordered_map.pop(char)
            seen.add(char)

        return ordered_map.popitem()[1] if ordered_map else -1


if __name__ == "__main__":
    solver = Solution()
    print(solver.firstUniqChar(s="leetcode"))
    print(solver.firstUniqChar(s="loveleetcode"))
    print(solver.firstUniqChar(s="acaadcad"))
