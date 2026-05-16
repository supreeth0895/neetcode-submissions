#SUPREETH - Multi source BFS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs():
            nonlocal cur_time,q
            for elem in q:
                row = elem[0]
                col = elem[1]
                grid[row][col] = 2
            
            possible_neighbors = set()
            for elem in q:
                row = elem[0]
                col = elem[1]
                if row > 0 and grid[row-1][col] == 1:
                    possible_neighbors.add((row-1, col))
                if col > 0 and grid[row][col-1] == 1:
                    possible_neighbors.add((row, col-1))
                if row < len(grid)-1 and grid[row+1][col] == 1:
                    possible_neighbors.add((row+1, col))
                if col < len(grid[0])-1 and grid[row][col+1] == 1:
                    possible_neighbors.add((row, col+1))
            
            q = list(possible_neighbors)
            if q:
                cur_time = cur_time+1
                bfs()

        q = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        cur_time = 0
        if q:
            bfs()

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return cur_time       