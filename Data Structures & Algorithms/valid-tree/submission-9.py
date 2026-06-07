# In an undirected graph,
#a cycle exists if you encounter a node that has already been visited,
#unless that node is the immediate parent (the node you just came from).
#The original code didn't track the prev node,
#leading it to mistake the back-and-forth nature of undirected edges for a cycle.

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
                return False
            visited.add(node)
            for val in adj[node]:
                if val != prev:
                    ret_val = dfs(val, node)
                    if not ret_val:
                        return False
            return True
            
        
        visited = set()
        count_of_disjoint_graphs = 0
        for i in range(0, n):
            if i not in visited:
                count_of_disjoint_graphs = count_of_disjoint_graphs +1
                if count_of_disjoint_graphs > 1:
                    return False
                ret_val = dfs(i,-1)
                if not ret_val:
                    return False
        return True

