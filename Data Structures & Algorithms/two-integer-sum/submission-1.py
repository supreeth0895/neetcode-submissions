class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for indx, elem in enumerate(nums):
            if target-elem in dict1:
                return [dict1[target-elem], indx]
            dict1[elem] = indx
        