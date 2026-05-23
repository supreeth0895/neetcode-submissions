class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        end=0
        cur_sum = 0
        max_sum  = 0
        negetive_nums = 0
        while end<len(nums):
            if cur_sum+nums[end] < 0:
                cur_sum = 0
                start = end+1
                end = end+1
                continue
            cur_sum = cur_sum+nums[end]
            max_sum = max(max_sum, cur_sum)
            end = end+1
        
        if max_sum ==0:
            return max(nums)
        
        return max_sum  