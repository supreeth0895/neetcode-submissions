#SUPREETH
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur_arr, remaining_set):
            if not remaining_set:
                ans.append(cur_arr)
                return
            
            for val in remaining_set:
                new_set = set(remaining_set)
                new_set.remove(val)
                new_cur_arr = cur_arr[:]
                new_cur_arr.append(val)
                backtrack(new_cur_arr, new_set)


        backtrack([], set(nums))
        return ans
            
            
