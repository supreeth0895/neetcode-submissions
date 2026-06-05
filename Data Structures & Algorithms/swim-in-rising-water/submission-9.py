class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        start = (0,0)
        end = (len(grid),len(grid[0]))

        visited = set()
        
        pq = []

        heapq.heappush(pq, (grid[start[0]][start[1]], start[0], start[1]))  #max val, row, col

        while len(pq) != 0 :
            cur_max_val,row,col = heapq.heappop(pq)
            cur_max_val = cur_max_val

            if row == len(grid)-1 and col == len(grid[0])-1:
                return cur_max_val
            
            if row+1 < len(grid):
                new_row = row+1
                new_col = col
                if (new_row, new_col) not in visited:
                    new_max_val = max(cur_max_val, grid[new_row][new_col])
                    heapq.heappush(pq, (new_max_val, new_row, new_col))
                    visited.add((new_row, new_col))
            
            if col+1 < len(grid[0]):
                new_row = row
                new_col = col+1
                if (new_row, new_col) not in visited:
                    new_max_val = max(cur_max_val, grid[new_row][new_col])
                    heapq.heappush(pq, (new_max_val, new_row, new_col))
                    visited.add((new_row, new_col))
            
            if row-1 >= 0 :
                new_row = row-1
                new_col = col
                if (new_row, new_col) not in visited:
                    new_max_val = max(cur_max_val, grid[new_row][new_col])
                    heapq.heappush(pq, (new_max_val, new_row, new_col))
                    visited.add((new_row, new_col))
            
            if col-1 >= 0:
                new_row = row
                new_col = col-1
                if (new_row, new_col) not in visited:
                    new_max_val = max(cur_max_val, grid[new_row][new_col])
                    heapq.heappush(pq, (new_max_val, new_row, new_col))
                    visited.add((new_row, new_col))
        

        return 0