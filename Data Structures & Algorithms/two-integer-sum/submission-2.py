class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BF hash 
        dict1 = {}
        for idx, elem in enumerate(nums):
            if target - elem not in dict1:
                dict1[elem] = idx
            else:
                return [dict1[(target-elem)], idx]

                
