class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for time in times:
            adj[time[0]] = []

        for time in times:
            adj[time[0]].append((time[1], time[2])) # adj[source] = (dest,distance)
        
        pq = []
        heapq.heappush(pq, (0,k)) # (dist from source (k), node)

        visited = set()

        max_dist = 0

        while len(pq) != 0:
            cur_node_dist, cur_node_name = heapq.heappop(pq)
            if cur_node_name in visited:
                continue
            visited.add(cur_node_name)
            max_dist = max(max_dist,cur_node_dist)

            if len(visited) == n:
                break
            
            if cur_node_name not in adj:
                continue 

            for new_node_name, new_node_dist in adj[cur_node_name]:
                dist_from_source = cur_node_dist + new_node_dist
                heapq.heappush(pq, (dist_from_source, new_node_name))
        if len(visited) != n:
            return -1
        return max_dist
            








        

        

        