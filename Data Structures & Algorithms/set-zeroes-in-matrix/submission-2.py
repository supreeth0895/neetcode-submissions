class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_has_zero = False
        first_col_has_zero = False
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        for i in range(0, len(matrix[0])):
            if matrix[0][i] == 0:
                first_row_has_zero = True
                break

        for i in range(0, len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    break
        for i in range(1, len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_col_has_zero:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0
        if first_row_has_zero:
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0
        
        


        



                
                
        

            
        
        