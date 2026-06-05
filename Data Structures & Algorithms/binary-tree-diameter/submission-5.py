#SUPREETH2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def helper(root):
            nonlocal max_diameter
            if not root:
                return 0
            left_subtree_height = helper(root.left)
            right_subtree_height = helper(root.right)
            max_diameter = max(max_diameter, left_subtree_height+right_subtree_height)
            return max(left_subtree_height,right_subtree_height)+1

        helper(root)
        return max_diameter
        