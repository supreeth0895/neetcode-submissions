class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for elem in strs:
            temp = [0]*26
            for char in elem:
                temp[ord(char)-ord('a')] += 1
            dict1[tuple(temp)].append(elem)
        return list(dict1.values())