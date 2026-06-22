class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        max_val = 1
        interim_max = 1
        i = 1
        while i < len(nums):
            if nums[i]-nums[i-1] == 1:
                interim_max+=1
            elif nums[i]-nums[i-1] == 0:
                i+=1
                continue
            else:
                max_val = max(max_val, interim_max)
                interim_max = 1
            i+=1
        max_val = max(max_val, interim_max)
        return max_val