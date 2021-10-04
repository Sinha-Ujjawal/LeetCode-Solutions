from typing import List


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(n - 1):
            row = [1]
            for i in range(1, len(ans[-1])):
                row.append(ans[-1][i] + ans[-1][i - 1])
            row.append(1)
            ans.append(row)
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.generate(n=5))
