#SUPREETH
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for idx, point in enumerate(points):
            dist = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(q,(-dist,idx))
            if len(q) > k:
                heapq.heappop(q)

        ans = []
        for val in q:
            ans.append(points[val[1]])
        return ans

        