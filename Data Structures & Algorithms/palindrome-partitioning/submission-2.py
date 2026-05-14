class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        def backtrack(cur_list,cur_index):
            if cur_index == len(s):
                new_str = cur_list[len(cur_list)-1]
                if new_str == new_str[::-1]:
                    answer.append(cur_list)
                return 
            ch = s[cur_index]

            if len(cur_list) == 0:
                new_list =cur_list[:]
                new_list.append(ch)
                backtrack(new_list, cur_index+1)
            

            if len(cur_list) > 0:
                new_str = cur_list[len(cur_list)-1]
                new_str = new_str + ch
                new_list = cur_list[:]
                new_list[len(cur_list)-1] = new_str
                backtrack(new_list, cur_index+1)

                new_str = cur_list[len(cur_list)-1]
                if new_str == new_str[::-1]:
                    new_list =cur_list[:]
                    new_list.append(ch)
                    backtrack(new_list, cur_index+1)


        
        backtrack([],0)
        return answer







                #                         aab
                # a,a,b            aa,b               a,ab    aab