#SUPREETH2
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q=deque()
        for i in range(0,len(board)):
            if board[i][0] == "O":
                q.append((i,0))
                board[i][0] = "Y"
            if board[i][len(board[0])-1] == "O":
                q.append((i,len(board[0])-1))
                board[i][len(board[0])-1] = "Y"

        for i in range(0,len(board[0])):
            if board[0][i] == "O":
                q.append((0,i))
                board[0][i] = "Y"
            if board[len(board)-1][i] == "O":
                q.append((len(board)-1,i))
                board[len(board)-1][i] = "Y"
        
        while len(q) != 0:
            row,col = q.popleft()
            
            if row >0 and board[row-1][col] == "O":
                q.append((row-1,col))
                board[row-1][col] = "Y"

            if row < len(board)-1 and board[row+1][col] == "O":
                q.append((row+1,col))
                board[row+1][col] = "Y"

            if col >0 and board[row][col-1] == "O":
                q.append((row,col-1))
                board[row][col-1] = "Y"

            if col < len(board[0])-1 and board[row][col+1] == "O":
                q.append((row,col+1))
                board[row][col+1] = "Y"
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Y":
                    board[i][j] = "O"

