#SUPREETH2
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_count = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row,col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        if fresh_count == 0: return 0
        time = -1

        while len(q) != 0:
            temp = []
            for elem in q:
                row = elem[0]
                col = elem[1]
                if row < len(grid)-1 and grid[row+1][col] == 1:
                    temp.append((row+1,col))
                    grid[row+1][col] = 2
                    fresh_count -= 1

                if row > 0 and grid[row-1][col] == 1:
                    temp.append((row-1,col))
                    grid[row-1][col] = 2
                    fresh_count -= 1

                if col < len(grid[0])-1 and grid[row][col+1] == 1:
                    temp.append((row,col+1))
                    grid[row][col+1] = 2
                    fresh_count -= 1

                if col > 0 and grid[row][col-1] == 1:
                    temp.append((row,col-1))
                    grid[row][col-1] = 2
                    fresh_count -= 1
            q = deque(temp)
            time = time + 1

        return time if fresh_count == 0 else -1