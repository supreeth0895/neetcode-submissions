class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for flight in flights:
            if flight[0] in adj:
                adj[flight[0]].append((flight[1], flight[2]))
            else:
                adj[flight[0]] = [(flight[1], flight[2])]

        pq = []
        heapq.heappush(pq, (0, 0, src))  # (cost, hops, node)
        visited_nodes = {}  # node -> min hops when popped

        while pq:
            popped_dist, popped_num_hops, popped_node = heapq.heappop(pq)

            if popped_node == dst:
                return popped_dist  # PQ is cost-ordered, first pop is cheapest

            if popped_num_hops > k:
                continue

            # Pop-time pruning: skip if already popped with fewer/equal hops
            if popped_node in visited_nodes and visited_nodes[popped_node] <= popped_num_hops:
                continue
            visited_nodes[popped_node] = popped_num_hops

            for neighbor_node, neighbor_dist in adj.get(popped_node, []):
                heapq.heappush(pq, (popped_dist + neighbor_dist, popped_num_hops + 1, neighbor_node))

        return -1