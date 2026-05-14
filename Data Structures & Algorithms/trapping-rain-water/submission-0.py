class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_height = [0] * len(height)
        max_right_height = [0] * len(height)

        for i in range(0, len(height)):
            if i == 0:
                max_left_height[i] = 0
                continue
            max_left_height[i] = max(height[i-1], max_left_height[i-1])
        
        for i in range(len(height)-1, -1,-1):
            if i ==len(height)-1 :
                max_right_height[i] = 0
                continue
            max_right_height[i] = max(max_right_height[i+1],height[i+1])
        
        amount_of_water_that_can_be_stored = [0]*len(height)

        print(max_right_height)

        for i in range(0, len(height)):
            capacity= min(max_left_height[i], max_right_height[i]) - height[i]
            if capacity > 0:
                amount_of_water_that_can_be_stored[i] = capacity

        return sum(amount_of_water_that_can_be_stored)


        