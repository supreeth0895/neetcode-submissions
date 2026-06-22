class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force time : o(n), space : o(n)
        '''set1 = {}
        for num in nums:
            if num not in set1:
                set1.add(num)
            else:
                return True
        return False'''
        # Brute force time : o(n), space : o(1)
        nums = sorted(nums)
        prev = None
        for num in nums:
            if num != prev:
                prev = num
            elif prev == num:
                return True
        return False
        # simple method using Data structures o(n), space : o(n)
        # return len(set(nums)) != len(nums)