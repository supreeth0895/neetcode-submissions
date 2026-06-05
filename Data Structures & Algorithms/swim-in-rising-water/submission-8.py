class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        start = (0,0)
        end = (len(grid),len(grid[0]))

        visited = {}
        
        pq = []

        heapq.heappush(pq, (1*grid[start[0]][start[1]], start[0], start[1]))  #max val, row, col

        while len(pq) != 0 :
            cur_max_val,row,col = heapq.heappop(pq)

            if row == len(grid)-1 and col == len(grid[0])-1:
                print(pq)
                print(visited)
                return cur_max_val
            
            if row+1 < len(grid):
                new_row = row+1
                new_col = col
                new_max_val = max(cur_max_val, grid[new_row][new_col])
                if (new_row, new_col) not in visited or visited[(new_row, new_col)] > new_max_val:
                    heapq.heappush(pq, (new_max_val, new_row, new_col))
                    visited[(new_row, new_col)] = new_max_val
            
            if col+1 < len(grid[0]):
                new_row = row
                new_col = col+1
                new_max_val = max(cur_max_val, grid[new_row][new_col])
                if (new_row, new_col) not in visited or visited[(new_row, new_col)] > new_max_val:
                    heapq.heappush(pq, (new_max_val, new_row, new_col))
                    visited[(new_row, new_col)] = new_max_val
            
            if row-1 >= 0 :
                new_row = row-1
                new_col = col
                new_max_val = max(cur_max_val, grid[new_row][new_col])
                if (new_row, new_col) not in visited or visited[(new_row, new_col)] > new_max_val:
                    heapq.heappush(pq, (new_max_val, new_row, new_col))
                    visited[(new_row, new_col)] = new_max_val
            
            if col-1 >= 0:
                new_row = row
                new_col = col-1
                new_max_val = max(cur_max_val, grid[new_row][new_col])
                if (new_row, new_col) not in visited or visited[(new_row, new_col)] > new_max_val:
                    heapq.heappush(pq, (new_max_val, new_row, new_col))
                    visited[(new_row, new_col)] = new_max_val
        

        return 0