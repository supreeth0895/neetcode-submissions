class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for elem in nums:
            if elem in visited:
                return True
            visited.add(elem)
        return False