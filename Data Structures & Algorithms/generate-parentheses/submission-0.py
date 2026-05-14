class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans =[]
        def backtrack(cur_string, number_of_extra_open_brackets):
            if len(cur_string) == 2*n:
                if number_of_extra_open_brackets == 0:
                    ans.append(cur_string)
                return
            if number_of_extra_open_brackets < 0 :
                return
            if number_of_extra_open_brackets == 0:
                new_str= cur_string+"("
                backtrack(new_str, 1)
            else:
                new_str= cur_string+"("
                backtrack(new_str, number_of_extra_open_brackets+1)
                new_str2 = cur_string+")"
                backtrack(new_str2, number_of_extra_open_brackets-1)
        backtrack("",0)
        return ans




#         ((()))
#                                             [],0
#         [(, 1]                                                                             [), -1]
#     ((,2    (),0                                                        
# (((,3   (()1 
    
        