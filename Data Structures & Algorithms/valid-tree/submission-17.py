#SUPREETH2

# Note: 
# In an undirected graph, you must take prev as an arg to skip adding parent nodes.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for i in range(0, n):
            adj[i] = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node, prev):
            if node in visited:
                return False  # Cycle detected
            visited.add(node)
            for val in adj[node]:
                if val != prev:  # Skip parent to avoid treating undirected back-edge as cycle
                    if not dfs(val, node):
                        return False
            return True
            
        visited = set()
        count_of_disjoint_graphs = 0

        #Do DFS from Node 0. It must visit all nodes without detecting Cycle.
        ret_val = dfs(0, -1)
        if ret_val == False:
            return False
        
        # Check for disjoint Graphs
        if len(visited) != n:
            return False

        return True