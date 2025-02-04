from typing import List

# Time complexity = O(n)
# Space complexity = O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cheapestPriceSoFar = prices[0]

        for i in range(len(prices)):

            if prices[i] < cheapestPriceSoFar:
                cheapestPriceSoFar = prices[i]

            if prices[i] - cheapestPriceSoFar > maxProfit:
                maxProfit = prices[i] - cheapestPriceSoFar

        return maxProfit
