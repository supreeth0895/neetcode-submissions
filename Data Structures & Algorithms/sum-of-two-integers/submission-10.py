class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a = a & mask
        b = b & mask
        carry = 0
        reversed_answer = 0
        num_bits = 0

        while a != 0 or b != 0 or carry != 0:
            if num_bits >= 32: break
            right_most_bit1 = a & 1
            right_most_bit2 = b & 1
            answer_digit = right_most_bit1 ^ right_most_bit2 ^ carry
            carry = (right_most_bit1 & right_most_bit2) | (right_most_bit1 & carry) | (right_most_bit2 & carry)
            reversed_answer = (reversed_answer << 1) | answer_digit  # fix: shift first, then OR
            a = a >> 1
            b = b >> 1
            num_bits += 1

        answer = 0
        for i in range(num_bits):
            leftmost_bit = reversed_answer & 1
            answer = answer | (leftmost_bit << num_bits - 1 - i)
            reversed_answer = reversed_answer >> 1

        return answer if answer <= 0x7FFFFFFF else ~(answer ^ mask)