class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        len1 = len(s1)
        s1_array = [0] * 26
        s2_array = [0] * 26
        for i in range(len(s1)):
            s1_array[ord(s1[i])-ord('a')]+=1
            s2_array[ord(s2[i])-ord('a')]+=1
        if s1_array == s2_array:
            return True
        for r in range(len(s1), len(s2)):
            s2_array[ord(s2[r-len1])-ord('a')]-=1
            s2_array[ord(s2[r])-ord('a')]+=1
            if s2_array == s1_array:
                return True
        return False
