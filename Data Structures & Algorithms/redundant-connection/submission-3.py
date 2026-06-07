class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(len(edges) + 1):
            adj[i] = []
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(node, prev):
            nonlocal cycle_start, cycle_end
            if cycle_start != -1:
                return
            visited.add(node)
            for val in adj[node]:
                if val == prev:
                    continue
                if cycle_start != -1:
                    return
                if val in visited:
                    cycle_start = val  # cycle begins here
                    cycle_end = node   # cycle closes here
                    return
                path[val] = node       # track how we got to val
                dfs(val, node)

        visited = set()
        path = {}
        cycle_start = -1
        cycle_end = -1
        path[1] = -1
        dfs(1, -1)

        # Walk path back from cycle_end to cycle_start to get all cycle nodes
        cycle_nodes = set()
        cur = cycle_end
        while cur != cycle_start:
            cycle_nodes.add(cur)
            cur = path[cur]
        cycle_nodes.add(cycle_start)

        # Last edge in input whose both endpoints are in the cycle
        for u, v in reversed(edges):
            if u in cycle_nodes and v in cycle_nodes:
                return [u, v]