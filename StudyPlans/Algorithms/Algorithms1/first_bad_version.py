from typing import Optional

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


def isBadVersion(version: int):
    # I hate 4
    return version >= 4


class Solution:
    def firstBadVersion(self, n: int) -> Optional[int]:
        lb, ub = 1, n
        while lb <= ub:
            mid = (lb + ub) >> 1
            if isBadVersion(mid):
                ub = mid - 1
            else:
                lb = mid + 1

        return lb


if __name__ == "__main__":
    solver = Solution()
    print(solver.firstBadVersion(n=5))
