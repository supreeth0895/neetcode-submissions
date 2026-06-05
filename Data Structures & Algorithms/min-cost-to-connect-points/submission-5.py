#SUPREETH -2 : PRIMS AGLO - MST
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:        
        start = points[0]
        pq = []
        heapq.heappush(pq, (0,tuple(start))) #dist to add to MST,location of point
        visited = set()
        remaining_points = set()

        for point in points:
            remaining_points.add((point[0],point[1]))


        total_dist = 0
        while len(pq) != 0 :
            dist,location = heapq.heappop(pq)
            if location in visited:
                continue
            
            visited.add(location)
            remaining_points.remove(location)
            total_dist = total_dist+ dist

            if len(remaining_points) == 0:
                return total_dist

            for point in remaining_points:
                dist = abs(location[0]-point[0]) + abs(location[1]-point[1])
                heapq.heappush(pq, (dist, point))
        return -1
            






        


        
        