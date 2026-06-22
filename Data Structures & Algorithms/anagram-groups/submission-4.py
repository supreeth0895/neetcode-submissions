class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for elem in strs:
            occurances = [0]*26
            for each_char in elem:
                occurances[ord('a')-ord(each_char)]+=1
            occurances = tuple(occurances)
            dict1[occurances].append(elem)
        return list(dict1.values())