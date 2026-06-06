#SUPREETH2
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col):
            nonlocal area
            if (row, col) in visited:
                return 0 
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            visited.add((row,col))
            area = area+1
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        visited = set()
        max_area = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r,c)
                    max_area = max(max_area, area)
        return max_area