class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first we need to find the row range 
        # second , we need to find the column number in that row 
        # find row 
        row_number = None
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                row_number = i
        # handling out of bounds case 
        if row_number is None:
            return False
        # find the column number for that row
        nums = matrix[row_number]
        l = 0
        r = len(nums)-1
        while l<=r:
            pivot = (l+r)//2
            if nums[pivot]>target:
                r = pivot-1
            elif nums[pivot]<target:
                l = pivot+1
            elif nums[pivot] == target:
                return True
        return False