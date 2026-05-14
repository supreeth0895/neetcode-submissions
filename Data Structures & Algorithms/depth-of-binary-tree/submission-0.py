# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper_depth(root, 0)
    
    def helper_depth(self, root, level):
        if root == None:
            return level
        else:
            max_depth_left = self.helper_depth(root.left, level+1)
            max_right_depth = self.helper_depth( root.right, level+1)
            return max(max_depth_left, max_right_depth)



    
        
        