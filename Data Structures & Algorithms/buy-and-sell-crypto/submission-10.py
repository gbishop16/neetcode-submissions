class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxProfit = 0, 1, 0

        while l < r and r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1

        return maxProfit
            