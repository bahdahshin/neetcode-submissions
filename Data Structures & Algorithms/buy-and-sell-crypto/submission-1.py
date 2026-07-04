class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_buy = prices[0]

        for sell in prices:
            max_price = max(max_price, sell - min_buy)
            min_buy = min(min_buy, sell)

        return max_price