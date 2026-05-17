#SUPREETH - Backtracking + Memoization


# HINT1 was super helpful:
    # If the sum of the array elements is not even, we can immediately return false.
    # Think in terms of recursion, where we try to build a subset with a sum equal to half of the total sum.
    # If we find such a subset, the remaining elements will automatically form another subset with the same sum.
    # The entire array can also be considered as one subset, with the other being empty. Can you visualize this as a decision tree to process the array recursively?


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