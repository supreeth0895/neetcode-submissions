#SUPREETH
# """
# APPROACH: Dijkstra's Shortest Path
# ------------------------------------
# - Find shortest time from source k to ALL nodes.
# - Answer is the MAX of all shortest times (last node to receive the signal).
# - Use a min-heap to always process the closest unvisited node first.

# Time: O(E log E) | Space: O(N + E)
# """

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Build adjacency list: {src: [(weight, dst), ...]}
        adjecency = {}
        for time in times:
            if time[0] not in adjecency:
                adjecency[time[0]] = []
            adjecency[time[0]].append((time[2], time[1]))

        pq = []
        heapq.heappush(pq, (0, k))  # (cost, node) — start at k with cost 0
        visited = {}                 # {node: shortest_dist_from_k}

        while pq:
            cost, node = heapq.heappop(pq)

            # Skip if we already found a shorter path to this node
            if node in visited and visited[node] <= cost:
                continue

            visited[node] = cost

            for weight, neighbor in adjecency.get(node, []):
                heapq.heappush(pq, (cost + weight, neighbor))

        # If not all nodes reached, signal can't propagate to entire network
        if len(visited) != n:
            return -1

        return max(visited.values())