class Solution:
    def reverseBits(self, n: int) -> int:
        new_num = 0
        for i in range(0,32):
            bit = n >>i & 1
            temp_num = bit
            temp_num = temp_num<<31-i
            new_num = new_num | temp_num
        return new_num


        