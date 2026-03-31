class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxReturn = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = r + 1
            else:
                maxReturn = max(maxReturn, prices[r]-prices[l])
                r = r + 1
        
        return maxReturn