"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        my_map = {}
        def dfs_and_return_copy(cur_node):
            if cur_node not in my_map:
                copied_node = Node(cur_node.val)
                my_map[cur_node] = copied_node
                for neighbor in cur_node.neighbors:
                    copied_node.neighbors.append(dfs_and_return_copy(neighbor))
                return copied_node
            else:
                return my_map[cur_node]
            
        if not node:
            return None
        return dfs_and_return_copy(node)