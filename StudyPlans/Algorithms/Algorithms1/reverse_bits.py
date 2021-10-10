class Solution:
    def reverseBits(self, n: int) -> int:
        m = "{0:032b}".format(n)
        return int(m[::-1], 2)


if __name__ == "__main__":
    solver = Solution()
    n = 0b11111111111111111111111111111101
    print(solver.reverseBits(n))
