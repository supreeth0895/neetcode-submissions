from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = Counter(s)
        dict2 = Counter(t)
        for key, val in dict1.items():
            if key not in dict2:
                return False
            if val != dict2[key]:
                return False
            del dict2[key]
        if dict2:
            return False
        return True
