class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(row, col, dist):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] < dist:
                return
            
            grid[row][col] = dist
            dfs(row+1, col, dist + 1)
            dfs(row, col+1, dist + 1)
            dfs(row-1, col, dist + 1)
            dfs(row, col-1, dist + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j, 0)