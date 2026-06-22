class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str1 in strs:
            count = [0]*26
            for elem in str1:
                count[ord(elem)-ord('a')]+=1
            res[tuple(count)].append(str1)
        return list(res.values())