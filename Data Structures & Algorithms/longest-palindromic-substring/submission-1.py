#SUPREETH
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_str = ""

        #Note: This same expand around centers can be done via two pointer as well - Same TC, and even lesser SC.
        def backtrack(left_idx, right_idx):
            nonlocal max_len
            nonlocal max_str
            if left_idx < 0 or right_idx >= len(s) or s[left_idx] != s[right_idx]:
                cur_len = right_idx - left_idx -1
                if cur_len > max_len:
                    max_len = cur_len
                    max_str = s[left_idx+1:right_idx]
                return
            if s[left_idx] == s[right_idx]:
                left_idx = left_idx -1
                right_idx = right_idx + 1
                backtrack(left_idx, right_idx)

        #O(n^2)
        for i in range(0,len(s)): #O(n)
            backtrack(i,i) #O(n)
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    backtrack(i,i+1) #O(n)
        
        return max_str

        