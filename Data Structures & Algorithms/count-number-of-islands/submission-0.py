#SUPREETH
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0      
        def dfs(row, col):
            if row <0 or row >= len(grid) or col <0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] !="0":
                    num_islands = num_islands+1
                    dfs(i,j)

        return num_islands
