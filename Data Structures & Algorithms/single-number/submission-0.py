class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if i == 0:
                res = num
            else:
                res = res ^ num
        return res
        