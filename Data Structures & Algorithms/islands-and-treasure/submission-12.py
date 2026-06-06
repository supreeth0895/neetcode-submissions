#SUPREETH
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dist = 0
        while len(q) != 0:
            temp= []
            while len(q) != 0:
                elem = q.popleft()
                row = elem[0]
                col = elem[1]
                grid[row][col] = dist
                if row < len(grid)-1 and grid[row+1][col] == 2147483647:
                    temp.append((row+1,col))
                    grid[row+1][col] = -2 #To mark as Visiting 

                if row > 0 and grid[row-1][col] == 2147483647:
                    temp.append((row-1,col))
                    grid[row-1][col] = -2

                if col < len(grid[0])-1 and grid[row][col+1] == 2147483647:
                    temp.append((row,col+1))
                    grid[row][col+1] = -2

                if col > 0 and grid[row][col-1] == 2147483647:
                    temp.append((row,col-1))
                    grid[row][col-1] = -2
            q = deque(temp)
            dist = dist+1


    


            




        