class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjecency = {}
        for time in times:
            if time[0] not in adjecency:
                adjecency[time[0]] = []
            adjecency[time[0]].append((time[2],time[1])) #adj[vertex1] = (val, vertex2)
        
        pq = []
        heapq.heappush(pq, (0,k))
        visited = {}


        while pq:
            popped_vertex = heapq.heappop(pq)
            print(popped_vertex)
            if popped_vertex[1] not in visited:
                visited[popped_vertex[1]] = popped_vertex[0]
            else:
                if visited[popped_vertex[1]] <= popped_vertex[0]:
                    continue

                if visited[popped_vertex[1]] > popped_vertex[0]:
                    visited[popped_vertex[1]] = popped_vertex[0]
            neighbors_of_popped_edge = []
            if popped_vertex[1] in adjecency:
                neighbors_of_popped_edge = adjecency[popped_vertex[1]]
            for neighbor in neighbors_of_popped_edge:
                dist_from_start = popped_vertex[0] + neighbor[0]
                vertex = neighbor[1]
                heapq.heappush(pq, (dist_from_start,vertex))
        
        print(visited)
        if len(visited) != n:
            return -1

        return max(visited.values())
        