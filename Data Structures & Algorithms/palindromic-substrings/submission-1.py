#SUPREETH
class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0
        #Note: This is same as last problem
        #Basically expand around centers, and every time we see cur_string is a palindrome, we increment total_count
        # Nothing else matters.

        def backtrack(left_idx, right_idx):
            nonlocal total_count
            if left_idx < 0 or right_idx >= len(s) or s[left_idx] != s[right_idx]:
                return
            total_count = total_count+1
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
        
        return total_count

        