from typing import List


class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        if len(costs) == 0:
            return 0
        elif len(costs) == 1:
            return costs[0]
        else:
            fi, fiplus1 = costs[-2], costs[-1]
            for i in range(len(costs) - 3, -1, -1):
                fi, fiplus1 = min(fi, fiplus1) + costs[i], fi
            return min(fi, fiplus1)


if __name__ == "__main__":
    solver = Solution()
    print(solver.minCostClimbingStairs([10, 15, 20]))
    print(solver.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
