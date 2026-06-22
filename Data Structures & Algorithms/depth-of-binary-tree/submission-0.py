# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.depth = -math.inf
        self.dfs(root, 1)
        return self.depth
    def dfs(self, root, level):
        if not root:
            return 
        self.dfs(root.left, level+1)
        self.depth = max(self.depth, level)
        self.dfs(root.right, level+1)