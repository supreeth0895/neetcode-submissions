#Multi source BFS is more optimal.
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        def multisourcebfs():
            nonlocal q, cur_level
            if len(q) == 0:
                return
            neighbors = []
            #Set the elements in the Queue:
            for element in q:
                row = element[0]
                col = element[1]
                grid[row][col] = cur_level

            #Prepare neighbors, which will e be the next seto fo queue values
            for element in q:
                row = element[0]
                col = element[1]
                if row < len(grid)-1 and grid[row+1][col] > 0 and grid[row+1][col] > cur_level+1:
                    neighbors.append((row+1,col))
                if col < len(grid[0])-1 and grid[row][col+1] > 0 and grid[row][col+1] > cur_level+1:
                    neighbors.append((row,col+1))
                if row > 0 and grid[row-1][col] > 0 and grid[row-1][col] > cur_level+1:
                    neighbors.append((row-1,col))
                if col > 0 and grid[row][col-1] > 0 and grid[row][col-1] > cur_level+1:
                    neighbors.append((row,col-1))
                
            q =[]
            q = neighbors
            print(q)
            cur_level = cur_level +1
            multisourcebfs()



        cur_level = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        print(q)
        multisourcebfs()
        

        







#DFS from treasure: -Option -1 TC - (mn)^2

# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         def dfs(row, col, dist):
#             if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] < dist:
#                 return
            
#             grid[row][col] = dist
#             dfs(row+1, col, dist + 1)
#             dfs(row, col+1, dist + 1)
#             dfs(row-1, col, dist + 1)
#             dfs(row, col-1, dist + 1)

#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 0:
#                     dfs(i, j, 0)