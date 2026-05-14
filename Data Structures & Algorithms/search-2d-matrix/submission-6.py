class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_rows = len(matrix)
        total_col = len(matrix[0])
        len_of_matrix = total_rows*total_col
        start = 0
        end = len_of_matrix

        while start <= end:
            #Convert linear index into 2d index
            mid = (start+end)//2
            mid_row = (mid)//total_col
            mid_col = (mid)%total_col

            if mid_row>=total_rows or mid_col > total_col:
                return False

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                start = mid+1
            else:
                end = mid-1
        
        return False