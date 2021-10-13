from functools import lru_cache


class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


class Solution3:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        m = max(n, 0)
        for i in range(2, m + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[m]


class Solution4:
    def fib(self, n: int) -> int:
        f0, f1 = 0, 1
        for _ in range(abs(n)):
            f0, f1 = f1, f0 + f1
        return f0


class Solution4:
    def fib(self, n: int) -> int:
        z = [0, 1, 1, 1]
        m = abs(n)
        f = [1, 0, 0, 1]

        def mul_mat4(m1, m2):
            a11, a12, a21, a22 = m1
            b11, b12, b21, b22 = m2
            c11 = a11 * b11 + a12 * b21
            c12 = a11 * b12 + a12 * b22
            c21 = a21 * b11 + a22 * b21
            c22 = a21 * b12 + a22 * b22
            return [c11, c12, c21, c22]

        while m:
            while not (m & 1):
                z = mul_mat4(z, z)
                m >>= 1
            f = mul_mat4(f, z)
            m -= 1
        a11, a12, a21, a22 = f
        f0, f1 = 0, 1
        return f0 * a11 + f1 * a12


if __name__ == "__main__":
    solver = Solution4()
    for i in range(10):
        print(i, solver.fib(i))
