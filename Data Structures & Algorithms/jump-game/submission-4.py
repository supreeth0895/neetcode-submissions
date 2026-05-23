class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal_idx = len(nums)-1

        while goal_idx > 0:
            left_idx = goal_idx-1
            #if index at the left has a value less than minimum jumps required, keep moving left
            while nums[left_idx] < goal_idx-left_idx:
                left_idx = left_idx-1
                if left_idx < 0:
                    return False

            #Once you find a left index which can reach current goal, upate new goal_idx to that index and repeat
            goal_idx = left_idx
        if goal_idx == 0:
            return True




#I initially came up with a DP approach , but that was O(n^2):

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         def backtrack(cur_idx):
#             if cur_idx in memo:
#                 return memo[cur_idx]
#             if cur_idx == len (nums)-1:
#                 memo[cur_idx] = True
#                 return True
#             if cur_idx > len (nums)-1:
#                 memo[cur_idx] = False
#                 return False
            
#             for i in range(1, nums[cur_idx]+1):
#                 if backtrack(cur_idx+i):
#                     memo[cur_idx] = True
#                     return True
#             memo[cur_idx] = False
#             return False
#         memo = {}            
#         return backtrack(0)