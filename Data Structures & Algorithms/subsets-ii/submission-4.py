class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        visited = set()

        def backtrack(cur_traversed_arr, cur_index):
            if tuple([tuple(cur_traversed_arr),cur_index]) in visited:
                return
            else:
                visited.add(tuple([tuple(cur_traversed_arr),cur_index]))

            if cur_index == len(nums):
                ans.add(tuple(cur_traversed_arr))
                return
            backtrack(cur_traversed_arr,cur_index +1 )
            for i in range(cur_index, len(nums)):
                val = nums[i]
                new_arr = cur_traversed_arr[:]
                new_arr.append(val)
                backtrack(new_arr,i+1)
        nums.sort()
        backtrack([],0)
        ret_val = []
        for val in ans:
            ret_val.append(list(val))

        return ret_val

        




                #             []
                # []  [1]     [2]     [1]
                #     [1,2] [11] [21] 21
        