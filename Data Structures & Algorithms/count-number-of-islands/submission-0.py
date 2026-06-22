class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        res = 0
        def dfs(r, c):
            if r <0 or c<0 or r>=rows or c>=cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for r1, c1 in directions:
                row = r1+r
                col = c1+c
                dfs(row, col)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res+=1
        return res