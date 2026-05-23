#SUPREETH
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        cur_sum = 0
        max_sum = 0

        while end < len(nums):
            # If adding the current element makes the sum negative,
            # reset and start a new subarray from the next element
            if cur_sum + nums[end] < 0:
                cur_sum = 0
                start = end + 1
                end = end + 1
                continue

            # Extend the current subarray and update the running sum
            cur_sum = cur_sum + nums[end]

            # Track the best sum seen so far
            max_sum = max(max_sum, cur_sum)
            end = end + 1

        # Edge case: all numbers are negative — max_sum stays 0,
        # so just return the largest (least negative) element
        if max_sum == 0:
            return max(nums)

        return max_sum