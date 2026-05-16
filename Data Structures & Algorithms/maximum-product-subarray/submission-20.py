#SUPREETH
#Kadance solution SC- O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Edge case: empty array (not needed per constraints but safe)
        if not nums:
            return 0
        
        # Initialize with the first element
        max_val = nums[0]  # overall maximum product found so far
        cur_max = nums[0]  # max product ending at current position
        cur_min = nums[0]  # min product ending at current position

        # Start from the second element
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Since we need the old cur_max and cur_min for the next step,
            # store the current product using the old cur_max first.
            # temp_max = max of: num itself (start new subarray),
            #                   num * previous max product,
            #                   num * previous min product (may flip sign)
            temp_max = max(num, num * cur_max, num * cur_min)
            
            # Update cur_min using the original cur_max (before update)
            cur_min = min(num, num * cur_max, num * cur_min)
            
            # Now update cur_max with the computed temp_max
            cur_max = temp_max
            
            # Update the overall maximum
            max_val = max(max_val, cur_max)
        
        return max_val




# This is more readable Kadance algo but SC-  O(n)
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         # DP arrays where dp_max[i] = max product of subarray starting at i
#         # dp_min[i] = min product of subarray starting at i (to handle negatives)
#         max_product_subarray_from_index = [0] * len(nums)
#         min_product_subarray_from_index = [0] * len(nums)

#         max_val = nums[0]  # overall maximum product

#         # Traverse from right to left (bottom-up DP)
#         for i in range(len(nums) - 1, -1, -1):
#             if i == len(nums) - 1:
#                 # Base case: single element at end
#                 max_product_subarray_from_index[i] = nums[i]
#                 min_product_subarray_from_index[i] = nums[i]
#             else:
#                 # Two ways to extend subarray starting at i:
#                 # 1) Multiply nums[i] with max product starting at i+1
#                 # 2) Multiply nums[i] with min product starting at i+1
#                 # (a negative * negative can become a large positive, so we consider both)
#                 possibility1 = nums[i] * max_product_subarray_from_index[i + 1]
#                 possibility2 = nums[i] * min_product_subarray_from_index[i + 1]

#                 # The max product at i is the best of: starting fresh with nums[i],
#                 # or extending from i+1 using either max or min (sign can flip)
#                 max_product_subarray_from_index[i] = max(possibility1, possibility2, nums[i])
#                 # Similarly, the min product at i (needed for future negative numbers)
#                 min_product_subarray_from_index[i] = min(possibility1, possibility2, nums[i])

#             # Update overall max
#             max_val = max(max_val, max_product_subarray_from_index[i])

#         return max_val

#This is backtracking aproach, if you don't know kandance solution:
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         my_map = {}
#         def backtrack(start_idx,end_idx):
#             if (start_idx,end_idx) in my_map:
#                 return my_map[(start_idx,end_idx)]
#             if end_idx ==len(nums):
#                 return -100000000
            
#             current_prod = 1
#             for i in range(start_idx, end_idx+1):
#                 current_prod = current_prod*nums[i]

#             res1 = backtrack(start_idx, end_idx+1)
#             res2 = backtrack(end_idx+1, end_idx+1)
#             my_map[(start_idx,end_idx)] = max(current_prod, res1,res2)
#             return max(current_prod, res1,res2)

#         val = backtrack(0,0)
#         return val