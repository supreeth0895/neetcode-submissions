#SUPREETH
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Approach: Simulate addition from the rightmost digit with an initial carry of 1.
        # If a digit becomes 10, set it to 0 and propagate the carry left.
        # If carry remains after the loop (e.g. [9,9,9]), insert 1 at the front.

        cur_idx = len(digits) - 1
        carry = 1

        while cur_idx >= 0:
            digits[cur_idx] = digits[cur_idx] + carry
            if digits[cur_idx] == 10:  # Carry propagates
                digits[cur_idx] = 0
                carry = 1
            else:                      # No carry, we're done
                carry = 0
                break
            cur_idx -= 1

        if carry:                      # Edge case: all 9s (e.g. [9,9,9] -> [1,0,0,0])
            digits.insert(0, 1)

        return digits