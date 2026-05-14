class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        start_row = 0
        end_row = 9
        start_col = 0
        end_col = 9
        print("Hi")
        for i in range (start_row, end_row) :
            my_set =set()
            for j in range(start_col, end_col) :
                if board[i][j] == ".":
                    continue
                if board[i][j] in my_set:
                    print(my_set)
                    return False
                my_set.add(board[i][j])
            
        

        for i in range (start_col, end_col) :
            my_set =set()
            for j in range (start_row, end_row) :
                if board[j][i] == ".":
                    continue
                if board[j][i] in my_set:
                    return False
                my_set.add(board[j][i])
        print("columns fine")

        for start_row in range(0,6,3):
            end_row = start_row + 3
            for start_col in range(0,6,3):
                end_col = start_col + 3
                my_set =set()
                for i in range(start_row, end_row):
                    for j in range(start_col, end_col):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in my_set:
                            return False
                        my_set.add(board[i][j])
                print("box fine")
        return True
        
        


        