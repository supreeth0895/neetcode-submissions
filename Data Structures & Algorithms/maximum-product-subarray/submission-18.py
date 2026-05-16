class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product_subarray_from_index = [0]* len(nums)
        min_product_subarray_from_index = [0]* len(nums)

        max_val = nums[0]
        for i in range(len(nums)-1, -1,-1):
            if i == len(nums)-1:
                if nums[i]>= 0 :
                    max_product_subarray_from_index[i] = nums[i]
                    min_product_subarray_from_index[i] = nums[i]
                else:
                    max_product_subarray_from_index[i] = nums[i]
                    min_product_subarray_from_index[i] = nums[i]
            else:
                possibility1 = nums[i]*max_product_subarray_from_index[i+1]
                possibility2 = nums[i]*min_product_subarray_from_index[i+1]

                max_product_subarray_from_index[i] = max(possibility1,possibility2, nums[i])
                min_product_subarray_from_index[i] = min(possibility1,possibility2, nums[i])
            max_val = max(max_val, max_product_subarray_from_index[i])
        
        return max_val
        
                
            







# This is Dynamic programing - But has more than 1000 recursion calls

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
