class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Summary:
        # Modified Dijkstra with hop-count constraint.
        # PQ ordered by cost ensures first time dst is popped = cheapest valid path.
        # Pop-time pruning: skip a node if we've already processed it with fewer/equal hops,
        # since that path dominates (same or better hop budget, guaranteed cheaper cost due to PQ ordering).
        # Push-time pruning is intentionally avoided — a costlier path with fewer hops
        # may still be useful if the cheaper path exhausts the hop limit before reaching dst.

        adj = {}

        for flight in flights:
            if flight[0] in adj:
                adj[flight[0]].append((flight[1], flight[2]))
            else:
                adj[flight[0]] = [(flight[1], flight[2])]
        
        pq = []
        heapq.heappush(pq, (0,0,src)) #dist,num_hops,node
        visited_nodes = {}  # node -> min hops at which it was popped and processed

        while len(pq) != 0:
            popped_dist, popped_num_hops, popped_node = heapq.heappop(pq)

            neighbors = []
            if popped_node in adj:
                neighbors = adj[popped_node]

            # First pop of dst is always the cheapest due to cost-ordered PQ
            if popped_node == dst:
                return popped_dist

            # Exceeded hop limit (k stops = k+1 edges, hops counts edges)
            if popped_num_hops > k:
                continue

            # Already processed this node with fewer/equal hops — current path is dominated
            if popped_node in visited_nodes and visited_nodes[popped_node] <= popped_num_hops:
                continue
            visited_nodes[popped_node] = popped_num_hops  # mark as processed with current hop count

            for neighbor in neighbors:
                neighbor_dist = neighbor[1]
                neighbor_node = neighbor[0]
                # Always push — let pop-time pruning decide, not push-time
                heapq.heappush(pq, (popped_dist+neighbor_dist, popped_num_hops+1, neighbor_node))

        return -1  # No valid path within k stops