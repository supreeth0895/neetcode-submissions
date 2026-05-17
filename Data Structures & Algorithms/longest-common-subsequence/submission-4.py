class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def backtrack(cur_idx1,cur_idx2):
            if cur_idx1 == len(text1) or cur_idx2 == len(text2):
                return 0
            if (cur_idx1,cur_idx2) in my_map:
                return my_map[(cur_idx1,cur_idx2)]
            option1 = 0
            if text1[cur_idx1] == text2[cur_idx2]:
                option1 = 1 + backtrack(cur_idx1+1,cur_idx2+1)
            option2 = backtrack(cur_idx1+1,cur_idx2)
            option3 = backtrack(cur_idx1,cur_idx2+1)

            my_map[(cur_idx1,cur_idx2)] = max(option1, option2, option3)
            return max(option1, option2, option3)
        
        my_map = {}
        return backtrack(0,0)