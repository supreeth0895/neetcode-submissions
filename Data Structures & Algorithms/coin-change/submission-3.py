class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_coin_count = amount
        my_map = {}
        def backtrack(remaining_amt, cur_idx):
            nonlocal max_coin_count
            key = tuple([cur_idx,remaining_amt])
            if key in my_map:
                return my_map[key]

            if remaining_amt == 0:
                return 0
            if remaining_amt < 0:
                return max_coin_count+1 #because amount+1 is actually not possible highest total coin count would  be amount
            if cur_idx ==len(coins):
                return max_coin_count+1

            possibility1 = 1 + backtrack(remaining_amt-coins[cur_idx], cur_idx)
            possibility2 = backtrack(remaining_amt, cur_idx+1)

            my_map[key] = min(possibility1, possibility2)
            return min(possibility1, possibility2)

        max_coin_count = backtrack(amount, 0)
        if max_coin_count > amount:
            return -1
        return  max_coin_count

# This was the approach I came up with first - Backtracking and no memo:
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         min_coins = amount + 1
#         def backtrack(remaining_amt, cur_idx, total_coins):
#             nonlocal min_coins
#             if remaining_amt == 0:
#                 min_coins = min(min_coins, total_coins)
#                 return
#             if remaining_amt < 0:
#                 return
#             if cur_idx ==len(coins):
#                 return
#             backtrack(remaining_amt-coins[cur_idx], cur_idx, total_coins+1)
#             backtrack(remaining_amt, cur_idx+1, total_coins)
#         backtrack(amount, 0, 0)
#         if min_coins == amount+1:
#             return -1
#         return  min_coins