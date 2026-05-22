class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        wall_left = 0
        wall_right = len(matrix[0])-1
        wall_up = 0
        wall_down = len(matrix)-1
        answer = []
        while wall_left <= wall_right and wall_up <= wall_down:
            for i in range(wall_left, wall_right+1):
                answer.append(matrix[wall_up][i])
            wall_up = wall_up + 1
            
            for i in range(wall_up, wall_down+1):
                answer.append(matrix[i][wall_right])
            wall_right = wall_right - 1

            if wall_up <= wall_down:  # there is still a valid row left
                for i in range(wall_right, wall_left-1, -1):
                    answer.append(matrix[wall_down][i])
                wall_down = wall_down - 1

            if wall_left <= wall_right:  # there is still a valid column left
                for i in range(wall_down, wall_up-1,-1):
                    answer.append(matrix[i][wall_left])
                wall_left = wall_left+1
        return answer