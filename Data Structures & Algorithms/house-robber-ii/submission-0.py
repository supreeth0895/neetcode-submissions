#SUPREETH
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_amount_robbed_at_index = {}

        def backtrack(cur_index, is_first_house_robbed):
            #check if we have already calculated this path - hashmap - memoization
            if tuple([cur_index,is_first_house_robbed]) in max_amount_robbed_at_index:
                return max_amount_robbed_at_index[tuple([cur_index,is_first_house_robbed])]

            if cur_index == len(nums)-1 and is_first_house_robbed:
                return 0
            
            if cur_index == len(nums):
                return 0

            #calculate profit if current house not is robbed, ie; go to next house:
            profit_if_cur_index_not_robbed = backtrack(cur_index+1, is_first_house_robbed)

            #calculate profit if current house is robbed. So he would have option to rob all houses from cur_idx+2 to len(nums)
            max_amount_if_cur_index_robbed = 0

            if cur_index == 0:
                is_first_house_robbed = True
                
            for i in range(cur_index+2, len(nums)):
                amount_robbed = backtrack(i, is_first_house_robbed)
                max_amount_if_cur_index_robbed = max(max_amount_if_cur_index_robbed, amount_robbed)
            profit_if_cur_index_robbed = nums[cur_index]+max_amount_if_cur_index_robbed




            max_amount_robbed = max(profit_if_cur_index_robbed, profit_if_cur_index_not_robbed)
            
            # Add it to the hashmap for memoization
            max_amount_robbed_at_index[tuple([cur_index,is_first_house_robbed])] = max_amount_robbed

            return max_amount_robbed
        
        return backtrack(0, False)

        