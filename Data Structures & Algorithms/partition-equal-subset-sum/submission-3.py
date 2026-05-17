class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum %2 != 0:
            return False
        target_sum = total_sum/2
        
        def backtrack(cur_idx,remaining_sum):
            if (cur_idx,remaining_sum) in memo:
                return memo[(cur_idx,remaining_sum)]
            if cur_idx >= len(nums):
                return False
            if remaining_sum == 0:
                return True
            if remaining_sum < 0:
                return False
            
            ret_val1 = backtrack(cur_idx+1, remaining_sum - nums[cur_idx])
            ret_val2 = backtrack(cur_idx+1, remaining_sum)

            memo[(cur_idx,remaining_sum)] = ret_val1 or ret_val2
            return ret_val1 or ret_val2

        memo = {}
        return backtrack(0, target_sum)