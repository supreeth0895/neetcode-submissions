# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         my_map = {}
#         def backtrack(cur_idx, highest_num):
#             if (cur_idx,highest_num) in my_map:
#                 return my_map[(cur_idx,highest_num)]
#             if cur_idx == len(nums):
#                 return 0
#             val1 = -1001
#             if nums[cur_idx] > highest_num:
#                 highest_num2 = nums[cur_idx]
#                 val1 = 1+backtrack(cur_idx+1, highest_num2)
#             val2 = backtrack(cur_idx+1, highest_num)
#             my_map[(cur_idx,highest_num)] = max(val1,val2)
#             return max(val1,val2)
        
#         return backtrack(0,-1001)

from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS