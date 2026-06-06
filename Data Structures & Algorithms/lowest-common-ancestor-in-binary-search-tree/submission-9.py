# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(root, p , q):
            if not root:
                return None

            if p.val <= root.val and q.val >= root.val:
                return root
            
            if p.val < root.val and q.val < root.val:
                return helper(root.left, p,q)
            
            if p.val > root.val and q.val > root.val:
                return helper(root.right, p, q)
        
        if p.val <= q.val:
            return helper(root, p, q)
        else:
            return helper(root, q, p) 
            

        