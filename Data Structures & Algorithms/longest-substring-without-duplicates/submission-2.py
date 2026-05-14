class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        my_set =set()
        while right <len(s):
            if s[right] not in my_set:
                my_set.add(s[right])
                right = right+1
            else:
                max_length = max(len(my_set), max_length)
                while s[left] != s[right]:
                    my_set.remove(s[left])
                    left = left+1
                my_set.remove(s[left])
                left = left+1
        
        max_length = max(len(my_set), max_length)
        return max_length
                
                






        