class Solution:
    def jump(self, nums: List[int]) -> int:
        goal_idx = len(nums)-1
        jump_count = 0
        while goal_idx > 0 :
            for i in range(0, goal_idx):
                if nums[i]+i >= goal_idx:
                    jump_count = jump_count+1
                    goal_idx = i
                    break
        
        return jump_count

                 
                



            
        