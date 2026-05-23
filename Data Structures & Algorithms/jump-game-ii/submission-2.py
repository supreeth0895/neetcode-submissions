#SUPREETH
# This is possible because the input GUARENTEES THAT THERE EXISTS a PATH to the last index
# 1. Treat each jump range as a BFS level
# 2. count levels to reach the end.

#O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        left_idx = 0
        right_idx = 0        # current BFS level spans [left_idx, right_idx]
        level = 0            # jumps taken so far
        farthest_index_we_can_reach = 0

        while right_idx < len(nums) - 1:    # stop once last index is in range
            for i in range(left_idx, right_idx + 1):
                # expand the frontier: farthest index reachable from this level
                farthest_index_we_can_reach = max(farthest_index_we_can_reach, nums[i] + i)

            left_idx = right_idx + 1            # next level starts after current
            right_idx = farthest_index_we_can_reach   # next level ends at frontier
            level += 1

        return level

# Initially came up with this, but this is O(n ^2). Even DP is O(n^2)
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

                 
                



            
        