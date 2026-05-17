# SUPREETH
#Do multisource dfs or bfs from_the_border
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def multisourcedfs(row,col,is_atl):
            if is_atl:
                if (row,col) in visited_atl:
                    return 
            else:
                if (row,col) in visited_pac:
                    return 
            if row < 0 or col < 0 or row >= len(heights) or col > len(heights[0]):
                return
            
            if is_atl:
                visited_atl.add((row,col))
            else:
                visited_pac.add((row,col))

            if row-1 >= 0 and heights[row-1][col] >= heights[row][col]:
                multisourcedfs(row-1,col,is_atl)
            if col-1 >= 0  and heights[row][col-1] >= heights[row][col]:
                multisourcedfs(row,col-1,is_atl)
            if row+1 < len(heights) and heights[row+1][col] >= heights[row][col]:
                multisourcedfs(row+1,col,is_atl)
            if col+1 < len(heights[0]) and heights[row][col+1] >= heights[row][col]:
                multisourcedfs(row,col+1,is_atl)


        visited_atl = set()
        visited_pac = set()
        for i in range(0, len(heights)):
            for j in range(0, len(heights[0])):
                if i == 0 or j == 0:
                    multisourcedfs(i,j,False)
                if i == len(heights)-1 or j == len(heights[0])-1:
                    multisourcedfs(i,j,True)
        answer = []
        for val in visited_atl:
            if val in visited_pac:
                answer.append([val[0], val[1]])
        return answer





        