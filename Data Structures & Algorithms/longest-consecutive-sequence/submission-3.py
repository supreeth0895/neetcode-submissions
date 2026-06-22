class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        longest = 0
        for num in set1:
            if num-1 in set1:
                continue
            else:
                interim = 1
                interim_num = num+1
                while interim_num in set1:
                    interim_num+=1
                    interim+=1
                longest = max(longest, interim)
        return longest