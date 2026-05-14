class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}
        for ch in s:
            if ch in my_map :
                my_map[ch] = my_map[ch] + 1
            else:
                my_map[ch] = 1
        
        for ch in t:
            if ch in my_map :
                my_map[ch] = my_map[ch] - 1 
            else:
                return False
        
        for ch in my_map:
            if my_map[ch] != 0 :
                return False
        
        return True