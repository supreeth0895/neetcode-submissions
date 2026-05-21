#SUPREETH
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Dictionary to store bit counts for numbers we've already computed
        my_map = {0:0, 1:1}
        
        # 'power' tracks which power of 2 range we're in
        # 'offset' is how far we are from the current power of 2
        power = 1
        offset = 0
        num = 2**power + offset  # Start from 2 (2^1 + 0)
        
        while num <= n:
            # When we reach the next power of 2, reset offset and increment power
            # Example: when num reaches 4 (2^2), we move to the next range [4-7]
            if num == 2**(power+1):
                power = power + 1
                offset = 0
            
            # Key insight: Every number in range [2^k, 2^(k+1)-1] can be written as 2^k + offset
            # The number of 1-bits = 1 (from the 2^k bit) + number of 1-bits in offset
            
            # Remove the highest bit (the 2^power bit) to get the offset
            # This works because offset < 2^power, so we're removing exactly the bit we set
            new_num1 = 1
            new_num1 = new_num1 << power  # Create a mask with only the power-th bit set
            new_num1 = ~new_num1          # Invert to mask all bits EXCEPT the power-th bit
            new_num1 = num & new_num1     # Apply mask to get the offset part
            
            # The bit count of 'num' = 1 (for the 2^power bit) + bit count of the offset
            total_count = my_map[new_num1] + 1
            my_map[num] = total_count
            
            num = num + 1
            offset = offset + 1
        
        # Convert dictionary to list for the answer
        answer = []
        for num in range(0, n + 1): 
            answer.append(my_map[num])
        return answer