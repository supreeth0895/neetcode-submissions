#SUPREETH2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col):
            if (row, col) in visited:
                return
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            visited.add((row,col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        visited = set()
        count = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == "1":
                    count  = count +1
                    dfs(r,c)
        return count