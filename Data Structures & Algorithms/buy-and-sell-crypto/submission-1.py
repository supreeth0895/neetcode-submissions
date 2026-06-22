class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = math.inf
        for elem in prices:
            min_buy = min(min_buy, elem)
            max_profit = max(max_profit, abs(min_buy-elem))
        return max_profit