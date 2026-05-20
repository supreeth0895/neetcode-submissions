#Remember:
# For this Problem you should do it backwords, meaninging,
# option 1 - elememnt 0 will be removed last - return maxCoins(leftmost_elem, left sub array, rightmost_element)+ element[0] +maxCoins(leftmost_elem, Right sub array,leftmost_elem)
# Option 2 - element 1 will be removed last - return maxCoins(leftmost_elem, left sub array, rightmost_element)+ element[1] +maxCoins(leftmost_elem, Right sub array,leftmost_elem)
# Option 3 - Element 2 will be removed last - return maxCoins(leftmost_elem, left sub array, rightmost_element)+ element[2] +maxCoins(leftmost_elem, Right sub array,leftmost_elem)
# return max of options

# Note Initially leftmost_elem and rightmost_element will be 1. But start and end will be from 0 and len-1

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        def backtrack(left_idx, right_idx):
            if left_idx > right_idx:
                return 0
            if (left_idx, right_idx) in memo:
                return memo[(left_idx, right_idx)]
            options = []
            for i in range(left_idx, right_idx+1):
                product = nums[i]*nums[left_idx-1]*nums[right_idx+1]
                options.append(backtrack(left_idx, i-1) + product + backtrack(i+1, right_idx))

            max_val = 0
            for val in options:
                max_val = max(val,max_val)
            memo[(left_idx, right_idx)] = max_val
            return max_val
                

        
        memo = {}
        nums = [1]+nums+[1]
        return backtrack(1, len(nums)-2)

            


                
        