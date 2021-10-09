class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        other_half = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in "{[(":
                stack.append(char)
            elif char in ")]}" and stack and stack[-1] == other_half[char]:
                stack.pop()
            else:
                return False
        return not stack


if __name__ == "__main__":
    solver = Solution()
    print(solver.isValid("()[]{}"))
    print(solver.isValid("([)]"))
