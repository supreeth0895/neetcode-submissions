#SUPREETH

# When two identical numbers are XORed, they cancel out, resulting in zero. Since every number appears twice except for one, the XOR of the entire array gives the number that appears only once.



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Key insight: XOR has these properties:
        # - a ^ a = 0 (any number XORed with itself is 0)
        # - a ^ 0 = a (any number XORed with 0 is itself)
        # - XOR is commutative and associative (order doesn't matter)
        # 
        # Since every number appears twice except one:
        # nums[0] ^ nums[1] ^ nums[2] ^ ... 
        # = (pairs cancel out to 0) ^ single_number
        # = single_number
        
        res = 0  # Initialize to 0 (neutral element for XOR)
        
        # Iterate through each number in the array
        for num in nums:
            # XOR current number with running result
            # Pairs will cancel out, leaving only the single number
            res = res ^ num
        
        return res
        