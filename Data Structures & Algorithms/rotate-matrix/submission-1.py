# SUPREETH

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Do a Transpose , and then mirror the rows

        #TRANSPOSE
        for i in range(0, len(matrix)):
            for j in range(0, i):
                if i == j:
                    continue
                temp  = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        #MIRROR
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[0])-1 -j]
                matrix[i][len(matrix[0])-1 -j] = temp
        