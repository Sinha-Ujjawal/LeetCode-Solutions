class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        m = {}
        for end, char in enumerate(s):
            if m.get(char, -1) >= start:  # if in the current range
                start = m[char] + 1
            max_len = max(max_len, end - start + 1)
            m[char] = end
        return max_len


if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLongestSubstring("abcabcbb"))
    print(solver.lengthOfLongestSubstring("bbbbbb"))
    print(solver.lengthOfLongestSubstring("pwwkew"))
