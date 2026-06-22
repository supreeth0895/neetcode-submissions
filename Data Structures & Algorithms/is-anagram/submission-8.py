class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        for elem in s:
            dict1[elem]+=1
        for elem in t:
            if elem not in dict1:
                return False
            else:
                dict1[elem]-=1
                if dict1[elem] == 0:
                    del dict1[elem]
        if dict1:
            return False
        return True