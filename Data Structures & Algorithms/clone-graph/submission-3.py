#SUPREETH -dfs 
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        def dfs(cur_node):
            if cur_node.val in my_visited_map:
                return
            new_node = Node(cur_node.val, cur_node.neighbors)
            my_visited_map[cur_node.val] = new_node
            for neighbor in cur_node.neighbors:
                dfs(neighbor)

        # Iterate the Graph and make a copy of every node and add it into a Map. Neighbors will still be pointing to old graph
        my_visited_map = {}
        dfs(node)


        #Update the neighbors to point to new graph
        for node_val in my_visited_map:
            new_neighbor_list = []
            for neighbor in my_visited_map[node_val].neighbors:
                key = neighbor.val
                new_neighbor_list.append(my_visited_map[key])
            my_visited_map[node_val].neighbors = new_neighbor_list
        
        return my_visited_map[node.val]
