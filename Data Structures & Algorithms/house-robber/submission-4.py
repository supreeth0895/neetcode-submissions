#SUPREETH
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_amount_robbed_at_index = {}

        def backtrack(cur_index):
            #check if we have already calculated this path - hashmap - memoization
            if cur_index in max_amount_robbed_at_index:
                return max_amount_robbed_at_index[cur_index]
            
            if cur_index == len(nums):
                return 0

            #calculate profit if current house is robbed. So he would have option to rob all houses from cur_idx+2 to len(nums)
            max_amount_if_cur_index_robbed = 0
            for i in range(cur_index+2, len(nums)):
                amount_robbed = backtrack(i)
                max_amount_if_cur_index_robbed = max(max_amount_if_cur_index_robbed, amount_robbed)
            profit_if_cur_index_robbed = nums[cur_index]+max_amount_if_cur_index_robbed


            #calculate profit if current house not is robbed, ie; go to next house:
            profit_if_cur_index_not_robbed = backtrack(cur_index+1)

            max_amount_robbed = max(profit_if_cur_index_robbed, profit_if_cur_index_not_robbed)
            
            #Add it to the hashmap for memoization
            max_amount_robbed_at_index[cur_index] = max_amount_robbed

            return max_amount_robbed
        
        return backtrack(0)

        