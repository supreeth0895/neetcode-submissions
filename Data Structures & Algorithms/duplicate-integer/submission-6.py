class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for elem in nums:
            if elem not in visited:
                visited.add(elem)
            else:
                return True
        return False