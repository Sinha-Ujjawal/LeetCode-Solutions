class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = f1 = 1
        for _ in range(n):
            f0, f1 = f1, f0 + f1
        return f0


if __name__ == "__main__":
    solver = Solution()
    print(solver.climbStairs(2))
    print(solver.climbStairs(3))
