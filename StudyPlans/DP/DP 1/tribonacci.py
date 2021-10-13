class Solution:
    def tribonacci(self, n: int) -> int:
        z = [0, 1, 0, 0, 0, 1, 1, 1, 1]
        m = abs(n)
        f = [1, 0, 0, 0, 1, 0, 0, 0, 1]

        def mul_mat9(a, b):
            c = [0] * 9
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        c[i * 3 + j] += a[i * 3 + k] * b[k * 3 + j]
            return c

        while m:
            while not (m & 1):
                z = mul_mat9(z, z)
                m >>= 1
            f = mul_mat9(f, z)
            m -= 1

        f0, f1, f2 = 0, 1, 1
        a11, a12, a13, *_ = f
        return f0 * a11 + f1 * a12 + f2 * a13


if __name__ == "__main__":
    solver = Solution()
    for i in range(10):
        print(i, solver.tribonacci(i))
