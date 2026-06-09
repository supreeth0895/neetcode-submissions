class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            if visit[node]:
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n + 1)

            if dfs(u, -1):
                return [u, v]
        return []

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:  
#         #Keeps walking up until it finds a node that points to itself — that's the root.
#         def find(node):
#             #recursively go to the top of the tree
#             while parent[node] != node:
#                 node = parent[node]
#             return node
        
#         #Finds the root of each node. If they're different trees, attach one root under the other.
#         def union(v1,v2):
#             #check top root assigned to both vertitces.
#             #If they are different, set the parent.

#             root1 = find(v1)
#             root2  = find(v2)
#             if root1 != root2:
#                 parent[root2]  = root1

#         num_edges = len(edges)
#         parent = [0]*(num_edges+1)

#         for i in range(1, len(parent)):
#             parent[i] = i
        
#         #Main loop — process edges one by one
#         for v1,v2 in edges:
#             #check if v1 and v2 are in two same set, then simply return that edge
#             #since that will cause cycle:
#             if find(v1) == find(v2):
#                 return [v1,v2]
#             else:
#                 union(v1,v2)
#         return []





        

