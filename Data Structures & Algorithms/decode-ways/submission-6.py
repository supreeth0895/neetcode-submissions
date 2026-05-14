#SUPREETH
class Solution:
    def numDecodings(self, s: str) -> int:
        my_map = {}
        def backtrack(cur_idx):
            if cur_idx in my_map:
                return my_map[cur_idx]
            if cur_idx == len(s):
                return 1
            if s[cur_idx] == "0":
                return 0

            ways1 = backtrack(cur_idx+1)
            ways2 = 0
            if cur_idx < len(s)-1:
                if (s[cur_idx] == "1") or (s[cur_idx] == "2" and s[cur_idx+1] <= "6"):
                    ways2 = backtrack(cur_idx+2)
            my_map[cur_idx] = ways1+ways2
            return ways1+ways2
            
        return backtrack(0)