class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = set()
        for elem in nums:
            if elem not in dict1:
                dict1.add(elem)
            else:
                return True
        return False
        