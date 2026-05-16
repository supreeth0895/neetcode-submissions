class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col):
            nonlocal cur_count
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return
            if grid[row][col] == 0:
                return
            grid[row][col] = 0
            cur_count = cur_count+1
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)
        
        cur_count = 0
        max_count  = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] != 0:
                    cur_count = 0
                    dfs(i,j)
                    max_count = max(max_count,cur_count)
        return max_count

        