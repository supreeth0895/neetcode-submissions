class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for point1 in points:
            for point2 in points:
                if point1 != point2: 
                    if tuple(point1) in adj:
                        adj[tuple(point1)].append(tuple(point2))
                    else:
                        adj[tuple(point1)] = [tuple(point2)]

        pq = []
        heapq.heappush(pq, (0, points[0], points[0]))#(dist, from, to)
        visited = set()
        total_dist = 0
        while len(visited) < len(points):
            dist,v1,v2 = heapq.heappop(pq)
            if tuple(v2) in visited:
                continue
            visited.add(tuple(v2))
            total_dist = total_dist + dist

            if len(visited) == len(points):
                break


            cur_node = v2
            neighbors = adj[tuple(cur_node)]
            for neighbor in neighbors:
                if neighbor not in visited:
                    dist = abs(cur_node[0]- neighbor[0]) + abs(cur_node[1]- neighbor[1])
                    heapq.heappush(pq, (dist, tuple(cur_node), tuple(neighbor)))
        return total_dist

            



        