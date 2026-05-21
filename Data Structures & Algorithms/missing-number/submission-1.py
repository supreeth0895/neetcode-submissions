#SUPREETH
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # expected_sum = n*(n+1)//2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum


        # XOR PROPERTIES - a ^ 0 = a, a ^ a = a
        n = len(nums)
        temp = 0
        for i in range(0,n+1):
            temp = temp ^ i
        for i in range(0,n):
            temp  = temp ^ nums[i]
        return temp


    