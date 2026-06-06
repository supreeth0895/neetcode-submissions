# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def dfs(root, max_in_path):
            nonlocal counter
            if not root:
                return
            if root.val >= max_in_path :
                counter = counter+1
            new_max_in_path = max(max_in_path, root.val)
            dfs(root.left, new_max_in_path)
            dfs(root.right, new_max_in_path)
        
        dfs(root, -100000)
        return counter