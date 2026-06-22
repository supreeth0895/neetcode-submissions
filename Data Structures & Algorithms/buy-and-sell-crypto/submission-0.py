class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy =math.inf
        max_profit =-math.inf
        for i in range(len(prices)):
            min_buy = min(min_buy, prices[i])
            max_profit = max(max_profit, (prices[i]-min_buy))
        return max_profit