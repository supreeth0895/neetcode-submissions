class Solution:
    def getSum(self, a: int, b: int) -> int:
        i = 0
        answer = 0
        carry_bit = 0
        max_bits = 32  # 32-bit integers
        
        while i < max_bits:
            right_most_a_bit = a & 1
            right_most_b_bit = b & 1
            
            bit = right_most_a_bit ^ right_most_b_bit ^ carry_bit
            carry_bit = (right_most_a_bit & right_most_b_bit) | (carry_bit & (right_most_a_bit ^ right_most_b_bit))
            
            answer |= (bit << i)
            a >>= 1
            b >>= 1
            i += 1
        
        # Convert to signed 32-bit integer
        if answer >= 2**31:
            answer -= 2**32
        
        return answer