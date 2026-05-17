class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def backtrack(left_idx, right_idx):
            if (left_idx, right_idx) in memo:
                return memo[(left_idx, right_idx)]

            if right_idx >= len(prices):
                if left_idx == right_idx:
                    return 0
                memo[(left_idx, right_idx)] = prices[len(prices)-1]
                return prices[len(prices)-1]
            if left_idx == right_idx:
                option1 = 0 - prices[left_idx] + backtrack(left_idx, right_idx+1)
                option2 = backtrack(left_idx+1, right_idx+1)
                max_val =  max(option1, option2)
            else:
                option1 = prices[right_idx] +  backtrack(right_idx+2, right_idx+2)
                option2 = backtrack(left_idx, right_idx+1)
                max_val = max(option1, option2)
            memo[(left_idx, right_idx)] = max_val
            return max_val
        
        memo = {}
        return backtrack(0,0)


        
        