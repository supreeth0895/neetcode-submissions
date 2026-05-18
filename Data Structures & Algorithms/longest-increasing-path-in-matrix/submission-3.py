#SUPREETH
#Dfs + memoization for all cells
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(row,col):
            if row == len(matrix) or col == len(matrix[0]) or row <0 or col <0:
                return 0
            if (row,col) in memo:
                return memo[(row,col)]
            option1,option2,option3,option4 = 0,0,0,0
            if row < len(matrix)-1 and matrix[row+1][col] > matrix[row][col]:
                option1 = 1+dfs(row+1,col)
            if col < len(matrix[0])-1 and matrix[row][col+1] > matrix[row][col]:
                option2 = 1+dfs(row,col+1)
            if row > 0 and matrix[row-1][col] > matrix[row][col]:
                option3 = 1+dfs(row-1,col)
            if col > 0 and matrix[row][col-1] > matrix[row][col]:
                option4 = 1+dfs(row,col-1)
            
            memo[(row,col)] = max(option1,option2,option3,option4)
            
            return max(option1,option2,option3,option4)

        memo = {}
        max_val = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if (i,j) in memo:
                    val = memo[(i,j)]
                else:
                    val = dfs(i,j)
                max_val = max(max_val, val)
        
        return max_val+1
            

            



        