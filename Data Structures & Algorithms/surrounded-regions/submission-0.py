#You need to understand that:
#For any solution "CANNOT be surrounded", MUST have a cell at the Border. Once this is known,, everything else is easy.
#Then:
# 1. You scan all border cells, get the O's at the Border. On each of them, run a BFS or DFS, and visit all connecting O's.
# 2. Replace the entire Group into say 'T'
# 3. Apart from this T, everything else can be surrounded , So mark all remaining O's as X's and then rename the T's  back to an O.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        cell_list_at_the_border = []
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                    if board[i][j] == "O":
                        cell_list_at_the_border.append((i,j))

        

        def dfs(row,col):
            if row < 0 or col < 0 or row > len(board)-1 or col > len(board[0])-1:
                return 
            if board[row][col] != "O":
                return
            board[row][col] = "T"            
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row,col+1)
            dfs(row,col-1)

        for cell in cell_list_at_the_border:
            dfs(cell[0],cell[1])
        
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "T":
                    board[i][j] = "O"




        

        