class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        cur_idx = len(digits)-1
        carry = 1
        while cur_idx >= 0:
            digits[cur_idx] = digits[cur_idx] + carry
            if digits[cur_idx] == 10:
                digits[cur_idx] = 0
                carry = 1
            else:
                carry = 0
                break
            cur_idx = cur_idx -1
        if carry:
            digits.reverse()
            digits.append(1)
            digits.reverse()
        return digits