from typing import List


class Solution:
    def getRow(self, index: int) -> List[int]:
        assert index >= 0
        ans = [None] * (index + 1)
        ans[0] = ans[-1] = ncr = 1
        for r in range(1, (len(ans) >> 1) + (len(ans) & 1)):
            ans[r] = ans[index - r] = ncr = ncr * (index + 1 - r) // r
        return ans


if __name__ == "__main__":
    solver = Solution()
    for i in range(10):
        print(solver.getRow(i))
