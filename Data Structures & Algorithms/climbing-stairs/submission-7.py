#SUPREETH
#BACKTRACKING + MEMOIZATION
class Solution:
    def climbStairs(self, n: int) -> int:
        my_map = {0 : 1, 1:1}

        def backtrack(n):
            if n in my_map:
                return my_map[n]
            if n == 0:
                return 1
            if n==1:
                return 1
            val1 = backtrack(n-1)
            val2 = backtrack(n-2)
            my_map[n] = val1 + val2
            my_map[n-1] = val1
            my_map[n-2] = val2
            return val1+val2
        return backtrack(n)


# #WITHOUT MEMOIZATION _ Only backtracking - TLE. Must add in Memoization
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return 1
#         val1 = self.climbStairs(n-1)
#         val2 = self.climbStairs(n-2)
#         return val1+val2