class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[abs(nums[i])] > 0:
               nums[abs(nums[i])] = nums[abs(nums[i])] * -1
            else:
                return abs(nums[i])