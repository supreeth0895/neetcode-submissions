# This is possible because the input GUARENTEES THAT THERE EXISTS ONE ANSWER.
#Basically bfs
class Solution:
    def jump(self, nums: List[int]) -> int:
        left_idx = 0
        right_idx = 0
        level = 0
        farthest_index_we_can_reach = 0
        while right_idx < len(nums)-1:
            for i in range(left_idx,right_idx+1):
                farthest_index_we_can_reach = max(farthest_index_we_can_reach, nums[i]+i, i)
            left_idx = right_idx+1
            right_idx = farthest_index_we_can_reach
            level = level+1
        return level


# I Initially came up with this, but thsi si O(n square)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         goal_idx = len(nums)-1
#         jump_count = 0
#         while goal_idx > 0 :
#             for i in range(0, goal_idx):
#                 if nums[i]+i >= goal_idx:
#                     jump_count = jump_count+1
#                     goal_idx = i
#                     break
        
#         return jump_count

                 
                



            
        