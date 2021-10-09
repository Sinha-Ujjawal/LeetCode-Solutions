class Solution:
    def hammingWeight(self, n: int) -> int:
        wt = 0
        is_non_neg = n >= 0
        offset = int(not is_non_neg)
        n = abs(n)
        for _ in range(32):
            if is_non_neg and n == 0:
                break
            wt += (n + offset) & 1
            n >>= 1
        return wt


class Solution2:
    def hammingWeight(self, n: int) -> int:
        return "{0:032b}".format(abs(n)).count("1" if n >= 0 else "0")


if __name__ == "__main__":
    solver = Solution()
    solver2 = Solution2()
    for num in range(-5, 5):
        print(f"HammingWeight({bin(num)}): {solver.hammingWeight(num)}")
        print(f"HammingWeight({bin(num)}): {solver2.hammingWeight(num)}")
