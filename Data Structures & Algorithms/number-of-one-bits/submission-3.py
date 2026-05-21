#SUPREETH
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        # Continue looping while n is not 0
        while n:
            # Check if the least significant bit (rightmost bit) is 1
            # n & 1 performs bitwise AND with 1
            # Result is 1 if the rightmost bit is 1, otherwise 0
            if n & 1:
                count = count + 1
            
            # Right shift n by 1 position
            # This effectively removes the rightmost bit we just checked
            # Example: 1011 >> 1 = 0101
            n = n >> 1
        
        return count

        