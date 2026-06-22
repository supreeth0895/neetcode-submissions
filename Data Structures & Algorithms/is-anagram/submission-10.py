class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # BF O(n) , O(n)
        '''dict1 = defaultdict(int)
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
        return True'''
        # BF sort both and compare
        '''s = sorted(s)
        t = sorted(t)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True'''
        # Brute force -- Array 
        if len(s)!=len(t):
            return False
        
        hash1 = [0]*26
        for i in range(len(s)):
            hash1[ord(s[i]) - ord('a')] +=1
            hash1[ord(t[i]) - ord('a')] -=1

        for elem in hash1:
            if elem!=0:
                return False
        return True

