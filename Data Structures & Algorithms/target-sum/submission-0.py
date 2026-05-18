class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(cur_idx, cur_sum):
            if (cur_idx, cur_sum) in memo:
                return memo[(cur_idx, cur_sum)]
            if cur_idx == len(nums):
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            val1 = backtrack(cur_idx+1, cur_sum +nums[cur_idx])
            val2 = backtrack(cur_idx+1, cur_sum -nums[cur_idx])

            memo[(cur_idx, cur_sum)] = val1+val2

            return val1+val2
        memo = {}
        return backtrack(0,0)




        