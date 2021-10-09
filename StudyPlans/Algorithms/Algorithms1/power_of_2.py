from math import log2


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1 and (not (n & 1)):
            n >>= 1
        return n == 1


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return log2(n).is_integer() if n > 0 else False


if __name__ == "__main__":
    solver = Solution()
    solver2 = Solution2()
    for num in range(-10, 10):
        assert solver.isPowerOfTwo(num) == solver2.isPowerOfTwo(num)
