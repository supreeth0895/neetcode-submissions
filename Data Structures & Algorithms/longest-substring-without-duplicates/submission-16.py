class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        set1 = set()
        max_val = 0
        while r<len(s):
            if s[r] not in set1:
                set1.add(s[r])
                r+=1
            else:
                while s[r] in set1:
                    set1.remove(s[l])
                    l+=1
            max_val = max(max_val, (r-l))
        return (max_val)