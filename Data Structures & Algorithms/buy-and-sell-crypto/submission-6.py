class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = [0] * len(prices)
        max_right = [0] * len(prices)

        for i in range(0, len(prices)):
            if i== 0:
                min_left[i] = prices[i]
            else:
                min_left[i] = min(min_left[i-1], prices[i])

        max_profit = 0
        for i in range(len(prices)-1,-1,-1):
            if i == len(prices) -1:
                max_right[i] = prices[i]
            else:
                max_right[i] = max(max_right[i-1], prices[i])
            max_profit = max(max_profit,max_right[i] - min_left[i])            
        
        return max_profit


        
        



        