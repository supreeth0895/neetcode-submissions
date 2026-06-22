from collections import defaultdict, Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = Counter(s)
        dict2 = Counter(t)
        for key, val in dict1.items():
            if key not in dict2:
                return False
            dict2[key] -= val
            if dict2[key] == 0:
                del dict2[key]
        if len(dict2) == 0:
            return True
        return False
