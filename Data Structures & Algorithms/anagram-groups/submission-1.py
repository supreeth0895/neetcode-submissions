class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for elem in strs:
            dict1["".join(sorted(elem))].append(elem)
        return list(dict1.values())