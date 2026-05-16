#SUPREETH
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        my_map = {}
        def backtrack(cur_idx):
            if cur_idx == len(s):
                return True
            if cur_idx in my_map:
                return my_map[cur_idx]
            for i in range(cur_idx, len(s)):
                if s[cur_idx: i+1] in wordDict:
                    val = backtrack(i+1)
                    if val:
                        my_map[cur_idx] = True
                        return True
            my_map[cur_idx] = False
            return False
        
        return backtrack(0)


        