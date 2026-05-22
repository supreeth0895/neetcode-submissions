# Reverse Integer with Overflow Check

# This solution reverses the digits of a signed 32-bit integer while ensuring
# the result stays within the range [-2^31, 2^31 - 1].

# The approach extracts digits one by one in a loop, then checks the boundary
# condition (214748364 = MAX // 10) to determine if the final digit can be safely
# added without causing overflow.

# Time Complexity: O(log|x|) - we process each digit once
# Space Complexity: O(1) - only using a few variables

class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647   #  2^31 - 1
        MIN = -2147483648  # -2^31
        
        new_num = 0
        temp = abs(x)
        
        # Extract all digits except the last
        while temp >= 10:
            digit = temp % 10
            temp = temp // 10
            new_num = new_num * 10 + digit
        
        # Handle the last digit with overflow check
        last_digit = temp  # This is the final remaining digit (0-9)
        
        if new_num == 214748364:
            # Boundary case: check if last digit fits
            if x >= 0 and last_digit > 7:
                return 0
            if x < 0 and last_digit > 8:
                return 0
        elif new_num > 214748364:
            # Already overflowed
            return 0
        
        # Safe to add the last digit
        new_num = new_num * 10 + last_digit
        
        if x < 0:
            new_num = -new_num
        
        return new_num