#SUPREETH
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, isbalanced = self.helper(root)
        return isbalanced
    
    def helper(self, root):
        if root == None:
            return 0, True
        height_left, isbalanced_left = self.helper(root.left)
        height_right, isbalanced_right = self.helper(root.right)
        
        height = max(height_left, height_right) + 1
        if isbalanced_left == False or isbalanced_right == False:
            return height, False
        elif abs(height_left - height_right) > 1:
            return height, False
        return height, True