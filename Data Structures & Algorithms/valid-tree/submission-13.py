# In an undirected graph,
#a cycle exists if you encounter a node that has already been visited,
#unless that node is the immediate parent (the node you just came from).
#The original code didn't track the prev node,
#leading it to mistake the back-and-forth nature of undirected edges for a cycle.

#SUPREETH2
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

        ret_val = dfs(0, -1)
        if ret_val == False:
            return False
        if len(visited) != n:
            return False

        return True