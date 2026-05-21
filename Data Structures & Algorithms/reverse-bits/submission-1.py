#SUPREETH
class Solution:
    def reverseBits(self, n: int) -> int:
        new_num = 0
        
        # Iterate through all 32 bits
        for i in range(0, 32):
            # Extract the i-th bit from the right
            # >> shifts n right by i positions, & 1 isolates the rightmost bit
            bit = n >> i & 1
            
            # Store the extracted bit
            temp_num = bit
            
            # Shift the bit to its reversed position (31 - i)
            # If we're reading from position i, it should go to position 31-i
            temp_num = temp_num << 31 - i
            
            # Add (OR) this bit into our result
            # Using | ensures we don't overwrite previous bits
            new_num = new_num | temp_num
        
        return new_num