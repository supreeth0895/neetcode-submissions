#SUPREETH
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        ans = []
        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st in my_map:
                my_map[sorted_st].append(st)
            else:
                my_map[sorted_st] = [st]
        
        for key in my_map:
            ans.append(my_map[key])
        
        return ans



