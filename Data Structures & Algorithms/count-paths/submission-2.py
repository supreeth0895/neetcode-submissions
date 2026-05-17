class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        counter = 0
        def dfs(row,col):
            nonlocal counter
            if (row,col) in memo:
                counter = counter+1
                return memo[(row,col)]
            
            if row >= m or col >= n or row < 0 or col < 0:
                return False,0
            if row == m-1 and col == n-1:
                return True,1

            val1,count1 = dfs(row+1, col)
            val2,count2 = dfs(row, col+1)

            memo[(row, col)] = (val1 or val2, count1+count2)

            return val1 or val2, count1+count2
        
        memo= {}
        v = dfs(0,0)
        return v[1]


# Initially I came up with this - This will traverse every path again and again, this is not good.
# Instead for every index, store whether it can reach target or not after first traversal - Refer above solution
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         counter = 0
#         def dfs(row,col):
#             nonlocal counter
#             if row >= m or col >= n or row < 0 or col < 0:
#                 return
#             if row == m-1 and col == n-1:
#                 counter = counter+1
#                 return

#             dfs(row+1, col)
#             dfs(row, col+1)
        
#         dfs(0,0)
#         return counter


        