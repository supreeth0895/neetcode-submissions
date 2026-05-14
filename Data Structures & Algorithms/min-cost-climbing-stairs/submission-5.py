#SUPREETH
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        my_map = {}

        def backtrack(cur_index):
            if cur_index in my_map:
                return my_map[cur_index]
            if cur_index >= len(cost):
                return 0
            val1 = backtrack(cur_index +1)
            val2 = backtrack(cur_index+ 2)
            my_map[cur_index] = cost[cur_index] + min(val1, val2)
            return cost[cur_index] + min(val1, val2)
        
        return min(backtrack(0), backtrack(1))


#PITFALL: I tried to do something like this, but I could not perform Memoization. There was no need to pass curr_cost.
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def backtrack(cur_cost,cur_index):
#             if cur_index >= len(cost):
#                 return cur_cost
#             val1 = backtrack(cur_cost + cost[cur_index], cur_index +1)
#             val2 = backtrack(cur_cost + cost[cur_index], cur_index+ 2)
#             return min (val1, val2)
        
        
#         return min(backtrack(0,0), backtrack(0,1))

        