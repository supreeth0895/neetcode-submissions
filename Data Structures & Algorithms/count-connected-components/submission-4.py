class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for i in range(0,n):
            adj[i] = []

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor != prev:
                    dfs(neighbor, node)
        
        visited = set()
        count_of_disconnected_graphs = 0
        for i in range(0,n):
            if i not in visited:
                count_of_disconnected_graphs = count_of_disconnected_graphs +1
                dfs(i,-1)
        
        return count_of_disconnected_graphs
                
