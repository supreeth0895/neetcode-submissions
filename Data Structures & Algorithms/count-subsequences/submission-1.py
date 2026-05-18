class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def backtrack(cur_idx1, cur_idx2):
            if (cur_idx1, cur_idx2) in memo:
                return memo[(cur_idx1, cur_idx2)]
            if cur_idx2 == len(t):
                return 1
            if cur_idx1 == len(s):
                return 0
            if s[cur_idx1] != t[cur_idx2]:
                option1 = backtrack(cur_idx1+1, cur_idx2)
                memo[(cur_idx1, cur_idx2)] = option1
                return option1
            else:
                option1 = backtrack(cur_idx1+1, cur_idx2)
                option2 = backtrack(cur_idx1+1, cur_idx2+1)
                memo[(cur_idx1, cur_idx2)] = option1+ option2
                return option1+ option2
        
        memo = {}
        return backtrack(0,0)



        