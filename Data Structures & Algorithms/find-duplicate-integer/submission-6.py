#SUPREETH
#nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
#Make use of this. To mark nums[i] as visited, mark the number at index nums[i] negetive.
#So if you encounter another nums[i], we see that negetive sign and relaize that this is repeated
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[abs(nums[i])] > 0:
               nums[abs(nums[i])] = nums[abs(nums[i])] * -1
            else:
                return abs(nums[i])