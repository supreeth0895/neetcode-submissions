class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # BF : sort and compare o(n), o(n)
        '''s = sorted(s)
        t = sorted(t)
        return s == t'''
        # BF O(n) , O(n)
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
