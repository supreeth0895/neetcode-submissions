class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        rightmost_bit = n &1
        ans = ans | rightmost_bit
        for i in range(0, 31):
            n = n >> 1
            ans = ans << 1
            rightmost_bit = n &1
            ans = ans | rightmost_bit
        
        return ans
        