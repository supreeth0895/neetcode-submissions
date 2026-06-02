class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}

        for flight in flights:
            if flight[0] in adj:
                adj[flight[0]].append((flight[1], flight[2]))
            else:
                adj[flight[0]] = [(flight[1], flight[2])]
        
        pq = []
        heapq.heappush(pq, (0,0,src)) #dist,num_hops,node
        visited_nodes = {}

        while len(pq) != 0:
            popped_dist, popped_num_hops, popped_node = heapq.heappop(pq)

            neighbors = []
            if popped_node in adj:
                neighbors = adj[popped_node]

            if popped_node == dst:
                return popped_dist

            if popped_num_hops > k:
                continue
            if popped_node in visited_nodes and visited_nodes[popped_node] <= popped_num_hops:
                continue
            visited_nodes[popped_node] = popped_num_hops

            for neighbor in neighbors:
                neighbor_dist = neighbor[1]
                neighbor_node = neighbor[0]
                heapq.heappush(pq, (popped_dist+neighbor_dist, popped_num_hops+1, neighbor_node))

        return -1