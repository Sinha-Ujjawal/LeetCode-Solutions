from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell = max_profit = 0
        for price in reversed(prices):
            max_profit = max(max_profit, max_sell - price)
            max_sell = max(max_sell, price)
        return max_profit


if __name__ == "__main__":
    solver = Solution()
    print(solver.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
