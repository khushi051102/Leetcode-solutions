class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=prices[0]
        max_diff=0
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                max_diff=max(max_diff,prices[i]-min_price)
        return max_diff