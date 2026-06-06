class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_q = deque()
        atlantic_q = deque()

        visited_pacific = set()
        visited_atlantic = set()

        for i in range(0, len(heights)):
            pacific_q.append((i,0))
            visited_pacific.add((i,0))
            atlantic_q.append((i, len(heights[0])-1))
            visited_atlantic.add((i,len(heights[0])-1))

        for i in range(0, len(heights[0])):
            pacific_q.append((0,i))
            visited_pacific.add((0,i))
            atlantic_q.append((len(heights)-1, i))
            visited_atlantic.add((len(heights)-1,i))
        

        while len(pacific_q) != 0:
            #tracking levels is not needed. So no inner loop and temp needed
            r, c = pacific_q.popleft()

            if r < len(heights)-1 and (r+1,c) not in visited_pacific and heights[r+1][c] >= heights[r][c]:
                pacific_q.append((r+1,c))
                visited_pacific.add((r+1,c))
            
            if r > 0 and (r-1,c) not in visited_pacific and heights[r-1][c] >= heights[r][c]:
                pacific_q.append((r-1,c))
                visited_pacific.add((r-1,c))
            
            if c < len(heights[0])-1 and (r,c+1) not in visited_pacific and heights[r][c+1] >= heights[r][c]:
                pacific_q.append((r,c+1))
                visited_pacific.add((r,c+1))
            
            if c > 0 and (r,c-1) not in visited_pacific and heights[r][c-1] >= heights[r][c]:
                pacific_q.append((r,c-1))
                visited_pacific.add((r,c-1))
        
        while len(atlantic_q) != 0:
            #tracking levels is not needed. So no inner loop and temp needed
            r, c = atlantic_q.popleft()

            if r < len(heights)-1 and (r+1,c) not in visited_atlantic and heights[r+1][c] >= heights[r][c]:
                atlantic_q.append((r+1,c))
                visited_atlantic.add((r+1,c))
            
            if r > 0 and (r-1,c) not in visited_atlantic and heights[r-1][c] >= heights[r][c]:
                atlantic_q.append((r-1,c))
                visited_atlantic.add((r-1,c))
            
            if c < len(heights[0])-1 and (r,c+1) not in visited_atlantic and heights[r][c+1] >= heights[r][c]:
                atlantic_q.append((r,c+1))
                visited_atlantic.add((r,c+1))
            
            if c > 0 and (r,c-1) not in visited_atlantic and heights[r][c-1] >= heights[r][c]:
                atlantic_q.append((r,c-1))
                visited_atlantic.add((r,c-1))
        
        answer = []

        for elem in visited_atlantic:
            if elem in visited_pacific:
                answer.append([elem[0], elem[1]])
        return answer