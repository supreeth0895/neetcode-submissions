#SUPREETH
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def backtrack(idx1, idx2, idx3):
            if (idx1, idx2, idx3) in memo:
                return memo[(idx1, idx2, idx3)]

            if idx3 == len(s3) and idx2 == len(s2) and idx1 == len(s1):
                return True
            if idx3 == len(s3):
                return False
            if ((idx1 < len(s1) and s1[idx1] != s3[idx3] ) or idx1 == len(s1)) and  ((idx2 < len(s2) and s2[idx2] != s3[idx3] ) or idx2 == len(s2)):
                return False
            ret_val = False
            if idx1 < len(s1) and s1[idx1] == s3[idx3] and (idx2 == len(s2) or s2[idx2] != s3[idx3]):
                option1 = backtrack(idx1+1, idx2, idx3+1)
                ret_val = option1
            elif idx2 < len(s2) and s2[idx2] == s3[idx3] and (idx1 == len(s1) or s1[idx1] != s3[idx3]):
                option1 = backtrack(idx1, idx2+1, idx3+1)
                ret_val = option1
            elif idx1 < len(s1) and idx2 < len(s2) and s1[idx1] == s3[idx3] and s2[idx2] == s3[idx3]:
                option1 = backtrack(idx1+1, idx2, idx3+1)
                option2 = backtrack(idx1, idx2+1, idx3+1)
                ret_val = option1 or option2
            memo[(idx1, idx2, idx3)] = ret_val
            return ret_val
        
        memo = {}
        return backtrack(0,0,0)