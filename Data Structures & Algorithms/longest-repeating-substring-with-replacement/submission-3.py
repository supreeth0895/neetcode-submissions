class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1 = defaultdict(int)
        l, r = 0, 0
        max_len = 0
        while r<len(s):
            dict1[s[r]]+=1
            if (r-l+1)<= max(dict1.values())+k:
                max_len = max(max_len, (r-l+1))
                r+=1
            else:
                dict1[s[r]]-=1
                dict1[s[l]]-=1
                l+=1
        return max_len