class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:  
        #return topmost parent of node
        def find(node):
            #recursively go to the top of the tree
            while parent[node] != node:
                node = parent[node]
            return node
        
        def union(v1,v2):
            #check root of both. If they are same:
            root1 = find(v1)
            root2  = find(v2)
            if root1 != root2:
                parent[root2]  = root1

        num_edges = len(edges)
        parent = [0]*(num_edges+1)

        for i in range(1, len(parent)):
            parent[i] = i
        
        #loop on all edges, try to add them
        for v1,v2 in edges:
            #check if v1 and v2 are in two same set, then simply return that edge
            #since that will cause cycle:
            if find(v1) == find(v2):
                return [v1,v2]
            else:
                union(v1,v2)
        return []





        

