#SUPREETH

# When two identical numbers are XORed, they cancel out, resulting in zero. Since every number appears twice except for one, the XOR of the entire array gives the number that appears only once.



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if i == 0:
                res = num
            else:
                res = res ^ num
        return res
        