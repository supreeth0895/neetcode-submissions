"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict1 = {}
        if not node:
            return None
        def dfs(node):
            if node in dict1:
                return dict1[node]
            new_node = Node(node.val)
            dict1[node] = new_node
            for neigh in node.neighbors:
                new_neighbor = dfs(neigh)
                new_node.neighbors.append(new_neighbor)
            return new_node
        return dfs(node)