class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def backtrack (cur_idx,rem_amt):
            if (cur_idx,rem_amt) in memo:
                return memo[(cur_idx,rem_amt)]
            if cur_idx == len(coins):
                return 0
            if rem_amt < 0:
                return 0
            if rem_amt == 0:
                return 1
            path1 = backtrack(cur_idx, rem_amt - coins[cur_idx])
            path2 = backtrack(cur_idx+1, rem_amt)
            memo[(cur_idx,rem_amt)] = path1+path2
            return path1+path2
        
        memo = {}
        return backtrack(0, amount)
            
            


        