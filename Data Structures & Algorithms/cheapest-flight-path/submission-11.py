#SUPREETH2 - Dikstra's with k hops allowed.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj  = {}
        for flight in flights:
            source = flight[0]
            dest = flight[1]
            dist = flight[2]
            if source not in adj:
                adj[source] = [(dest,dist)]
            else:
                adj[source].append((dest,dist))
        
        print(adj)
        min_dist = 100000
        pq = []
        heapq.heappush(pq, (0,0,src)) #dist from source, num hops, src node

        while len(pq) != 0:
            dist, num_hops, node = heapq.heappop(pq)
            if num_hops > k+1:
                continue
            if node == dst and num_hops <= k+1:
                min_dist = min(min_dist, dist)
                break
            if node in adj:
                for neighbor in adj[node]:
                    heapq.heappush(pq, (dist+neighbor[1],num_hops+1,neighbor[0]))
        if min_dist == 100000:
            return -1
        return min_dist

