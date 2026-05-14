# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#INORDER APPROACH:
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         visited = []
    
#         def inorder(root):
#             if not root:
#                 return
#             inorder(root.left)
#             visited.append(root.val)
#             inorder(root.right)
        
#         inorder(root)
#         return visited[k-1]



#Optimized Inorder:
#In a BST, the inorder traversal (Left → Node → Right) naturally visits nodes in sorted order.
# So instead of storing all values, we can:
    #Traverse the tree in inorder
    #Count nodes as we visit them,
    #Stop as soon as we visit the k-th smallest node.
    #This avoids storing all node values, and the early return lets us stop once the k-th smallest node is found.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        total_visited = 0
        kthSmallest_val = 0

        def inorder(root):
            nonlocal total_visited, kthSmallest_val
            if not root:
                return
            if total_visited == k:
                return
            inorder(root.left)
            total_visited += 1
            if total_visited == k:
                kthSmallest_val = root.val
                return
            inorder(root.right)
        
        inorder(root)
        return kthSmallest_val
