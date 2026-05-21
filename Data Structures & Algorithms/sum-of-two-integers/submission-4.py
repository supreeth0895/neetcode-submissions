class Solution:
    def getSum(self, a: int, b: int) -> int:
        i = 0  # Track current bit position
        answer = 0  # Store the result
        carry_bit = 0  # Track carry from previous addition
        max_bits = 32  # 32-bit integers (constraint for negative numbers)
        
        # Process each bit position from right to left
        while i < max_bits:
            # Extract the rightmost bit from a and b
            right_most_a_bit = a & 1
            right_most_b_bit = b & 1
            
            # Calculate result bit: XOR all three (a_bit, b_bit, carry)
            # XOR gives 1 if odd number of 1s, 0 if even
            bit = right_most_a_bit ^ right_most_b_bit ^ carry_bit
            
            # Calculate new carry for next position:
            # - (a & b): both bits are 1
            # - (carry & (a ^ b)): carry is 1 AND bits are different
            carry_bit = (right_most_a_bit & right_most_b_bit) | (carry_bit & (right_most_a_bit ^ right_most_b_bit))
            
            # Place the result bit at position i in the answer
            answer |= (bit << i)
            
            # Shift both numbers right to process next bit
            a >>= 1
            b >>= 1
            
            # Move to next bit position
            i += 1
        
        # Convert to signed 32-bit integer
        # If the result is >= 2^31, it represents a negative number in two's complement
        if answer >= 2**31:
            answer -= 2**32
        
        return answer