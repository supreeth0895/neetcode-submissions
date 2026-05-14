class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_map = {
            "2": ['a','b','c'],
            "3": ['d', 'e', 'f'],
            "4" : ['g', 'h', 'i'],
            "5" : ['j', 'k', 'l'],
            "6" : ['m', 'n', 'o'],
            "7" : ['p', 'q', 'r', 's'],
            "8" : ['t', 'u', 'v'],
            "9" : ['w', 'x', 'y', 'z']
        }
        def backtrack(cur_str,cur_idx):
            if cur_idx == len(digits):
                if cur_str != "":
                    answer.append(cur_str)
                return
            
            for val in my_map[digits[cur_idx]]:
                new_str = cur_str + val
                backtrack(new_str, cur_idx + 1)
        answer = []
        backtrack("",0)
        return answer


        









    #                     []
    #     d               e                       f
    # dg  dh  di      eg  eh  ei      fg  fh  fi