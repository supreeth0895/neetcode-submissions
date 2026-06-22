class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = dict(collections.Counter(s1))
        l = 0
        length = len(s1)
        for r in range(len(s2)):
            count2 = defaultdict(int)
            for j in range(r, r+length):
                if j >=len(s2):
                    return False
                count2[s2[j]]+=1
            if count1 == count2:
                return True
            else:
                count2[s2[l]]-=1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l+=1
        return False