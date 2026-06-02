#SUPREETH
#Remember:
# For this Problem you should do it backwords, meaninging,
# option 1 - elememnt 0 will be removed last - return maxCoins(leftmost_elem, left sub array, rightmost_element)+ element[0] +maxCoins(leftmost_elem, Right sub array,leftmost_elem)
# Option 2 - element 1 will be removed last - return maxCoins(leftmost_elem, left sub array, rightmost_element)+ element[1] +maxCoins(leftmost_elem, Right sub array,leftmost_elem)
# Option 3 - Element 2 will be removed last - return maxCoins(leftmost_elem, left sub array, rightmost_element)+ element[2] +maxCoins(leftmost_elem, Right sub array,leftmost_elem)
# return max of options

# Note Initially leftmost_elem and rightmost_element will be 1. But start and end will be from 0 and len-1

class Solution:
    def maxCoins(self, nums):
        # add padding of 1 on both sides
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}

        def helper(left, right):
            if right - left < 2:       # no balloons between boundaries
                return 0
            if (left, right) in memo:
                return memo[(left, right)]

            best = 0
            for i in range(left + 1, right):  # try each balloon as last to burst
                coins = nums[left] * nums[i] * nums[right]
                coins += helper(left, i) + helper(i, right)
                best = max(best, coins)

            memo[(left, right)] = best
            return best

        return helper(0, n - 1)