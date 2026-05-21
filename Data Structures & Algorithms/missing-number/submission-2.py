#SUPREETH
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR PROPERTIES - a ^ 0 = a, a ^ a = 0
        # Key insight: XORing a number with itself cancels it out
        # All numbers in range [0, n] except the missing one will cancel out
        
        n = len(nums)
        temp = 0
        
        # XOR all numbers in the expected range [0, n]
        for i in range(0, n + 1):
            temp = temp ^ i
        
        # XOR all numbers that actually exist in nums
        # This will cancel out all numbers that appear in both the range and the array
        for i in range(0, n):
            temp = temp ^ nums[i]
        
        # The result is the missing number (the only one not canceled out)
        return temp




    # NOTE: MY initial approach was using Sum of n numbers = n(n+1)/2 . This approach works as well.
    # But just wanted to showcase bit manipulation.
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     expected_sum = n*(n+1)//2
    #     actual_sum = sum(nums)
    #     return expected_sum - actual_sum
